# Debugging guide for Waldur Mastermind

## Introduction

This guide provides systematic approaches for troubleshooting Waldur Mastermind deployments. Use these techniques to diagnose issues with API, worker processes, email delivery, and resource provisioning.

## Common debugging scenarios

### Symptom-based troubleshooting guide

| Symptom | First Check | Next Steps |
|---------|-------------|------------|
| Users not receiving emails | Email logs | SMTP configuration, email templates |
| API returning errors | API logs | HTTP status codes, request parameters |
| Resources stuck in provisioning | Worker logs | Backend connectivity, quota issues |
| Slow performance | Database logs | Query performance, connection pooling |
| Authentication failures | API logs with auth filter | IdP configuration, token issues |

## Accessing and filtering logs

### Email-related events

#### Docker Compose

Check your specific deployment logs location, typically:

```bash
# Find log location first
docker inspect waldur-mastermind-worker | grep LogPath
# Then view logs
cat /var/lib/docker/containers/[container-id]/[container-id]-json.log | grep -i "about to send"
```

#### Helm

```bash
# Replace 'waldur' with your namespace if different
kubectl logs -n waldur -l app=waldur-mastermind-worker --tail=1000 | grep -i "about to send"
```

### Component logs

#### API Logs in Helm

```bash
# Replace 'waldur' with your namespace if different
kubectl logs -n waldur -l app=waldur-mastermind-api --tail=100
```

#### Worker Logs in Helm

```bash
# Replace 'waldur' with your namespace if different
kubectl logs -n waldur -l app=waldur-mastermind-worker --tail=100
```

### Advanced log filtering

```bash
# Find errors in API logs (replace namespace if needed)
kubectl logs -n waldur -l app=waldur-mastermind-api --tail=1000 | grep -i "error\|exception"

# Track specific request by UUID
kubectl logs -n waldur -l app=waldur-mastermind-api --tail=1000 | grep "request-uuid-here"

# View all logs for a specific user (be careful with sensitive information)
kubectl logs -n waldur -l app=waldur-mastermind-api --tail=1000 | grep "user@example.com"
```

## Troubleshooting component issues

### API server problems

1. Check if the API container is running:

   ```bash
   # Docker Compose
   docker ps | grep waldur-mastermind-api
   
   # Kubernetes (replace namespace if needed)
   kubectl get pods -n waldur -l app=waldur-mastermind-api
   ```

2. Verify API health endpoint:

   ```bash
   # Use appropriate authentication if required
   curl https://your-waldur-instance/health-check/
   ```

3. Check for configuration issues:

   ```bash
   # Docker Compose
   docker exec -it waldur-mastermind-api cat /etc/waldur/override.conf.py
   
   # Kubernetes (replace namespace if needed)
   kubectl -n waldur get configmap api-override-config -o yaml
   ```

### Worker issues

1. Check Celery worker status:

   ```bash
   # Docker Compose
   docker exec -it waldur-mastermind-worker celery -A waldur_core.server inspect active
   
   # Kubernetes (replace namespace if needed)
   kubectl -n waldur exec -it $(kubectl -n waldur get pods -l app=waldur-mastermind-worker -o name | head -1) -- celery -A waldur_core.server inspect active
   ```

2. Verify task queue connectivity:

   ```bash
   # Docker Compose
   docker exec -it waldur-mastermind-worker celery -A waldur_core.server inspect ping
   
   # Kubernetes (replace namespace if needed)
   kubectl -n waldur exec -it $(kubectl -n waldur get pods -l app=waldur-mastermind-worker -o name | head -1) -- celery -A waldur_core.server inspect ping
   ```

## Database troubleshooting

1. Check database connectivity:

   ```bash
   # Docker Compose - if you have direct access
   docker exec -it waldur-mastermind-api waldur shell -c "from django.db import connection; connection.ensure_connection(); print('Connected')"
   
   # Kubernetes (replace namespace if needed)
   kubectl -n waldur exec -it $(kubectl -n waldur get pods -l app=waldur-mastermind-api -o name | head -1) -- waldur shell -c "from django.db import connection; connection.ensure_connection(); print('Connected')"
   ```

2. Identify slow queries (requires database access rights):

   ```sql
   -- For PostgreSQL 9.6+
   SELECT pid, now() - pg_stat_activity.query_start AS duration, query 
   FROM pg_stat_activity 
   WHERE state = 'active' AND now() - pg_stat_activity.query_start > interval '5 seconds'
   ORDER BY duration DESC;
   ```

## API endpoint issues

1. Test endpoint with curl (store tokens in environment variables for security):

   ```bash
   # Set token in environment variable first
   export WALDUR_TOKEN="your_token_here"
   
   # Then use it safely
   curl -v -H "Authorization: Token $WALDUR_TOKEN" https://your-waldur-instance/api/customers/
   ```

