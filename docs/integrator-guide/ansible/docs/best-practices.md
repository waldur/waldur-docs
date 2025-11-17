# Best practices

## Installing from Ansible Galaxy

Once the collection is published, any Ansible user can easily install and use it.

1. **Install the Collection:**

   ```bash
    ansible-galaxy collection install waldur.structure
   ```

2. **Use it in a Playbook:**
    After installation, the modules are available globally. Users can simply write playbooks referencing the FQCN.

    ```yaml
    - name: Create a Waldur Project
      hosts: my_control_node
      tasks:
        - name: Ensure project exists
          waldur.structure.project:
            state: present
            name: "Production Project"
            customer: "Customer Name"
            api_url: "http://127.0.0.1:8000/api/"
            access_token: "{{ my_waldur_token }}"
    ```

## Use in a Playbook

This is the standard and recommended way to use the collection for automation.

**`test_playbook.yml`:**

```yaml
- name: Manage Waldur Resources with Generated Collection
 hosts: localhost
 connection: local
 gather_facts: false
 # Good practice to declare the collection you are using
 collections:
   - waldur.structure

 vars:
  waldur_api_url: "https://api.example.com/api/"
  waldur_access_token: "WALDUR_ACCESS_TOKEN"

 tasks:
   - name: Ensure 'My Playbook Project' exists
     # Use the FQCN of the module
     project:
       state: present
       name: "My Playbook Project"
       customer: "Big Corp"
       api_url: "{{ waldur_api_url }}"
       access_token: "{{ waldur_access_token }}"
     register: project_info

   - name: Show the created or found project details
     ansible.builtin.debug:
       var: project_info.resource

```

**Run the playbook:**

```bash
# Set the environment variables first
export ANSIBLE_COLLECTIONS_PATH=./outputs
export WALDUR_ACCESS_TOKEN='YOUR_SECRET_TOKEN'

# Run the playbook
ansible-playbook test_playbook.yml
```

**Example Output (Success, resource created):**

```text
PLAY [Manage Waldur Resources with Generated Collection] ******************

TASK [Ensure 'My Playbook Project' exists] **************************************
changed: [localhost]

TASK [Show the created or found project details] ********************************
ok: [localhost] => {
  "project_info": {
      "changed": true,
      "commands": [
          {
              "body": {
                  "customer": "https://api.example.com/api/customers/...",
                  "name": "My Playbook Project"
              },
              "description": "Create new project",
              "method": "POST",
              "url": "https://api.example.com/api/projects/"
          }
      ],
      "failed": false,
      "resource": {
          "created": "2024-03-21T12:05:00.000000Z",
          "customer": "https://api.example.com/api/customers/...",
          "customer_name": "Big Corp",
          "description": "",
          "name": "My Playbook Project",
          "url": "https://api.example.com/api/projects/...",
          "uuid": "a1b2c3d4e5f67890abcdef1234567890"
      }
  }
}

PLAY RECAP **********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    ...
```

## Running Modules Locally

Since all Waldur modules interact with a remote API, they are considered "control-plane" modules.
They should always be executed from the Ansible control node (`localhost`), not on remote target hosts.

The recommended way to achieve this is by setting `connection: local` at the top of your playbook.

**`manage_waldur.yml`:**

```yaml
- name: Manage Waldur Resources
  hosts: localhost
  connection: local
  gather_facts: false
  collections:
    - waldur.structure

  vars:
    waldur_api_url: "https://api.example.com/api/"
    waldur_access_token: "{{ lookup('env', 'WALDUR_ACCESS_TOKEN') }}"

  tasks:
    - name: Ensure 'My Ansible-Managed Project' exists
      project:
        state: present
        name: "My Ansible-Managed Project"
        customer: "Big Corp"
        api_url: "{{ waldur_api_url }}"
        access_token: "{{ waldur_access_token }}"
```

This ensures that Ansible runs the tasks on the machine executing the playbook,
which is the correct context for making API calls.

## Reducing Boilerplate with `module_defaults`

