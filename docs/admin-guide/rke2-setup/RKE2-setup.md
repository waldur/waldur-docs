# RKE2 installation and setup

For basic installation of [RKE2](https://docs.rke2.io/), an user needs to:

1. Install [Ansible](https://docs.ansible.com/ansible/2.9/) with version >= 2.9.
1. Download the [playbook archive](rke2-setup.tar.gz)
1. Unarchive it

    ```bash
    tar xvfz rke2-setup.tar.gz
    ```

1. Install `kubernetes.core` collection from ansible galaxy and download installation files.

    ```bash
    ansible-galaxy collection install kubernetes.core
    curl -o rke2-install.sh https://get.rke2.io
    curl -o get-helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
    ```

1. Run the playbook

    ```bash
    ansible-playbook -D -i rke2_inventory.ini rke2-setup.yaml
    ```
