# RKE2 installation and setup

To install Waldur on top of [RKE2](https://docs.rke2.io/) you need to:

1. Install [Ansible](https://docs.ansible.com/ansible/2.9/) with version >= 2.9.

1. Download this repository

1. Install `kubernetes.core` collection from ansible galaxy and download installation files.

    ```bash
    ansible-galaxy collection install kubernetes.core
    # or
    curl -o ansible-galaxy/kubernetes-core-2.3.2.tar.gz --create-dirs https://galaxy.ansible.com/download/kubernetes-core-2.3.2.tar.gz
    ansible-galaxy collection install ansible-galaxy/kubernetes-core-2.3.2.tar.gz


    cd ansible-config/

    curl -o rke2/rke2-install.sh --create-dirs https://get.rke2.io

    curl -fsSL -o helm/get_helm.sh --create-dirs https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
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
    ansible-playbook -D -i rke2_inventory main.yaml
    ```