2. Common HTTP status codes:
   - 401/403: Authentication/authorization issue
   - 404: Resource not found
   - 500: Server error (check logs)

3. For development environments only (⚠️ NEVER in production):
   Temporarily increase debug verbosity through admin settings panel or by editing configuration files.

## Authentication problems

1. Check token validity:

   ```bash
   # Docker Compose
   docker exec -it waldur-mastermind-api waldur shell -c "from rest_framework.authtoken.models import Token; print(Token.objects.filter(key='your_token_here').exists())"
   
   # Kubernetes (replace namespace if needed)
   kubectl -n waldur exec -it $(kubectl -n waldur get pods -l app=waldur-mastermind-api -o name | head -1) -- waldur shell -c "from rest_framework.authtoken.models import Token; print(Token.objects.filter(key='your_token_here').exists())"
   ```

2. Verify IdP configuration:

   ```bash
   # For SAML2 configuration (replace namespace if needed)
   kubectl -n waldur get configmap waldur-saml2-conf-config -o yaml
   ```

## Resource provisioning failures

1. Check resource state:

   ```bash
   # Docker Compose
   docker exec -it waldur-mastermind-api waldur shell -c "from waldur_mastermind.marketplace import models; print(models.Resource.objects.filter(uuid='RESOURCE_UUID').values('state', 'error_message'))"
   
   # Kubernetes (replace namespace if needed)
   kubectl -n waldur exec -it $(kubectl -n waldur get pods -l app=waldur-mastermind-api -o name | head -1) -- waldur shell -c "from waldur_mastermind.marketplace import models; print(models.Resource.objects.filter(uuid='RESOURCE_UUID').values('state', 'error_message'))"
   ```

2. Check backend connectivity (if you have the right plugin installed):

   ```bash
   # For OpenStack
   kubectl -n waldur exec -it $(kubectl -n waldur get pods -l app=waldur-mastermind-api -o name | head -1) -- waldur shell -c "from waldur_openstack.openstack import models; tenant = models.Tenant.objects.first(); print('No tenants found' if not tenant else tenant.get_backend().verify_connection())"
   ```

## Log management

### Log rotation

Both Docker Compose and Kubernetes deployments typically have configured log rotation:

```bash
# Check Docker log rotation configuration
docker info | grep "Logging Driver"

# For Kubernetes, it depends on your cluster configuration
kubectl -n waldur describe pod $(kubectl -n waldur get pods -l app=waldur-mastermind-api -o name | head -1)
```

### Centralized logging

For production deployments, consider:

- Fluentd for log collection
- Elasticsearch for storage and search
- Kibana for visualization

## Troubleshooting broker / Celery worker timeouts

This section covers Sentry events of the form `SystemExit: 1` originating in
`waldur_mastermind/policy/handlers.py` (or any handler chain that ends in
`kombu/basic_publish_confirm`), and HTTP 500s on high-frequency endpoints such
as `set_usage` and `set_state_done`. The pattern is gunicorn killing a worker
that is parked in `recv()` waiting for an AMQP publish ACK that never arrives.

### Symptom checklist

The following combination strongly suggests a broker / connection-state issue
rather than slow application code:

- Sentry error type is `SystemExit: 1` (not a Python exception class)
- The deepest in-app frame is in
  `policy/handlers.py` (or `marketplace/handlers.py`) calling
  `tasks.X.delay(...)`
- The bottom of the stack is
  `kombu/messaging.py → amqp/channel.py:basic_publish_confirm → amqp/transport.py:_read → recv`
- HTTP transaction shows the worker dying right at the gunicorn worker timeout
  (default 30 s)
- Restarting the broker temporarily reduces the rate but does not eliminate it

### Layered diagnostic plan

When chasing these failures, isolate one layer at a time. The first layer that
behaves correctly is the layer *above* where the bug lives.

#### Layer 0: confirm the failing call path is broker-bound

Capture AMQP traffic on a single API pod during a failure window:

```bash
# Replace 'waldur' with your namespace and 'POD' with the actual pod name
POD=$(kubectl -n waldur get pods -l app=waldur-mastermind-api -o name | head -1 | cut -d/ -f2)
kubectl -n waldur debug pod/$POD --image=nicolaka/netshoot --target=waldur-mastermind-api -- \
  bash -c "tcpdump -i any -w /tmp/amqp.pcap port 5672 -G 60 -W 1"
kubectl -n waldur cp $POD:/tmp/amqp.pcap ./amqp.pcap
tshark -r amqp.pcap -Y "amqp" -T fields -e _ws.col.Time -e amqp.method.class \
  | awk '{print $3}' | sort | uniq -c
```

