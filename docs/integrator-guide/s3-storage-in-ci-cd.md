# S3 storage in a CI/CD pipeline { data-requires="setting:PAT_ENABLED" }

A pipeline can order S3 storage from Waldur, pick up its access key, use it, and
terminate the storage again, all with a personal access token limited to that
job. This page shows the same flow four ways: the REST API, `waldur-cli`,
Ansible and Terraform. Each example was run end to end against a Waldur
deployment with a site-agent S3 offering.

!!! note "Needs Waldur 8.1.5-rc.4 or later"
    From Waldur 8.1.5-rc.4, a key is revealed with `POST`, and a personal
    access token that carries `RESOURCE.REVEAL_API_KEY` may reveal it. The
    tools follow the same release: `waldur-cli`'s `marketplace api-key`
    commands, the Ansible modules `resource_api_key_facts` and
    `resource_api_key_reveal`, and the Terraform data source
    `waldur_marketplace_resource_api_keys` and ephemeral resource
    `waldur_marketplace_resource_api_key` come with their 8.1.5-rc.4 or later
    releases.

    On an earlier Waldur, a key is revealed only with `GET` and an account
    token, as shown under [Single requests](#single-requests). Ordering,
    following the order and terminating work the same way on both.

## How it works

1. The pipeline creates a marketplace **order** for the S3 offering in a
   project. Waldur creates the **resource**, and the provider's site agent
   creates the S3 identity behind it.
2. The site agent then issues the resource's **API keys**: S3 access key pairs
   that Waldur stores encrypted. A key can be used once its state is `OK`.
3. The pipeline **reveals** one key: `POST
   /api/marketplace-resource-api-keys/{uuid}/reveal/` returns the access key ID
   (`client_id`) and the secret (`api_key`). Every reveal is recorded in the
   resource's event log.
4. The S3 endpoint and region are in the resource's `backend_metadata`
   (`s3_endpoint`, `s3_region`).
5. When the job is done, the pipeline deletes its buckets and **terminates** the
   resource, which removes the S3 identity and its keys. Termination fails while
   the resource still owns a bucket.

## What the pipeline needs { data-requires="setting:PAT_ENABLED" }

**A personal access token** for a user who may order in the project and
reveal its resources' keys. Create it under **User profile → Personal access
tokens**, or through `POST /api/personal-access-tokens/`, with these scopes:

| Scope | Used for |
| --- | --- |
| `ORDER.CREATE` | ordering the storage |
| `ORDER.LIST` | following the order |
| `RESOURCE.LIST` | reading the resource and listing its keys |
| `RESOURCE.REVEAL_API_KEY` | revealing a key |
| `RESOURCE.TERMINATE` | terminating the storage at the end |

- Bind the token to the project, so that it reaches nothing else.
- A token without `RESOURCE.REVEAL_API_KEY` is refused when it reveals a key.
  So is a token whose bindings do not reach the resource.
- The token's user also needs `RESOURCE.REVEAL_API_KEY` through a role in the
  project or its organization. By default the organization owner, the project
  administrator, manager and member, the principal investigator and the
  co-investigator hold it.
- Send the token as `Authorization: Bearer <token>`. Store it as a masked,
  protected CI/CD variable, for example `WALDUR_ACCESS_TOKEN`.

**The UUIDs of the S3 offering and of the project**, from the offering's and the
project's pages in Waldur, or from `GET /api/marketplace-public-offerings/` and
`GET /api/projects/`.

**The order attributes the offering takes.** The examples below set the
resource's `name` and `max_storage_limit`, the storage ceiling in GB. The
offering's order form in Waldur shows what it accepts.

The examples read these environment variables:

```bash
export WALDUR_API_URL=https://waldur.example.com
export WALDUR_ACCESS_TOKEN=w_...            # the personal access token
export S3_OFFERING_UUID=<offering uuid>
export PROJECT_UUID=<project uuid>
```

## REST API { data-requires="setting:PAT_ENABLED" }

### Single requests

For a resource that already exists, two requests get its credentials. The
first lists the resource's keys that are ready to use. It never returns a
secret.

```bash
curl -sSf -H "Authorization: Bearer $WALDUR_ACCESS_TOKEN" \
  "$WALDUR_API_URL/api/marketplace-resource-api-keys/?resource_uuid=$RESOURCE_UUID&state=OK" \
  | jq '.[] | {uuid, client_id, state, user_uuid}'
```

```json
{
  "uuid": "c5924ba0ae68415a9dab736748cc7870",
  "client_id": "ZH9OUSEB2VNZWZ5SMX0E",
  "state": "OK",
  "user_uuid": null
}
```

The second reveals one of them. It is a `POST` with no body, and it answers
with the key's fields plus `api_key`, the secret. Pick a key whose `user_uuid`
is empty: a key assigned to a user is revealed only to that user.

```bash
curl -sSf -X POST -H "Authorization: Bearer $WALDUR_ACCESS_TOKEN" \
  "$WALDUR_API_URL/api/marketplace-resource-api-keys/$KEY_UUID/reveal/" \
  | jq '{client_id, api_key}'
```

```json
{
  "client_id": "ZH9OUSEB2VNZWZ5SMX0E",
  "api_key": "<the secret access key>"
}
```

This prints the secret. In a job, capture the answer in a variable instead, as
the script below does. The answer carries `Cache-Control: no-store`, and every
reveal is recorded in the resource's event log.

!!! warning "Revealing with `GET` is deprecated and will be removed"
    Waldur releases up to 8.1.5-rc.3 reveal a key with `GET` only, and refuse
    personal access tokens on it, so there the request needs the user's own API
    token, sent as `Token`. Such a token expires once its user's token lifetime
    has passed since it was issued, and the request then fails with
    `401 Token has expired.`

    ```bash
    # Deprecated: GET reveal, for Waldur 8.1.5-rc.3 and earlier
    curl -sSf -H "Authorization: Token $WALDUR_API_TOKEN" \
      "$WALDUR_API_URL/api/marketplace-resource-api-keys/$KEY_UUID/reveal/"
    ```

    From 8.1.5-rc.4, Waldur still answers `GET` the same way, and accepts a personal
    access token on it, but mark it deprecated in the OpenAPI schema
    (`marketplace_resource_api_keys_reveal_retrieve`). It will be removed, and
    `POST` will be the only way to reveal a key. Switch to `POST` as soon as
    your Waldur has it. A Waldur without it answers the `POST` with
    `405 Method "POST" not allowed.` An account API token reaches everything
    its user can, so move to a scoped personal access token at the same time.

### A provisioning script

The script orders the storage, waits for the order and for a key, reveals the
key, and prints the connection details as shell `export` lines for the next
step of the job. It needs `curl` and `jq`.

As soon as the resource exists, the script writes its UUID to `.s3-resource`
(or `$S3_RESOURCE_FILE`), so a cleanup step can terminate it even when a later
step fails. Its output holds the secret: only ever run it inside `eval`.

```bash title="s3-provision.sh"
#!/usr/bin/env bash
# Order S3 storage from Waldur, wait for it and its access keys, and print the
# connection details as shell exports for the rest of the pipeline.
set -euo pipefail
: "${WALDUR_API_URL:?}" "${WALDUR_ACCESS_TOKEN:?}" "${S3_OFFERING_UUID:?}" "${PROJECT_UUID:?}"
NAME="${RESOURCE_NAME:-ci-artifacts}"
STORAGE_GB="${STORAGE_GB:-10}"

# Only a personal access token carries the scopes and bindings that limit it.
case "$WALDUR_ACCESS_TOKEN" in w_*) ;; *) echo "use a personal access token (w_...)" >&2; exit 1 ;; esac
api() { curl -sSf -H "Authorization: Bearer $WALDUR_ACCESS_TOKEN" -H 'Content-Type: application/json' "$@"; }

# 1. Order the resource
OFFERING_URL="$WALDUR_API_URL/api/marketplace-public-offerings/$S3_OFFERING_UUID/"
PLAN_URL=$(api "$OFFERING_URL" | jq -r '.plans[0].url')
ORDER_UUID=$(api -X POST "$WALDUR_API_URL/api/marketplace-orders/" -d "$(jq -n \
  --arg offering "$OFFERING_URL" --arg plan "$PLAN_URL" \
  --arg project "$WALDUR_API_URL/api/projects/$PROJECT_UUID/" \
  --arg name "$NAME" --argjson gb "$STORAGE_GB" \
  '{offering: $offering, project: $project, plan: $plan,
    attributes: {name: $name, max_storage_limit: $gb},
    accepting_terms_of_service: true}')" | jq -r .uuid)
echo "order $ORDER_UUID" >&2

# 2. Wait for the order to finish
for _ in $(seq 120); do
  ORDER=$(api "$WALDUR_API_URL/api/marketplace-orders/$ORDER_UUID/")
  case $(jq -r .state <<<"$ORDER") in
    done) break ;;
    erred|rejected|canceled) jq -r '"order \(.state): \(.error_message)"' <<<"$ORDER" >&2; exit 1 ;;
  esac
  sleep 5
done
[ "$(jq -r .state <<<"$ORDER")" = done ] || { echo "order not done after 10 minutes" >&2; exit 1; }
RESOURCE_UUID=$(jq -r .marketplace_resource_uuid <<<"$ORDER")
echo "resource $RESOURCE_UUID" >&2
# Recorded now, so that cleanup can terminate the resource if a later step fails.
printf '%s\n' "$RESOURCE_UUID" > "${S3_RESOURCE_FILE:-.s3-resource}"

# 3. Wait for an access key the site agent has issued. A key assigned to a user
#    is revealed only to that user, so take an unassigned one.
for _ in $(seq 60); do
  KEY_UUID=$(api "$WALDUR_API_URL/api/marketplace-resource-api-keys/?resource_uuid=$RESOURCE_UUID&state=OK" \
    | jq -r '[.[] | select(.user_uuid == null)][0].uuid // empty')
  [ -n "$KEY_UUID" ] && break
  sleep 5
done
[ -n "$KEY_UUID" ] || { echo "no access key was issued" >&2; exit 1; }

# 4. Reveal it, and read the endpoint the site agent published
KEY=$(api -X POST "$WALDUR_API_URL/api/marketplace-resource-api-keys/$KEY_UUID/reveal/")
META=$(api "$WALDUR_API_URL/api/marketplace-resources/$RESOURCE_UUID/" | jq .backend_metadata)

# jq's @sh quotes every value, so nothing in them runs when the output is eval'd.
echo "export WALDUR_S3_RESOURCE_UUID=$RESOURCE_UUID"
jq -r '@sh "export AWS_ENDPOINT_URL=\(.s3_endpoint) AWS_DEFAULT_REGION=\(.s3_region)"' <<<"$META"
jq -r '@sh "export AWS_ACCESS_KEY_ID=\(.client_id) AWS_SECRET_ACCESS_KEY=\(.api_key)"' <<<"$KEY"
```

Use it as `creds="$(./s3-provision.sh)" && eval "$creds"`: the assignment
fails when the script does, where a bare `eval "$(./s3-provision.sh)"` would
carry on with no credentials. Then run the S3 commands, then terminate the
storage:

```bash
curl -sSf -X POST -H "Authorization: Bearer $WALDUR_ACCESS_TOKEN" \
  "$WALDUR_API_URL/api/marketplace-resources/$WALDUR_S3_RESOURCE_UUID/terminate/"
```

## waldur-cli { data-requires="setting:PAT_ENABLED" }

[`waldur-cli`](waldur-cli/index.md) waits for the order itself, and, from
its 8.1.5-rc.4 release, has `marketplace api-key` commands to list, wait for, reveal and rotate a
resource's keys. It reads `WALDUR_API_URL` and `WALDUR_ACCESS_TOKEN`.

```bash title="s3-pipeline.sh"
#!/usr/bin/env bash
# Order an S3 resource, pick up its credentials, and terminate it again.
#
# Needs WALDUR_API_URL, WALDUR_ACCESS_TOKEN (the personal access token),
# S3_OFFERING_UUID and PROJECT_UUID, plus waldur-cli and jq on PATH.
set -euo pipefail

: "${S3_OFFERING_UUID:?}" "${PROJECT_UUID:?}"
NAME="ci-cli-$(date +%Y%m%d%H%M%S)"

# 1. The offering's URL and its plan's URL, as JSON strings for the order body.
OFFERING=$(waldur-cli marketplace offering list --filter uuid_list="$S3_OFFERING_UUID" \
  --format json --jmespath '[0].url')
PLAN=$(waldur-cli marketplace offering list --filter uuid_list="$S3_OFFERING_UUID" \
  --format json --jmespath '[0].plans[0].url')

# 2. Order the resource. provision waits for the order to finish and prints the
#    resource; tsv's first column is its uuid.
RESOURCE_UUID=$(waldur-cli marketplace resource provision --project "$PROJECT_UUID" \
  --format tsv --request "$(cat <<JSON
{
  "offering": $OFFERING,
  "plan": $PLAN,
  "attributes": {"name": "$NAME", "max_storage_limit": 1},
  "accepting_terms_of_service": true
}
JSON
)" | cut -f1)
echo "resource $NAME: $RESOURCE_UUID"
# Terminate the resource on every exit: success, a failed step, or a cancelled
# job (GitLab sends SIGTERM, which the TERM trap turns into an exit).
trap 'waldur-cli marketplace resource terminate "$RESOURCE_UUID" || true' EXIT
trap 'exit 143' TERM

# 3. The site agent issues the keys after the order is done: wait for one in OK.
KEY_UUID=""
for _ in $(seq 60); do
  KEY_UUID=$(waldur-cli marketplace api-key list \
    --filter resource_uuid="$RESOURCE_UUID" --filter state=OK \
    --format json --jmespath '[0].uuid' | jq -r '. // empty')
  [ -n "$KEY_UUID" ] && break
  sleep 5
done
[ -n "$KEY_UUID" ] || { echo "no key in OK after 5 minutes" >&2; false; }
echo "key: $KEY_UUID"

# 4. Reveal the key, and read the S3 endpoint and region off the resource.
KEY_JSON=$(waldur-cli marketplace api-key reveal "$KEY_UUID" --format json)
AWS_ACCESS_KEY_ID=$(printf '%s' "$KEY_JSON" | jq -r .client_id)
AWS_SECRET_ACCESS_KEY=$(printf '%s' "$KEY_JSON" | jq -r .api_key)
RESOURCE_JSON=$(waldur-cli marketplace resource get "$RESOURCE_UUID" --format json)
AWS_ENDPOINT_URL=$(printf '%s' "$RESOURCE_JSON" | jq -r .backend_metadata.s3_endpoint)
AWS_DEFAULT_REGION=$(printf '%s' "$RESOURCE_JSON" | jq -r .backend_metadata.s3_region)
export AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_ENDPOINT_URL AWS_DEFAULT_REGION
echo "endpoint: $AWS_ENDPOINT_URL, region: $AWS_DEFAULT_REGION"
echo "access key id: $AWS_ACCESS_KEY_ID, secret: ${#AWS_SECRET_ACCESS_KEY} characters"

# ... the job's S3 work goes here ...

# 5. The EXIT trap terminates the resource; terminate waits for its order too.
```

`marketplace api-key reveal` prints the secret; keep its output out of the job
log, as the script does by capturing it in a variable.

## Ansible { data-requires="setting:PAT_ENABLED" }

From its 8.1.5-rc.4 release, the `waldur.marketplace` collection has `resource_api_key_facts`, which lists a
resource's keys, and `resource_api_key_reveal`, which reveals one. The playbook
orders the storage, waits for the order and for a key, writes the credentials
to a file only the job can read, and terminates the storage. Run every task
that handles the secret with `no_log: true`.

```yaml title="s3-credentials.yml"
---
# Order an S3 resource, wait for its access key, reveal the key and hand it to
# the rest of the pipeline, then terminate the resource.
#
# Requires:
#   WALDUR_API_URL       e.g. https://waldur.example.com (no /api suffix)
#   WALDUR_ACCESS_TOKEN  the personal access token (w_...)
#   S3_OFFERING_UUID, PROJECT_UUID
- name: Provision S3 credentials for a CI job
  hosts: localhost
  gather_facts: false
  vars:
    waldur_api_url: "{{ lookup('ansible.builtin.env', 'WALDUR_API_URL') }}"
    waldur_access_token: "{{ lookup('ansible.builtin.env', 'WALDUR_ACCESS_TOKEN') }}"
    s3_offering_uuid: 0ec43b44d34e40b78127da2d451eab78
    project_uuid: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    resource_name: "ci-ansible-{{ lookup('ansible.builtin.pipe', 'date +%Y%m%d%H%M%S') }}"
    credentials_file: "{{ playbook_dir }}/s3-credentials.env"

  tasks:
    - name: Look up the S3 offering and its plan
      waldur.marketplace.offering_facts:
        api_url: "{{ waldur_api_url }}"
        access_token: "{{ waldur_access_token }}"
        name: "{{ s3_offering_uuid }}"
      register: offering

    - name: Order the S3 resource
      waldur.marketplace.order:
        api_url: "{{ waldur_api_url }}"
        access_token: "{{ waldur_access_token }}"
        name: "{{ resource_name }}"
        project: "{{ project_uuid }}"
        offering: "{{ s3_offering_uuid }}"
        plan: "{{ offering.resources[0].plans[0].url }}"
        attributes:
          name: "{{ resource_name }}"
          max_storage_limit: 1
        accepting_terms_of_service: true
      register: new_order

    - name: Wait for the order to complete
      waldur.marketplace.order_facts:
        api_url: "{{ waldur_api_url }}"
        access_token: "{{ waldur_access_token }}"
        name: "{{ new_order.resource.uuid }}"
      register: order_state
      until: order_state.resources[0].state in ['done', 'erred', 'rejected', 'canceled']
      retries: 30
      delay: 10
      failed_when: order_state.resources[0].state != 'done'

    - name: Remember the resource
      ansible.builtin.set_fact:
        resource_uuid: "{{ order_state.resources[0].marketplace_resource_uuid }}"

    # Everything from here on runs in a block, so that the resource is terminated
    # whether the tasks succeed or fail.
    - name: Use the resource, then terminate it
      block:
        - name: Wait until the resource has an API key in state OK
          waldur.marketplace.resource_api_key_facts:
            api_url: "{{ waldur_api_url }}"
            access_token: "{{ waldur_access_token }}"
            resource: "{{ resource_uuid }}"
            state: [OK]
          register: api_keys
          until: api_keys.resources | selectattr('user_uuid', 'none') | list | length > 0
          retries: 30
          delay: 10

        - name: Reveal the API key
          waldur.marketplace.resource_api_key_reveal:
            api_url: "{{ waldur_api_url }}"
            access_token: "{{ waldur_access_token }}"
            uuid: "{{ (api_keys.resources | selectattr('user_uuid', 'none') | first).uuid }}"
          register: revealed
          no_log: true

        - name: Read the S3 endpoint and region of the resource
          waldur.marketplace.resource_facts:
            api_url: "{{ waldur_api_url }}"
            access_token: "{{ waldur_access_token }}"
            name: "{{ resource_uuid }}"
          register: resource

        - name: Write the credentials for the next pipeline step
          ansible.builtin.copy:
            dest: "{{ credentials_file }}"
            mode: "0600"
            content: |
              AWS_ENDPOINT_URL={{ resource.resources[0].backend_metadata.s3_endpoint }}
              AWS_DEFAULT_REGION={{ resource.resources[0].backend_metadata.s3_region }}
              AWS_ACCESS_KEY_ID={{ revealed.resource.client_id }}
              AWS_SECRET_ACCESS_KEY={{ revealed.resource.api_key }}
          no_log: true

        - name: Show what was provisioned, without the secret
          ansible.builtin.debug:
            msg:
              resource: "{{ resource_name }} ({{ resource_uuid }})"
              endpoint: "{{ resource.resources[0].backend_metadata.s3_endpoint }}"
              region: "{{ resource.resources[0].backend_metadata.s3_region }}"
              access_key_id: "{{ revealed.resource.client_id }}"
              secret_length: "{{ revealed.resource.api_key | length }}"
              revealed_changed: "{{ revealed.changed }}"

        # ... the CI job would use the credentials here ...

      always:
        - name: Terminate the S3 resource
          waldur.marketplace.resource_action:
            api_url: "{{ waldur_api_url }}"
            access_token: "{{ waldur_access_token }}"
            name: "{{ resource_uuid }}"
            action: terminate

        - name: Wait until the resource is terminated
          waldur.marketplace.resource_facts:
            api_url: "{{ waldur_api_url }}"
            access_token: "{{ waldur_access_token }}"
            name: "{{ resource_uuid }}"
          register: terminated
          until: terminated.resources[0].state == 'Terminated'
          retries: 30
          delay: 10
```

```bash
ansible-galaxy collection install waldur.marketplace
ansible-playbook s3-credentials.yml
```

## Terraform

From its 8.1.5-rc.4 release, the provider has a data source that lists a resource's keys,
`waldur_marketplace_resource_api_keys`, and an ephemeral resource that reveals
one, `waldur_marketplace_resource_api_key`. An ephemeral resource is read on
every run and never written to the plan or the state, so the secret stays out
of the state file. It needs Terraform 1.10 or later.

The configuration orders the storage, waits for the site agent to issue a key,
reveals it, and writes the credentials to a file only the job can read. It
reads `WALDUR_API_URL` and `WALDUR_ACCESS_TOKEN` from the environment.

```hcl title="main.tf"
terraform {
  # Ephemeral resources need Terraform 1.10 or later.
  required_version = ">= 1.10"

  required_providers {
    waldur = {
      source = "waldur/waldur"
    }
    time = {
      source  = "hashicorp/time"
      version = "~> 0.13"
    }
  }
}

variable "offering_uuid" {
  description = "UUID of the S3 storage offering"
  type        = string
}

variable "project_uuid" {
  description = "UUID of the project that owns the storage"
  type        = string
}

variable "resource_name" {
  description = "Name of the S3 resource"
  type        = string
}

variable "storage_gb" {
  description = "Storage quota in GB"
  type        = number
  default     = 1
}

variable "s3_endpoint" {
  description = "S3 endpoint of the offering"
  type        = string
}

variable "s3_region" {
  description = "S3 region of the offering"
  type        = string
  default     = "default"
}

variable "credentials_file" {
  description = "File the access key is written to, readable by its owner only"
  type        = string
  default     = "s3.env"
}

# Reads WALDUR_API_URL and WALDUR_ACCESS_TOKEN from the environment.
provider "waldur" {}

data "waldur_marketplace_offering" "s3" {
  id = var.offering_uuid
}

data "waldur_structure_project" "ci" {
  id = var.project_uuid
}

# Waits for the order to be done; marketplace_resource_uuid is the new resource.
resource "waldur_marketplace_order" "s3" {
  offering                   = data.waldur_marketplace_offering.s3.url
  project                    = data.waldur_structure_project.ci.url
  plan                       = data.waldur_marketplace_offering.s3.plans[0].url
  accepting_terms_of_service = true
  attributes = {
    name              = var.resource_name
    max_storage_limit = var.storage_gb
  }
}

# The site agent issues the access keys shortly after the order is done.
resource "time_sleep" "keys_issued" {
  create_duration = "30s"
  triggers = {
    resource_uuid = waldur_marketplace_order.s3.marketplace_resource_uuid
  }
}

data "waldur_marketplace_resource_api_keys" "s3" {
  filters = {
    resource_uuid = time_sleep.keys_issued.triggers["resource_uuid"]
    state         = "OK"
  }

  lifecycle {
    postcondition {
      condition     = length(self.items) > 0
      error_message = "The site agent has not issued an access key yet. Run terraform apply again."
    }
  }
}

# Revealed on every run, never written to the plan or the state.
ephemeral "waldur_marketplace_resource_api_key" "s3" {
  id = data.waldur_marketplace_resource_api_keys.s3.items[0].id
}

# Hands the key to the rest of the pipeline in a file only its owner can read.
# The values reach the command through its environment, never its text.
# Rewritten on every apply: a rotated key keeps its id, so only a fresh reveal
# picks up its new secret.
resource "terraform_data" "credentials_file" {
  triggers_replace = [plantimestamp()]
  input            = var.credentials_file

  provisioner "local-exec" {
    command = <<-EOT
      umask 077
      printf 'export AWS_ENDPOINT_URL=%s\nexport AWS_DEFAULT_REGION=%s\nexport AWS_ACCESS_KEY_ID=%s\nexport AWS_SECRET_ACCESS_KEY=%s\n' \
        "$S3_ENDPOINT" "$S3_REGION" "$S3_ACCESS_KEY" "$S3_SECRET_KEY" > "${var.credentials_file}"
    EOT
    environment = {
      S3_ENDPOINT   = var.s3_endpoint
      S3_REGION     = var.s3_region
      S3_ACCESS_KEY = ephemeral.waldur_marketplace_resource_api_key.s3.client_id
      S3_SECRET_KEY = ephemeral.waldur_marketplace_resource_api_key.s3.api_key
    }
  }

  provisioner "local-exec" {
    when    = destroy
    command = "rm -f '${self.input}'"
  }
}

# Destroying an order only forgets it: orders are records. This terminates the
# resource the order created when the configuration is destroyed.
resource "terraform_data" "terminate_on_destroy" {
  input = waldur_marketplace_order.s3.marketplace_resource_uuid

  provisioner "local-exec" {
    when    = destroy
    command = "curl -fsS -X POST -H \"Authorization: Bearer $WALDUR_ACCESS_TOKEN\" -H 'Content-Type: application/json' -d '{}' \"$WALDUR_API_URL/api/marketplace-resources/${self.input}/terminate/\""
  }
}

output "resource_uuid" {
  value = waldur_marketplace_order.s3.marketplace_resource_uuid
}

output "access_key_uuid" {
  value = data.waldur_marketplace_resource_api_keys.s3.items[0].id
}

output "credentials_file" {
  value = terraform_data.credentials_file.output
}
```

```hcl title="terraform.tfvars"
offering_uuid = "<offering uuid>"
project_uuid  = "<project uuid>"
resource_name = "ci-artifacts"
s3_endpoint   = "https://s3.example.com"
```

```bash
terraform init
terraform apply -auto-approve
. ./s3.env                     # the credentials, for the job's S3 commands
terraform destroy -auto-approve
```

- The credentials go to a file because a later job step needs them, and the
  provisioner passes them through its environment, so they never appear in the
  command or the log. The file is rewritten on every apply, so a rotated key's
  new secret replaces the old one. Feeding them to the `aws` provider in the same
  configuration does not work on the first apply: the ephemeral values are not
  known at plan time.
- Destroying a `waldur_marketplace_order` only removes the order from the
  state. The `terminate_on_destroy` resource terminates the storage when the
  configuration is destroyed. Delete the buckets first, as with the other
  examples.
- The site agent issues the keys shortly after the order completes; the
  configuration waits 30 seconds. If no key is ready by then, the postcondition
  stops the run and a second `terraform apply` picks the key up.

## Using the credentials

The credentials work with any S3 client. With the AWS CLI:

```bash
creds="$(./s3-provision.sh)" && eval "$creds"
aws s3api create-bucket --bucket ci-artifacts
aws s3 cp build/artifact.tar.gz s3://ci-artifacts/$CI_PIPELINE_ID/
```

- `AWS_ENDPOINT_URL` points the AWS CLI at the provider's endpoint instead of
  AWS. It needs AWS CLI 2.13 or later.
- Create buckets with `aws s3api create-bucket`. `aws s3 mb` sends the region
  as a location constraint, which a Ceph gateway refuses unless it matches the
  gateway's own zone group.

## A GitLab CI job

```yaml title=".gitlab-ci.yml"
publish-artifacts:
  image: alpine:3.20
  variables:
    S3_OFFERING_UUID: "<offering uuid>"
    PROJECT_UUID: "<project uuid>"
    # WALDUR_API_URL and WALDUR_ACCESS_TOKEN are masked, protected CI/CD variables
  before_script:
    - apk add --no-cache bash curl jq aws-cli
  script:
    # The assignment fails the job when the script fails; a bare eval would not.
    - creds="$(./s3-provision.sh)"
    - eval "$creds"
    - aws s3api create-bucket --bucket ci-artifacts
    - aws s3 cp build/ "s3://ci-artifacts/$CI_PIPELINE_ID/" --recursive
    # ... consume the artifacts ...
    - aws s3 rb s3://ci-artifacts --force
  after_script:
    - |
      RESOURCE_UUID=$(cat .s3-resource 2>/dev/null || true)
      [ -n "$RESOURCE_UUID" ] || exit 0
      curl -sSf -X POST -H "Authorization: Bearer $WALDUR_ACCESS_TOKEN" \
        "$WALDUR_API_URL/api/marketplace-resources/$RESOURCE_UUID/terminate/"
```

`after_script` runs in its own shell, also when the job fails or is cancelled.
`s3-provision.sh` saves only the resource UUID for it, as soon as the resource
exists, never the credentials. A failed job can leave
a bucket behind, even an empty one, and the termination then fails until the
bucket is deleted.

Storage that should outlive one job is ordered once instead. Each job then only
lists the existing resource's keys and reveals one.

## Good practice { data-mentions="setting:PAT_ENABLED" }

- Give the pipeline its own personal access token with only the scopes above,
  bound to one project, and an expiry date.
- Never print a revealed key. CI masking hides only values it knows in
  advance, and a revealed key is new on every run.
- A credentials file, such as the Ansible and Terraform examples write, is not
  for version control or job artifacts. In CI, write it outside the project
  directory (for example under `$RUNNER_TEMP_PROJECT_DIR` or `/tmp`), so that
  `artifacts:untracked` or a cache cannot pick it up.
- A revealed key is valid until it is rotated or its resource is terminated.
  For storage that outlives the job, rotate the key regularly with
  `POST /api/marketplace-resource-api-keys/{uuid}/rotate/` or
  `waldur-cli marketplace api-key rotate`.
- Every reveal appears in the resource's event log with the user who made it.
