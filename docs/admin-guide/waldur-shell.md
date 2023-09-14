# Waldur Shell

Waldur provides a shell for command line scripting. To start a shell, run ``waldur shell`` in the MasterMind context.

For docker-compose deployments, please run:

``docker exec -it waldur-mastermind-api waldur shell``

For Helm-based K8s deployments, please run:

```
kubectl get pods -A | grep waldur-mastermind-worker  # to find POD id
kubectl exec --stdin --tty waldur-mastermind-worker-POD-ID -- waldur shell
```

## Examples

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
from waldur_openstack.openstack.models import Tenant

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

from waldur_openstack.openstack.models import Tenant
from waldur_openstack.openstack_tenant.models import Instance, Volume
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
        ss = ServiceSettings.objects.get(scope=tenant)
        # RAM > 16 GB
        big_vm_count = Instance.objects.filter(service_settings=ss, ram__gt=16 * 1024).count()
        # Disk > 256 GB
        big_storage_count = Volume.objects.filter(service_settings=ss, size__gt=256 * 1024).count()
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