If `publish` count equals `basic-ack` count, the broker is sending ACKs the
publisher fails to receive (move to Layer 1). If `publish` exceeds `basic-ack`,
the broker is slow to ACK or never ACKs (move to Layer 2).

#### Layer 1: kernel-level socket health on the publisher

Inspect TCP state of the API pod's AMQP connections while a `recv()` is stuck:

```bash
kubectl -n waldur exec -it $POD -- bash -c '
ss -tnpio "( sport = :5672 or dport = :5672 )" 2>/dev/null || \
  awk "/:1628 / {print \$1,\$2,\$3,\$4}" /proc/net/tcp
'
```

Pay attention to:

- `State`: `ESTABLISHED` with a stuck `recv()` indicates the connection
  silently went half-open
- `unacked` and `retrans` columns: non-zero values mean the kernel is
  retransmitting and the peer is not responding
- `Recv-Q`: bytes sitting in the receive buffer but not consumed — extremely
  unusual when `recv()` is blocked, suggests application-level deadlock

Check whether TCP keepalive is enabled on AMQP sockets (it should be, py-amqp
sets `SO_KEEPALIVE=1` unconditionally):

```bash
kubectl -n waldur exec $POD -- bash -c '
python3 -c "
import socket
for line in open(\"/proc/net/tcp\"):
    p = line.split()
    if len(p) > 4 and p[2].endswith(\":1628\") and p[3] == \"01\":
        print(line)
"'
```

#### Layer 2: broker-side per-publish latency

Measure confirm RTT directly from inside the API pod against the real broker.
The `probe_broker_latency` management command publishes N no-op messages with
a long countdown (so they land in a delay queue without executing) and
reports percentiles:

```bash
# Defaults: 100 publishes, countdown=86400s
kubectl -n waldur exec -it $POD -- waldur probe_broker_latency

# Tighter check for CI / alerting
kubectl -n waldur exec -it $POD -- waldur probe_broker_latency \
    --samples 200 --p99-threshold-ms 500 --json
```

Interpretation:

- p99 < 50 ms — broker is fast. Failures live in the network / connection
  layer (Layer 1)
- p99 50–500 ms — broker is slow but usually tolerable; combined with
  publish amplification can still exceed the worker timeout
- p99 > 1 s — broker has a real latency problem; investigate quorum WAL,
  disk I/O on the broker PVC, or memory pressure
- `max` close to the worker timeout — occasional confirms are nearly
  fatal; an upper bound on confirm wait is required

The probe payload uses an invalid `scope_id` so the task body is a no-op
even when it eventually executes. With `countdown=86400` the messages land
in a deep `celery_delayed_*` bucket and will rotate down naturally; no
manual cleanup is required.

#### Layer 3: Kubernetes network / conntrack on the worker nodes

If broker confirms are fast but a percentage of requests still time out,
something on the kernel network path is dropping the ACK frame in transit.
The most common cause in busy Kubernetes clusters is conntrack table
exhaustion.

```bash
# On each worker node that hosts API or RabbitMQ pods
ssh <node> 'cat /proc/sys/net/netfilter/nf_conntrack_count
             cat /proc/sys/net/netfilter/nf_conntrack_max
             dmesg | grep -i conntrack | tail -20
             conntrack -L 2>/dev/null | wc -l'
```

A `count / max` ratio above ~0.7, or any `nf_conntrack: table full,
dropping packets` log line, is the signal. Resolution is a node-level
sysctl bump (`net.netfilter.nf_conntrack_max`) and tighter `nf_conntrack_*`
TCP timeouts.

If `kubectl debug node/<node>` is permitted in your cluster, the
equivalent is:

```bash
kubectl debug node/<node-name> --image=nicolaka/netshoot -- \
  bash -c 'cat /host/proc/sys/net/netfilter/nf_conntrack_count
           cat /host/proc/sys/net/netfilter/nf_conntrack_max
           chroot /host dmesg | grep -i conntrack | tail'
```

#### Layer 4: gunicorn and Celery configuration

Verify gunicorn's effective timeout and Celery's actual broker config from
inside a running API pod (config values flow through Django settings):

```bash
kubectl -n waldur exec $POD -- cat /etc/waldur/gunicorn.conf.py | grep -i timeout
kubectl -n waldur exec $POD -- waldur shell -c "
from celery import current_app
print('broker_heartbeat:',
      current_app.conf.broker_heartbeat)
print('transport_options:',
      current_app.conf.broker_transport_options)
print('connection_max_retries:',
      current_app.conf.broker_connection_max_retries)
print('publish_retry_policy:',
      current_app.conf.task_publish_retry_policy)
"
```

If `broker_heartbeat` is `None`, the negotiation falls back to the broker's
default — typically 60 s. Combined with two-missed-heartbeat detection,
that means dead connections are detected ~120 s after the fact, which is
*after* gunicorn has already killed the worker.

