# Modele author guide

## Core Concept

The generator works by combining three main components:

1. **OpenAPI Specification (`waldur_api.yaml`):** The single source of truth for all available API endpoints,
   their parameters, and their data models.
2. **Generator Configuration (`generator_config.yaml`):** A user-defined YAML file where you describe the Ansible
   Collection and the modules you want to create. This is where you map high-level logic (like "create a resource")
   to specific API operations.
3. **Plugins:** The engine of the generator. A plugin understands a specific workflow or pattern (e.g., fetching
   facts, simple CRUD, or complex marketplace orders) and contains the logic to build the corresponding Ansible
   module code.

## Getting Started

### Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/docs/#installation) (for dependency management and running scripts)
- Ansible Core (`ansible-core >= 2.14`) for building and using the collection.

### Installation

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd ansible-waldur-generator
   ```

2. Install the required Python dependencies using Poetry:

   ```bash
   poetry install
   ```

   This will create a virtual environment and install packages like `PyYAML`, and `Pytest`.

### Running the Generator

To generate the Ansible Collection, run the `generate` script defined in `pyproject.toml`:

```bash
poetry run ansible-waldur-generator
```

By default, this command will:

- Read `inputs/generator_config.yaml` and `inputs/waldur_api.yaml`.
- Use the configured collection name (e.g., `waldur.openstack`) to create a standard Ansible Collections
  structure.
- Place the generated collection into the `outputs/` directory.

The final structure will look like this:

```text
outputs/
└── ansible_collections/
    └── waldur/
        ├── structure/          # Collection 1
        │   ├── galaxy.yml
        │   ├── plugins/
        │   │   ├── modules/
        │   │   │   ├── customer.py
        │   │   │   └── project.py
        │   │   └── module_utils/
        │   └── ...
        ├── openstack/          # Collection 2
        │   ├── galaxy.yml
        │   ├── plugins/
        │   │   ├── modules/
        │   │   │   ├── volume.py
        │   │   │   └── security_group.py
        │   │   └── module_utils/
        │   └── ...
        └── slurm/              # Collection 3
            ├── galaxy.yml
            └── ...
```

You can customize the path using command-line options:

```bash
poetry run generate --config my_config.yaml --output-dir ./dist
```

Run `poetry run ansible-waldur-generator --help` for a full list of options.

## The Plugin System

The generator uses a plugin-based architecture to handle different types of module logic. Each plugin is
specialized for a common interaction pattern with the Waldur API. When defining a module in
`generator_config.yaml`, the `type` key determines which plugin will be used.

The header defines Ansible collection namespace, name and version.

```yaml
collections:
  - namespace: waldur
    name: structure
    version: 1.0.0
    modules:
      - name: modename
        plugin: crud
