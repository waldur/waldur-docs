# Waldur Shell

Waldur provides a shell for command line scripting. To start a shell, run ``waldur shell`` in the MasterMind context.

For docker-compose deployments, please run:

``docker exec -it waldur-mastermind-api waldur shell``

For Helm-based K8s deployments, please run:

``kubectl exec --stdin --tty waldur-mastermind-worker-POD-ID -- waldur shell``

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
