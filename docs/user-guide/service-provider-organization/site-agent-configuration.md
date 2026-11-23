# Configure a site agent from Waldur

A [Waldur site agent](../../admin-guide/providers/site-agent/index.md) runs next to a provider's
backend, such as a SLURM cluster, and keeps it in sync with a **Waldur site agent** offering.
Waldur can hold the agent's configuration for that offering. The agent then loads it from Waldur
when it starts, and its local file keeps only what it needs to reach Waldur and its secrets.

This page is for the service provider. It covers what Waldur stores, how to set it, how to run
the agent with it, and who may change it. The agent's own settings are described in its
[configuration reference](../../admin-guide/providers/site-agent/docs/configuration.md), in the
section "Configuration from Waldur".

## What Waldur stores for a site agent offering

Each site agent offering has an **agent configuration**. It holds:

| Part | What it decides |
|------|-----------------|
| `order_processing_backend`, `membership_sync_backend`, `reporting_backend` | Which agent plugin fills each role, such as `slurm` |
| `username_management_backend` | Which plugin creates usernames, such as `base` or `ldap` |
| `custom_backends` | Plugins of your own that Waldur does not know |
| `backend_settings` | The plugin settings, without secrets |
| `backend_components` | Extra per-component fields that only the agent reads, such as `unit_factor_reporting` |
| `event_settings` | Whether the agent takes events over STOMP, and where it connects for them |
| `agent_settings` | `resource_import_enabled`, `username_reconciliation_enabled`, `preserve_unmanaged_backend_users` and `omit_anomalous_usage_components` |

Waldur adds the rest of the agent's offering configuration from the offering itself:

- the offering's name;
- the components, from the offering's **Accounting** components: measured unit, unit factor,
  accounting type, label and limit;
- the SLURM periodic usage policy of the offering, if it has one, as `policy_settings`.

An offering whose configuration names no backend for any role gets SLURM for all three roles.
Once you set one role, a role you leave empty stays off.

## What stays on the agent host

Waldur never stores secrets. These stay in the agent's local file:

- how the agent reaches Waldur: `waldur_api_url`, `waldur_offering_uuid`, `verify_ssl`, and the
  agent's credentials (`waldur_api_token`, or the three `oidc_*` settings);
- the plugin secrets, such as the LDAP `bind_password` of a SLURM offering;
- the settings at the top of the file, which belong to the agent process rather than to one
  offering: `timezone`, `log_level`, `sentry_dsn`, `global_proxy` and the others.

Waldur refuses a secret sent as part of the configuration. It also refuses any setting whose name
contains a word such as `password`, `token`, `secret` or `key`, for example `bind_password` or
`api_key`, unless an agent plugin declares it as an ordinary setting. Words are the parts of the
name between underscores, so `keycloak_url` is accepted.

## Set the agent configuration through the API

Waldur's interface has no editor for the agent configuration yet. Set it through the API.

### Find the current configuration

The provider offering shows it in its `agent_configuration` field:

```bash
curl -H "Authorization: Token <your token>" \
  https://waldur.example.com/api/marketplace-provider-offerings/<offering UUID>/
```

Only users who may update the offering's integration see this field.

### Change the configuration

Send the whole configuration to the offering's `update_integration` action. A write replaces the
whole agent configuration, so start from the current one and change what you need. Leave out a
part to clear it.

```bash
curl -X POST -H "Authorization: Token <your token>" -H "Content-Type: application/json" \
  https://waldur.example.com/api/marketplace-provider-offerings/<offering UUID>/update_integration/ \
  -d @agent-configuration.json
```

An example `agent-configuration.json` for a SLURM cluster with LDAP project groups:

```json
{
  "agent_configuration": {
    "order_processing_backend": "slurm",
    "membership_sync_backend": "slurm",
    "reporting_backend": "slurm",
    "backend_settings": {
      "default_account": "root",
      "customer_prefix": "hpc_",
      "project_prefix": "hpc_",
      "allocation_prefix": "hpc_",
      "ldap": {
        "uri": "ldaps://ldap.example.com",
        "bind_dn": "cn=site-agent,dc=example,dc=com",
        "base_dn": "dc=example,dc=com"
      }
    },
    "event_settings": {
      "stomp_enabled": true
    },
    "agent_settings": {
      "resource_import_enabled": false
    }
  }
}
```

