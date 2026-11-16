---
requires:
  - setting:MCP_ENABLED
---

# Connect AI clients over MCP

AI clients such as Claude, ChatGPT, Cursor and VS Code can read your Waldur data over the
Model Context Protocol (MCP). Ask them about your organizations, projects, resources,
orders, costs and the marketplace, and they call Waldur's tools to answer. The tools
only read: a client can't change anything in Waldur.

A client acts as you. It sees what you see in the portal, with your roles in
organizations and projects. For the tools it can call, see [MCP tools](mcp-tools.md).

## What you need to connect a client

- **The server URL.** It is `/mcp` on your portal's API address, such as
  `https://api.example.com/mcp`. Ask your Waldur administrator if you don't know the API
  address. Enter the URL exactly, without a slash at the end.
- **A way to sign in.** Most clients sign in with OAuth: they open Waldur in your
  browser, and you approve them there. Some clients take a personal access token
  instead. See [Sign in with OAuth or a personal access token](#sign-in-with-oauth-or-a-personal-access-token).

Some clients connect from the vendor's cloud rather than from your computer: Claude.ai
and Claude Desktop's connectors, ChatGPT, Atlassian Rovo and Microsoft Copilot Studio. They reach Waldur only if your
portal's API is reachable from the internet.

## Sign in with OAuth or a personal access token

**OAuth** is the default for most clients. The client opens Waldur's consent page in your
browser. Sign in to the portal if asked. Check the **Application** name, and the
address under **Sends you back to**, which should belong to the client you are
connecting. Then select **Allow**. The client renews its access by itself, and loses it
after 30 days without use.

**A personal access token** suits clients that take a fixed `Authorization` header. Not
every token works on `/mcp`. See
[Use a personal access token](#use-a-personal-access-token).

## Connect Claude.ai or Claude Desktop

Add Waldur as a custom connector in Claude. A connector you add works in Claude.ai, Claude
Desktop and the Claude mobile apps. Claude connects to Waldur from Anthropic's cloud,
and only on port 443, the default for HTTPS.

On a personal plan:

1. Open **Customize > Connectors**.
2. Select **Add**, then **Add custom connector**.
3. Enter a name, such as `Waldur`, and the server URL. Select **Continue**.
4. Keep the authentication options marked **Detected**, and select **Add**.
5. Select **Connect**, and approve Claude on Waldur's consent page.

On a Team or Enterprise plan, an owner adds the connector once, under **Organization
settings > Connectors**, with **Add > Custom > Web**. Members then open **Customize >
Connectors**, find the connector marked **Custom**, and select **Connect**. Each member
approves it with their own Waldur account.

## Connect ChatGPT

Custom MCP servers are available on some ChatGPT plans only, and in a workspace an admin
may have to allow you to add them. ChatGPT connects to Waldur from OpenAI's cloud.

1. Open [chatgpt.com/plugins](https://chatgpt.com/plugins), select **+**, then **Add
   custom MCP server**.
2. Enter a name, such as `Waldur`.
3. Under **Connection**, enter the server URL.
4. For authentication, choose **OAuth**.
5. Select **I understand and want to continue**, then **Create as a plugin**.
6. Install the plugin, and approve ChatGPT on Waldur's consent page.

ChatGPT can't send a fixed `Authorization` header, so it always signs in with OAuth.

## Connect Claude Code

Add the server from a terminal:

```bash
claude mcp add --transport http waldur https://api.example.com/mcp
```

Then, in Claude Code, run `/mcp`, select `waldur`, and sign in. Claude Code opens Waldur's
consent page in your browser.

By default, the server is available in the current project only. Add `--scope user` to
use it in all your projects, or `--scope project` to share it with your team in the
project's `.mcp.json`. Each team member then signs in with their own account.

### Give Claude Code a token { data-requires="setting:PAT_ENABLED" }

To use a personal access token instead of signing in, pass it as a header:

```bash
claude mcp add --transport http waldur https://api.example.com/mcp \
  --header "Authorization: Bearer $WALDUR_TOKEN"
```

In a shared `.mcp.json`, refer to an environment variable, so that the token stays out
of the file:

```json
{
  "mcpServers": {
    "waldur": {
      "type": "http",
      "url": "https://api.example.com/mcp",
      "headers": { "Authorization": "Bearer ${WALDUR_TOKEN}" }
    }
  }
}
```

## Connect Cursor

Add the server to `~/.cursor/mcp.json` for all your projects, or to `.cursor/mcp.json`
in one project:

```json
{
  "mcpServers": {
    "waldur": {
      "url": "https://api.example.com/mcp"
    }
  }
}
```

Cursor's MCP settings then show that the server needs you to sign in. Start the sign-in
there, and approve Cursor on Waldur's consent page.

### Give Cursor a token { data-requires="setting:PAT_ENABLED" }

To use a personal access token instead of signing in, add a header that reads it from an
environment variable:

```json
{
  "mcpServers": {
    "waldur": {
      "url": "https://api.example.com/mcp",
      "headers": { "Authorization": "Bearer ${env:WALDUR_TOKEN}" }
    }
  }
}
```

## Connect VS Code

These steps are for GitHub Copilot in VS Code. In a Copilot Business or Enterprise
organization, an administrator must turn on the **MCP servers in Copilot** policy first.

1. Open the Command Palette and run **MCP: Add Server**.
2. Choose **HTTP (HTTP or Server-Sent Events)**.
3. Enter the server URL, and a name such as `waldur`.
4. When VS Code asks, allow it to sign in, and approve it on Waldur's consent page. If
   it doesn't ask, start the sign-in with the server's **Authenticate** action.

### Give VS Code a token { data-requires="setting:PAT_ENABLED" }

To use a personal access token instead of signing in, add a `headers` entry with
`"Authorization": "Bearer <token>"` to the server's configuration. Read the token from an
environment variable or a VS Code input variable, rather than writing it into the file.

## Connect Atlassian Rovo

An Atlassian organization admin adds Waldur to Rovo once, in Atlassian Administration:

1. Select the organization, go to **Apps > Sites**, select the site, then **Connected
   apps**.
2. Open the menu next to **Explore apps**, and select **Add external MCP server**.
3. Select **Agree and continue**, then **Custom MCP server**, then **Next**.
4. Enter the server URL and a name, such as `Waldur`, and finish the installation.
5. Under **View app details > Tools selection**, choose the Waldur tools Rovo may use.

To use the tools, add them to an agent in Rovo Studio: open the agent's **Details**,
select **Edit**, then **Tools > Add tools**. Each user connects their own Waldur account
the first time they use the tools, on Waldur's consent page. Rovo connects to Waldur from
Atlassian's cloud.

## Connect Microsoft Copilot Studio

1. On your agent's **Tools** page, select **Add a tool**, then **New tool**, then **Model
   Context Protocol**.
2. Enter a **Server name**, a **Server description** that tells the agent what Waldur
   holds, and the **Server URL**.
3. For authentication, choose **OAuth 2.0**, then **Dynamic discovery**.
4. Select **Create**. Under **Add tool**, select **Create a new connection**, approve
   Copilot Studio on Waldur's consent page, then select **Add to agent**.

Copilot Studio connects to Waldur from Microsoft's cloud.

If the sign-in fails with **Dynamic discovery**, ask your Waldur administrator to
register a client for Copilot Studio, and choose **Manual** instead. Enter the client ID
and secret you get, and these values:

| Field | Value |
|-------|-------|
| **Authorization URL** | `https://api.example.com/oauth/authorize/` |
| **Token URL template** | `https://api.example.com/oauth/token/` |
| **Refresh URL** | `https://api.example.com/oauth/token/` |
| **Scopes** | `mcp:read` |

Give the administrator the callback URL that Copilot Studio shows.

### Give Copilot Studio a token { data-requires="setting:PAT_ENABLED" }

To use a personal access token instead, choose **API key** for authentication, with the
type **Header** and the header name `Authorization`. Whoever uses the agent then enters
`Bearer` and a space, followed by their token.

## Connect another MCP client

Other clients that support remote MCP servers over Streamable HTTP, such as the MCP
Inspector, connect the same way. Give the client the server URL, and it finds Waldur's
sign-in by itself. Waldur accepts clients that register themselves through Dynamic Client
Registration, and clients that identify themselves with a client ID metadata document.
Neither needs any setup in Waldur.

If a client asks for OAuth settings instead, ask your Waldur administrator for a client ID
and secret, and enter these values:

| Setting | Value |
|---------|-------|
| Authorization URL | `https://api.example.com/oauth/authorize/` |
| Token URL | `https://api.example.com/oauth/token/` |
| Scope | `mcp:read` |

### Give another client a token { data-requires="setting:PAT_ENABLED" }

A client that sends a fixed header can use a personal access token instead, with the
header `Authorization: Bearer <your token>`.

## Reconnect as a staff or support user

A staff or support user's first OAuth connection works only after a second approval:

1. On the first consent page, Waldur warns **This app will not work for your account
   yet**, because the client didn't ask for your staff or support access. Select
   **Allow** anyway.
2. The client's first call fails with `insufficient_scope`. Most clients then start the
   sign-in again by themselves. If yours doesn't, reconnect it.
3. This time the client asks for the `mcp:staff` or `mcp:support` scope, and the consent
   page warns **This app asks for staff access** or **This app asks for support
   access**. The client will be able to see what your account can see anywhere in the
   portal, not only in your own organizations and projects. Select **Allow** only if
   you trust the client with that.

A client never gets your staff or support access without that second approval.

## Manage connected apps

Open **Profile > Credentials > Connected apps** to see the clients you have approved.
Each row shows the client's name and host, how it registered with Waldur, its scopes,
when you first authorized it and when it last called Waldur.

To end a client's access, select **Revoke** on its row. Waldur deletes the client's
tokens at once, and the client has to ask for your approval again to reconnect.

Only you see your connected apps. They can't be managed while you are signed in with a
token.

## Use a personal access token

Create a token under **Profile > Credentials > Personal access tokens**, as described in
[Personal access tokens](personal-access-tokens.md), and give the client this header:

```text
Authorization: Bearer <your token>
```

The token works on `/mcp` like on the REST API, except that Waldur refuses:

- a token limited to particular organizations, projects or other entities, under
  **Restrict to specific entities**;
- a staff user's token without the **Access staff** scope (`STAFF.ACCESS`);
- a support user's token without **Access support** (`SUPPORT.ACCESS`) or
  **Access staff**.

The token's scopes also limit the tools the client lists. Its **Allowed networks**
apply too: the address Waldur checks is that of the client, which for a client in the
vendor's cloud is not your own.

## Fix a client that doesn't connect

| What the client reports | What to do |
|-------------------------|------------|
| 404 Not Found | The MCP server is off, or the URL is wrong. Check the URL, and ask your administrator whether the MCP server is turned on. |
| 401 with `invalid_token` | The token has expired or was revoked, or Waldur refuses it. Sign in again, or check the token against [Use a personal access token](#use-a-personal-access-token). |
| 403 with `insufficient_scope` | You are a staff or support user. Reconnect the client, as in [Reconnect as a staff or support user](#reconnect-as-a-staff-or-support-user). |
| The browser shows "Invalid sign-in request" | The client's sign-in request is malformed, or names a server that this portal doesn't serve. Check the URL. |
| A tool answers "Unable to process this request. Please try rephrasing." | Waldur's input checks refused the tool's arguments, for example text that reads like instructions to the model, or a secret such as a private key. Ask again in other words, and leave secrets out. |
| A tool answers "An error occurred while executing the tool." | The tool failed, or took too long. Ask for less at once, such as one project rather than all of them. If it keeps failing, tell your administrator. |
| The client signs in but lists fewer tools than [MCP tools](mcp-tools.md) | Some tools depend on your role, your token's scopes and the portal's settings. See [Which tools your client lists](mcp-tools.md#which-tools-your-client-lists). |
