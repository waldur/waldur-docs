# Waldur on RKE2

## RKE2 installation and setup

To install Waldur on top of [RKE2](https://docs.rke2.io/) you need to:

1. Install [Ansible](https://docs.ansible.com/ansible/2.10/) with version >= 2.10 and ensure python3 is installed.

1. Download this repository

1. Install `kubernetes.core` collection from ansible galaxy and download installation files.

    ```bash
    ansible-galaxy collection install kubernetes.core
    # or
    curl -o ansible-galaxy/kubernetes-core-2.3.2.tar.gz --create-dirs https://galaxy.ansible.com/download/kubernetes-core-2.3.2.tar.gz
    ansible-galaxy collection install ansible-galaxy/kubernetes-core-2.3.2.tar.gz


    cd ansible-config/

    curl -o rke2/rke2-install.sh --create-dirs https://get.rke2.io

    curl -fsSL -o helm/get-helm.sh --create-dirs https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
    ```

1. Download Helm chart archives if your target machines don't have internet access

    ```bash
    cd ansible-config/
    curl -o longhorn/longhorn-1.3.1.tgz --create-dirs https://github.com/longhorn/charts/releases/download/longhorn-1.3.1/longhorn-1.3.1.tgz
    curl -o kubernetes-dashboard/k8s-dashboard-5.10.0.tar.gz --create-dirs https://kubernetes.github.io/dashboard/kubernetes-dashboard-5.10.0.tgz
    curl -s -o bitnami/postgresql-11.9.1.tgz --create-dirs https://charts.bitnami.com/bitnami/postgresql-11.9.1.tgz
    curl -s -o bitnami/rabbitmq-10.3.5.tgz --create-dirs https://charts.bitnami.com/bitnami/rabbitmq-10.3.5.tgz
    curl -sL -o waldur/waldur-chart.zip --create-dirs https://github.com/waldur/waldur-helm/archive/refs/heads/master.zip
    ```

1. Adjust variables in `ansible-config/rke2_vars` file

1. Run the playbook

    ```bash
    cd ansible-config
    ansible-playbook -D -i rke2_inventory install.yaml
    ```

You can check Waldur release installation with the following steps:

1. ssh to a node from inventory with `initial_server=true` mark
2. check all the pods from namespace:

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

## Update of Waldur

To update Waldur user needs to execute the corresponding playbook:

```bash
cd ansible-config
ansible-playbook -D -i rke2_inventory update.yaml
```

## Update SSL certificates

To update the SSL certificates, please do the following steps:

1. Copy the certificates and keys to the `ansible-config/waldur/tls` directory. **NB: key must be named `tls.key` and cert itself - `tls.crt`**
2. [Update Waldur release](#update-of-waldur)

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
