# Web shell

The web shell lets staff users open the [Waldur shell](waldur-shell.md) (`waldur shell`) in a
browser tab, straight from the Waldur user menu. It is meant for development and demo
deployments, where it saves a trip to the host or the cluster to look at data or try a snippet.

!!! danger "Development and demo deployments only"
    The web shell gives every staff user an interactive Python shell inside the Waldur
    container, with full access to the database and to every secret in the settings. It works
    only when Waldur runs with `DEBUG`, which must never be on in production. Before you enable
    it, check who can become staff on the deployment: a demo identity provider or LDAP
    directory with published passwords makes the shell reachable by anyone who knows them.

## How it works

1. A staff user selects **Web shell** in the user menu, and the page is opened in a new tab.
2. Homeport asks the API for a link (`POST /api/web-shell-ticket/`). The link carries a
   single-use ticket that expires after 60 seconds.
3. The page connects to a separate `waldur web_shell` process, which checks the ticket and
   starts `waldur shell` for that user.

The page header shows where the shell is connected: the site name, the portal domain, the host
and the database. The status bar shows the full name, username and email of the signed-in user.

The menu entry appears only for staff, and only when the API reports the web shell as enabled.
That requires all three of:

- `DEBUG` (`GLOBAL_DEBUG=true` in the container images);
- `WALDUR_CORE["WEB_SHELL_ENABLED"] = True` (`WALDUR_WEB_SHELL_ENABLED=true`);
- `WALDUR_CORE["WEB_SHELL_URL"]` set to the public URL of the web shell page
  (`WALDUR_WEB_SHELL_URL`), for example `https://waldur.example.com/webshell/`.

Without them the ticket endpoint returns 404 and the `waldur web_shell` process refuses to
start.

## Enabling it

=== "Docker Compose"

    Set these in `.env` and start the `web-shell` profile:

    ```bash
    GLOBAL_DEBUG=true
    WALDUR_WEB_SHELL_ENABLED=true
    WALDUR_WEB_SHELL_URL=https://waldur.example.com/webshell/
    # Either add the profile here, or pass --profile web-shell to docker compose.
    COMPOSE_PROFILES=web-shell
    ```

    ```bash
    docker compose up -d
    ```

    Caddy routes `/webshell` to the `waldur-mastermind-web-shell` service. The route has no IP
    allowlist; to restrict it, replace `config/caddy-includes/web-shell.conf` with your own. See
    the [Docker Compose guide](deployment/docker-compose/index.md#web-shell-development-only).

=== "Helm"

    ```yaml
    waldur:
      debug: true
      webShell:
        enabled: true
        # Optional. Defaults to <apiScheme>://<apiHostname>/webshell/
        url: ""
    ```

    The chart refuses to render the web shell without `waldur.debug`, and routes `/webshell`
    behind the same IP allowlist as the Django admin. See the
    [Helm guide](deployment/helm/docs/web-shell.md).

=== "Local development"

    The `dev_settings_web_shell` settings module enables the web shell with the page at
    `http://localhost:18090/webshell/`. Run the API and the web shell with the same settings:

    ```bash
    export DJANGO_SETTINGS_MODULE=waldur_core.server.dev_settings_web_shell
    uv run waldur web_shell --fetch-assets   # once: downloads the terminal assets
    uv run waldur web_shell                  # listens on the port of WEB_SHELL_URL
    ```

    `uv run waldur web_shell --mint <username>` prints a single-use link for a staff user
    without going through Homeport.

## Access and limits

- **Staff only.** Every link works once and expires after 60 seconds.
- **Bound to the Waldur login.** The shell is tied to the login token the link was issued for.
  It closes within 30 seconds when that token goes away (the user logs out, or the token
  expires or is revoked), or when the user loses staff status or is deactivated. If the check
  itself fails three times in a row, for example while the database is down, the shell closes
  too.
- **One shell per user.** Opening a second one is refused while the first is open.
- **Idle timeout.** A shell with no input for 15 minutes is closed.
- **Host and Origin checks.** Only the host of `WEB_SHELL_URL`, `localhost` and any names in
  `WALDUR_WEB_SHELL_ALLOWED_HOSTS` are served. Browser connections must come from the origin
  of `WEB_SHELL_URL`.
- **No outside resources.** The page loads nothing from other sites and sends no referrer. The
  terminal ([ghostty-web](https://github.com/waldur/ghostty-web), Waldur's fork with security
  fixes) ships in the image, pinned by version and checksum.

## Settings

The `waldur web_shell` process reads these environment variables:

| Variable | Default | Purpose |
|----------|---------|---------|
| `WALDUR_WEB_SHELL_ENABLED` | `false` | Maps to `WALDUR_CORE["WEB_SHELL_ENABLED"]` in the container images. |
| `WALDUR_WEB_SHELL_URL` | empty | Maps to `WALDUR_CORE["WEB_SHELL_URL"]`: the public URL of the page. |
| `WALDUR_WEB_SHELL_ALLOWED_HOSTS` | empty | Comma-separated extra Host names to serve, for a proxy that forwards under an internal name. |
| `WALDUR_WEB_SHELL_IDLE_TIMEOUT` | `900` | Seconds without input before a shell is closed. |
| `WALDUR_WEB_SHELL_ACCESS_CHECK_INTERVAL` | `30` | Seconds between checks of the user's login and staff status. |
| `WALDUR_WEB_SHELL_TRANSCRIPT_DIR` | unset | Directory to record each session in, one file per session. |
| `WALDUR_WEB_SHELL_ASSETS_DIR` | `/usr/share/waldur/web-shell` in the image | Where the terminal assets are installed. Outside the image they are cached under `~/.cache/waldur-web-shell/`. |

The `waldur web_shell` command takes `--host` (default `127.0.0.1`), `--port` (default: the port
of `WEB_SHELL_URL`, or 8090), `--fetch-assets` and `--mint <username>`.

## Troubleshooting

| Symptom | Cause |
|---------|-------|
| No **Web shell** entry in the user menu | The user is not staff, or `DEBUG`, `WEB_SHELL_ENABLED` or `WEB_SHELL_URL` is missing on the API. |
| The tab shows **502** | The web shell process is not running (for Docker Compose, the `web-shell` profile is not active). |
| `Forbidden host` | The request reached the web shell under a Host name it does not serve. Add it to `WALDUR_WEB_SHELL_ALLOWED_HOSTS`. |
| `Bad origin` | The page was opened from a different origin than `WEB_SHELL_URL`. Check that the setting matches the address in the browser. |
| **Invalid ticket** | The link was already used or is older than 60 seconds. Open the shell again from the menu. |
| **Shell already open** | The user has another web shell open. Close it first. |
| **Signed out of Waldur**, **No longer staff** or **Account deactivated** | The Waldur login behind the shell ended. Sign in again and reopen the shell. |