The LDAP `bind_password` is not in it: it goes into the agent's local file.

You can also send `agent_configuration` when you create an offering through the API, and it is
part of an offering export and import. The same checks apply on every path.

Waldur records each change in the offering's history, with who made it and when
(`GET /api/marketplace-provider-offerings/<offering UUID>/history/`). The history does not show
the configuration itself.

### What Waldur checks when you save

Waldur knows the agent's plugins from a list that the site agent publishes and Waldur ships with:
which roles each plugin can fill, which settings it accepts, and which of them are secret. Waldur
validates the configuration against that list, the plugin catalogue. A save is refused with an
error that names the setting when:

- a role names a backend that is not in the catalogue. Add your own plugin's name to
  `custom_backends` to use it; Waldur does not check the settings of a custom backend;
- a backend cannot fill the role it is set for;
- `backend_settings` do not match the settings schema of the backends in use;
- the configuration has an unknown key, or a value of the wrong type;
- a setting is a secret, or is named like one;
- `backend_components` names a component the offering does not have. When you rename or remove
  a component, Waldur moves or removes its entry for you;
- `backend_components` sets a field that belongs to the offering component, such as
  `measured_unit`, `unit_factor` or `limit`. Set those on the component in **Accounting**;
- the offering is not a site agent offering;
- the change needs a permission you do not have. See
  [Who can change the agent configuration](#who-can-change-the-agent-configuration).

## Generate the agent configuration file

Waldur can also write the configuration out as a complete YAML file for the agent. Use it for an
agent that keeps its configuration in the local file (`configuration_source: local`, the
default). A change made in Waldur then reaches the agent only when you generate the file again,
replace it on the agent host and restart the agent.

To generate the file:

1. Open the offering's **Edit** tab, then **Integration → Credentials**.
2. Click **Actions → Generate Site Agent Config**.
3. Optionally, set the Waldur API URL the agent should use and its time zone, and choose
   whether to include the SLURM periodic usage policy.
4. Click **Generate Configuration**. Copy the result or click **Download YAML**.

To generate one file for several offerings, use **Generate Site Agent Config** in the actions
of the offering list under **Marketplace → Offerings** and select the offerings.

The file has no secrets. The agent's API token and each required backend secret get an empty
value marked with a `# SECRET:` comment. A secret required only inside an optional block, such as
the LDAP `bind_password`, gets one only when that block is configured. The header lists every
backend secret, including the optional ones that have no placeholder. Fill them in on the agent
host.

Generating the file needs the permission to read the service provider's API secret code. Waldur
checks it on the provider's organization, so by default only organization owners and staff can
generate the file. Offering managers and service provider managers see the action, but Waldur
refuses it.

Through the API the action is
`POST /api/marketplace-service-providers/<provider UUID>/generate_site_agent_config/` with
`{"offering_uuids": ["<offering UUID>"]}`. There, `"secret_format": "env"` writes each secret as
a `${VARIABLE}` reference to fill in with a tool such as `envsubst`. The same body sent to
`POST /api/marketplace-service-providers/<provider UUID>/site_agent_config_secrets/` lists the
secrets as data.

## Run the agent with the configuration from Waldur

### Write the bootstrap file

Set `configuration_source: waldur` on the offering in the agent's file. The offering may then
hold only these keys:

- `waldur_api_url` and `waldur_offering_uuid`;
- `waldur_api_token`, or `oidc_token_url`, `oidc_client_id` and `oidc_client_secret`;
- `verify_ssl`;
- `configuration_source`;
- `name`, optionally. Waldur's offering name is used otherwise;
- `backend_settings` with the secrets only, at the paths Waldur lists for the offering.

```yaml
timezone: "UTC"
log_level: "INFO"

offerings:
  - name: "HPC cluster"
    configuration_source: waldur
    waldur_api_url: "https://waldur.example.com/api/"
    waldur_api_token: "<agent token>"
    waldur_offering_uuid: "<offering UUID>"
    verify_ssl: true
    backend_settings:
      ldap:
        bind_password: "<LDAP bind password>"
```

Any other key fails the load with an error that names it. A setting that looks configured in the
file but would be replaced by Waldur's is never accepted silently.

To see which secrets an offering needs, read
`GET /api/marketplace-provider-offerings/<offering UUID>/site_agent_config/`. Its `secrets` list
gives the path of each secret, the backend that reads it and whether it is required. A secret
marked `required_with_parent` is needed only when its block, such as `ldap`, is configured.

The offering UUID and the Waldur API URL are shown on the offering's **Edit** tab under
**Integration → Credentials**.

### Choose a token for the agent { data-mentions="setting:PAT_ENABLED" }

Use a personal access token made from the `site_agent` template. It carries
`OFFERING.MANAGE_AGENT` and the other scopes the agent needs, and is bound to the one offering. It
can load the agent configuration, but it cannot change it.

To create one:

1. Open the offering's **Edit** tab, then **Integration → Credentials**.
2. Click **Actions → Create agent token**. The token wizard opens with the `site_agent` template
   and this offering already selected.
3. Finish the wizard and copy the token into the agent's file as `waldur_api_token`.

The item is enabled when Waldur can make a working agent token for you on this offering, as it
can for the offering's managers. If it cannot, for example for an organization owner who is not
the offering's manager, the item is disabled and suggests adding yourself as the offering's
manager.

Through the API, the template's endpoints are `GET /api/personal-access-tokens/templates/` and
`GET /api/personal-access-tokens/template_targets/?template=site_agent`. See
[Personal access tokens](../../developer-guide/personal-access-tokens.md) for how to create the
token there, and for the dedicated agent user that staff can create for an offering.

Other credentials work too. To load the configuration, the token's user must be allowed to update
the offering's integration or to run its agent. To run the agent as well, the user needs a role
such as offering manager. An offering manager's own API token works, but it also allows changing
the agent configuration. Whoever holds the agent's token can do what the token allows, so prefer
the template token.

### What happens when the agent starts

For each offering with `configuration_source: waldur`, the agent:

1. calls `GET /api/marketplace-provider-offerings/<offering UUID>/site_agent_config/` with the
   offering's credentials;
2. adds the secrets from its local file to `backend_settings`;
3. checks that every required secret is set and not empty;
4. validates the result like a local configuration;
5. logs the offering, the configuration `version` Waldur reports, and the source.

Waldur's answer never changes how the agent reaches Waldur. The API URL, the offering UUID, the
credentials, `verify_ssl` and `configuration_source` always come from the local file.

The `version` is a hash of the whole offering configuration that Waldur serves. It changes when,
and only when, that configuration changes. Compare the version in the agent's log with the one
Waldur returns now to see whether the agent runs the latest configuration.

### Apply a change to the configuration

The agent reads its configuration once, when the process starts. A change takes effect only
after you restart the agent's services. That applies to every part Waldur serves, not only the
agent configuration:

- a change to the agent configuration;
- a change to the offering's name or its **Accounting** components;
- a change to the offering's SLURM periodic usage policy;
- a Waldur upgrade that brings new plugin defaults.

The agent's services run one per mode, and each serves every offering in the agent's file. To
restart all of them on the host:

```bash
systemctl restart 'waldur-agent-*'
```

### Fix an agent that stops at startup

The agent does not start with a configuration it could not load. It exits with status 1 and one
error line that names the offering and the cause, when:

- Waldur cannot be reached;
- Waldur answers with an error, such as 401 for invalid credentials, 403 for a token without
  permission, 404 for an unknown offering, or 400 for an offering that is not a site agent
  offering;
- the file holds a key that is not allowed;
- a required secret is missing;
- the file sets a secret for a block that Waldur does not configure, such as
  `ldap.bind_password` when the configuration in Waldur has no `ldap` block;
- the configuration Waldur serves fails the agent's own validation.

There is no cached copy to fall back on. An agent that cannot reach Waldur could not process
orders or report usage either. The agent's systemd units restart it after 30 seconds, so it
starts once the cause is fixed. See the agent's
[deployment guide](../../admin-guide/providers/site-agent/docs/deployment.md) for its logs.

### Check a locally configured agent for drift

An offering that the agent still configures from its local file is compared with what Waldur
would serve for it, each time the agent starts. Each difference is logged as a warning that names
the offering and what differs:

- per component: `accounting_type`, `unit_factor`, `unit_factor_reporting`, `limit`, and a
  component Waldur does not have;
- per role: the backend, with both values;
- per backend setting: the key only. The value is never logged, as it may be a credential.

The check never stops the agent. If Waldur is unreachable or the token may not read the
configuration, the agent only logs a debug message.

### Move an agent to the configuration from Waldur

1. Set the agent configuration in Waldur to match the agent's current file.
2. Restart the agent and read its drift warnings. Fix the configuration in Waldur until there
   are none.
3. Replace the offering in the file with the bootstrap keys and `configuration_source: waldur`,
   keeping the secrets.
4. Restart the agent and check that it logs the configuration version.

### Stop using `waldur_site_load_components`

`waldur_site_load_components` is deprecated. It created the offering's components in Waldur from
the agent's `backend_components`. Configure the components in the offering's **Accounting**
instead, and use `configuration_source: waldur`. The command skips offerings whose
configuration comes from Waldur.

## Who can change the agent configuration

Two permissions guard the agent configuration. Reading it on the offering, and changing it,
needs `OFFERING.UPDATE_INTEGRATION`. A change to the parts that decide where the agent connects,
what it runs and what access it grants needs `OFFERING.UPDATE_AGENT_CONFIGURATION` as well. The
agent itself can also load the configuration with `OFFERING.MANAGE_AGENT`, which is what the
`site_agent` token template carries.

By default, the roles hold these permissions:

| Permission | Organization owner | Service provider manager | Offering manager |
|------------|:------------------:|:------------------------:|:----------------:|
| `OFFERING.UPDATE_INTEGRATION`: read and change the agent configuration | Yes | Yes | Yes |
| `OFFERING.UPDATE_AGENT_CONFIGURATION`: change its trust-sensitive parts | Yes | Yes | Yes |
| `SERVICE_PROVIDER.GET_API_SECRET_CODE` on the organization: generate the YAML file | Yes | No | No |
| `OFFERING.MANAGE_AGENT`: run the agent and load its configuration | Yes | No | Yes |

### Which changes need `OFFERING.UPDATE_AGENT_CONFIGURATION`

A change to any of these needs the permission. Adding, removing or emptying a value counts as a
change.

- any role backend and `custom_backends`;
- any key of `event_settings`;
- `resource_import_enabled`, `username_reconciliation_enabled` and
  `preserve_unmanaged_backend_users` in `agent_settings`. `omit_anomalous_usage_components` does
  not need it;
- a backend setting that the plugin catalogue marks as sensitive, such as SLURM's `ldap.uri`,
  `rest_api.url` and `rest_api.token_file`, or the Waldur plugin's `target_api_url`;
- a backend setting that none of the backends in use declares. With a custom backend this can be
  every setting.

Any other change, such as a SLURM account prefix, needs only `OFFERING.UPDATE_INTEGRATION`.
Without the permission, Waldur refuses the save with 403 and lists the settings you may not
change. When an offering is created with a configuration, the permission is checked on its
organization.

### Why the permission controls the agent host

!!! warning
    With `configuration_source: waldur`, whoever may change the agent configuration decides, at
    the agent's next restart, where the agent connects, what it runs and what access it grants.
    That includes where the secrets in the agent's local file are sent. For example:

    - an LDAP `uri` changed in Waldur receives the local LDAP `bind_password`;
    - a token file path, such as SLURM's `rest_api.token_file`, makes the agent read that file on
      its host and send its content to the configured endpoint;
    - a STOMP host with `websocket_use_tls: false` receives the agent's API token in plain text.

    With a local file, the person who copies a generated file onto the host sees such a change
    before the agent acts on it. Here nobody does.

Treat `OFFERING.UPDATE_AGENT_CONFIGURATION` as control over the agent host. Grant the roles that
hold it, and any token that carries it, only to people you would let edit the agent's
configuration file.

If that is too broad for your site, either:

- keep the offering on `configuration_source: local`; or
- ask your Waldur administrator to remove the permission from the roles that should not have it,
  for example with
  [`waldur override_roles`](../../admin-guide/mastermind-configuration/cli-guide.md#override_roles).
