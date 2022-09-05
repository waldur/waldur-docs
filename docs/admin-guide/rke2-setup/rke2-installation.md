# Installation of RKE2

For basic installation of [RKE2](https://docs.rke2.io/), an user needs to:

1. Download and update [inventory](src/rke2_inventory.ini)
1. Download and update [vars](src/rke2_vars.yaml)
1. Download the [playbook](src/rke2-setup.yaml) and run the script below. It requires [Ansible](https://docs.ansible.com/ansible/2.9/) with version >= 2.9.

    ```bash
    curl -o rke2-install.sh https://get.rke2.io
    ansible-playbook -D -i rke2_inventory.ini rke2-setup.yaml
    ```
