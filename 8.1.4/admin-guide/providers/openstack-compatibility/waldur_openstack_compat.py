#!/usr/bin/env python3
"""Check that Waldur can perform every OpenStack operation it supports on one cloud.

Drives a Waldur's REST API through the full OpenStack lifecycle -- offering,
tenant, networking, ports, floating IPs, instances, volumes, snapshots,
backups, server groups, load balancers, RBAC sharing, quotas, pulls,
Placement -- and records each operation as passed, failed or skipped. Waldur's
backend and Celery worker make every call to the cloud, so a pass means
Waldur's own code works there: its client versions, its pinned
microversions, its parsing of the responses. One run reports every
incompatibility rather than the first one, and the teardown always runs.

It needs Python 3.9+ and ``requests``, nothing else, so it can be copied to
any host that can reach the Waldur API -- a cloud's controller, say, where the admin
credentials already are::

    source admin-openrc.sh
    python3 waldur_openstack_compat.py \\
        --waldur-url https://waldur.example.com --waldur-token <staff token> \\
        --image "Ubuntu 24.04" --flavor m1.small --volume-type ssd

The cloud credentials default to the ``OS_*`` variables an RC file sets; the
Waldur ones to ``WALDUR_URL`` and ``WALDUR_TOKEN`` (or ``WALDUR_USERNAME`` and
``WALDUR_PASSWORD``). The Waldur must be staff-accessible with this token,
must reach the cloud's public endpoints, and must run a real Celery worker.

The run registers the cloud as a new offering under a new organization, so
the admin password ends up in that Waldur's service settings, as it would on
onboarding. Every name it creates carries a random suffix; the offering is
archived at the end. The exit status is 0 when nothing failed.
"""

import argparse
import contextlib
import dataclasses
import ipaddress
import json
import logging
import os
import secrets
import sys
import time
import traceback
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path

import requests

logger = logging.getLogger("waldur_openstack_compat")

SUFFIX = uuid.uuid4().hex[:6]

TENANT_CIDR = "10.76.0.0/24"
NETWORK_CIDR = "10.77.0.0/24"
PORT_IP_MOVED = "10.77.0.51"
PAIR_CIDR = "10.77.0.240/28"


@dataclass
class Config:
    waldur_url: str
    waldur_token: str = dataclasses.field(repr=False)
    os_auth_url: str
    os_username: str
    os_password: str = dataclasses.field(repr=False)
    os_project: str = "admin"
    os_domain: str = "Default"
    os_verify_ssl: bool = False
    waldur_verify_ssl: bool = True
    external_network: str = None
    image: str = None
    flavor: str = None
    resize_flavor: str = None
    volume_type: str = None
    retype_to: str = None
    rescue_image: str = None
    rbac: bool = True
    image_upload: bool = False
    live_volume_resize: bool = False
    timeout: int = 600
    report: str = "openstack-compat.json"


def wait_until(predicate, timeout=180, interval=3, description="condition"):
    """Poll ``predicate`` until it returns a truthy value, and return that."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        result = predicate()
        if result:
            return result
        time.sleep(interval)
    raise AssertionError(f"Timed out after {timeout}s waiting for {description}")


class Skip(Exception):
    """A step that does not apply to this cloud or configuration."""


class ApiError(Exception):
    pass


@dataclass
class Result:
    name: str
    status: str
    seconds: float
    detail: str = ""


class Api:
    def __init__(self, base, token, verify=True):
        self.base = base.rstrip("/")
        self.headers = {"Authorization": f"Token {token}"}
        self.verify = verify

    def url(self, path):
        return path if path.startswith("http") else f"{self.base}/api/{path}"

    def call(self, method, path, payload=None, params=None, expect_json=True):
        # Reads are retried through a passing hiccup -- a 502 from a proxy, a
        # dropped connection -- which a 30-minute run otherwise turns into a
        # failed step. Writes are not: they may have taken effect.
        attempts = 3 if method == "GET" else 1
        for attempt in range(attempts):
            try:
                response = requests.request(
                    method,
                    self.url(path),
                    json=payload,
                    params=params,
                    headers=self.headers,
                    timeout=120,
                    verify=self.verify,
                )
            except requests.ConnectionError:
                if attempt + 1 == attempts:
                    raise
            else:
                if (
                    response.status_code not in (502, 503, 504)
                    or attempt + 1 == attempts
                ):
                    break
            time.sleep(5)
        if not response.ok:
            raise ApiError(
                f"{method} {path} -> {response.status_code}: {response.text[:500]}"
            )
        if expect_json and response.content:
            return response.json()
        return None

    def get(self, path, **params):
        return self.call("GET", path, params={"page_size": 300, **params})

    def post(self, path, payload=None):
        return self.call("POST", path, payload or {})

    def patch(self, path, payload):
        return self.call("PATCH", path, payload)

    def delete(self, path):
        return self.call("DELETE", path, expect_json=False)


class Run:
    """Runs steps, records their outcome, and never lets one stop the rest."""

    def __init__(self):
        self.results = []

    def step(self, name, fn, needs=()):
        missing = [label for label, value in needs if not value]
        if missing:
            self._record(name, "skipped", 0, f"needs {', '.join(missing)}")
            return None
        started = time.monotonic()
        try:
            value = fn()
        except Skip as exc:
            self._record(name, "skipped", time.monotonic() - started, str(exc))
            return None
        except Exception as exc:  # noqa: BLE001 -- the point is to keep going
            logger.debug("Step %s failed:\n%s", name, traceback.format_exc())
            self._record(name, "failed", time.monotonic() - started, str(exc))
            return None
        self._record(name, "passed", time.monotonic() - started)
        return value if value is not None else True

    def _record(self, name, status, seconds, detail=""):
        result = Result(name, status, round(seconds, 1), detail[:1000])
        self.results.append(result)
        logger.info("[%s] %s (%.0fs) %s", status.upper(), name, seconds, detail[:300])

    def report(self, path):
        width = max(len(r.name) for r in self.results)
        lines = [f"{'operation'.ljust(width)}  status   secs  detail"]
        for r in self.results:
            lines.append(
                f"{r.name.ljust(width)}  {r.status.ljust(7)} {r.seconds:5.0f}  "
                f"{r.detail[:160]}"
            )
        counts = {
            s: sum(r.status == s for r in self.results)
            for s in ("passed", "failed", "skipped")
        }
        lines.append(
            "passed {passed}, failed {failed}, skipped {skipped}".format(**counts)
        )
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps([asdict(r) for r in self.results], indent=2) + "\n")
        return "\n".join(lines), counts


class Cloud:
    """Waldur's view of one tenant: waits on its resources and actions."""

    def __init__(self, api, timeout):
        self.api = api
        self.timeout = timeout

    def wait(self, url, states=("OK",), runtime=None, timeout=None):
        def check():
            obj = self.api.get(url)
            if (obj.get("state") or "").upper() == "ERRED":
                raise ApiError(
                    f"{obj.get('name') or url} is Erred: {obj.get('error_message')}"
                )
            if runtime and obj.get("runtime_state") in ("ERROR", "error"):
                raise ApiError(
                    f"{obj.get('name') or url} went to {obj.get('runtime_state')}: "
                    f"{obj.get('error_message') or 'no message'}"
                )
            if (obj.get("state") or "").upper() in {s.upper() for s in states} and (
                runtime is None or obj.get("runtime_state") in runtime
            ):
                return obj
            return None

        return wait_until(
            check, timeout=timeout or self.timeout, interval=5, description=url
        )

    def wait_gone(self, url, timeout=None):
        def check():
            # One read per poll: a check followed by a second read races the
            # deletion, and a 404 on either is the answer, not an error.
            try:
                obj = self.api.get(url)
            except ApiError as exc:
                if " -> 404:" in str(exc):
                    return True
                raise
            if (obj.get("state") or "").upper() == "ERRED":
                raise ApiError(f"deleting {url} erred: {obj.get('error_message')}")
            return None

        return wait_until(
            check,
            timeout=timeout or self.timeout,
            interval=5,
            description=f"{url} gone",
        )

    def act(self, url, action, payload=None, states=("OK",), runtime=None):
        """POST an action and wait for the resource to settle again."""
        self.api.post(f"{url.rstrip('/')}/{action}/", payload)
        # The executor marks the resource as scheduled within the request, so
        # the first poll never sees the state from before the action.
        return self.wait(url, states=states, runtime=runtime)

    def recover(self, url):
        """Put an Erred resource back to OK so later steps can still run."""
        try:
            # Let a transition in flight finish first: an action that failed
            # may still be on its way to Erred.
            def settled():
                current = self.api.get(url)
                state = (current.get("state") or "").upper()
                return current if state in ("OK", "ERRED") else None

            obj = wait_until(
                settled, timeout=120, interval=5, description=f"{url} to settle"
            )
            if (obj.get("state") or "").upper() == "ERRED":
                self.api.post(f"{url.rstrip('/')}/set_ok/")
                self.api.post(f"{url.rstrip('/')}/pull/")
                self.wait(url, timeout=120)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not recover %s: %s", url, exc)

    def order(self, offering_url, project_url, attributes, limits=None, plan=None):
        payload = {
            "offering": offering_url,
            "project": project_url,
            "attributes": attributes,
            "accepting_terms_of_service": True,
        }
        if limits:
            payload["limits"] = limits
        if plan:
            payload["plan"] = plan
        order = self.api.post("marketplace-orders/", payload)
        return self.wait_order(order["uuid"])

    def wait_order(self, order_uuid, timeout=None):
        def check():
            order = self.api.get(f"marketplace-orders/{order_uuid}/")
            state = order["state"]
            if state == "pending-consumer":
                self.api.post(f"marketplace-orders/{order_uuid}/approve_by_consumer/")
            elif state == "pending-provider":
                self.api.post(f"marketplace-orders/{order_uuid}/approve_by_provider/")
            elif state == "done":
                return order
            elif state in ("erred", "rejected", "canceled"):
                message = order.get("error_message") or self._scope_error(order)
                raise ApiError(f"order {order_uuid} {state}: {message}")
            return None

        return wait_until(
            check,
            timeout=timeout or self.timeout,
            interval=5,
            description=f"order {order_uuid}",
        )

    def _scope_error(self, order):
        """A termination order can err without a message of its own; the
        reason is then on the resource it was acting on."""
        try:
            resource = self.api.get(
                f"marketplace-resources/{order['marketplace_resource_uuid']}/"
            )
            return self.api.get(resource["scope"]).get("error_message") or ""
        except Exception:  # noqa: BLE001
            return ""

    def scope_of(self, order):
        resource = self.api.get(
            f"marketplace-resources/{order['marketplace_resource_uuid']}/"
        )
        return resource, self.api.get(resource["scope"])

    def delete(self, obj, timeout=None):
        """DELETE and wait until gone; a resource that is already gone -- a
        floating IP released with the instance it was on, say -- is done."""
        try:
            self.api.delete(obj["url"])
        except ApiError as exc:
            if " -> 404:" not in str(exc):
                raise
            return
        self.wait_gone(obj["url"], timeout=timeout)

    def remove(self, obj, attributes=None):
        """Delete a resource the way a user can: a marketplace resource is
        terminated through an order, anything else is deleted directly."""
        current = self.api.get(obj["url"])
        if current.get("marketplace_resource_uuid"):
            self.terminate(current["marketplace_resource_uuid"], attributes)
        else:
            self.api.delete(obj["url"])
        self.wait_gone(obj["url"], timeout=max(self.timeout, 900))

    def terminate(self, resource_uuid, attributes=None):
        # Gone with something else already -- a volume deleted along with the
        # instance it was still attached to, say.
        resource = self.api.get(f"marketplace-resources/{resource_uuid}/")
        if resource.get("state") == "Terminated":
            return None
        response = self.api.post(
            f"marketplace-resources/{resource_uuid}/terminate/",
            {"attributes": attributes or {}},
        )
        return self.wait_order(response["order_uuid"], timeout=max(self.timeout, 900))