```

Below is a detailed explanation of each available plugin.

---

### 1. The `facts` Plugin

- **Purpose:** For creating **read-only** Ansible modules that fetch information about existing resources.
  These modules never change the state of the system and are analogous to Ansible's `_facts` modules (e.g.,
  `setup_facts`).

- **Workflow:**
  1. The module's primary goal is to find and return resource data based on an identifier (by default, `name`).
  2. The module expects to find a single resource. It will fail if zero or multiple
resources are found, prompting the user to provide a more specific identifier.
  3. It can filter its search based on parent resources (like a `project` or `tenant`).
This is configured using the standard `resolvers` block.

- **Configuration Example (`generator_config.yaml`):**
  This example creates a `waldur_openstack_security_group_facts` module to get information about security groups
  within a specific tenant.

    ```yaml
    modules:
      - name: security_group_facts
        plugin: facts
        resource_type: "security group"
        description: "Get facts about OpenStack security groups."

        # Defines the base prefix for API operations. The 'facts' plugin uses
        # this to automatically infer the necessary operation IDs:
        #  - `list`: via `openstack_security_groups_list`
        #  - `retrieve`: via `openstack_security_groups_retrieve`
        # This avoids the need for an explicit 'operations' block for conventional APIs.
        base_operation_id: "openstack_security_groups"

        # If `true`, the module is allowed to return a list of multiple resources
        # that match the filter criteria. An empty list is a valid result.
        # If `false` (the default), the module would fail if zero or more than one
        # resource is found, ensuring a unique result.
        many: true

        # This block defines how to resolve context parameters to filter the search.
        resolvers:
          # Using shorthand for the 'tenant' resolver. The generator will infer
          # 'openstack_tenants_list' and 'openstack_tenants_retrieve' from the base.
          tenant:
            base: "openstack_tenants"
            # This key is crucial. It tells the generator to use the resolved
            # tenant's UUID as a query parameter named 'tenant_uuid' when calling
            # the `openstack_security_groups_list` operation.
            check_filter_key: "tenant_uuid"
    ```

---

### 2. The `crud` Plugin

- **Purpose:** For managing the full lifecycle of resources with **simple, direct, synchronous** API calls.
  This is ideal for resources that have distinct `create`, `list`, `update`, and `destroy` endpoints.

- **Workflow:**
  - **`state: present`**:
    1. Calls the `list` operation to check if a resource with the given name already exists.
    2. If it **does not exist**, it calls the `create` operation.
    3. If it **does exist**, it checks for changes:
       - For simple fields in `update_config.fields`, it sends a `PATCH` request if values differ.
       - For complex `update_config.actions`, it calls a dedicated `POST` endpoint. If this action is
         asynchronous (returns `202 Accepted`) and `wait: true`, it will poll the resource until it reaches a
         stable state.
  - **`state: absent`**: Finds the resource and calls the `destroy` operation.

- **Return Values:**
  - `resource`: A dictionary representing the final state of the resource.
  - `commands`: A list detailing the HTTP requests made.
  - `changed`: A boolean indicating if any changes were made.

- **Configuration Example (`generator_config.yaml`):**
  This example creates a `security_group` module that is a **nested resource** under a tenant and supports both
  simple updates (`description`) and a complex, asynchronous action (`set_rules`).

    ```yaml
    modules:
      - name: security_group
        plugin: crud
        resource_type: "OpenStack security group"
        description: "Manage OpenStack Security Groups and their rules in Waldur."

        # The core prefix for inferring standard API operation IDs.
        # The generator automatically enables:
        #  - `check`: via `openstack_security_groups_list`
        #  - `destroy`: via `openstack_security_groups_destroy`
        base_operation_id: "openstack_security_groups"

        # The 'operations' block is now for EXCEPTIONS and detailed configuration.
        operations:
          # Override the 'create' operation because it's a NESTED action under a
          # tenant and doesn't follow the standard '[base_id]_create' pattern.
          create:
            id: "openstack_tenants_create_security_group"
            # This block maps the placeholder in the API URL path
            # (`/api/openstack-tenants/{uuid}/...`) to an Ansible parameter (`tenant`).
            path_params:
              uuid: "tenant"

          # Explicitly define the update operation to infer updatable fields from.
          update:
            id: "openstack_security_groups_partial_update"
            # Define a special, idempotent action for managing rules.
            actions:
              set_rules:
                # The specific operationId to call for this action.
                operation: "openstack_security_groups_set_rules"
                # The Ansible parameter that triggers this action. The runner only
                # calls the operation if the user provides 'rules' AND its value
                # differs from the resource's current state.
                param: "rules"

        # Define how the module should wait for asynchronous actions to complete.
        wait_config:
          ok_states: ["OK"]        # State(s) that mean success.
          erred_states: ["ERRED"]  # State(s) that mean failure.
          state_field: "state"     # Key in the resource dict that holds the state.

        # Define how to resolve dependencies.
        resolvers:
          # A resolver for 'tenant' is required by `path_params` for the 'create'
          # operation. This tells the generator how to convert a user-friendly
          # tenant name into the internal UUID needed for the API call.
          tenant: "openstack_tenants" # Shorthand for the tenants resolver.
    ```

---

### 3. The `order` Plugin

- **Purpose:** The most powerful plugin, designed for resources managed through Waldur's **asynchronous
  marketplace order workflow**. This is for nearly all major cloud resources like VMs, volumes, databases, etc.

- **Key Features:**
  - **Attribute Inference**: Specify an `offering_type` to have the generator automatically create all necessary
    Ansible parameters from the API schema, drastically reducing boilerplate.
  - **Termination Attributes**: Define optional parameters for deletion (e.g., `force_destroy`) by configuring
    the `operations.delete` block.
  - **Hybrid Updates**: Intelligently handles both simple `PATCH` updates and complex, asynchronous `POST`
    actions on existing resources.

- **Workflow:**
  - **`state: present`**:
    1. Checks if the resource exists.
    2. If not, it creates a marketplace order and polls for completion.
    3. If it exists, it performs direct synchronous (`PATCH`) or asynchronous (`POST` with polling) updates
       as needed.
  - **`state: absent`**: Finds the resource and calls the `marketplace_resources_terminate` endpoint.

- **Configuration Example (`generator_config.yaml`):**
  This example creates a marketplace `volume` module.

    ```yaml
    modules:
      - name: volume
        plugin: order
        resource_type: "OpenStack volume"
        description: "Create, update, or delete an OpenStack Volume via the marketplace."

        # The most important key for this plugin. The generator will find the
        # 'OpenStack.Volume' schema and auto-create Ansible parameters for
        # 'size', 'type', 'image', 'availability_zone', etc.
        offering_type: "OpenStack.Volume"

        # The base prefix for inferring standard API operations. The plugin uses this for:
        #  - `check`: `openstack_volumes_list` (to see if the volume already exists).
        #  - `update`: `openstack_volumes_partial_update` (for direct updates).
        base_operation_id: "openstack_volumes"

        # This block defines how to resolve dependencies and filter choices.
        resolvers:
          # This resolver is for the 'type' parameter, which was auto-inferred.
          type:
            # Shorthand for the volume types API endpoints.
            base: "openstack_volume_types"
            # A powerful feature for dependent filtering. It tells the generator
            # to filter available volume types based on the cloud settings
            # of the selected 'offering'.
            filter_by:
              - # Use the resolved 'offering' parameter as the filter source.
                source_param: "offering"
                # Extract this key from the resolved offering's API response.
                source_key: "scope_uuid"
                # Use it as this query parameter. The final API call will be:
                # `.../openstack-volume-types/?tenant_uuid=<offering_scope_uuid>`
                target_key: "tenant_uuid"
    ```

---

### 4. The `actions` Plugin

- **Purpose:** For creating modules that execute specific, one-off **actions** on an existing resource
  (e.g., `reboot`, `pull`, `start`). These modules are essentially command runners for your API.

- **Workflow:**
  1. Finds the target resource using an identifier and optional context filters. Fails if not found.
  2. Executes a `POST` request to the API endpoint corresponding to the user-selected `action`.
  3. Always reports `changed=True` on success and returns the resource's state after the action.

- **Configuration Example (`generator_config.yaml`):**
  This example creates a `vpc_action` module to perform operations on an OpenStack Tenant (VPC).

    ```yaml
    modules:
      - name: vpc_action
        plugin: actions
        resource_type: "OpenStack tenant"
        description: "Perform actions on an OpenStack tenant (VPC)."

        # The base ID used to infer `_list`, `_retrieve`, and all action operations.
        # For example, 'pull' becomes 'openstack_tenants_pull'.
        base_operation_id: "openstack_tenants"

        # A list of action names. These become the `choices` for the module's
        # `action` parameter. The generator infers the full `operationId` for each.
        actions:
          - pull
          - unlink

        # Use resolvers to help locate the specific resource to act upon.
        resolvers:
          project:
            base: "projects"
            check_filter_key: "project_uuid"
    ```

---

### 5. The `link` Plugin

The `link` plugin is designed for a special but common use case: managing the state
of a relationship between two existing resources. It generates modules that can,
for example, attach a volume to a server, add a user to a project, or assign a
floating IP to a port.

Its core responsibility is to determine if the `source` resource is currently
linked to the `target` resource and execute an API call to create or remove that link
based on `state: present` or `state: absent`.

#### Configuration Example

Here is a complete configuration for generating a `volume_attachment` module using
the `link` plugin. This module attaches and detaches OpenStack volumes.

```yaml
# In generator_config.yaml