To avoid repeating common parameters like `api_url`, `access_token`, `customer`, `project`, and `tenant`
in every task, you can use Ansible's powerful `module_defaults` feature. Each generated Waldur collection
comes with a predefined **action group** that includes all of its modules.

You can set default values for these parameters once at the play or block level,
making your playbooks dramatically cleaner and easier to maintain.

**Before (Repetitive and Hard to Read):**

Without `module_defaults`, a typical OpenStack provisioning playbook becomes verbose and error-prone,
with the same five context parameters repeated in every task.

```yaml
- name: Provision OpenStack Resources (The Repetitive Way)
  hosts: localhost
  connection: local

  vars:
    # Define common parameters as variables
    waldur_api_url: "https://api.example.com/api/"
    waldur_access_token: "{{ lookup('env', 'WALDUR_ACCESS_TOKEN') }}"
    waldur_customer: "Big Corp Inc."
    waldur_project: "Production Project"
    waldur_tenant: "Cloud Tenant A"

  tasks:
    - name: Ensure a security group for web servers exists
      waldur.openstack.security_group:
        state: present
        name: "web-servers-sg"
        # --- Boilerplate ---
        api_url: "{{ waldur_api_url }}"
        access_token: "{{ waldur_access_token }}"
        customer: "{{ waldur_customer }}"
        project: "{{ waldur_project }}"
        tenant: "{{ waldur_tenant }}"

    - name: Ensure a data volume exists
      waldur.openstack.volume:
        state: present
        name: "app-data-volume"
        offering: "Volume offering in {{ waldur_tenant }}"
        size: 50 # in GiB
        # --- Boilerplate ---
        api_url: "{{ waldur_api_url }}"
        access_token: "{{ waldur_access_token }}"
        customer: "{{ waldur_customer }}"
        project: "{{ waldur_project }}"

    - name: Provision the main web server VM
      waldur.openstack.instance:
        state: present
        name: "web-server-01"
        offering: "VM offering in {{ waldur_tenant }}"
        flavor: "g-standard-2"
        image: "Ubuntu 22.04"
        system_volume_size: 20
        security_groups:
          - "web-servers-sg"
        # --- Boilerplate ---
        api_url: "{{ waldur_api_url }}"
        access_token: "{{ waldur_access_token }}"
        customer: "{{ waldur_customer }}"
        project: "{{ waldur_project }}"
```

**After (Clean, DRY, and Recommended):**

By using `module_defaults`, you define the shared context once. The tasks become short, readable,
and focused only on what makes them unique.

The generator creates a group named after the collection.
For the `waldur.openstack` collection, the group name is `waldur.openstack.openstack`.

```yaml
- name: Provision OpenStack Resources (The Clean Way)
  hosts: localhost
  connection: local

  vars:
    # Define your common parameters as variables
    waldur_api_url: "https://api.example.com/api/"
    waldur_access_token: "{{ lookup('env', 'WALDUR_ACCESS_TOKEN') }}"
    waldur_customer: "Big Corp Inc."
    waldur_project: "Production Project"
    waldur_tenant: "Cloud Tenant A"

  # Set defaults for the entire 'waldur.openstack' group of modules.
  # This applies to security_group, volume, instance, and all others.
  module_defaults:
    group/waldur.openstack.openstack:
      api_url: "{{ waldur_api_url }}"
      access_token: "{{ waldur_access_token }}"
      customer: "{{ waldur_customer }}"
      project: "{{ waldur_project }}"
      # 'tenant' is specific to OpenStack, so we add it here.
      tenant: "{{ waldur_tenant }}"

  tasks:
    - name: Ensure a security group for web servers exists
      # No boilerplate needed!
      waldur.openstack.security_group:
        state: present
        name: "web-servers-sg"
        # The 'tenant' default is automatically applied.

    - name: Ensure a data volume exists
      waldur.openstack.volume:
        state: present
        name: "app-data-volume"
        offering: "Volume offering in {{ waldur_tenant }}"
        size: 50 # in GiB
        # 'project' and auth parameters are inherited.

    - name: Provision the main web server VM
      waldur.openstack.instance:
        state: present
        name: "web-server-01"
        offering: "VM offering in {{ waldur_tenant }}"
        flavor: "g-standard-2"
        image: "Ubuntu 22.04"
        system_volume_size: 20
        security_groups:
          - "web-servers-sg"
        # 'project' and 'tenant' context for resolving security_groups
        # are also inherited from the module defaults.
```

