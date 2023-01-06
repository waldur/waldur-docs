# Waldur on RKE2

## RKE2 installation and setup

To install Waldur on top of [RKE2](https://docs.rke2.io/) you need to:

1. Install [Ansible](https://docs.ansible.com/ansible/2.10/) with version >= 2.10 and ensure python3 is installed.

1. Download this repository

1. Install `kubernetes.core` collection from ansible galaxy.

    ```bash
    ansible-galaxy collection install kubernetes.core
    ansible-galaxy collection install ansible.posix
    # or
    curl -L -o ansible-galaxy/kubernetes-core-2.3.2.tar.gz --create-dirs https://galaxy.ansible.com/download/kubernetes-core-2.3.2.tar.gz
    ansible-galaxy collection install ansible-galaxy/kubernetes-core-2.3.2.tar.gz

    curl -L -o ansible-galaxy/ansible-posix-1.4.0.tar.gz https://galaxy.ansible.com/download/ansible-posix-1.4.0.tar.gz
    ansible-galaxy collection install ansible-galaxy/ansible-posix-1.4.0.tar.gz
    ```

1. Adjust variables in `ansible-config/rke2_vars` file

1. (Optional) Run the playbook to setup infrastructure (Kubernetes and Longhorn):

    ```bash
    cd ansible-config
    ansible-playbook -D -i rke2_inventory install-infrastructure.yaml
    ```

1. Run the playbook to install Waldur and dependencies:

    ```bash
    cd ansible-config
    ansible-playbook -D -i rke2_inventory install-applications.yaml
    ```

You can check Waldur release installation with the following steps:

1. ssh to a node from inventory with `initial_server=true` and check all the pods from the default namespace:

    ```bash
    export KUBECONFIG=/etc/rancher/rke2/rke2.yaml
    kubectl get pods -n default
    ```

If you run Waldur in a different namespace, please adjust the value of the `-n` option in the last command above.

## Add admin ssh keys

1. Setup `admin_keys` and `revoked_admin_keys` vars in the `ansible-config/rke2_vars` file
1. Run the corresponding playbook

    ```bash
    cd ansible-config
    ansible-playbook -D -i rke2_inventory add-ssh-keys.yml
    ```

## Add haproxy load balancer

1. Setup `haproxy_stats_password` var in the `ansible-config/rke2_vars` file
1. Run the corresponding playbook

    ```bash
    cd ansible-config
    ansible-playbook -D -i rke2_inventory add-haproxy-host.yml
    ```

## Waldur Helm configuration

A user can override default settings for Waldur Helm. The `ansible-config/waldur/values.yaml` is the main settings file. Additional configuration features files (e.g. for SAML2, whitelabeling, bootstrapping, etc.) can be included by placing into corresponding subdirectories of `ansible-config/waldur/` folder. The paths to the subdirectories should be specified in `ansible-config/waldur/values.yaml`, e.g. `waldur.saml2.dir` value.

Waldur Helm configuration is described in [the public docs](https://docs.waldur.com/admin-guide/deployment/helm/); example `values.yaml` file: [link](https://github.com/waldur/waldur-helm/blob/master/waldur/values.yaml), example additional files: [link](https://github.com/waldur/waldur-helm/tree/master/waldur/test).

## Update of Waldur

To update Waldur user needs to execute the corresponding playbook:

```bash
cd ansible-config
ansible-playbook -D -i rke2_inventory update-waldur.yaml
```

## Update of Waldur dependencies

To update Waldur dependencies, a user should:

1. Setup the desired components for update in `ansible-config/rke2_vars` file, e.g. set `setup_postgresql` to `yes` in case of PostgreSQL Helm chart update. **NB: please, don't change chart versions manually, it can cause failure of Waldur application**
1. Run the corresponding playbook:

    ```bash
    cd ansible-config
    ansible-playbook -D -i rke2_inventory update-dependencies.yaml
    ```

Example of changes in `ansible-config/rke2_vars` file:

```yaml
# Waldur dependency setup
setup_postgresql: yes # User can skip PostgreSQL setup
postgresql_version: 11.9.1 # Version of PostgreSQL Helm chart

setup_rabbitmq: no # User can skip RabbitMQ setup
rabbitmq_version: 10.3.5 # Version of RabbitMQ Helm chart

setup_minio: no # User can skip MinIO setup
minio_version: 11.10.16 # Version of MinIO Helm chart
```

With this setup, the playbook will update PostgreSQL release only. If the user wants to update RabbitMQ too, they should set `setup_rabbitmq: yes`

## Waldur log fetching

To get logs from Waldur containers, a users needs to connect to one of the RKE2 nodes:

```bash
ssh <node-ip>
```

A node IP should be chosen from the inventory file (e.g. `rke2_inventory`).

In the node's shell, the user should run the following to setup Kubernetes client:

```bash
export KUBECONFIG=/etc/rancher/rke2/rke2.yaml
```

After this, the user can get Waldur API logs:

```bash
kubectl logs --tail 100 -l app=waldur-mastermind-api -n default
```

Same works for Celery worker:

```bash
kubectl logs --tail 100 -l app=waldur-mastermind-worker -n default
```

**Note**: if you use a non-default namespace for Waldur release, please change the value for `-n` option in the aforementioned command

## Update SSL certificates

To update the SSL certificates, please do the following steps:

1. Copy the certificates and keys to the `ansible-config/waldur/tls` directory. **NB: key must be named `tls.key` and cert itself - `tls.crt`**
1. [Update Waldur release](#update-of-waldur)

## Enable K8s dashboard

Make sure that K8s dashboard is deployed. Login to one of the K8s nodes.

```bash
# create / renew token for admin user
kubectl -n kubernetes-dashboard create token admin-user

# setup kubectl port fortward to k8s-dashboard service
kubectl port-forward -n kubernetes-dashboard service/kubernetes-dashboard --address 0.0.0.0 8001:443
```

K8s dashboard should now be accessible on port 8001 in that node -- or load balancer node on port 8001 if configured.

## Recover data from DB backup

In order to apply an existing backup to database, a corresponding playbook exists.

**NB:**

- **This operation drops an existing database, creates an empty one and applies the pre-created backup**
- **During restoration process, the site will be unavailable**

During execution, you will be asked about backup name. You should input it in a correct way. Example of running playbook:

```log
TASK [List backups] ****************************************************************************************************************************************
ok: [csl-stg-kubs01] => {}

MSG:

[+] LOCAL_PG_BACKUPS_DIR :
[+] MINIO_PG_BACKUPS_DIR : pg/data/backups/postgres
[+] Setting up the postgres alias for minio server (http://minio.default.svc.cluster.local:9000)
[+] Last 5 backups
[2022-12-01 05:00:02 UTC]  91KiB backup-2022-12-01-05-00.sql.gz
[2022-11-30 05:00:02 UTC]  91KiB backup-2022-11-30-05-00.sql.gz
[2022-11-29 05:00:02 UTC]  91KiB backup-2022-11-29-05-00.sql.gz
[2022-11-28 16:30:37 UTC]  91KiB backup-2022-11-28-16-30.sql.gz
[2022-11-28 16:28:27 UTC]  91KiB backup-2022-11-28-16-28.sql.gz
[+] Finished
[Choose backup]
Please enter backup's name:
```

After this, you should input one of the following lines:

- backup-2022-12-01-05-00.sql.gz
- backup-2022-11-30-05-00.sql.gz
- backup-2022-11-29-05-00.sql.gz
- backup-2022-11-28-16-30.sql.gz
- backup-2022-11-28-16-28.sql.gz

Otherwise, the entire process will fail, but the site and database with old data will be still available.

To start the process, please, execute the following line in the machine connected to RKE2 nodes:

```bash
ansible-playbook -D -i rke2_inventory restore-data.yaml
```
