# Remote MCP server

AI clients such as Claude, ChatGPT, Cursor, VS Code, Atlassian Rovo and Microsoft Copilot
Studio can connect to Waldur over the Model Context Protocol (MCP). They call read-only
tools on `/mcp`, on the API's host, and act as the user who connected them. Users sign
them in with OAuth, or give them a personal access token.

For users' instructions, see [Connect AI clients over MCP](../user-guide/end-users/mcp-clients.md).
For the tools, see [MCP tools](../user-guide/end-users/mcp-tools.md).

## How the MCP server works

- **A separate process serves `/mcp`.** `waldur mcp_server` runs apart from the API
  workers, on port 8091 by default. It answers `POST /mcp`, the OAuth resource
  metadata under `/.well-known/oauth-protected-resource`, and `/health`, with CORS
  headers for browser-based clients. It keeps no sessions, so replicas need no session
  affinity.
- **The API is the OAuth authorization server.** It serves the authorization server
  metadata, and the authorize, token, revoke and client registration endpoints under
  `/oauth/`. The authorize endpoint sends the browser to the portal's consent page,
  `/oauth/consent` under `HOMEPORT_URL`, where the user approves the client.
- **Clients register themselves.** A client either registers through Dynamic Client
  Registration (RFC 7591), or uses an HTTPS URL as its client ID and publishes its
  details there (Client ID Metadata Document, CIMD). No staff action is needed.