This approach leverages standard Ansible features to provide the exact convenience you're looking for,
making the generated collections a pleasure to use in complex, real-world scenarios.

## Dynamic Resource Composition (Find-Then-Use)

This is a powerful and highly recommended best practice that combines `facts` modules
with resource management modules (`order` or `crud`). It allows you to write
declarative playbooks that don't rely on hardcoded, opaque identifiers like URLs or UUIDs.

The workflow is simple:

1. Use a `facts` module with filters (`fixed_ips`, `network_name`, etc.)
   to find the exact resource you need. The module will ensure exactly one resource is found.
2. Register the result.
3. Use the `url` from the registered `resource` object to create or update another resource.

This pattern is the solution for attaching pre-existing resources,
such as a network port with a specific IP address, to a new VM.

**Example: Create a VM and attach a pre-existing port by its IP address.**

```yaml
- name: Provision a VM with a specific, pre-existing port
  hosts: localhost
  collections:
    - waldur.openstack

  tasks:
    - name: "Find the port with the static IP 192.168.10.55"
      port_facts:
        api_url: "{{ waldur_api_url }}"
        access_token: "{{ waldur_access_token }}"
        project: "Cloud Project"
        network_name: "Waldur internal network"
        # Filter by the IP address. The facts module will find the port.
        fixed_ips: "192.168.10.55"
      register: static_port_info

    - name: "Provision the VM and attach the found port"
      instance:
        api_url: "{{ waldur_api_url }}"
        access_token: "{{ waldur_access_token }}"
        state: present
        project: "Cloud Project"
        offering: "VM in MyCloud"
        name: "vm-with-static-ip"
        flavor: "g-standard-2"
        image: "Ubuntu 22.04"
        system_volume_size: 20
        # Use the URL directly from the registered 'resource' object.
        ports:
          - port: "{{ static_port_info.resource.url }}"
```

## Low-Level Order Management (`crud` plugin on orders)

This is an **advanced pattern** for users who need to interact directly with the order object itself, similar
to the old generic `waldur_marketplace` module. The `waldur.marketplace.order` module is used for this.

- You define the **order itself**, passing all resource-specific details in the `attributes` dictionary.
- The module creates the order and returns the **order object**. It does *not* wait for the resource to be
  provisioned.

```yaml
- name: Create a generic order
  hosts: localhost
  collections:
    - waldur.marketplace

  tasks:
    - name: "Create a marketplace order object"
      order:
        api_url: "{{ waldur_api_url }}"
        access_token: "{{ waldur_access_token }}"
        state: present
        project: "Cloud Project"
        offering: "VM in MyCloud"
        plan: "Standard Plan"
        attributes:
          name: "my-vm-from-generic-order"
          flavor: http://api.example.com/api/openstack-flavors/flavor-uuid/
          image: http://api.example.com/api/openstack-images/image-uuid/
          system_volume_size: 10240
```

## Mapping UI Terms to Ansible Parameters

To provide the best possible user experience, Ansible playbook parameters are designed to be intuitive.
However, terminology can sometimes differ between the Waldur Web UI and the underlying cloud platform (like OpenStack).
This guide provides a mapping for the most common terms to help you write your playbooks with confidence.

| Waldur UI Term | Ansible Parameter | OpenStack Term | Notes |
| :--- | :--- |:--- | :--- |
| **Organization** | `customer` | N/A | This is the top-level entity in Waldur that holds projects and cloud resources. |
| **Project** | `project` | N/A | Waldur project is a container for organizing resources and teams. |
| **Virtual Private Cloud / VPC** | `tenant` | Project / Tenant | In Ansible term Tenant is used. |
| **Instance / VM** | `instance` | Server | OpenStack refer to this as a "Server". |