@contextlib.contextmanager
def cleanup(undo):
    """Run ``undo`` after the block, without letting its failure hide the
    block's own: the block's error is the one a step should report."""
    try:
        yield
    except BaseException:
        try:
            undo()
        except Exception as exc:  # noqa: BLE001
            logger.warning("Cleanup after a failed step also failed: %s", exc)
        raise
    undo()


def pick(items, name, what, key="name"):
    if name:
        for item in items:
            if name in (item.get(key), item.get("backend_id"), item.get("uuid")):
                return item
        raise Skip(f"{what} {name!r} is not visible to the tenant")
    if not items:
        raise ApiError(f"the tenant sees no {what}")
    return items[0]


def ip_in(instance, cidr):
    """The instance's address on the subnet with this CIDR."""
    network = ipaddress.ip_network(cidr)
    candidates = [
        fixed_ip.get("ip_address")
        for port in instance.get("ports") or []
        for fixed_ip in port.get("fixed_ips") or []
    ] + list(instance.get("internal_ips") or [])
    for address in candidates:
        if address and ipaddress.ip_address(address) in network:
            return address
    return None


def run_compat(cfg):
    """Run every operation against the cloud and return the recorded Run."""
    api = Api(cfg.waldur_url, cfg.waldur_token, verify=cfg.waldur_verify_ssl)
    cloud = Cloud(api, cfg.timeout)
    run = Run()
    creds = {
        "auth_url": cfg.os_auth_url,
        "username": cfg.os_username,
        "password": cfg.os_password,
        "project_name": cfg.os_project,
        "domain": cfg.os_domain,
    }
    ctx = {}

    discovery_payload = {
        "auth_url": creds["auth_url"],
        "username": creds["username"],
        "password": creds["password"],
        "user_domain_name": creds["domain"],
        "project_domain_name": creds["domain"],
        "project_name": creds["project_name"],
        "verify_ssl": cfg.os_verify_ssl,
    }

    # -- Discovery: the stateless checks an operator runs before onboarding --

    run.step(
        "discovery: validate credentials",
        lambda: api.post(
            "openstack/discovery/validate_credentials/", discovery_payload
        ),
    )

    def discover_external_network():
        networks = api.post(
            "openstack/discovery/discover_external_networks/", discovery_payload
        )
        wanted = cfg.external_network
        chosen = pick(networks, wanted, "external network", key="name")
        ctx["external_network_id"] = chosen["id"]
        return chosen

    run.step("discovery: external networks", discover_external_network)
    for kind in (
        "flavors",
        "volume_types",
        "instance_availability_zones",
        "volume_availability_zones",
    ):
        run.step(
            f"discovery: {kind.replace('_', ' ')}",
            lambda kind=kind: api.post(
                f"openstack/discovery/discover_{kind}/", discovery_payload
            ),
        )

    # -- Provider side: organization, offering, service settings --

    def setup_provider():
        customer = api.post("customers/", {"name": f"OS compat {SUFFIX}"})
        project = api.post(
            "projects/", {"name": f"OS compat {SUFFIX}", "customer": customer["url"]}
        )
        api.post("marketplace-service-providers/", {"customer": customer["url"]})
        categories = api.get("marketplace-categories/", title="OpenStack compat")
        category = (
            categories[0]
            if categories
            else api.post("marketplace-categories/", {"title": "OpenStack compat"})
        )
        ctx.update(customer=customer, project=project, category=category)

    run.step("setup: organization, project, service provider", setup_provider)

    def create_offering():
        components = [
            {
                "type": component,
                "name": component.title(),
                "measured_unit": unit,
                "billing_type": "limit",
                "limit_period": None,
            }
            for component, unit in (
                ("cores", "cores"),
                ("ram", "MB"),
                ("storage", "MB"),
            )
        ]
        offering = api.post(
            "marketplace-provider-offerings/",
            {
                "name": f"OS compat {SUFFIX}",
                "category": ctx["category"]["url"],
                "customer": ctx["customer"]["url"],
                "type": "OpenStack.Tenant",
                "shared": True,
                "attributes": {},
                "plugin_options": {"storage_mode": "fixed"},
                "components": components,
                "plans": [{"name": "Default", "unit": "month"}],
            },
        )
        ctx["offering"] = offering
        offering_path = f"marketplace-provider-offerings/{offering['uuid']}"
        # Creation ignores service_attributes: the service settings come into
        # being when the integration is written, as the Credentials tab does.
        api.post(
            f"{offering_path}/update_integration/",
            {
                "service_attributes": {
                    "backend_url": creds["auth_url"],
                    "username": creds["username"],
                    "password": creds["password"],
                    "tenant_name": creds["project_name"],
                    "domain": creds["domain"],
                    "external_network_id": ctx["external_network_id"],
                    "verify_ssl": cfg.os_verify_ssl,
                    "live_resize_of_volumes_enabled": cfg.live_volume_resize,
                }
            },
        )
        api.post(f"{offering_path}/activate/")
        resyncs = iter(range(2))

        def settings_ok():
            current = api.get(f"{offering_path}/")
            state = (current.get("scope_state") or "").upper()
            if state == "ERRED":
                # A pull racing the settings' own creation can fail once;
                # an operator would press Synchronize again.
                if next(resyncs, None) is None:
                    raise ApiError(
                        f"service settings Erred: {current.get('scope_error_message')}"
                    )
                api.post(f"{offering_path}/sync/")
            elif not state:
                api.post(f"{offering_path}/sync/")
            return current if state == "OK" else None

        ctx["offering"] = wait_until(
            settings_ok,
            timeout=cfg.timeout,
            interval=5,
            description="service settings OK",
        )
        ctx["settings_uuid"] = ctx["offering"]["scope_uuid"]

    run.step(
        "offering: register cloud and pull service properties",
        create_offering,
        needs=[
            ("project", ctx.get("project")),
            ("external network", ctx.get("external_network_id")),
        ],
    )

    have_offering = ("offering", ctx.get("settings_uuid"))

    def settings_properties():
        settings = ctx["settings_uuid"]
        counts = {
            kind: len(api.get(f"openstack-{kind}/", settings_uuid=settings))
            for kind in ("flavors", "images", "volume-types")
        }
        empty = [k for k, v in counts.items() if not v]
        if empty:
            raise ApiError(f"nothing pulled for {empty}: {counts}")
        return counts

    run.step(
        "pull: flavors, images, volume types",
        settings_properties,
        needs=[have_offering],
    )

    def placement_reads():
        settings = ctx["settings_uuid"]
        hypervisors = api.get("openstack-hypervisors/", settings_uuid=settings)
        if not hypervisors:
            raise ApiError("no hypervisors pulled (Nova os-hypervisors or Placement)")
        api.get("openstack-hypervisors/summary/", settings_uuid=settings)
        api.get(
            "openstack-hypervisors/allocation_candidates/",
            settings_uuid=settings,
            resources="VCPU:1,MEMORY_MB:512",
            limit=5,
        )
        return len(hypervisors)

    run.step(
        "placement: hypervisors, inventories, allocation candidates",
        placement_reads,
        needs=[have_offering],
    )

    # -- Tenant --

    def public_offering(offering):
        """Orders take the public offering and its plans, not the provider's."""
        return api.get(f"marketplace-public-offerings/{offering['uuid']}/")

    def order_tenant(name, key, **extra):
        order = cloud.order(
            public_offering(ctx["offering"])["url"],
            ctx["project"]["url"],
            {"name": name, "subnet_cidr": TENANT_CIDR, **extra},
            limits={"cores": 40, "ram": 81920, "storage": 512000},
            plan=public_offering(ctx["offering"])["plans"][0]["url"],
        )
        resource, tenant = cloud.scope_of(order)
        ctx[key] = resource  # teardown terminates it even if the wait fails
        return resource, cloud.wait(tenant["url"])

    def create_tenant():
        _, tenant = order_tenant(f"oscompat-{SUFFIX}", "tenant_resource")
        ctx["tenant"] = tenant

    run.step(
        "tenant: create (Keystone project, user, roles, router, network, subnet)",
        create_tenant,
        needs=[have_offering],
    )
    tenant = ctx.get("tenant")
    has_tenant = ("tenant", tenant)
    tid = tenant and tenant["uuid"]
    turl = tenant and tenant["url"]

    try:
        run.step("tenant: pull", lambda: cloud.act(turl, "pull"), needs=[has_tenant])
        run.step(
            "tenant: update name and description",
            lambda: (
                api.patch(turl, {"description": "compatibility run"}),
                cloud.wait(turl),
            ),
            needs=[has_tenant],
        )
        run.step(
            "tenant: change user password",
            lambda: cloud.act(
                turl, "change_password", {"user_password": secrets.token_urlsafe(16)}
            ),
            needs=[has_tenant],
        )

        def set_quotas():
            cloud.act(
                turl,
                "set_quotas",
                {
                    "instances": 15,
                    "volumes": 30,
                    "snapshots": 40,
                    "vcpu": 30,
                    "ram": 61440,
                    "storage": 409600,
                    "security_group_count": 20,
                    "security_group_rule_count": 200,
                    "floating_ip_count": 4,
                    "network_count": 10,
                    "subnet_count": 10,
                    "port_count": 100,
                },
            )
            cloud.act(turl, "pull_quotas")
            quotas = {q["name"]: q["limit"] for q in api.get(turl).get("quotas", [])}
            if quotas.get("instances") not in (None, 15):
                raise ApiError(
                    f"instances quota reads back as {quotas.get('instances')}"
                )
            return quotas

        run.step(
            "tenant: set and pull quotas (Nova, Cinder, Neutron)",
            set_quotas,
            needs=[has_tenant],
        )

        def tenant_properties():
            flavors = api.get("openstack-flavors/", tenant_uuid=tid, o="ram")
            images = api.get("openstack-images/", tenant_uuid=tid)
            volume_types = api.get("openstack-volume-types/", tenant_uuid=tid)
            ctx["instance_azs"] = api.get(
                "openstack-instance-availability-zones/", tenant_uuid=tid
            )
            ctx["volume_azs"] = api.get(
                "openstack-volume-availability-zones/", tenant_uuid=tid
            )

            flavor = pick(flavors, cfg.flavor, "flavor")
            resize_name = cfg.resize_flavor
            bigger = [
                f
                for f in flavors
                if f["ram"] > flavor["ram"] and f["disk"] == flavor["disk"]
            ]
            ctx["resize_flavor"] = (
                pick(flavors, resize_name, "flavor")
                if resize_name
                else (bigger[0] if bigger else None)
            )
            plain = [i for i in images if not i.get("is_rescue_image")]
            ctx["image"] = pick(plain, cfg.image, "image")
            rescue_name = cfg.rescue_image
            rescue = [i for i in images if i.get("is_rescue_image")]
            ctx["rescue_image"] = (
                pick(images, rescue_name, "image")
                if rescue_name
                else (rescue[0] if rescue else None)
            )
            ctx["volume_type"] = pick(volume_types, cfg.volume_type, "volume type")
            retype = cfg.retype_to
            ctx["retype_to"] = (
                pick(volume_types, retype, "volume type") if retype else None
            )
            ctx["flavor"] = flavor
            return {
                "flavors": len(flavors),
                "images": len(images),
                "volume_types": len(volume_types),
            }

        run.step(
            "tenant: flavors, images, volume types, availability zones",
            tenant_properties,
            needs=[has_tenant],
        )

        def defaults():
            ctx["default_subnet"] = pick(
                api.get("openstack-subnets/", tenant_uuid=tid), None, "subnet"
            )
            ctx["router"] = pick(
                api.get("openstack-routers/", tenant_uuid=tid), None, "router"
            )
            groups = api.get("openstack-security-groups/", tenant_uuid=tid)
            ctx["default_sg"] = pick(groups, "default", "security group")

        run.step(
            "tenant: default subnet, router, security group",
            defaults,
            needs=[has_tenant],
        )

        for action in (
            "pull_security_groups",
            "pull_server_groups",
            "pull_floating_ips",
        ):
            run.step(
                f"tenant: {action}",
                lambda action=action: cloud.act(turl, action),
                needs=[has_tenant],
            )
        for view in ("backend_instances", "backend_volumes", "topology"):
            run.step(
                f"tenant: {view}",
                lambda view=view: api.get(f"openstack-tenants/{tid}/{view}/"),
                needs=[has_tenant],
            )

        # -- Security groups --

        def security_group():
            group = api.post(
                f"openstack-tenants/{tid}/create_security_group/",
                {
                    "name": f"compat-sg-{SUFFIX}",
                    "description": "compatibility run",
                    "rules": [
                        {
                            "ethertype": "IPv4",
                            "direction": "ingress",
                            "protocol": "tcp",
                            "from_port": 22,
                            "to_port": 22,
                            "cidr": "0.0.0.0/0",
                        },
                        {
                            "ethertype": "IPv4",
                            "direction": "ingress",
                            "protocol": "icmp",
                            "from_port": -1,
                            "to_port": -1,
                            "cidr": "0.0.0.0/0",
                        },
                    ],
                },
            )
            ctx["sg"] = cloud.wait(group["url"])

        run.step(
            "security group: create with rules", security_group, needs=[has_tenant]
        )
        sg = ctx.get("sg")

        def set_rules():
            cloud.act(
                sg["url"],
                "set_rules",
                [
                    {
                        "ethertype": "IPv4",
                        "direction": "ingress",
                        "protocol": "tcp",
                        "from_port": 22,
                        "to_port": 22,
                        "cidr": "0.0.0.0/0",
                    },
                    {
                        "ethertype": "IPv4",
                        "direction": "ingress",
                        "protocol": "tcp",
                        "from_port": 80,
                        "to_port": 80,
                        "cidr": "0.0.0.0/0",
                    },
                    {
                        "ethertype": "IPv4",
                        "direction": "ingress",
                        "protocol": "tcp",
                        "from_port": 1,
                        "to_port": 65535,
                        "remote_group": sg["url"],
                    },
                ],
            )

        run.step(
            "security group: replace rules (incl. remote group)",
            set_rules,
            needs=[("sg", sg)],
        )

        def update_sg():
            api.patch(sg["url"], {"description": "compatibility run, updated"})
            cloud.wait(sg["url"])

        run.step("security group: update", update_sg, needs=[("sg", sg)])

        # -- Networks, subnets, routers --

        def network():
            net = api.post(
                f"openstack-tenants/{tid}/create_network/",
                {"name": f"compat-net-{SUFFIX}"},
            )
            ctx["network"] = cloud.wait(net["url"])

        run.step("network: create", network, needs=[has_tenant])
        net = ctx.get("network")
        run.step(
            "network: update",
            lambda: (
                api.patch(net["url"], {"description": "compat"}),
                cloud.wait(net["url"]),
            ),
            needs=[("network", net)],
        )
        run.step(
            "network: set MTU",
            lambda: cloud.act(net["url"], "set_mtu", {"mtu": 1400}),
            needs=[("network", net)],
        )

        def subnet():
            sub = api.post(
                f"{net['url'].rstrip('/')}/create_subnet/",
                {
                    "name": f"compat-subnet-{SUFFIX}",
                    "cidr": NETWORK_CIDR,
                    "dns_nameservers": ["1.1.1.1"],
                    "allocation_pools": [{"start": "10.77.0.10", "end": "10.77.0.200"}],
                },
            )
            ctx["subnet"] = cloud.wait(sub["url"])

        run.step(
            "subnet: create (attached to the tenant router)",
            subnet,
            needs=[("network", net)],
        )
        sub = ctx.get("subnet")

        def update_subnet():
            api.patch(
                sub["url"],
                {
                    "name": sub["name"],
                    "host_routes": [
                        {"destination": "10.99.0.0/24", "nexthop": "10.77.0.5"}
                    ],
                },
            )
            cloud.wait(sub["url"])

        run.step("subnet: update host routes", update_subnet, needs=[("subnet", sub)])
        run.step(
            "subnet: disconnect from router",
            lambda: cloud.act(sub["url"], "disconnect"),
            needs=[("subnet", sub)],
        )
        run.step(
            "subnet: connect to router",
            lambda: cloud.act(sub["url"], "connect"),
            needs=[("subnet", sub)],
        )

        router = ctx.get("router")

        def routes():
            api.post(
                f"{router['url'].rstrip('/')}/set_routes/",
                {"routes": [{"destination": "10.98.0.0/24", "nexthop": "10.77.0.6"}]},
            )
            cloud.wait(router["url"])
            api.post(f"{router['url'].rstrip('/')}/set_routes/", {"routes": []})
            cloud.wait(router["url"])

        run.step(
            "router: set and clear static routes",
            routes,
            needs=[("router", router), ("subnet", sub)],
        )

        def gateway():
            api.post(f"{router['url'].rstrip('/')}/remove_external_gateway/")
            cloud.wait(router["url"])
            api.post(
                f"{router['url'].rstrip('/')}/set_external_gateway/",
                {
                    "external_network_id": ctx["external_network_id"],
                    "enable_snat": True,
                },
            )
            cloud.wait(router["url"])

        run.step(
            "router: remove and set external gateway",
            gateway,
            needs=[("router", router)],
        )

        def router_interface():
            api.post(
                f"{router['url'].rstrip('/')}/remove_router_interface/",
                {"subnet": sub["url"]},
            )
            cloud.wait(router["url"])
            api.post(
                f"{router['url'].rstrip('/')}/add_router_interface/",
                {"subnet": sub["url"]},
            )
            cloud.wait(router["url"])

        run.step(
            "router: remove and add interface",
            router_interface,
            needs=[("router", router), ("subnet", sub)],
        )

        def extra_router():
            created = api.post(
                "openstack-routers/",
                {"tenant": turl, "name": f"compat-router-{SUFFIX}"},
            )
            extra = cloud.wait(created["url"])
            api.delete(extra["url"])
            cloud.wait_gone(extra["url"])

        run.step(
            "router: create and delete a second router",
            extra_router,
            needs=[has_tenant],
        )

        # -- Ports --

        def port():
            created = api.post(
                "openstack-ports/",
                {
                    "name": f"compat-port-{SUFFIX}",
                    "network": net["url"],
                    "security_groups": [{"url": sg["url"]}],
                },
            )
            ctx["port"] = cloud.wait(created["url"])

        run.step(
            "port: create with security group",
            port,
            needs=[("network", net), ("subnet", sub), ("sg", sg)],
        )
        prt = ctx.get("port")
        has_port = ("port", prt)
        run.step(
            "port: update fixed IP",
            lambda: cloud.act(
                prt["url"],
                "update_port_ip",
                {"subnet": sub["url"], "ip_address": PORT_IP_MOVED},
            ),
            needs=[has_port],
        )
        run.step(
            "port: set allowed address pairs",
            lambda: cloud.act(
                prt["url"],
                "set_allowed_address_pairs",
                {"allowed_address_pairs": [{"ip_address": PAIR_CIDR}]},
            ),
            needs=[has_port],
        )
        run.step(
            "port: update security groups",
            lambda: cloud.act(
                prt["url"],
                "update_security_groups",
                {"security_groups": [sg["url"], ctx["default_sg"]["url"]]},
            ),
            needs=[has_port, ("default sg", ctx.get("default_sg"))],
        )
        run.step(
            "port: disable",
            lambda: cloud.act(prt["url"], "disable_port"),
            needs=[has_port],
        )
        run.step(
            "port: enable",
            lambda: cloud.act(prt["url"], "enable_port"),
            needs=[has_port],
        )

        def port_security_off():
            cloud.act(prt["url"], "update_security_groups", {"security_groups": []})
            api.post(
                f"{prt['url'].rstrip('/')}/set_allowed_address_pairs/",
                {"allowed_address_pairs": []},
            )
            cloud.wait(prt["url"])
            cloud.act(prt["url"], "disable_port_security")

        run.step("port: disable port security", port_security_off, needs=[has_port])
        run.step(
            "port: enable port security",
            lambda: cloud.act(prt["url"], "enable_port_security"),
            needs=[has_port],
        )

        # -- Floating IPs --

        def floating_ip():
            created = api.post(
                f"openstack-tenants/{tid}/create_floating_ip/",
                {"router": router["url"]},
            )
            ctx["fip"] = cloud.wait(created["url"])

        run.step(
            "floating IP: allocate", floating_ip, needs=[has_tenant, ("router", router)]
        )
        fip = ctx.get("fip")
        run.step(
            "floating IP: attach to port",
            lambda: cloud.act(fip["url"], "attach_to_port", {"port": prt["url"]}),
            needs=[("fip", fip), has_port],
        )
        run.step(
            "floating IP: detach from port",
            lambda: cloud.act(fip["url"], "detach_from_port"),
            needs=[("fip", fip), has_port],
        )
        run.step(
            "floating IP: update description",
            lambda: cloud.act(
                fip["url"], "update_description", {"description": "compat"}
            ),
            needs=[("fip", fip)],
        )

        # -- Server group --

        def server_group():
            created = api.post(
                f"openstack-tenants/{tid}/create_server_group/",
                {"name": f"compat-group-{SUFFIX}", "policy": "soft-anti-affinity"},
            )
            ctx["server_group"] = cloud.wait(created["url"])

        run.step("server group: create", server_group, needs=[has_tenant])

        # -- Instance --

        def offering_of(kind):
            # The offering's scope is the tenant, which the offering list's
            # scope_uuid filter does not search; its name is fixed, though.
            prefix = {
                "OpenStack.Instance": "Virtual machine",
                "OpenStack.Volume": "Volume",
            }[kind]
            offerings = api.get(
                "marketplace-provider-offerings/",
                name_exact=f"{prefix} in {tenant['name']}",
                type=kind,
            )
            if not offerings:
                raise ApiError(f"no {kind} offering was created for the tenant")
            return public_offering(offerings[0])

        def instance():
            image = ctx["image"]
            # min_disk is in MiB, as the order wants it
            system_volume_mib = max(image.get("min_disk") or 0, 10240)
            attributes = {
                "name": f"compat-vm-{SUFFIX}",
                "flavor": ctx["flavor"]["url"],
                "image": image["url"],
                "system_volume_size": system_volume_mib,
                "system_volume_type": ctx["volume_type"]["url"],
                "data_volume_size": 1024,
                "data_volume_type": ctx["volume_type"]["url"],
                "ports": [{"subnet": ctx["default_subnet"]["url"]}],
                "floating_ips": [{"subnet": ctx["default_subnet"]["url"]}],
                "security_groups": [
                    {"url": ctx["default_sg"]["url"]},
                    {"url": sg["url"]},
                ],
                "user_data": "#cloud-config\n",
                "metadata": {"purpose": "compat"},
            }
            if ctx.get("server_group"):
                attributes["server_group"] = {"url": ctx["server_group"]["url"]}
            order = cloud.order(
                offering_of("OpenStack.Instance")["url"],
                ctx["project"]["url"],
                attributes,
            )
            resource, vm = cloud.scope_of(order)
            ctx["vm_resource"] = resource
            ctx["vm"] = cloud.wait(vm["url"], runtime=("ACTIVE",))

        run.step(
            "instance: create (boot from volume, data volume, FIP, SGs, server group)",
            instance,
            needs=[
                has_tenant,
                ("flavor/image", ctx.get("image")),
                ("default subnet", ctx.get("default_subnet")),
                ("sg", sg),
            ],
        )
        vm = ctx.get("vm")
        has_vm = ("instance", vm)
        vurl = vm and vm["url"]

        def guarded(fn):
            """An instance action, followed by recovery if it left it Erred."""

            def wrapped():
                try:
                    return fn()
                finally:
                    cloud.recover(vurl)

            return wrapped

        run.step(
            "instance: pull", guarded(lambda: cloud.act(vurl, "pull")), needs=[has_vm]
        )
        run.step(
            "instance: update name",
            guarded(
                lambda: (
                    api.patch(vurl, {"name": vm["name"], "description": "compat"}),
                    cloud.wait(vurl),
                )
            ),
            needs=[has_vm],
        )
        run.step(
            "instance: console URL",
            lambda: api.get(f"{vurl.rstrip('/')}/console/")["url"],
            needs=[has_vm],
        )
        run.step(
            "instance: console log",
            lambda: api.get(f"{vurl.rstrip('/')}/console_log/", length=20),
            needs=[has_vm],
        )
        run.step(
            "instance: set metadata",
            guarded(
                lambda: cloud.act(
                    vurl,
                    "set_metadata",
                    {"metadata": {"purpose": "compat", "run": SUFFIX}},
                )
            ),
            needs=[has_vm],
        )
        run.step(
            "instance: placement allocations",
            lambda: api.get(f"{vurl.rstrip('/')}/placement_allocations/"),
            needs=[has_vm],
        )
        run.step(
            "instance: diagnose connectivity",
            lambda: api.post(
                f"{vurl.rstrip('/')}/diagnose_connectivity/", {"target": "external"}
            ),
            needs=[has_vm],
        )
        run.step(
            "instance: stop",
            guarded(lambda: cloud.act(vurl, "stop", runtime=("SHUTOFF",))),
            needs=[has_vm],
        )

        def resize():
            if not ctx.get("resize_flavor"):
                raise Skip(
                    "no larger flavor with the same disk; name one with --resize-flavor"
                )
            current = cloud.wait(vurl)
            if current.get("runtime_state") != "SHUTOFF":
                cloud.act(vurl, "stop", runtime=("SHUTOFF",))
            cloud.act(
                vurl,
                "change_flavor",
                {"flavor": ctx["resize_flavor"]["url"]},
                runtime=("SHUTOFF", "ACTIVE"),
            )
            resized = api.get(vurl)
            if resized.get("flavor_name") != ctx["resize_flavor"]["name"]:
                raise ApiError(f"flavor reads back as {resized.get('flavor_name')}")

        run.step(
            "instance: resize (change flavor, confirm)", guarded(resize), needs=[has_vm]
        )
        run.step(
            "instance: start",
            guarded(lambda: cloud.act(vurl, "start", runtime=("ACTIVE",))),
            needs=[has_vm],
        )
        run.step(
            "instance: restart",
            guarded(lambda: cloud.act(vurl, "restart", runtime=("ACTIVE",))),
            needs=[has_vm],
        )

        def rescue():
            if not ctx.get("rescue_image"):
                raise Skip(
                    "no rescue image (hw_rescue_device/hw_rescue_bus) visible to the tenant"
                )
            if cloud.wait(vurl).get("runtime_state") != "ACTIVE":
                cloud.act(vurl, "start", runtime=("ACTIVE",))
            cloud.act(
                vurl,
                "rescue",
                {"rescue_image": ctx["rescue_image"]["url"]},
                runtime=("RESCUE",),
            )
            cloud.act(vurl, "unrescue", runtime=("ACTIVE",))

        run.step(
            "instance: update security groups",
            guarded(
                lambda: cloud.act(
                    vurl,
                    "update_security_groups",
                    {"security_groups": [ctx["default_sg"]["url"]]},
                )
            ),
            needs=[has_vm],
        )
        run.step(
            "instance: update ports (attach interface on a second network)",
            guarded(
                lambda: cloud.act(
                    vurl,
                    "update_ports",
                    {
                        "ports": [
                            {"subnet": ctx["default_subnet"]["url"]},
                            {"subnet": sub["url"]},
                        ]
                    },
                )
            ),
            needs=[has_vm, ("subnet", sub)],
        )
        run.step(
            "instance: update allowed address pairs",
            guarded(
                lambda: cloud.act(
                    vurl,
                    "update_allowed_address_pairs",
                    {
                        "subnet": ctx["default_subnet"]["url"],
                        "allowed_address_pairs": [{"ip_address": "10.76.0.240/28"}],
                    },
                )
            ),
            needs=[has_vm],
        )
        run.step(
            "instance: update floating IPs",
            guarded(
                lambda: cloud.act(
                    vurl,
                    "update_floating_ips",
                    {"floating_ips": [{"subnet": ctx["default_subnet"]["url"]}]},
                )
            ),
            needs=[has_vm],
        )

        # -- Volumes and snapshots --

        def volume():
            order = cloud.order(
                offering_of("OpenStack.Volume")["url"],
                ctx["project"]["url"],
                {
                    "name": f"compat-vol-{SUFFIX}",
                    "size": 1024,
                    "type": ctx["volume_type"]["url"],
                },
            )
            resource, vol = cloud.scope_of(order)
            ctx["volume_resource"] = resource
            ctx["volume"] = cloud.wait(vol["url"], runtime=("available",))

        run.step(
            "volume: create",
            volume,
            needs=[has_tenant, ("volume type", ctx.get("volume_type"))],
        )
        vol = ctx.get("volume")
        has_vol = ("volume", vol)
        volurl = vol and vol["url"]

        def vguarded(fn):
            def wrapped():
                try:
                    return fn()
                finally:
                    cloud.recover(volurl)

            return wrapped

        run.step(
            "volume: update",
            vguarded(
                lambda: (
                    api.patch(volurl, {"name": vol["name"], "description": "compat"}),
                    cloud.wait(volurl),
                )
            ),
            needs=[has_vol],
        )
        run.step(
            "volume: attach to instance",
            vguarded(
                lambda: cloud.act(
                    volurl, "attach", {"instance": vurl}, runtime=("in-use",)
                )
            ),
            needs=[has_vol, has_vm],
        )
        run.step(
            "volume: detach",
            vguarded(lambda: cloud.act(volurl, "detach", runtime=("available",))),
            needs=[has_vol, has_vm],
        )
        run.step(
            "volume: extend",
            vguarded(lambda: cloud.act(volurl, "extend", {"disk_size": 2048})),
            needs=[has_vol],
        )

        def retype():
            if not ctx.get("retype_to"):
                raise Skip("name a second volume type with --retype-to")
            cloud.act(volurl, "retype", {"type": ctx["retype_to"]["url"]})

        run.step("volume: retype", vguarded(retype), needs=[has_vol])

        def extend_attached():
            # Without live resize Waldur extends an attached volume only with
            # its instance stopped; with it, it asks Cinder for an in-use
            # extend (microversion 3.51).
            cloud.act(volurl, "attach", {"instance": vurl}, runtime=("in-use",))

            def detach():
                cloud.recover(volurl)
                cloud.act(volurl, "detach", runtime=("available",))

            def restart():
                # A failed extend errs the instance too; set it right first.
                cloud.recover(vurl)
                cloud.act(vurl, "start", runtime=("ACTIVE",))

            with cleanup(detach):
                if cfg.live_volume_resize:
                    cloud.act(volurl, "extend", {"disk_size": 3072})
                    return
                cloud.act(vurl, "stop", runtime=("SHUTOFF",))
                with cleanup(restart):
                    cloud.act(volurl, "extend", {"disk_size": 3072})

        run.step(
            "volume: extend while attached"
            + (
                " (live, Cinder 3.51)"
                if cfg.live_volume_resize
                else " (instance stopped)"
            ),
            vguarded(extend_attached),
            needs=[has_vol, has_vm],
        )

        def snapshot():
            snap = api.post(
                f"{volurl.rstrip('/')}/snapshot/", {"name": f"compat-snap-{SUFFIX}"}
            )
            ctx["snapshot"] = cloud.wait(snap["url"])

        run.step("snapshot: create", snapshot, needs=[has_vol])
        snap = ctx.get("snapshot")

        def snapshot_restore():
            api.post(
                f"{snap['url'].rstrip('/')}/restore/",
                {"name": f"compat-restored-{SUFFIX}"},
            )
            restored = wait_until(
                lambda: api.get(
                    "openstack-volumes/",
                    tenant_uuid=tid,
                    name=f"compat-restored-{SUFFIX}",
                ),
                timeout=120,
                interval=5,
                description="restored volume",
            )[0]
            restored = cloud.wait(restored["url"])
            cloud.remove(restored)

        run.step(
            "snapshot: restore to a volume, delete it",
            snapshot_restore,
            needs=[("snapshot", snap)],
        )

        def snapshot_delete():
            api.delete(snap["url"])
            cloud.wait_gone(snap["url"])

        run.step("snapshot: delete", snapshot_delete, needs=[("snapshot", snap)])

        # -- Backups (Cinder snapshots of every instance volume) --

        def backup():
            created = api.post(
                f"{vurl.rstrip('/')}/backup/", {"name": f"compat-backup-{SUFFIX}"}
            )
            ctx["backup"] = cloud.wait(created["url"])

        run.step("backup: create", guarded(backup), needs=[has_vm])
        bkp = ctx.get("backup")

        def backup_restore():
            api.post(
                f"{bkp['url'].rstrip('/')}/restore/",
                {
                    "flavor": ctx["flavor"]["url"],
                    "name": f"compat-restored-vm-{SUFFIX}",
                    "ports": [{"subnet": ctx["default_subnet"]["url"]}],
                    "security_groups": [{"url": ctx["default_sg"]["url"]}],
                },
            )
            restored = wait_until(
                lambda: api.get(
                    "openstack-instances/",
                    tenant_uuid=tid,
                    name=f"compat-restored-vm-{SUFFIX}",
                ),
                timeout=120,
                interval=5,
                description="restored instance",
            )[0]
            ctx["restored_vm"] = cloud.wait(restored["url"], runtime=("ACTIVE",))

        run.step(
            "backup: restore to a new instance", backup_restore, needs=[("backup", bkp)]
        )

        def restored_delete():
            cloud.remove(
                ctx["restored_vm"],
                {"delete_volumes": True, "release_floating_ips": True},
            )
            ctx.pop("restored_vm")

        # Before the backup: on copy-on-write storage such as Ceph RBD the
        # restored volumes are clones of the backup's snapshots, and Cinder
        # refuses to delete a snapshot that still has dependent volumes.
        run.step(
            "backup: delete the restored instance",
            restored_delete,
            needs=[("restored instance", ctx.get("restored_vm"))],
        )

        def backup_delete():
            api.delete(bkp["url"])
            cloud.wait_gone(bkp["url"])

        run.step("backup: delete", backup_delete, needs=[("backup", bkp)])

        # -- Load balancer (Octavia) --

        def delete_lb_objects():
            """Delete the load balancer and what hangs off it, newest first."""
            for obj in reversed(ctx.get("lb_objects", [])):
                cloud.delete(obj, timeout=max(cfg.timeout, 900))
            ctx["lb_objects"] = []
            ctx.pop("lb", None)

        ctx["delete_lb_objects"] = delete_lb_objects

        def load_balancer():
            created = api.post(
                "openstack-loadbalancers/",
                {
                    "name": f"compat-lb-{SUFFIX}",
                    "tenant": turl,
                    "vip_subnet": ctx["default_subnet"]["url"],
                },
            )
            # Recorded at once: tenant termination does not delete load
            # balancers, so teardown must know of one that never got ready.
            ctx["lb_objects"] = [created]
            lb_url = cloud.wait(created["url"], timeout=max(cfg.timeout, 900))["url"]

            def active():
                current = api.get(lb_url)
                status = current.get("provisioning_status")
                if status == "ERROR":
                    raise ApiError("Octavia reports provisioning_status ERROR")
                if status == "ACTIVE":
                    return current
                cloud.act(lb_url, "pull")
                return None

            ctx["lb"] = wait_until(
                active,
                timeout=max(cfg.timeout, 900),
                interval=10,
                description="load balancer ACTIVE",
            )

        def vip_port_ready():
            """Octavia builds the VIP port after the API call returns; Waldur
            links it on a pull and refuses the VIP actions until then."""

            def check():
                current = api.get(lb["url"])
                if current.get("vip_port"):
                    return current
                cloud.act(lb["url"], "pull")
                return None

            wait_until(
                check,
                timeout=180,
                interval=10,
                description="load balancer VIP port in Waldur",
            )

        run.step(
            "load balancer: create",
            load_balancer,
            needs=[has_tenant, ("default subnet", ctx.get("default_subnet"))],
        )
        lb = ctx.get("lb")
        has_lb = ("load balancer", lb)

        def lb_children():
            pool = api.post(
                "openstack-pools/",
                {
                    "name": f"compat-pool-{SUFFIX}",
                    "load_balancer": lb["url"],
                    "protocol": "TCP",
                    "lb_algorithm": "SOURCE_IP_PORT",
                },
            )
            ctx["lb_objects"].append(pool)
            ctx["pool"] = cloud.wait(pool["url"])
            listener = api.post(
                "openstack-listeners/",
                {
                    "name": f"compat-listener-{SUFFIX}",
                    "load_balancer": lb["url"],
                    "protocol": "TCP",
                    "protocol_port": 80,
                    "default_pool": ctx["pool"]["url"],
                },
            )
            ctx["lb_objects"].append(listener)
            ctx["listener"] = cloud.wait(listener["url"])

        run.step("load balancer: pool and listener", lb_children, needs=[has_lb])

        def lb_member():
            address = ip_in(api.get(vurl), ctx["default_subnet"]["cidr"])
            if not address:
                raise ApiError("instance has no fixed IP to add as a member")
            member = api.post(
                "openstack-pool-members/",
                {
                    "name": f"compat-member-{SUFFIX}",
                    "pool": ctx["pool"]["url"],
                    "address": address,
                    "protocol_port": 80,
                    "subnet": ctx["default_subnet"]["url"],
                    "weight": 1,
                },
            )
            ctx["lb_objects"].append(member)
            ctx["member"] = cloud.wait(member["url"])
            api.patch(ctx["member"]["url"], {"weight": 2})
            cloud.wait(ctx["member"]["url"])

        run.step(
            "load balancer: pool member",
            lb_member,
            needs=[("pool", ctx.get("pool")), has_vm],
        )

        def health_monitor():
            monitor = api.post(
                "openstack-health-monitors/",
                {
                    "name": f"compat-hm-{SUFFIX}",
                    "pool": ctx["pool"]["url"],
                    "type": "TCP",
                    "delay": 10,
                    "timeout": 5,
                    "max_retries": 3,
                    "max_retries_down": 3,
                },
            )
            ctx["lb_objects"].append(monitor)
            ctx["monitor"] = cloud.wait(monitor["url"])

        run.step(
            "load balancer: health monitor",
            health_monitor,
            needs=[("pool", ctx.get("pool"))],
        )

        def lb_guarded(fn):
            """A load balancer action, followed by recovery if it left the
            load balancer Erred, so the next action still has one to act on."""

            def wrapped():
                try:
                    return fn()
                finally:
                    cloud.recover(lb["url"])

            return wrapped

        lb_fip = run.step(
            "load balancer: attach floating IP",
            lb_guarded(
                lambda: (
                    vip_port_ready()
                    or cloud.act(
                        lb["url"], "attach_floating_ip", {"floating_ip": fip["url"]}
                    )
                )
            ),
            needs=[has_lb, ("fip", fip)],
        )
        run.step(
            "load balancer: detach floating IP",
            lb_guarded(lambda: cloud.act(lb["url"], "detach_floating_ip")),
            needs=[("attached floating IP", lb_fip)],
        )
        run.step(
            "load balancer: set VIP security groups",
            lb_guarded(
                lambda: (
                    vip_port_ready()
                    or cloud.act(
                        lb["url"],
                        "set_security_groups",
                        {"security_groups": [sg["url"]]},
                    )
                )
            ),
            needs=[has_lb, ("sg", sg)],
        )

        def lb_teardown():
            delete_lb_objects()

        run.step(
            "load balancer: delete members, monitor, listener, pool, LB",
            lb_teardown,
            needs=[has_lb],
        )

        # Last of the instance's actions: a rescue the compute host cannot
        # carry out (the rescue image is copied to its local disk) leaves the
        # instance in ERROR, and nothing after it could use the instance.
        run.step(
            "instance: rescue and unrescue (stable device, BFV)",
            guarded(rescue),
            needs=[has_vm],
        )

        # -- RBAC: share a network with a second tenant --

        def rbac():
            if not cfg.rbac:
                raise Skip("disabled with --no-rbac")
            _, consumer = order_tenant(
                f"oscompat-b-{SUFFIX}", "consumer_resource", skip_connection_extnet=True
            )
            policy = api.post(
                f"{net['url'].rstrip('/')}/rbac_policy_create/",
                {"target_tenant": consumer["url"], "policy_type": "access_as_shared"},
            )
            cloud.wait(net["url"])
            cloud.act(consumer["url"], "pull")
            api.delete(f"{net['url'].rstrip('/')}/rbac_policy_delete/{policy['uuid']}/")
            cloud.wait(net["url"])

        run.step(
            "network RBAC: share with and revoke from a second tenant",
            rbac,
            needs=[("network", net)],
        )

        # -- Image upload (opt-in) --

        def image_upload():
            if not cfg.image_upload:
                raise Skip("enable with --image-upload; the image outlives the tenant")
            tenant_resource = ctx["tenant_resource"]["uuid"]
            image = api.post(
                f"openstack-marketplace-tenants/{tenant_resource}/create_image/",
                {
                    "name": f"compat-image-{SUFFIX}",
                    "disk_format": "raw",
                    "container_format": "bare",
                    "visibility": "private",
                },
            )
            image_id = image.get("id") or image.get("backend_id")
            response = requests.post(
                api.url(
                    f"openstack-marketplace-tenants/{tenant_resource}/upload_image_data/{image_id}/"
                ),
                data=os.urandom(1024 * 1024),
                headers={**api.headers, "Content-Type": "application/octet-stream"},
                timeout=300,
                verify=api.verify,
            )
            if not response.ok:
                raise ApiError(
                    f"upload -> {response.status_code}: {response.text[:300]}"
                )

        run.step("image: create and upload data", image_upload, needs=[has_tenant])

    finally:
        teardown(run, api, cloud, ctx)

    return run