- name: volume_attachment
  plugin: link
  resource_type: "OpenStack volume attachment"
  description: "Attach and detach OpenStack volumes from instances."

  # The "source" is the primary resource on which an action is performed.
  # For an attachment, this is the volume.
  source:
    param: "volume"
    resource_type: "volume"
    # The plugin needs to fetch the full volume object to check its state.
    retrieve_op: "openstack_volumes_retrieve"

  # The "target" is the resource being linked to the source.
  target:
    param: "instance"
    resource_type: "instance"

  # The API operations for creating and removing the link.
  link_op: "openstack_volumes_attach"
  unlink_op: "openstack_volumes_detach"

  # The key in the source resource's API response that holds the URL
  # of the target resource when they are linked. This is crucial for idempotency.
  # For a Waldur volume, this field is named "instance".
  link_check_key: "instance"

  # Optional parameters passed only to the link_op.
  link_params:
    - name: "device"
      type: "string"
      description: "Device path on the instance (e.g., /dev/vdb)."

  # Define resolvers to find all involved resources. This allows users
  # to provide names instead of UUIDs and ensures the lookups are
  # performed in the correct context (e.g., within a specific tenant).
  resolvers:
    <<: [*base_openstack_resolvers] # Includes tenant, project, and customer
    instance:
      base: "openstack_instances"
      filter_by: *tenant_filter
    volume:
      base: "openstack_volumes"
      filter_by: *tenant_filter
