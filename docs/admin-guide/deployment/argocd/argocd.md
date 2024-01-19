# csl-poc

This repository contains ansible playbook settings for infrastructure setup (`ansible/` directory)
together with Kubernetes manifest files for different application managed by ArgoCD (`applications/` directory).

## Infrastructure setup

Before user begins with management of applications, infrastructure setup is required.
For this, you should use the playbook `ansible/cloud-infrastructure-setup.yaml`.
Given an access to virtual machines with python3.8+ installed, it is capable of:

1. Disk setup in case if each virtual machine has a separate disk attached as a device;
2. Installation of [RKE2-managed Kubernetes cluster](https://docs.rke2.io/) with a single server and workers;
3. Installation of [Helm tool binary](https://helm.sh/);
4. Installation of ArgoCD: both Kubernetes manifests and command-line binary.

All these steps can be customized via either `ansible/vars.defaults` or `ansible/vars.custom` file.

The example infra has 3 VMs with python3.9 installed.
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

```bash
kubectl create namespace longhorn-system
argocd app create -f applications/longhorn/application.yaml
argocd app sync argocd/longhorn
```

### PostgreSQL operator

```bash
kubectl create namespace postgres-operator-system
argocd app create -f applications/postgresql-operator/application.yaml
argocd app sync argocd/postgres-operator
```

### Waldur

```bash
kubectl create namespace waldur
```

```bash
argocd app create -f applications/waldur-postgresql/application.yaml
argocd app sync argocd/waldur-postgresql
```

*NB*: RabbitMQ included

```bash
argocd app create -f applications/waldur/application.yaml
argocd app sync argocd/waldur
```
