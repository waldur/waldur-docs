## Waldur Helm

Waldur publishes a Helm chart for easy deployment on a Kubernetes cluster using the [Helm](https://helm.sh) package manager.

## Installing prerequisites

1. Install Kubernetes server.
2. Install Kubernetes client, i.e. kubetctl.
3. Install [Helm](https://helm.sh/docs/intro/install/)

## Installing the Chart

1. Add the stable repository
```
  helm repo add stable https://charts.helm.sh/stable
```
2. Install Chart dependencies:
```
  helm dep update waldur
```
3. Setup database:

    3.1 Setup single PostgreSQL DB: [instructions](https://github.com/waldur/waldur-helm/blob/master/docs/postgres-db.md), or

    3.2 Setup PostgreSQL HA DB: [instructions](https://github.com/waldur/waldur-helm/blob/master/docs/postgres-db-ha.md)

    **NB** Only one of these two options should be used. Otherwise, DB will be unavailable.
4. Install minio (for media): [instructions](https://github.com/waldur/waldur-helm/blob/master/docs/minio.md)
5. Install RabbitMQ for task queue: [instructions](https://github.com/waldur/waldur-helm/blob/master/docs/rabbitmq.md)
5. Install Helm package:
```
  # in 'waldur-helm-poc/'
  helm install waldur waldur
```
**NB** After this command, Waldur release will run in `default` namespace. Please, pay attention in which namespace which release is running.

For instance, you can install Waldur release in `test` namespace in the following way:

1. Create `test` namespace:
```
  kubectl create namespace test
```
2. Install release:
```
  helm install waldur waldur --namespace test
```

## Adding admin user
Open waldur-mastermind-worker shell and execute the following command:

1. Get waldur-mastermind-worker pod name
```
  # Example:
  kubectl get pods -A | grep waldur-mastermind-worker # -->
  # default       waldur-mastermind-worker-6d98cd98bd-wps8n   1/1     Running     0          9m9s
```
2. Connect to pod via shell
```
  # Example:
  kubectl exec -it waldur-mastermind-worker-6d98cd98bd-wps8n -- /bin/bash
```
3. Execute command to add admin user
```
  waldur createstaffuser -u user -p password -e admin@example.com
```

## Waldur Helm chart release upgrading
Delete initdb job (if exitsts):
```bash
  kubectl delete job waldur-mastermind-initdb-job || true
```

Upgrade Waldur dependencies and release:
```bash
  helm dep update waldur/
  helm upgrade waldur waldur/
```

Restart deployments to apply configmaps changes:

```bash
  kubectl rollout restart deployment waldur-mastermind-beat
  kubectl rollout restart deployment waldur-mastermind-api
  kubectl rollout restart deployment waldur-mastermind-worker
  kubectl rollout restart deployment waldur-homeport
```