```

#### Key `link` Plugin Options

- **`source`**: A dictionary defining the "active" resource in the relationship.
  - `param`: The name of the Ansible parameter for this resource (e.g., `volume`).
  - `resource_type`: A user-friendly name (e.g., `volume`).
  - `retrieve_op`: The `operationId` for fetching the full details of this resource.
- **`target`**: A dictionary defining the "passive" resource being linked to.
- **`link_op` / `unlink_op`**: The `operationId`s for the API calls that
   create and remove the link (e.g., `..._attach` and `..._detach`).
- **`link_check_key`**: The field name on the **source** resource's data that
  contains the URL or reference to the **target** when they are linked.
  This is the heart of the idempotency check.
- **`link_params`**: A list of additional parameters that are only relevant
  for the `link_op` (e.g., the `device` path for a volume attachment).
- **`resolvers`**: A standard resolver map used to find the `source`, `target`,
  and any other context resources (like `tenant` or `project`).

### Reusable Configuration with YAML Anchors

To keep your `generator_config.yaml` file DRY (Don't Repeat Yourself) and maintainable, you can use YAML's
built-in **anchors (`&`)** and **aliases (`*`)**. The generator fully supports this, allowing you to define a
configuration block once and reuse it. A common convention is to create a top-level `definitions` key to hold
these reusable blocks.

#### Example 1: Reusing a Common Resolver

**Before (Repetitive):**

```yaml
- name: security_group
  resolvers:
    tenant: { base: "openstack_tenants" }
- name: volume_facts
  resolvers:
    tenant: { base: "openstack_tenants" }
```

**After (Reusable):**
We define the resolver once with an anchor `&tenant_resolver`, then reuse it with the alias `*tenant_resolver`.

```yaml
definitions:
  tenant_resolver: &tenant_resolver
    base: "openstack_tenants"

modules:
  - name: security_group
    resolvers:
      tenant: *tenant_resolver
  - name: volume_facts
    resolvers:
      tenant: *tenant_resolver
```

#### Example 2: Composing Configurations with Merge Keys

You can combine anchors with the YAML **merge key (`<<`)** to build complex configurations from smaller,
reusable parts. This is perfect for creating a set of resolvers that apply to most resources in a collection.

```yaml
definitions:
  # Define small, reusable resolver fragments.
  project_context_resolver: &project_context_resolver
    project:
      base: "projects"
      check_filter_key: "project_uuid"

  tenant_context_resolver: &tenant_context_resolver
    tenant:
      base: "openstack_tenants"
      check_filter_key: "tenant_uuid"

  # Create a composite block by merging the fragments.
  base_openstack_resolvers: &base_openstack_resolvers
    <<: [ *project_context_resolver, *tenant_context_resolver ]