### Configuration knobs that actually fix this

These are the Celery / kombu settings that matter for broker resilience.
Each carries a gotcha that is easy to get wrong.

#### Heartbeat: must be set via `broker_transport_options`

The top-level `CELERY_BROKER_HEARTBEAT` setting is **silently dropped on
the publisher path**. Celery does not propagate it to
`app.broker_connection()` or `app.producer_pool`. To actually reach the
kombu `Connection`, the value must live inside `broker_transport_options`:

```python
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "confirm_publish": True,
    "heartbeat": 30,
    # ... see socket_settings below
}
```

py-amqp sends a heartbeat frame at half the configured interval. With
`heartbeat=30`, the broker drops the connection after roughly 30 s of
missed heartbeats — early enough to interrupt a stuck publisher before
gunicorn's 30 s worker timeout.

#### TCP keepalive: keys must be integer socket constants

py-amqp enables `SO_KEEPALIVE` unconditionally but ships defaults of
`TCP_KEEPIDLE=60`, `TCP_KEEPINTVL=10`, `TCP_KEEPCNT=9` — a total ~150 s
detection window that fires *after* the gunicorn timeout. Override with
tighter values so the kernel closes a stuck socket in ~25 s:

```python
import socket

_BROKER_SOCKET_SETTINGS = {}
for _opt, _val in (
    ("TCP_KEEPIDLE", 10),
    ("TCP_KEEPINTVL", 5),
    ("TCP_KEEPCNT", 3),
):
    _const = getattr(socket, _opt, None)
    if _const is not None:
        _BROKER_SOCKET_SETTINGS[_const] = _val

CELERY_BROKER_TRANSPORT_OPTIONS = {
    "confirm_publish": True,
    "heartbeat": 30,
    "socket_settings": _BROKER_SOCKET_SETTINGS,
}
```

The `socket_settings` keys **must be integer constants** from the
`socket` module — py-amqp passes them straight to
`setsockopt(SOL_TCP, opt, val)`. String keys raise
`TypeError: 'str' object cannot be interpreted as an integer` on the
first connection attempt. Some constants (`TCP_KEEPIDLE` in
particular) are Linux-only; the `getattr` guard above keeps the
settings importable on macOS dev machines.

#### Worker recycling: cost of low `max_tasks_per_child`

A low `CELERY_WORKER_MAX_TASKS_PER_CHILD` (e.g. 100) is often set
defensively against memory leaks, but each recycle costs a fork +
full broker reconnect handshake. Under heavy publish load this churn
measurably outweighs the leak protection. Values in the low
thousands (1000–2000) are typical for production celery workers
without leaks.

#### Per-publish `confirm_timeout` is not exposed

