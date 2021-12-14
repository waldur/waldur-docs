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