# ... in your collection definition ...
modules:
  - name: volume_facts
    plugin: facts
    base_operation_id: "openstack_volumes"
    # Now, simply merge in the entire block of common resolvers.
    resolvers:
      <<: *base_openstack_resolvers

  - name: security_group_facts
    plugin: facts
    base_operation_id: "openstack_security_groups"
    resolvers:
      <<: *base_openstack_resolvers
```

By using these standard YAML features, you can significantly reduce duplication and make your generator
configuration cleaner and easier to manage.

## How to Use the Generated Collection

Once generated, the collection can be used immediately for local testing or packaged for
distribution. End-users who are not developing the generator can skip directly to the
"Installing from Ansible Galaxy" section.

The most straightforward way to test is to tell Ansible where to find your newly generated
collection by setting an environment variable.

1. **Set the Collection Path:**
   From the root of your project, run:

   ```bash
    export ANSIBLE_COLLECTIONS_PATH=./outputs
   ```

   This command tells Ansible to look for collections inside the `outputs` directory. This setting lasts for
   your current terminal session.

2. **Run an Ad-Hoc Command:**
   You can now test any module using its **Fully Qualified Collection Name (FQCN)**. This is perfect for a
   quick check.

   **Command:**

   ```bash
    # Test the 'waldur.structure.project' module from the 'waldur.structure' collection
    ansible localhost -m waldur.structure.project \
      -a "state=present \
          name='My AdHoc Project' \
          customer='Big Corp' \
          api_url='https://api.example.com/api/' \
          access_token='YOUR_SECRET_TOKEN'"
   ```

   **Example Output (Success, resource created):**

   ```json
    localhost | CHANGED => {
        "changed": true,
        "commands": [
            {
                "body": {
                    "customer": "https://api.example.com/api/customers/...",
                    "name": "My AdHoc Project"
                },
                "description": "Create new project",
                "method": "POST",
                "url": "https://api.example.com/api/projects/"
            }
        ],
        "resource": {
            "created": "2024-03-21T12:00:00.000000Z",
            "customer": "https://api.example.com/api/customers/...",
            "customer_name": "Big Corp",
            "description": "",
            "name": "My AdHoc Project",
            "url": "https://api.example.com/api/projects/...",
            "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        }
    }
    ```

    **Example Output (Success, resource already existed):**

    ```json
    localhost | SUCCESS => {
        "changed": false,
        "commands": [],
        "resource": {
            "created": "2024-03-21T12:00:00.000000Z",
            "customer": "https://api.example.com/api/customers/...",
            "customer_name": "Big Corp",
            "description": "",
            "name": "My AdHoc Project",
            "url": "https://api.example.com/api/projects/...",
            "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        }
    }
    ```

    > **Security Warning**: Passing `access_token` on the command line is insecure. For
    > production, use Ansible Vault or environment variables as shown in the playbook method.

## Publishing and Installing

### Publishing to Ansible Galaxy

The generated output is ready to be published, making your modules available to everyone.

1. **Build the Collection Archive:**
   Navigate to the root of the generated collection and run the build command. The output tarball will be
   placed in the parent directory.

   ```bash
    # Navigate to the actual collection directory
    cd outputs/ansible_collections/waldur/structure/

    # Build the collection, placing the output tarball in the `outputs` directory
    ansible-galaxy collection build --output-path ../../../..
   ```

   This will create a file like `outputs/waldur-structure-1.0.0.tar.gz`.

2. **Get a Galaxy API Key:**
   - Log in to [galaxy.ansible.com](https://galaxy.ansible.com/).
   - Navigate to `Namespaces` and select your namespace.
   - Copy your API key from the "API Key" section.

3. **Publish the Collection:**
    Use the `ansible-galaxy` command to upload your built archive.

    ```bash
    # Set the token as an environment variable (note the correct variable name)
    export ANSIBLE_GALAXY_TOKEN="your_copied_api_key"

    # From the `outputs` directory, publish the tarball
    cd outputs/
    ansible-galaxy collection publish waldur-structure-1.0.0.tar.gz
    ```