- **Tokens act as the user.** An OAuth access token lasts one hour and its refresh
  token 30 days. Each refresh replaces the refresh token. A personal access token works
  as on the REST API, within the rules in
  [Personal access tokens on /mcp](#personal-access-tokens-on-mcp).
- **No language model runs in Waldur.** The client brings its own model, so the MCP
  server needs neither the AI assistant nor its settings.

Images up to 8.1.5-rc.2 accept only personal access tokens on `/mcp`. OAuth sign-in
needs later mastermind and homeport images.

## Enable the MCP server

1. Run the server:
    - **Helm:** set `waldur.mcp.enabled`. See [Remote MCP server](deployment/helm/docs/mcp.md)
      in the Helm guide.
    - **Docker Compose:** start the `mcp` profile. See the
      [MCP server](deployment/docker-compose/index.md#mcp-server) section of the Docker
      Compose guide.
    - **Elsewhere:** run `waldur mcp_server --host 0.0.0.0 --port 8091` from the
      mastermind image, and route the paths in
      [Route the MCP endpoints through your proxy](#route-the-mcp-endpoints-through-your-proxy).
2. As staff, open **Administration > Configuration > Personal access tokens**. In the
   **MCP server** group:
    - turn on `MCP_ENABLED`;
    - set `MCP_RESOURCE_URLS` to the public URL of `/mcp`, such as
      `https://api.example.com/mcp`. See
      [Serve /mcp on the API's host](#serve-mcp-on-the-apis-host). The Helm chart
      seeds it from its API hosts while `waldur.initdbEnabled` is on, unless
      `waldur.settingsOverrides` sets it.
3. Check that `HOMEPORT_URL`, under **Administration > User interface > Branding**, is
   the portal's address. The OAuth sign-in sends the browser to the consent page there.
4. For personal access tokens, turn on `PAT_ENABLED` on the same page to give them to
   every user. To give them only to some users, leave it off and turn on the **Personal
   access tokens** option when editing each of those users.

While `MCP_ENABLED` is off, `/mcp`, its metadata and the OAuth endpoints answer 404, and
the portal hides **Connected apps**.

### Check the MCP server

The resource metadata names the URL from `MCP_RESOURCE_URLS`:

```bash
curl -s https://api.example.com/.well-known/oauth-protected-resource/mcp
# {"resource": "https://api.example.com/mcp", "authorization_servers": ["https://api.example.com"], ...}
```

A request to `/mcp` without a token answers 401. Its `WWW-Authenticate` header points
at the resource metadata, which is how clients find where to sign in:

```bash
curl -si -X POST https://api.example.com/mcp | grep -i '^www-authenticate'
# www-authenticate: Bearer resource_metadata="https://api.example.com/.well-known/oauth-protected-resource/mcp"
```

## Serve /mcp on the API's host

`MCP_RESOURCE_URLS` lists the public URLs of `/mcp`, separated by spaces:

- **OAuth tokens are bound to these URLs.** Waldur issues a token only for a listed URL,
  or for the first one when the client names none. While the setting is empty, Waldur
  issues no OAuth tokens, and clients can connect only with a personal access token.
- **Serve `/mcp` on the API's origin.** The resource metadata names that origin as the
  authorization server, and clients look for the OAuth endpoints there. On a separate
  host, such as `mcp.example.com`, clients can't find where to sign in.
- **List every host users connect to.** The metadata names the URL on the host the client
  reached, and clients reject metadata that names another host. If the API answers on
  several hosts, list `/mcp` on each.
- **List the path your proxy uses.** If a proxy serves `/mcp` under another path, such as
  `https://example.com/waldur/mcp`, list that URL. The server answers the metadata for each
  listed path, under `/.well-known/oauth-protected-resource/<path>`.
- **Removing a URL ends its sessions.** Tokens issued for it stop working, and clients
  can't refresh them.

Give users the URL without a trailing slash. Images up to 8.1.5-rc.2 redirect `/mcp/` to
`http://`, because the server sees plain HTTP behind a TLS proxy. Later images serve
`/mcp/` like `/mcp`.

## Route the MCP endpoints through your proxy

The Helm chart and the Compose stack set up these routes. Other deployments route them
on the API's host:

| Path | Served by |
|------|-----------|
| `/mcp` | MCP server |
| `/.well-known/oauth-protected-resource` and the paths below it | MCP server |
| `/.well-known/oauth-authorization-server` | API |
| `/oauth/authorize/`, `/oauth/token/`, `/oauth/revoke_token/` | API |
| `/oauth/register/` and the paths below it | API |

`/oauth/consent` is a portal page. If the portal shares the API's host, don't send it
to the API.

Browser-based MCP clients call these endpoints from their own origin. The API answers the
OAuth endpoints, and the MCP server answers `/mcp` and its metadata, with
`Access-Control-Allow-Origin: *`, no credentials, and `WWW-Authenticate` exposed. Those
answers have to reach the browser unchanged: a proxy that adds its own CORS headers can
replace `*` with the caller's origin and allow credentials. Images up to 8.1.5-rc.2 send
no CORS headers on `/mcp`. The Helm guide's [CORS section](deployment/helm/docs/mcp.md#cors)
explains what the chart does on each route. Clients that call `/mcp` from a server or from
the user's computer, such as those in the user guide, don't need CORS.

The API limits how many OAuth clients one address can register: 60 an hour, registered
through DCR or CIMD alike. It reads the address from `X-Forwarded-For`, counting the
proxies in `WALDUR_CORE["TRUSTED_PROXY_COUNT"]` from the right, the same setting every
other use of the client address follows. The default, 1, fits one proxy in front of the
API. Set it in the settings file, `override.conf.py`, to the number of proxies that add
to the header, or to 0 when the API is reached without a proxy. Helm sets it from
`waldur.trustedProxyCount`. Up to 8.1.5-rc.4 the limit read a separate
`MCP_OAUTH_TRUSTED_PROXY_COUNT`; later releases ignore it.

## Let cloud-hosted clients reach Waldur

Claude.ai, Claude Desktop's connectors, ChatGPT, Atlassian Rovo and Microsoft Copilot
Studio connect from their vendors' clouds, not from the user's computer. For them, `/mcp`
and the OAuth endpoints must be reachable from the internet, over HTTPS with a valid
certificate:

- Claude connects only on port 443.
- An IP allow-list in front of the API, and a personal access token's allowed networks,
  must let the vendor's addresses in. The vendors publish them.

Clients that run on the user's computer, such as Claude Code, Cursor and VS Code, need
only what the user's browser needs to reach the portal.

## Allow outbound HTTPS for client metadata

A client that uses a URL as its client ID publishes its name and redirect URIs at that
URL. The API fetches the document over HTTPS when the client first signs in, and again
when its cached copy expires, after 5 minutes to 24 hours.

- The API connects directly, not through `HTTPS_PROXY`, and only to public addresses.
- A fetch times out after 5 seconds, and a document over 16 KB is refused.
- Without outbound HTTPS from the API, these clients can't sign in. Clients that
  register through DCR, and personal access tokens, still work.

## See and revoke OAuth clients

Users see the clients they approved under **Profile > Credentials > Connected apps**,
and can revoke each one there. Revoking deletes the client's tokens and pending codes
for that user. Only the user sees their connected apps, not staff.

Staff see every registered client in the Django admin, in the **Django OAuth Toolkit**
section:

- **Applications** lists every client, with its **Registration source**: **Dynamic
  Client Registration**, **Client ID Metadata Document**, or **Manual** for clients an
  administrator added. Deleting a client deletes its tokens for every user.
- **Access tokens** and **Refresh tokens** list each user's sessions. Deleting both for a
  user and client ends that session.

When a user is deactivated, Waldur deletes their OAuth tokens and pending codes. A daily
task removes expired tokens, and CIMD clients whose metadata has expired and that hold
no live tokens. Such a client is registered again on its next sign-in.

## Register an OAuth client by hand

Most clients register themselves. For one that needs a client ID and secret from you,
such as Microsoft Copilot Studio with **Manual** authentication, register it in the
Django admin:

1. Under **Django OAuth Toolkit > Applications**, select **Add application**.
2. Set **Client type** to **Confidential** and **Authorization grant type** to
   **Authorization code**.
3. Enter the callback URL the client shows under **Redirect URIs**, and a **Name**. The
   consent page shows the name to users.
4. Copy the **Client ID** and **Client secret** before you save. Waldur stores only a
   hash of the secret.
5. Leave **Skip authorization** off, so that every user approves the client.

The client then uses `https://<api host>/oauth/authorize/` to sign in and
`https://<api host>/oauth/token/` for tokens, with the scope `mcp:read`. Waldur requires
PKCE with S256 from every client. When a sign-in request from such a client is invalid,
Waldur sends the error back to its redirect URI, which it doesn't do for clients that
registered themselves.

## Personal access tokens on /mcp

A personal access token that works on the REST API works on `/mcp`, except:

- a token restricted to particular organizations or projects;
- a staff user's token without the `STAFF.ACCESS` permission;
- a support user's token without `SUPPORT.ACCESS` or `STAFF.ACCESS`.

The tools only see the user, so `/mcp` can't apply those restrictions, and refuses these
tokens rather than giving them more than they hold. A token's permissions also limit the
tools it lists. Its network rules apply as on the REST API.

## Staff and support access over OAuth

A staff or support user's first OAuth connection fails once, with `insufficient_scope`.
The client then asks again for `mcp:staff` or `mcp:support`, and the consent page
warns the user that the client will act with their staff or support access.
A plain connection never carries that access.

## Audit events

| Event | Group | When |
|-------|-------|------|
| `mcp_tool_called` | `mcp` | A client called a tool. It names the user, the client and the tool, but not the arguments. |
| `oauth_consent_granted` | `auth` | A user approved a client. It names the client, its client ID, the host the browser was sent back to, and the scopes. |
| `oauth_consent_denied` | `auth` | A user refused a client. |
| `oauth_connected_app_revoked` | `auth` | A user revoked a connected app. |
| `pat_authentication_rejected` | `auth` | `/mcp` refused a personal access token for one of the reasons in [Personal access tokens on /mcp](#personal-access-tokens-on-mcp): `mcp_entity_bound`, `mcp_staff_access_missing` or `mcp_support_access_missing`. |
| `chat_injection_detected` | `chat` | A tool's arguments looked like a prompt injection, at high severity. |
| `chat_pii_detected` | `chat` | A tool's arguments held personal data or a secret, such as a private key, at high severity. |

The last two come from the input checks the MCP server shares with the AI assistant.
When the checks block a call, the client gets "Unable to process this request. Please try
rephrasing." The `chat` group is offered for subscription only while
`AI_ASSISTANT_ENABLED` is on, so with only the MCP server on, these events are recorded
but nobody can subscribe to them.

A personal access token also raises its own events, such as `pat_used_from_new_ip`,
since `/mcp` checks it on every request, as the REST API does.

## Size the database connections

Each MCP server process holds up to four Postgres connections, one per database thread.
Set the number with `--db-threads`: `waldur.mcp.dbThreads` in Helm, or
`WALDUR_MCP_DB_THREADS` in Docker Compose. Replicas times threads counts against
Postgres's `max_connections`, on top of the API and Celery.

### Limit how long database statements run

The MCP server cancels any database statement that runs for more than 30 seconds, so a
slow tool can't hold a database thread that other clients' token checks wait for. The
client then gets "An error occurred while executing the tool.", and the call's audit
event is kept.

Change the limit with `--statement-timeout <seconds>`, or turn it off with `0`. Neither
the Helm chart nor the Compose stack sets the option, so both use the default.