def teardown(run, api, cloud, ctx):
    """Delete what the run made, through the same paths a user would."""
    if ctx.get("lb_objects"):
        # First: tenant termination does not delete load balancers, and the
        # VIP port holds a security group deleted below.
        run.step("teardown: delete load balancer", ctx["delete_lb_objects"])
    vm_resource = ctx.get("vm_resource")
    if ctx.get("restored_vm"):
        run.step(
            "teardown: delete restored instance",
            lambda: cloud.remove(
                ctx["restored_vm"],
                {"delete_volumes": True, "release_floating_ips": True},
            ),
        )
    if vm_resource:
        run.step(
            "teardown: terminate instance (delete volumes, release floating IPs)",
            lambda: cloud.terminate(
                vm_resource["uuid"],
                {"delete_volumes": True, "release_floating_ips": True},
            ),
        )
    if ctx.get("volume_resource"):
        run.step(
            "teardown: terminate volume",
            lambda: cloud.terminate(ctx["volume_resource"]["uuid"]),
        )
    if ctx.get("server_group"):
        run.step(
            "teardown: delete server group",
            lambda: cloud.delete(ctx["server_group"]),
        )
    if ctx.get("port"):
        run.step(
            "teardown: delete port",
            lambda: cloud.delete(ctx["port"]),
        )
    if ctx.get("fip"):
        run.step(
            "teardown: release floating IP",
            lambda: cloud.delete(ctx["fip"]),
        )
    if ctx.get("subnet"):
        run.step(
            "teardown: delete subnet",
            lambda: cloud.delete(ctx["subnet"]),
        )
    if ctx.get("network"):
        run.step(
            "teardown: delete network",
            lambda: cloud.delete(ctx["network"]),
        )
    if ctx.get("sg"):
        run.step(
            "teardown: delete security group",
            lambda: cloud.delete(ctx["sg"]),
        )
    if ctx.get("consumer_resource"):
        run.step(
            "teardown: terminate second tenant",
            lambda: cloud.terminate(ctx["consumer_resource"]["uuid"]),
        )
    if ctx.get("tenant_resource"):
        run.step(
            "teardown: terminate tenant (Keystone project and user, everything left in it)",
            lambda: cloud.terminate(ctx["tenant_resource"]["uuid"]),
        )
    if ctx.get("offering"):
        run.step(
            "teardown: archive offering",
            lambda: api.post(
                f"marketplace-provider-offerings/{ctx['offering']['uuid']}/archive/"
            ),
        )


