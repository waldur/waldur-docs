# Waldur Shell

Waldur provides a shell for command line scripting. To start a shell, run ``waldur shell`` in the MasterMind context.

For Docker Compose deployments, please run:

``docker exec -it waldur-mastermind-api waldur shell``

For Helm-based K8s deployments, please run:

```bash
export KUBECONFIG=/etc/rancher/rke2/rke2.yaml  # if running from RKE2 node
kubectl get pods -A | grep waldur-mastermind-worker  # to find POD id
kubectl exec --stdin --tty waldur-mastermind-worker-POD-ID -- waldur shell
```

## Examples

### Setting/removing staff permissions for a user

```python
from waldur_core.core.models import User

user = User.objects.get(
    username="example_user",
)
user.set_password("somesecretpassword")
user.is_staff = True  # set to False if you want to remove permission
user.save()
```

### Creating a new user with token only authentication

```python
from rest_framework.authtoken.models import Token
from waldur_core.core.models import User

user = User.objects.create(
    username="example_accounting_user",
    first_name="Accounting",
    last_name="Reporter",
    email="test@example.com",
)
user.token_lifetime = None
user.set_unusable_password()
user.save()

token = Token.objects.get(user=user)
print(token)
```

### Triggering pulling of usage data from remote Waldur

```python
from waldur_mastermind.marketplace_remote.tasks import UsageListPullTask

UsageListPullTask().run()
```

### Apply changes in Waldur HPC plugin to existing users

```python
from waldur_core.core import models as core_models
from waldur_hpc.handlers import handle_new_user

for user in core_models.User.objects.filter(is_active=True, registration_method__iexact='saml2'):
    handle_new_user(None, user, created=True)
```

### Cleanup leftover ports from OpenStack Project

Lookup UUID of an OpenStack tenant (aka backend_id in Waldur).

```python
from waldur_openstack.models import Tenant

t_uuid = 'UUID_OF_TENANT'
t = Tenant.objects.get(backend_id=t_uuid)

nc = t.get_backend().neutron_client
all_ports = nc.list_ports()['ports']
tenant_ports = [port for port in all_ports if port['tenant_id'] == t_uuid and port.get('status') == 'DOWN']

for t in tenant_ports:
    print(t['id'], t['fixed_ips'][0]['ip_address'])
    nc.delete_port(t['id'])
```

### Add affiliations to user

```python
from waldur_core.core import models as core_models

user = core_models.User.objects.get(email='some.email@abc.example.com')
user.affiliations = ['some.affiliation@domain.example.com']
user.save()
```

### Create a service user for API access

To create a service user - without valid access credntials and non-expiring Token, please run the
following script.

```python
from waldur_core.core.models import User

u = User.objects.create(username='waldur_demo_user', first_name='Demo',
                        last_name='Waldur user', email='demo@example.com')

# make sure that token doesn't time out
u.token_lifetime = None
u.save()

# print user authentication token
print(u.auth_token.key)
```

### Synchronise SLURM associations

**Note**: `<allocation-uuid>` field can be found in an allocations's details page.

`Select Organization -> Select project -> Select allocation -> Find 'UUID' field in the page.`

```python
from waldur_slurm import models as slurm_models

allocation = slurm_models.Allocation.objects.get(uuid='<allocation-uuid>')
backend = allocation.get_backend()

backend.add_new_users(allocation) # Creates associations on SLURM level

backend.pull_allocation(allocation) # Sync associations on Waldur level
```

### Lookup user details from Eduteams

**Note**: `USER_CUID` is a unique ID of user in Eduteams.

```python
from waldur_auth_social.utils import get_remote_eduteams_user_info

USER_CUID='semi_secret@eduteams.org'

get_remote_eduteams_user_info(USER_CUID)
```

### Generate report for list of projects and their details

```python
import sys
import csv

from waldur_core.structure import models as structure_models


projects = structure_models.Project.objects.filter(created__lte='2022-05-31')
writer = csv.writer(sys.stdout)
for project in projects:
    owner = project.customer.get_owners().first()
    writer.writerow(
        [
            project.name,
            owner and owner.full_name,
            project.oecd_fos_2007_code,
            project.customer.country,
        ]
    )
```

