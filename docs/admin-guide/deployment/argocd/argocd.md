# Waldur deployment in ArgoCD

[This repository](https://github.com/waldur/csl-poc) contains ansible playbook settings for infrastructure setup (`ansible/` directory)
together with Kubernetes manifest files for different applications managed by ArgoCD (`applications/` directory).

## Infrastructure setup

Before beginning with application management, infrastructure setup is required.
For this, you should use the playbook [ansible/cloud-infrastructure-setup.yaml](https://github.com/waldur/csl-poc/blob/main/ansible/cloud-infrastructure-setup.yaml).
Given an access to virtual machines with python3.8+ installed, it is capable of:

1. Disk setup in case if each virtual machine has a separate disk attached as a device;
2. Installation of [RKE2-managed Kubernetes cluster](https://docs.rke2.io/) with a single server and workers;
3. Installation of [Helm tool binary](https://helm.sh/);
4. Installation of ArgoCD: both Kubernetes manifests and command-line binary.

All these steps can be customized via either [ansible/vars.defaults](https://github.com/waldur/csl-poc/blob/main/ansible/vars.defaults) or `ansible/vars.custom` file.

The example infra has 3 VMs with `python3.9` installed.
After establishing ssh-based connection to the machines, you can execute the playbook:

```bash
ansible-playbook -i hosts -D cloud-infrastructure-setup.yaml
```

After successful run, the infra is ready for further steps.

## Installation and management of applications

You should run all the command described below on the RKE2 server, where ArgoCD binary installed, only.

### Prerequisite

The following lines ensure user login to ArgoCD server via `argocd` binary.
They should run prior to every application-related action.

```bash
ARGOCD_SERVER_IP=$(kubectl get service argocd-server -n argocd -o jsonpath={.spec.clusterIP})
ARGOCD_ADMIN_PASSWORD=$(argocd admin initial-password -n argocd | head -n1)
argocd login $ARGOCD_SERVER_IP:80 --username admin --password $ARGOCD_ADMIN_PASSWORD --name default
```

You can validate authentication and access:

```bash
argocd account get-user-info
argocd app list
```

### Longhorn

You can use [this app manifest](https://github.com/waldur/csl-poc/blob/main/applications/longhorn/application.yaml) and
[this custom values file](https://github.com/waldur/csl-poc/blob/main/applications/longhorn/values-custom.yaml) for Longhorn installation.

This script creates a new Kubernetes namespace, where application is created synched:

```bash
kubectl create namespace longhorn-system
argocd app create -f applications/longhorn/application.yaml
argocd app sync argocd/longhorn
```

### PostgreSQL operator

You can use [this app manifest](https://github.com/waldur/csl-poc/blob/main/applications/postgresql-operator/application.yaml) and
[this custom values file](https://github.com/waldur/csl-poc/blob/main/applications/postgresql-operator/values-custom.yaml) for PostgreSQL operator installation.

This script creates a new Kubernetes namespace, where application is created synched:

```bash
kubectl create namespace postgres-operator-system
argocd app create -f applications/postgresql-operator/application.yaml
argocd app sync argocd/postgres-operator
```

### Waldur

Waldur requires PostgreSQL database as a persistent storage and RabbitMQ as a message queue to be up and running.

Firstly, you need to create a namespace for Waldur:

```bash
kubectl create namespace waldur
```

Secondly, create and sync PostgreSQL application managed by the operator installed before.
You can use [this manifest](https://github.com/waldur/csl-poc/blob/main/applications/waldur-postgresql/application.yaml) for ArgoCD app and [this manifest](https://github.com/waldur/csl-poc/blob/main/applications/waldur-postgresql/manifests/waldur-postgresql.yaml) for modification of the DB settings.

```bash
argocd app create -f applications/waldur-postgresql/application.yaml
argocd app sync argocd/waldur-postgresql
```

Finally, you can deploy Waldur using [this app manifest](https://github.com/waldur/csl-poc/blob/main/applications/waldur/application.yaml) and [these values](https://github.com/waldur/csl-poc/blob/main/applications/waldur/values-custom.yaml). **NB**: RabbitMQ is included in the deployment.

```bash
argocd app create -f applications/waldur/application.yaml
argocd app sync argocd/waldur
```