def keystone_v3(url):
    """RC files often name the Keystone root; Waldur wants the v3 endpoint."""
    url = (url or "").rstrip("/")
    return url if url.endswith("/v3") else f"{url}/v3"


def waldur_token(url, token, username, password, verify):
    if token:
        return token
    if not (username and password):
        sys.exit("Give --waldur-token, or --waldur-username and --waldur-password.")
    response = requests.post(
        f"{url.rstrip('/')}/api-auth/password/",
        json={"username": username, "password": password},
        timeout=30,
        verify=verify,
    )
    response.raise_for_status()
    return response.json()["token"]


def parse_args(argv=None):
    env = os.environ.get
    parser = argparse.ArgumentParser(
        description=__doc__.split("\n\n")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    waldur = parser.add_argument_group("Waldur")
    waldur.add_argument("--waldur-url", default=env("WALDUR_URL"))
    waldur.add_argument("--waldur-token", default=env("WALDUR_TOKEN"))
    waldur.add_argument("--waldur-username", default=env("WALDUR_USERNAME"))
    waldur.add_argument("--waldur-password", default=env("WALDUR_PASSWORD"))
    waldur.add_argument(
        "--waldur-insecure",
        action="store_true",
        help="do not verify the Waldur API's TLS certificate",
    )
    cloud = parser.add_argument_group("OpenStack (defaults: the OS_* variables)")
    cloud.add_argument("--os-auth-url", default=env("OS_AUTH_URL"))
    cloud.add_argument("--os-username", default=env("OS_USERNAME"))
    cloud.add_argument("--os-project", default=env("OS_PROJECT_NAME", "admin"))
    cloud.add_argument(
        "--os-domain",
        default=env("OS_USER_DOMAIN_NAME", "Default"),
        help="user and project domain",
    )
    cloud.add_argument(
        "--os-verify-ssl",
        action="store_true",
        help="have Waldur verify the cloud's TLS certificates",
    )
    choices = parser.add_argument_group(
        "What to use (default: picked from what the tenant sees)"
    )
    choices.add_argument("--external-network", help="name or id")
    choices.add_argument("--image", help="image name")
    choices.add_argument("--flavor", help="flavor name; default the smallest by RAM")
    choices.add_argument(
        "--resize-flavor", help="default: the next larger flavor with the same disk"
    )
    choices.add_argument("--volume-type")
    choices.add_argument(
        "--retype-to", help="a second volume type; retype is skipped without it"
    )
    choices.add_argument(
        "--rescue-image",
        help="default: any image with hw_rescue_device or hw_rescue_bus",
    )
    run = parser.add_argument_group("Run")
    run.add_argument(
        "--no-rbac",
        action="store_true",
        help="skip the second tenant the network RBAC share needs",
    )
    run.add_argument(
        "--image-upload",
        action="store_true",
        help="also upload an image; Waldur cannot delete it afterwards",
    )
    run.add_argument(
        "--live-volume-resize",
        action="store_true",
        help="enable live resize on the offering and extend a volume in use",
    )
    run.add_argument(
        "--timeout", type=int, default=600, help="seconds per asynchronous operation"
    )
    run.add_argument("--report", default="openstack-compat.json")
    run.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    missing = [
        flag
        for flag, value in (
            ("--waldur-url", args.waldur_url),
            ("--os-auth-url", args.os_auth_url),
            ("--os-username", args.os_username),
            ("OS_PASSWORD", env("OS_PASSWORD")),
        )
        if not value
    ]
    if missing:
        parser.error(f"missing {', '.join(missing)} (source the cloud's RC file?)")
    return args


def main(argv=None):
    args = parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    verify = not args.waldur_insecure
    # The password is read from the environment only, never from the command
    # line, where it would show in the process list and the shell history.
    cfg = Config(
        waldur_url=args.waldur_url,
        waldur_token=waldur_token(
            args.waldur_url,
            args.waldur_token,
            args.waldur_username,
            args.waldur_password,
            verify,
        ),
        os_auth_url=keystone_v3(args.os_auth_url),
        os_username=args.os_username,
        os_password=os.environ["OS_PASSWORD"],
        os_project=args.os_project,
        os_domain=args.os_domain,
        os_verify_ssl=args.os_verify_ssl,
        waldur_verify_ssl=verify,
        external_network=args.external_network,
        image=args.image,
        flavor=args.flavor,
        resize_flavor=args.resize_flavor,
        volume_type=args.volume_type,
        retype_to=args.retype_to,
        rescue_image=args.rescue_image,
        rbac=not args.no_rbac,
        image_upload=args.image_upload,
        live_volume_resize=args.live_volume_resize,
        timeout=args.timeout,
        report=args.report,
    )
    logger.info("Run %s against %s, cloud %s", SUFFIX, cfg.waldur_url, cfg.os_auth_url)
    run = run_compat(cfg)
    table, counts = run.report(cfg.report)
    print("\n" + table)
    print(f"\nReport: {cfg.report}")
    return 1 if counts["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