### Generate report for OpenStack resources across projects

```python
import csv
import sys

from waldur_openstack.models import Tenant, Instance, Volume
from waldur_core.structure.models import ServiceSettings

RAM_LIMIT_NAME = 'ram'
STORAGE_LIMIT_NAME = 'storage'

writer = csv.writer(sys.stdout)


def generate_report():
    tenants = Tenant.objects.filter(state=3)
    writer.writerow(
        [
            'Organisation',
            'Abbreviation',
            'Project',
            'VPC',
            'RAM limit',
            'RAM usage',
            'Storage limit',
            'Storage usage',
            'Number of VMs',
            'Big VM count',
            'Big volume count',
        ]
    )
    for tenant in tenants:
        number_of_vms = tenant.quotas.get(name='instances').usage
        ram_limit = tenant.quotas.get(name='ram').limit / 1024
        ram_usage = tenant.quotas.get(name='ram').usage / 1024
        storage_limit = tenant.quotas.get(name='storage').limit / 1024
        storage_usage = tenant.quotas.get(name='storage').usage / 1024
        # RAM > 16 GB
        big_vm_count = Instance.objects.filter(tenant=tenant, ram__gt=16 * 1024).count()
        # Disk > 256 GB
        big_storage_count = Volume.objects.filter(tenant=tenant, size__gt=256 * 1024).count()
        writer.writerow(
            [
                tenant.project.customer.name,
                tenant.project.customer.abbreviation,
                tenant.project.name,
                tenant,
                ram_limit,
                ram_usage,
                storage_limit,
                storage_usage,
                number_of_vms,
                big_vm_count,
                big_storage_count,
            ]
        )
```

### Update limits for all tenants in a specific organization

```python
from waldur_api_client import AuthenticatedClient
from waldur_api_client.api.openstack_tenants import openstack_tenants_list
from waldur_api_client.api.marketplace_resources import marketplace_resources_update_limits
from waldur_api_client.models import ResourceUpdateLimitsRequest

WALDUR_API_URL = '<CHANGEME>'
WALDUR_API_TOKEN = '<CHANGEME>'
CUSTOMER_UUID = '<CHANGEME>'

CORES_LIMIT = 1
RAM_GB_LIMIT = 10
STORAGE_GB_LIMIT = 100

TENANT_LIMITS = {
    'cores': CORES_LIMIT,
    'ram': RAM_GB_LIMIT * 1024,
    'storage': STORAGE_GB_LIMIT * 1024
}

client = AuthenticatedClient(
    base_url="https://api.example.com",
    token="SuperSecretToken",
)

tenants = openstack_tenants_list.sync(
    client=client,
    customer_uuid=CUSTOMER_UUID
)

for tenant in tenants:
    marketplace_resources_update_limits.sync(
        client=client,
        uuid=tenant.marketplace_resource_uuid,
        body=ResourceUpdateLimitsRequest(limits=TENANT_LIMITS)
    )

```

### Generate cost report for a specific organization by month

```python
import sys
import csv

from waldur_core.structure import models as structure_models
from waldur_mastermind.invoices import models as invoice_models

customer = structure_models.Customer.objects.get(abbreviation='Ada')
invoices = invoice_models.Invoice.objects.filter(customer=customer).order_by('year', 'month')
writer = csv.writer(sys.stdout)
for invoice in invoices:
    writer.writerow(
        [
            invoice.year,
            invoice.month,
            invoice.state,
            invoice.price,
            invoice.tax,
            invoice.total,
        ]
    )
```

### Generate a report for VMs created within a specific tenant offering

Upon running the script, please change `year` and `offering_uuid` variables.