py-amqp's `Channel._basic_publish` accepts a `confirm_timeout`
keyword that bounds the confirm wait per call, but kombu's
`Producer` does not surface it through Celery's app config (see
[celery#9259](https://github.com/celery/celery/issues/9259)). The
heartbeat + TCP keepalive combination above is the configuration-only
substitute. A future improvement is a custom `Producer` subclass that
injects `confirm_timeout` on every publish.

### Verifying a configuration change end-to-end

The wrong setting will silently no-op and ship broken. Run the
`audit_broker_config` management command for a static check, then
`probe_broker_latency` to confirm the broker actually responds in
the expected latency band:

```bash
# Static audit — no broker connection. Exit 0 = OK, 1 = warn, 2 = error.
kubectl -n waldur exec $POD -- waldur audit_broker_config

# Live probe against the broker
kubectl -n waldur exec $POD -- waldur probe_broker_latency
```

The audit command catches each of the gotchas listed above (top-level
`BROKER_HEARTBEAT` being ignored, string-keyed `socket_settings`,
missing `confirm_publish`, etc.) and prints a human-readable summary
plus a remediation hint per finding.

For a deeper inspection of the actual kombu connection state — useful
when verifying a brand-new transport option py-amqp may or may not
have picked up — drop into the Django shell and introspect the live
connection:

```bash
kubectl -n waldur exec -it $POD -- waldur shell -c "
import socket
from celery import current_app
with current_app.connection_for_write() as conn:
    conn.connect()
    p = conn.connection
    print(f'heartbeat:        {p.heartbeat}')
    print(f'confirm_publish:  {p.confirm_publish}')
    print(f'socket_settings:  {p.socket_settings}')
    sock = p.sock
    print(f'SO_KEEPALIVE:     {sock.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE)}')
    for opt in ('TCP_KEEPIDLE','TCP_KEEPINTVL','TCP_KEEPCNT'):
        c = getattr(socket, opt, None)
        if c is not None:
            print(f'{opt}: {sock.getsockopt(socket.IPPROTO_TCP, c)}')
"
```

`heartbeat` should be non-zero, `confirm_publish` should be `True`,
`socket_settings` should be a dict of integer keys, and the kernel
values should reflect the configured TCP keepalive parameters.

### Common signal handler / publish patterns that compound the problem

Independent of the transport layer, application code that publishes
many synchronous Celery tasks per HTTP request multiplies any tail
latency by the publish count. Two patterns are worth knowing:

#### Synchronous fan-out in `post_save` handlers

If multiple signal handlers are wired to the same model's `post_save`
and each issues `.delay()` synchronously, one HTTP request becomes N
broker round-trips. Each round-trip is a chance to hit the slow path.
Debounce repeated triggers on a per-scope cache key (see
`waldur_mastermind/policy/handlers.py:_debounced_call`) so a burst of
saves collapses to a single Celery publish per scope per debounce
window.

#### Deferring publishes to `transaction.on_commit`

When the trigger occurs inside a database transaction, publishing
through `transaction.on_commit(lambda: task.delay(...))` moves the
publish out of the transaction's critical section. This also avoids
the race where a Celery worker picks up the task before the DB row
that justifies it is committed.

### Cross-references

- [Architecture overview](architecture.md) — where the broker fits in
  the topology
- [Hardware requirements](hardware-requirements.md) — broker sizing
  and PVC recommendations
- [Troubleshooting gunicorn workers](#troubleshooting-gunicorn-workers)
  — complementary section below; broker timeouts manifest as
  gunicorn worker deaths

## Troubleshooting gunicorn workers

The gunicorn master spawns N worker processes. Workers handle HTTP
requests; if a worker doesn't return within `--timeout` seconds (default
30 s) the master sends it `SIGABRT` and logs `WORKER TIMEOUT (pid:…)`,
then forks a replacement. Long-running publishes, slow DB queries,
deadlocks, and certain library hangs all manifest as worker timeouts.
This section covers diagnosing what workers are actually doing and why
they die.

### Inspect effective gunicorn configuration

Configuration can live in `/etc/waldur/gunicorn.conf.py`, in command-line
flags on the master process, or in environment variables. Verify all
three:

```bash
POD=$(kubectl -n waldur get pods -l app=waldur-mastermind-api -o name | head -1 | cut -d/ -f2)

# Config file
kubectl -n waldur exec $POD -- cat /etc/waldur/gunicorn.conf.py

# Master process command line (catches --flags overrides)
kubectl -n waldur exec $POD -- bash -c 'cat /proc/1/cmdline | tr "\0" " "; echo'

# Environment variables that gunicorn respects (e.g. GUNICORN_CMD_ARGS)
kubectl -n waldur exec $POD -- bash -c 'tr "\0" "\n" < /proc/1/environ | grep -iE "gunicorn|workers|timeout"'
```

Settings to confirm:

- `timeout`: kill-worker threshold; default **30 s**
- `graceful_timeout`: SIGTERM grace before SIGKILL (default 30 s)
- `workers`: process count
- `worker_class`: `sync` (default), `gthread`, `gevent`, `eventlet`
- `threads`: only meaningful for `gthread`
- `preload_app`: if true, the app is imported in the master and inherited
  by workers via fork
- `max_requests`: requests per worker before recycle (0 = never)
- `max_requests_jitter`: randomisation to avoid synchronised recycles

### Inventory of worker processes and their ages

Sudden gaps in worker ages (one is 30 s old, others are minutes/hours)
mean workers are being killed and respawned. Steady ages mean they're
healthy.

```bash
kubectl -n waldur exec $POD -- bash -c '
echo "PID   AGE(s)  RSS(MB)  CMD"
for pid in $(pgrep -P 1 -f gunicorn); do
  age=$(( $(date +%s) - $(stat -c %Y /proc/$pid) ))
  rss=$(awk "/VmRSS/ {print int(\$2/1024)}" /proc/$pid/status)
  cmd=$(tr "\0" " " < /proc/$pid/cmdline | head -c 70)
  printf "%-5s %6s  %7s  %s\n" "$pid" "$age" "$rss" "$cmd"
done
'
```

If ages are all < `gunicorn timeout`, workers are dying continuously —
the symptom of stuck requests at the timeout boundary. Cross-check with
the worker-timeout log count below.

### Count `WORKER TIMEOUT` events in logs

The master process logs every timeout-kill. Count them over a window to
get a rate:

```bash
# Last 30 minutes, one pod
kubectl -n waldur logs --since=30m $POD 2>&1 | grep -c "WORKER TIMEOUT"

# Across all pods of the deployment
for p in $(kubectl -n waldur get pods -l app=waldur-mastermind-api -o name | cut -d/ -f2); do
  n=$(kubectl -n waldur logs --since=30m "$p" 2>&1 | grep -c "WORKER TIMEOUT")
  echo "$p: $n timeouts/30min"
done
```

A handful per hour can be normal under heavy load. Dozens per hour
across pods is a real problem and warrants the deeper investigation
in the next sections.

### Identify what a worker is currently stuck on

When a Sentry event arrives mid-request the stack at `SIGABRT` time is
captured automatically. To inspect a still-running worker mid-flight,
you have three tiers of options depending on the deployment's
security posture.

#### Why `kubectl exec ... py-spy/strace` usually fails

Production waldur containers ship hardened: they run as a non-root UID
with the bounding capability set stripped (no `CAP_SYS_PTRACE`), and
the kernel's `ptrace_scope` is typically `1` (restricted). Both
`py-spy` and `strace` use the `ptrace(2)` syscall, which the kernel
will reject with `EPERM` in this setup.

Confirm the limitation in your cluster before reaching for a
workaround:

```bash
POD=$(kubectl -n waldur get pods -l app=waldur-mastermind-api -o name | head -1 | cut -d/ -f2)
kubectl -n waldur exec $POD -- bash -c '
echo "ptrace_scope: $(cat /proc/sys/kernel/yama/ptrace_scope)"
grep -E "^CapEff:|^CapBnd:" /proc/1/status
id
'
```

- `CapEff: 0000000000000000` → zero effective capabilities; `ptrace` will fail
- `CapBnd` missing bit 19 (`0x80000`) → `CAP_SYS_PTRACE` cannot be raised
- `ptrace_scope: 1` → restricted; cannot attach to non-descendant processes
- Non-root `id` → no admin override

If all four apply you must use one of the elevated-privilege patterns
below.

#### Pattern A — Ephemeral debug container with `--profile=general`

`kubectl debug` injects a sidecar into a running pod. With
`--profile=general`, recent kubectl versions add the capabilities and
shared namespaces needed for ptrace tools. Permission to use this
requires `pods/ephemeralcontainers` in the namespace RBAC and a
PodSecurityStandard that allows the elevated profile.

```bash
POD=$(kubectl -n waldur get pods -l app=waldur-mastermind-api -o name | head -1 | cut -d/ -f2)

# Attach a debug container that shares PID + capabilities with the target
kubectl -n waldur debug pod/$POD \
  --image=python:3.13-slim \
  --profile=general \
  --target=waldur-mastermind-api \
  -it -- bash -c '
    pip install --quiet py-spy
    WORKER_PID=$(pgrep -P 1 -f "gunicorn: worker" | head -1)
    py-spy dump --pid $WORKER_PID
'
```

If `kubectl debug` is denied with `cannot create resource ... in
namespace`, jump to pattern B.

#### Pattern B — Standalone diagnostic pod pinned to the same node

When ephemeral containers are blocked, deploy a one-off privileged pod
on the *same node* as the target API pod, sharing the host's PID
namespace. The debug pod sees the API worker processes and can ptrace
them.

```yaml
# waldur-debug-pod.yaml — edit nodeName to match the target API pod
apiVersion: v1
kind: Pod
metadata:
  name: waldur-debug
  namespace: waldur
spec:
  nodeName: <node-of-target-api-pod>
  hostPID: true
  restartPolicy: Never
  containers:
  - name: debug
    image: python:3.13-slim
    command: ["sleep", "infinity"]
    securityContext:
      runAsUser: 0
      capabilities:
        add: ["SYS_PTRACE"]
```

Apply, then exec in and run the tool:

```bash
# Find the target node first
TARGET_POD=waldur-mastermind-api-XXXX
NODE=$(kubectl -n waldur get pod $TARGET_POD -o jsonpath='{.spec.nodeName}')

# Patch the manifest and apply
sed "s/<node-of-target-api-pod>/$NODE/" waldur-debug-pod.yaml | kubectl apply -f -
kubectl -n waldur wait --for=condition=Ready pod/waldur-debug --timeout=60s

# Use it
kubectl -n waldur exec -it waldur-debug -- bash -c '
  pip install --quiet py-spy
  # hostPID=true gives us the global pid view
  WORKER_PID=$(pgrep -f "gunicorn: worker" | head -1)
  echo "Worker PID on host: $WORKER_PID"
  py-spy dump --pid $WORKER_PID
'

# Clean up
kubectl -n waldur delete pod waldur-debug
```

Things to watch:

- Creating a pod with `hostPID: true` and `SYS_PTRACE` typically
  requires permissive PodSecurityStandard (`baseline` or `privileged`)
  on the namespace. If denied, work with the cluster admin to apply
  a temporary `PodSecurityPolicy` exemption.
- Pinning to `nodeName` is required so the pod sees the API worker
  in its (host) PID namespace.
- Keep the debug pod's lifetime short — delete it as soon as the
  dump is captured.

#### Pattern C — Ptrace-free alternative inside the regular pod

When neither pattern A nor B is available, you can still inspect
Python state from inside the regular waldur pod by sending the
process a signal it has installed a handler for, or by attaching via
Django's shell to introspect threading and module state. This won't
give you a stack of a *currently blocked* gunicorn worker — for that
you need ptrace. But it covers many "what's the app doing right
now" questions:

```bash
kubectl -n waldur exec $POD -- waldur shell -c '
import sys, traceback
# Stacks of every Python thread in THIS process (the shell), not workers
for tid, frame in sys._current_frames().items():
    print(f"--- thread {tid} ---")
    traceback.print_stack(frame)
'
```

For a more comprehensive picture without ptrace, write a long-running
diagnostic that the worker imports voluntarily (a debug middleware
that periodically dumps `sys._current_frames()` to a file when an
env var is set). Outside the scope of this guide.

### Syscalls to look for in py-spy / strace output

Once you have a stack from any of the patterns above:

- Repeated `recvfrom(<fd> ... <unfinished ...>` — worker is parked
  in a blocking read (broker confirm, HTTP upstream, slow DB)
- Repeated `poll([...], timeout=…)` — async event loop waiting
- `futex(... FUTEX_WAIT …)` — Python GIL or threading lock
  contention
- py-spy `Python frame` output names the exact file/function/line
  in the worker's Python stack — typically the fastest path to
  "what's slow"

### Worker memory and file descriptor usage

Memory leaks and FD leaks are common silent killers. Both grow until
the worker is OOM-killed by the kernel or hits `RLIMIT_NOFILE`.

```bash
kubectl -n waldur exec $POD -- bash -c '
echo "PID   RSS(MB)  VSZ(MB)  FDs   age(s)"
for pid in $(pgrep -P 1 -f "gunicorn: worker"); do
  rss=$(awk "/VmRSS/{print int(\$2/1024)}" /proc/$pid/status)
  vsz=$(awk "/VmSize/{print int(\$2/1024)}" /proc/$pid/status)
  fd=$(ls /proc/$pid/fd 2>/dev/null | wc -l)
  age=$(( $(date +%s) - $(stat -c %Y /proc/$pid) ))
  printf "%-5s %7s %7s %5s %6s\n" "$pid" "$rss" "$vsz" "$fd" "$age"
done
'
```

If RSS grows monotonically with age and resets when the worker recycles,
the app has a leak. `max_requests` (with jitter) is the configuration
workaround; the real fix is finding and closing the leak.

If FD count grows with age, sockets or files are being opened without
being closed. `ls -l /proc/$pid/fd` shows what types of FDs they are.

### `preload_app` and post-fork state

When `preload_app = True`, the master imports the Django/Celery app
once, then forks workers. Module-level state survives the fork and is
shared across workers via COW pages. This is good for memory (shared
code) but dangerous for:

- Open sockets (broker connections, DB connections) — multiple
  workers may inadvertently share a socket FD and corrupt the
  protocol
- RNG state — workers start with identical seeds unless re-seeded
  after fork
- Module-global mutable singletons (caches, connection pools)

Kombu and most DB drivers detect `os.fork()` and reset state, but only
if their `register_at_fork` hook was actually registered before the
fork. With `preload_app = False` (the default in waldur), each worker
imports the app independently after fork — no shared state, but
slightly slower boot. This is the safer baseline; deviate only with
specific reason.

### Worker-class implications for blocking I/O

| Worker class | Concurrency | Blocking I/O is OK? |
|---|---|---|
| `sync` (default) | 1 request/worker | Yes — each blocking call blocks one worker |
| `gthread` | N threads/worker | Yes — Python releases the GIL on I/O |
| `gevent` / `eventlet` | hundreds via monkey-patching | **No** — must use async-aware libraries everywhere |

If the deployment uses `gevent` or `eventlet`, **any synchronous
network library that wasn't monkey-patched at startup will block the
entire worker's event loop**, not just one greenlet. Common culprits:
psycopg, kombu pre-monkey-patch, native extensions. Always pair these
worker classes with `monkey.patch_all()` very early in app boot.

`sync` is the safest baseline. waldur ships with `sync`.

### Signal flow when a worker times out

1. Worker is parked > `timeout` seconds since last `notify()` to master
2. Master sends `SIGABRT` to the worker (NOT `SIGKILL`)
3. Python's default `SIGABRT` handler calls `sys.exit(1)` → Sentry
   captures `SystemExit: 1` with the current stack
4. Kernel cleans up worker's open sockets — RST sent to peers, hence
   the broker logs "client unexpectedly closed TCP connection"
5. Master forks a replacement worker

The "SystemExit" type in Sentry is the giveaway that gunicorn killed
the worker; if it were the application itself, you'd see a real
exception class.

Raising the gunicorn `timeout` only delays the kill — it does not
fix the underlying stuck request. The right fix is **not having
requests that block longer than the timeout**; see the broker /
Celery section above for one concrete class of fix.

### Emulating a Celery publisher / worker in a side pod

Many of the broker tests in the earlier section (publish latency probe,
heartbeat verification, socket option introspection) can be run from
the production API pod, but **you don't want to risk side effects on
real traffic**. A safer pattern is to deploy a short-lived "emulator"
pod that uses the same image and broker credentials as the production
API but is isolated from the deployment. Run experiments there, delete
when done.

#### Standalone publisher / worker emulator

This pod mirrors a real API pod's broker config (image, env vars,
ConfigMaps, Secrets) but does not register as part of the service.
Useful for:

