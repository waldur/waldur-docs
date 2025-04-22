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

## Debug mode activation

⚠️ **Warning**: Debug mode should ONLY be used in development environments.

For development deployments, you can enable debug mode:

```yaml
# In values.yaml
waldur:
  debug: true
```

For production troubleshooting, use targeted logging instead of enabling full debug mode.