```python
from waldur_mastermind.marketplace import models as mm
from urllib.parse import urlparse
from waldur_openstack import models as otm
import csv

year = 2024
offering_uuid = "changeme"

tenant_offering = mm.Offering.objects.get(uuid=offering_uuid)

vm_orders = mm.Order.objects.filter(
    offering__parent=tenant_offering,
    state=mm.Order.States.DONE,
    type=mm.Order.Types.CREATE,
    resource__created__year=year,
).order_by("created")

report = []

for order in vm_orders:
    resource = order.resource
    flavor_url = resource.attributes.get("flavor")

    if flavor_url is None:
        print("flavor_url is missing for order %s" % order)
        continue

    flavor_parsed_url = urlparse(flavor_url)
    flavor_url_parts = flavor_parsed_url.path.split("/")
    flavor_uuid = flavor_url_parts[-2]
    flavor = otm.Flavor.objects.filter(uuid=flavor_uuid).first()

    if flavor is None:
        print("There is no flavor for order %s" % order)
        continue

    system_volume_size = order.attributes["system_volume_size"]
    data_volume_size = resource.attributes.get("data_volume_size", 0)

    vm_terminated = ""
    if resource.state == mm.Resource.States.TERMINATED:
        termination_order = mm.Order.objects.filter(
            resource=resource, state=mm.Order.States.DONE, type=mm.Order.Types.TERMINATE
        ).first()

        if termination_order is None:
            print("Termination order for resource %s does not exist" % resource)
        else:
            vm_terminated = termination_order.consumer_reviewed_at.isoformat()

    report.append(
        {
            "vm_name": resource.name,
            "vm_created": resource.created.isoformat(),
            "vm_terminated": vm_terminated,
            "project_name": resource.project.name,
            "flavor_name": flavor.name,
            "flavor_cores": flavor.cores,
            "flavor_ram": flavor.ram,
            "flavor_disk": flavor.disk,
            "system_volume_size": system_volume_size,
            "data_volume_size": data_volume_size,
        }
    )

report_path = f"vm-report-{year}.csv"

with open(report_path, mode="w") as file:
    fieldnames = [
        "vm_name",
        "vm_created",
        "vm_terminated",
        "project_name",
        "flavor_name",
        "flavor_cores",
        "flavor_ram",
        "flavor_disk",
        "system_volume_size",
        "data_volume_size",
    ]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(report)
```

### Migrate users to a new Keycloak instance

#### Introduction

There are 3 scripts involved:

1. [export-keycloak-user-permissions.py](#export-keycloak-user-permissions): exports Keycloak user data to a `.yaml` file in the following format:

    ```yaml
    - username: johndoe
      email: johndoe@example.com
      full_name: John Doe
      permissions:
        - type: project
          project_uuid: bed45d99e83d4c17a5bf5908ad70554e
          role_uuid: e4130fde02474571a5166bb6742dc2d0
          project_name: "Project 01"
          role_name: "PROJECT.MANAGER"
        - type: customer
          customer_uuid: 1aaec6489ea7492cbe0401997de13653
          role_uuid: 16ec8cf8874d467d9a2c7a0c822c6b3e
          customer_name: "Organization 01"
          role_name: "CUSTOMER.OWNER"
    ```

2. [delete-keycloak-users.py](#delete-keycloak-users): removes data about all the users from an old Keycloak instance

3. [invite-keycloak-users.py](#invite-keycloak-users): creates and sends invitations to the user emails based on their roles in project and organizations

When you are ready to migrate users to the new Keyaloak instance:

1. copy the script file to the `waldur-mastermind-api` container using `docker cp` or `kubectl cp` commands;
2. connect to the container shell using `docker exec` or `kubectl exec`;
3. execute the scripts sequentially using `waldur shell`:

```bash
root@waldur-mastermind-api$ waldur shell < export-keycloak-user-permissions.py
root@waldur-mastermind-api$ waldur shell < delete-keycloak-users.py
root@waldur-mastermind-api$ waldur shell < invite-keycloak-users.py
```

#### export-keycloak-user-permissions

```python
from waldur_core.core import models as core_models
from waldur_core.structure import models as structure_models
from waldur_core.permissions.models import UserRole
from django.contrib.contenttypes.models import ContentType
import yaml

users = core_models.User.objects.filter(is_active=True, registration_method="keycloak")

project_content_type = ContentType.objects.get_for_model(structure_models.Project)
customer_content_type = ContentType.objects.get_for_model(structure_models.Customer)
roles = []

for user in users:
    entry = {
        "username": user.username,
        "email": user.email,
        "full_name": user.get_full_name(),
        "permissions": [],
    }
    perms = UserRole.objects.filter(user=user, is_active=True)

    for permission in perms:
        if permission.content_type == project_content_type:
            project = permission.scope
            entry["permissions"].append(
                {
                    "type": "project",
                    "project_uuid": project.uuid.hex,
                    "role_uuid": permission.role.uuid.hex,
                    "project_name": project.name,
                    "role_name": permission.role.name
                }
            )

        if permission.content_type == customer_content_type:
            customer = permission.scope
            entry["permissions"].append(
                {
                    "type": "customer",
                    "customer_uuid": customer.uuid.hex,
                    "role_uuid": permission.role.uuid.hex,
                    "customer_name": customer.name,
                    "role_name": permission.role.name
                }
            )

    roles.append(entry)

with open("roles.yaml", "w+") as output:
    yaml.dump(roles, output)

```

#### delete-keycloak-users

```python
from waldur_core.core import models as core_models

users = core_models.User.objects.filter(is_active=True, registration_method="keycloak")
users.delete()
```

#### invite-keycloak-users

```python
from waldur_core.structure import models as structure_models
from waldur_core.permissions import models as permission_models
from waldur_core.users import models as user_models
from waldur_core.core.utils import get_system_robot
from waldur_core.users import tasks as user_tasks
import yaml

system_robot = get_system_robot()

user_roles = []

with open("roles.yaml", "r") as roles_file:
    user_roles = yaml.safe_load(roles_file)

for user_role in user_roles:
    email = user_role["email"]
    full_name = user_role["full_name"]

    for perm in user_role["permissions"]:
        role_name = permission_models.Role.objects.get(uuid=perm["role_uuid"]).name
        role_name_suffix = role_name.split(".")[1].lower()

        if perm["type"] == "project":
            project = structure_models.Project.objects.get(uuid=perm["project_uuid"])

            invitation, created = user_models.Invitation.objects.get_or_create(
                email=email,
                full_name=full_name,
                customer=project.customer,
                project=project,
                project_role=role_name_suffix,
                created_by=system_robot,
            )

            if not created:
                continue

            print(
                f"Inviting user {full_name} ({email}) to project {project} as {role_name_suffix}"
            )
            user_tasks.send_invitation_created(
                invitation.uuid.hex, system_robot.full_name
            )

        if perm["type"] == "customer":
            customer = structure_models.Customer.objects.get(uuid=perm["customer_uuid"])

            invitation, created = user_models.Invitation.objects.get_or_create(
                email=email,
                full_name=full_name,
                customer=customer,
                customer_role=role_name_suffix,
                created_by=system_robot,
            )

            if not created:
                continue

            print(
                f"Inviting user {full_name} ({email}) to customer {customer} as {role_name_suffix}"
            )
            user_tasks.send_invitation_created(
                invitation.uuid.hex, system_robot.full_name
            )
```

### User deletion examples

#### Basic user deletion

```python
from waldur_core.core.models import User

# Delete user by exact username
user = User.objects.get(username='example_username')
user.delete()

# Delete user by email
user = User.objects.get(email='username@example.com')
user.delete()
```

#### Find and delete users with partial information

```python

from waldur_core.core.models import User

# Find and delete user when you only know part of the username
# Note: filter() can return multiple results, first() gets only the first match
user = User.objects.filter(username__icontains='smith').first()
if user:
    user.delete()
```

#### Find and delete user based on OfferingUser information

```python
from waldur_mastermind.marketplace.models import OfferingUser

# This is useful when the username of the main User comes for example from MyAcessId with a complex format, but you know information about their OfferingUser, for example their username
offering_user = OfferingUser.objects.get(username='test_user')

print(f"Found offering user: {offering_user}")

if offering_user:
    user = offering_user.user
    print(f"Found user: {user.username}")  # Verify it's the correct user
    user.delete()
```

⚠️ **Important notes**:

- Always verify you have the correct user before deletion
- User deletion will cascade and remove all related permissions and roles
- For users authenticated via external providers (LDAP, SAML, etc.), this only removes the user from Waldur