- Measuring broker publish latency without polluting Sentry
- A/B testing new `BROKER_TRANSPORT_OPTIONS` before rolling them out
- Verifying that a settings change actually flows through to kombu
  and the kernel socket (see the "Verifying a configuration change
  end-to-end" recipe in the broker section)
- Running the test-driver under `py-spy` or `strace` (the emulator
  pod can be deployed with `CAP_SYS_PTRACE`)

```yaml
# waldur-broker-emulator.yaml — drop into a writable namespace
apiVersion: v1
kind: Pod
metadata:
  name: waldur-broker-emulator
  namespace: waldur
spec:
  restartPolicy: Never
  serviceAccountName: <same-SA-as-waldur-mastermind-api>
  containers:
  - name: emulator
    # Pin to the same image tag as the running API to keep dependency
    # versions identical
    image: opennode/waldur-mastermind:<tag>
    command: ["sleep", "infinity"]
    # Inherit ALL env vars from the API's existing ConfigMap / Secret
    # so DATABASE_URL, broker URL, etc. are identical
    envFrom:
    - configMapRef:
        name: <api-configmap>
    - secretRef:
        name: <api-secret>
    securityContext:
      runAsUser: 1001          # waldur user
      capabilities:
        add: ["SYS_PTRACE"]    # so py-spy can attach to processes IN THIS pod
```

Exec in and run experiments. The emulator does not consume requests
or scheduled tasks (no celery worker is started), so it has no
visible side effect on the running deployment:

```bash
kubectl -n waldur apply -f waldur-broker-emulator.yaml
kubectl -n waldur wait --for=condition=Ready pod/waldur-broker-emulator

# Drop into the same shell environment as production API
kubectl -n waldur exec -it waldur-broker-emulator -- waldur shell

# Or run a one-shot publish-latency probe with the production celery config
kubectl -n waldur exec -it waldur-broker-emulator -- waldur shell -c "
import time
from waldur_mastermind.policy import tasks
ms = []
for _ in range(100):
    t = time.perf_counter()
    tasks.evaluate_policies_async.apply_async(
        args=['waldur_mastermind.policy.models.OfferingEstimatedCostPolicy', {'scope_id': -1}],
        countdown=86400,
    )
    ms.append((time.perf_counter() - t) * 1000)
ms.sort()
print(f'p50={ms[50]:.1f}ms p99={ms[99]:.1f}ms max={ms[-1]:.1f}ms')
"

# Delete when finished
kubectl -n waldur delete pod waldur-broker-emulator
```

#### Adding a worker arm to the emulator

If you want to also test the *consume* side (e.g., verify the
new heartbeat survives idle periods on a long-lived consumer
connection), extend the emulator with a second container that
runs a celery worker against a sandboxed queue. The worker
consumes only from a temporary queue you created for the test,
so it never picks up real tasks:

```yaml
spec:
  containers:
  - name: publisher         # as above
    # ...
  - name: worker
    image: opennode/waldur-mastermind:<tag>
    # Worker bound to a temporary queue
    command:
    - celery
    - -A
    - waldur_core.server.celery
    - worker
    - --loglevel=INFO
    - --queues=debug-temp           # ONLY this queue; never tasks-durable
    - --concurrency=1
    envFrom:
    - configMapRef:
        name: <api-configmap>
    - secretRef:
        name: <api-secret>
```

Then `tasks.evaluate_policies_async.apply_async(args=[...],
queue='debug-temp')` to route a test task to the emulator's worker
specifically. The real workers will not see it.

### Cross-references for gunicorn diagnostics

- [Troubleshooting broker / Celery worker timeouts](#troubleshooting-broker--celery-worker-timeouts)
  — the most common cause of gunicorn worker timeouts in waldur
- [API server problems](#api-server-problems) — higher-level
  HTTP-side debugging

## Debug mode activation

!!! warning "Production caveat"
    Debug mode should ONLY be used in development environments.

For development deployments, you can enable debug mode:

```yaml
# In values.yaml
waldur:
  debug: true
```

For production troubleshooting, use targeted logging instead of
enabling full debug mode.


