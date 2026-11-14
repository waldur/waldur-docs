# Go-live checklist

Work through this list on the production environment before you open Waldur to users, and keep
it with your deployment notes: several items are recurring tasks, not one-off ones.

It applies to both supported packagings. [Docker Compose](deployment/docker-compose/index.md)
runs everything on one server; [Helm](deployment/helm/index.md) runs Waldur on Kubernetes, with
the database and the message queue managed by operators. Where the two differ, an item names
the Helm value and the Docker Compose setting (an `.env` variable unless another file is named).
The linked pages have the full instructions.

Everything under **Before go-live** blocks the launch. **After go-live** covers what to settle
in the first weeks.

## Before you start

The shape of the deployment decides how much of the rest you can do. Docker Compose is simpler
to run; Helm is what gives you high availability and point-in-time recovery.

| | Docker Compose | Helm |
|---|---|---|
| Availability | One server; containers restart on failure (`restart: always`) | Several replicas of the API, workers and portal |
| Database | Bundled PostgreSQL container, data in `./pgsql` | An operator — [CloudNativePG or Zalando](deployment/helm/docs/postgres-operator.md) — or an [external database](deployment/helm/docs/external-db-integration.md). The bundled `postgresql` subchart is for demos only |
| Message queue | Bundled RabbitMQ container, not persisted | The [RabbitMQ Cluster Operator](deployment/helm/docs/rabbitmq-operator.md). The bundled `rabbitmq` subchart is for demos only |
| Backups | Nothing built in: schedule `pg_dump` yourself ([Backups](backups.md)) | A `pg_dump` CronJob to S3 (`postgresBackup`), or the operator's WAL archiving for point-in-time recovery |
| TLS | Caddy, with Let's Encrypt or your own certificate | The ingress or Gateway API, with cert-manager or a certificate Secret |
| Upgrades | Check out the new release tag, set the image tags it pins, `docker compose pull`, `up -d` | `helm upgrade` with the new chart version |

- [ ] **Run a stable release.** Release candidates (`-rc`) and `latest` are not for production.
      Record the version you deploy.
      Helm: chart version and `waldur.imageTag` · Compose: check out the release tag and keep
      `WALDUR_MASTERMIND_IMAGE_TAG` and `WALDUR_HOMEPORT_IMAGE_TAG` as it sets them.
- [ ] **Size the servers** from the [hardware requirements](hardware-requirements.md), including
      the add-ons you enable.
- [ ] **Name an owner** for each of: backups and restores, TLS certificates, upgrades, monitoring
      alerts, and security reports. The rest of this list assumes someone receives each alert.

## Before go-live

### Secrets and keys

The packaged defaults are placeholders. Nothing refuses to start with them.

- [ ] **Set a unique secret key.** Replace the placeholders `SecretKeyChangeMe` (Helm) and
      `changeme` (Compose) before the first start, with a long random value.
      Helm `waldur.secretKey` or `waldur.secretKeyExistingSecret` · Compose `GLOBAL_SECRET_KEY`.
      **Do not change it on a running instance** until the item below is done: while
      `FIELD_ENCRYPTION_KEY` is unset, the key that encrypts stored credentials is derived from it,
      and credentials stored before you set one stay encrypted with that derived key until
      `waldur reencrypt_fields` has run.
- [ ] **Set an explicit field encryption key**, and store it apart from the database backups.
      Helm `waldur.fieldEncryptionKey` or `waldur.fieldEncryptionKeyExistingSecret` ·
      Compose `FIELD_ENCRYPTION_KEY`. Rotate it only through `FIELD_ENCRYPTION_KEY_FALLBACKS` and
      `waldur reencrypt_fields`; see [Field encryption at rest](../developer-guide/field-encryption.md).
- [ ] **Replace every default password**: the database and RabbitMQ (`waldur`/`waldur` in Helm,
      `default` and `waldur` in Compose), and, if you run them, the bundled Keycloak
      (`KEYCLOAK_ADMIN_PASSWORD`, `KEYCLOAK_POSTGRESQL_PASSWORD`) and LiveKit
      (`WALDUR_LIVEKIT_SECRET`). PostgreSQL applies its password on first initialisation only; to
      change it later, use `ALTER USER` as well.
- [ ] **Keep secrets out of version control.** Helm: reference Kubernetes Secrets
      (`*ExistingSecret`, `rabbitmq.secret`, `externalDB.secretName`, `waldur.mail.existingSecret`)
      rather than writing values into a values file in git · Compose: `.env` readable by root
      only (`chmod 600 .env`) and never committed.

### Network, TLS and headers

- [ ] **Serve a trusted certificate, and redirect HTTP to HTTPS.**
      Helm `ingress.tls.enabled`, `ingress.tls.source`, with `apiScheme` and `homeportScheme` set
      to `https` ([TLS configuration](deployment/helm/docs/tls-config.md)) · Compose: set `TLS`
      explicitly to your ACME contact address or certificate files; `internal` is self-signed
      ([Using TLS](deployment/docker-compose/index.md#using-tls)).
      Check: `curl -sI http://<host>/` answers with a redirect to `https://`.
- [ ] **Send HSTS on every response.** Compose: Caddy sends it for the portal. Helm: it comes from
      the ingress controller — ingress-nginx sends it on TLS hosts by default, others need it
      configured. Check: `curl -sI https://<host>/ | grep -i strict-transport-security`.
- [ ] **Set the Content-Security-Policy sources** for the external services the portal talks
      to — Sentry, Matomo, Matrix, the AI assistant, and the SAML identity providers that use the
      POST binding. Roll changes out in report-only mode first.
      Helm `waldur.homeport.csp` · Compose `CSP_*` (the *Content-Security-Policy* section of the
      [Docker Compose guide](deployment/docker-compose/index.md)).
      Check: the browser console shows no CSP violations while you sign in and order something.
- [ ] **Behind a load balancer, pass the client address through.** Waldur's limit on failed
      passwords per address reads the client from `X-Forwarded-For`. Unless the proxy in front
      of Waldur takes the client from the balancer's entry, every user shares the balancer's
      address, and after `PASSWORD_FAILURES_PER_ADDRESS_LIMIT` failures from anyone, password
      sign-in is blocked for everyone.
      Compose: `CADDY_TRUSTED_PROXIES` set to the balancer's addresses, and
      `WALDUR_CORE["TRUSTED_PROXY_COUNT"] = 2` in `config/waldur-mastermind/override.conf.py`
      ([Docker Compose guide](deployment/docker-compose/index.md), *Behind a load balancer*) ·
      Helm: ingress-nginx with `use-forwarded-headers: "true"` and `proxy-real-ip-cidr` set to
      the balancer's addresses; `waldur.trustedProxyCount` stays at its default
      ([IP allow-listing](deployment/helm/docs/ip-whitelisting.md)).
      Trust only the balancer — never ingress-nginx's default `proxy-real-ip-cidr: 0.0.0.0/0`,
      which lets any client forge its address past the IP allow-lists — and make Caddy or the
      ingress reachable only through it.
      Check: after a failed sign-in, **Django admin → Axes → Access attempts** shows your own
      address, not the balancer's. (The event log is no proof: it reads the first entry.)
- [ ] **Expose only ports 80 and 443.** PostgreSQL, RabbitMQ and the Celery workers must not be
      reachable from outside. Compose publishes nothing else unless you enable the Matrix call
      add-on, which needs its own ports.
- [ ] **Restrict the Django admin (`/admin/`) to administrators' networks.**
      Helm `ingress.whitelistSourceRangeAdmin` ([IP allow-listing](deployment/helm/docs/ip-whitelisting.md)) ·
      Compose: a rule in `config/caddy-includes/`.
- [ ] **Configure the outbound proxy and private CAs**, if your network needs them, before you
      connect identity providers and service providers
      ([proxy setup](deployment/helm/docs/proxy-setup.md),
      [trusted CA certificates](deployment/helm/docs/trusted-ca-certificates.md)).

### Site identity and legal texts

- [ ] **Set the public URLs.** `HOMEPORT_URL` is used in email links and identity provider
      callbacks, and defaults to `https://example.com/`; `MASTERMIND_URL` is used in SAML
      metadata and callbacks and defaults to empty.
      Helm: `homeportScheme` and `homeportHostname` set `HOMEPORT_URL`; set `waldur.mastermindUrl` ·
      Compose: `homeport_url` in `config/waldur-mastermind/whitelabeling.yaml`, and
      `WALDUR_CORE["MASTERMIND_URL"]` in `config/waldur-mastermind/override.conf.py`.
- [ ] **Set the site name, contact details and branding**: `site_name`, `site_email`,
      `support_portal_url`, logos and colours. Helm `waldur.site` and `waldur.whitelabeling`
      ([whitelabeling](deployment/helm/docs/whitelabeling.md)) · Compose
      `config/waldur-mastermind/whitelabeling.yaml`. Settings applied this way are locked in the
      administration UI and re-applied on every start.
- [ ] **Load your own terms of service and privacy policy.**
      Helm `waldur.whitelabeling.tosHtmlPath` and `privacyHtmlPath` · Compose: mount the files at
      `/etc/waldur/terms-of-service.html` and `/etc/waldur/privacy-policy.html`, as the
      [Docker Compose guide](deployment/docker-compose/index.md) describes.
      Waldur loads them only when none are stored yet; to replace a loaded text, run
      `waldur load_user_agreements --tos <file> --pp <file> --force`.
- [ ] **Review the [cookie policy](cookie-policy.md)** and decide on usage telemetry
      (Helm `waldur.telemetry.enabled` · Compose `WALDUR_TELEMETRY_ENABLED`). If you keep it on,
      say so in your privacy policy. See also [data processing](../about/data-processing.md).

### Accounts and sign-in

- [ ] **Give every administrator a named staff account**
      (`waldur createstaffuser -u <username> -p <password> -e <email>`). Do not keep a shared
      `admin` account, the example credentials from the installation guides, or users from
      testing. Check: `waldur dumpusers` lists only the people you expect.
- [ ] **Require passkeys for staff.** Once every staff user has registered one, turn on
      enforcement. Helm `waldur.passkey.enforcedForStaff` · Compose
      `WALDUR_PASSKEY_ENFORCED_FOR_STAFF` ([passkeys](identities/passkeys.md)).
- [ ] **Connect your identity providers and test each one end to end**, with a user who has never
      signed in before ([identity providers](identities/summary.md)). For Keycloak, restrict the
      client's redirect URIs to your Waldur URL rather than `*`.
- [ ] **Offer only the sign-in methods you support.** Remove local password sign-in if every user
      comes through single sign-on. Helm `waldur.authMethods` · Compose
      `WALDUR_CORE["AUTHENTICATION_METHODS"]` in `config/waldur-mastermind/override.conf.py`.
- [ ] **Decide who may create an account** through single sign-on, and how accounts are matched:
      `OIDC_BLOCK_CREATION_OF_UNINVITED_USERS`, `OIDC_ALLOWED_USER_EMAIL_PATTERNS`,
      `OIDC_MATCHMAKING_BY_EMAIL`. Match by email only when the identity provider verifies it.
- [ ] **Review the session and token limits**: `TOKEN_LIFETIME` (sign-out after an hour of
      inactivity by default), `API_TOKEN_MAX_LIFETIME_MINUTES` (`0` allows tokens that never
      expire), `PAT_ENABLED`, and the
      [brute-force protection](mastermind-configuration/brute-force-protection.md) limits.

### Development and demo features

- [ ] **Debug mode is off.** Helm `waldur.debug` · Compose `GLOBAL_DEBUG`.
- [ ] **Demo presets are off**, and no demo data was loaded: loading a preset wipes the database.
      Helm `waldur.demoPresets.enabled` · Compose `WALDUR_DEMO_PRESETS_ENABLED`
      ([demo presets](demo-presets.md)).
- [ ] **The web shell is off.** Helm `waldur.webShell.enabled` · Compose `WALDUR_WEB_SHELL_ENABLED`.
- [ ] **Compose: keep the containers off the Docker socket unless you run script-based
      offerings.** Access to it is root on the server. Set `DOCKER_GROUP_ID` to a group that
      does not own the socket — not `0` where the socket belongs to root — and never make the
      socket world-writable. Check: `stat -c '%g %G' /var/run/docker.sock`
      ([Docker socket](deployment/docker-compose/index.md)).
- [ ] **Compose with the bundled Keycloak:** it ships a public client secret (`KEYCLOAK_SECRET`) and
      a realm that accepts any redirect URI. Change both, or use your own identity provider.

### Email and notifications

Outgoing email needs three separate things to be right. See
[Email configuration](mastermind-configuration/email.md) for the settings behind each item.

- [ ] **SMTP is configured and verified end to end.** Helm `waldur.mail`
      ([mail](deployment/helm/docs/mail.md)) · Compose `EMAIL_HOST` and the other `EMAIL_*`
      variables. Check: `waldur sendtestemail <your-address>`, or **Administration → System
      management → Email configuration** in the portal.
- [ ] **Outgoing addresses are set** (`DEFAULT_FROM_EMAIL`, `DEFAULT_REPLY_TO_EMAIL`), and the
      sending domain authorises the relay in its SPF record — ideally with DKIM signing as well.
- [ ] **The notifications relevant to the deployment are enabled.** **All notification types ship
      disabled**, so a correct SMTP setup on its own still sends nothing. Helm `waldur.notifications`
      · Compose `config/waldur-mastermind/notifications.json`.

### Backups and restore

A backup counts only once you have restored it. See [Backups](backups.md).

- [ ] **Back up the database automatically**, to storage that does not share a failure with the
      database itself. Helm: `postgresBackup` and `backupStorage`
      ([backup management](deployment/helm/docs/postgres-backup-management.md)), or the
      operator's scheduled backups with WAL archiving for point-in-time recovery · Compose: a
      scheduled `pg_dump` copied off the server. Uploaded files are stored in the database, so the
      dump includes them.
- [ ] **Back up the keys and secrets separately**: the field encryption key (or the secret key
      it is derived from) and its fallbacks, plus `.env` or your Kubernetes Secrets. A dump
      restored without them has unreadable credentials; a leak of both together exposes them.
- [ ] **Version the configuration**, without secrets: your Helm values, or the Compose `config/`
      folder and `.env` template.
- [ ] **Back up add-on data**, if enabled: the Matrix homeserver and its secrets
      ([Backups → Matrix chat](backups.md#matrix-chat)).
- [ ] **Agree how much data you can lose and how long a restore may take**, and pick the backup
      frequency and method from that.
- [ ] **Restore a backup into a separate environment, and time it.** Block its outgoing email and
      provider integrations first, so the copy does not act on real resources or mail real
      users. Check: you can sign in, and the newest records are there
      ([Test the restore](backups.md#test-the-restore)).
- [ ] **Alert when a backup fails or is missing.**

### Monitoring and logs

- [ ] **Probe `https://<host>/health-check/` from outside.** The trailing slash matters; it answers
      500 when the database, cache or migrations are unhealthy. Use the real hostname: Compose
      drops requests for any other host.
- [ ] **Send errors to Sentry**, with an environment name that tells production apart.
      Helm `waldur.sentryDSN` (the environment is the namespace) · Compose `SENTRY_DSN`,
      `SENTRY_ENVIRONMENT`. See [debugging](debugging.md).
- [ ] **Collect metrics** with the Waldur Prometheus exporter and the [Grafana dashboard](grafana.md).
      Helm `waldur.metricsExporter.enabled`.
- [ ] **Alert on** disk space for the database volume, certificate expiry, Celery workers that are
      down, and queues that keep growing.
- [ ] **Keep logs for as long as you need them, and no longer.** Compose: each container's
      Docker log rotates at `DOCKER_LOG_MAX_SIZE` × `DOCKER_LOG_MAX_FILE` (these override
      `/etc/docker/daemon.json`), and the copies in `LOG_FOLDER` follow the `logger` service's
      own limits. Helm: ship pod logs to your cluster's log platform.

### Capacity and resilience

- [ ] **Tune the workers to the server**: `CELERYD_CONCURRENCY` and
      `CELERY_WORKER_MAX_MEMORY_PER_CHILD` (Compose), `celery.concurrency` and
      `celery.maxMemoryPerChild` (Helm).
- [ ] **Helm: run at least two replicas** of the API and the portal (`replicaCount.api`,
      `replicaCount.homeport`), review the resource requests and limits (`apiResources`,
      `workerResources`, `homeportResources`), and run the database and message queue with
      their operators in a highly available setup. Autoscaling is optional; with it on, the
      autoscaler owns the API and worker counts, so set `hpa.api.minReplicas` to at least 2
      ([HPA](deployment/helm/docs/hpa.md)).
- [ ] **Reboot test:** restart every node that runs Waldur components. The application must come
      back without manual steps.

### Upgrades

- [ ] **Follow the release notes** ([changelog](../about/CHANGELOG.md)) so you learn about security
      fixes and configuration changes.
- [ ] **Write the upgrade procedure down, and rehearse it.** Back up immediately before upgrading.
      Database migrations run automatically and only forward: `helm rollback` or going back to the
      previous image tag does not undo them, so the way back is restoring that backup.
- [ ] **Keep a staging environment** on the same packaging and version, to rehearse upgrades
      and configuration changes.
- [ ] **Helm: do not upgrade with `--reuse-values`.** Keep your values in a file and pass it to
      every `helm upgrade`; branding and other chart-managed settings are re-applied each time.

### Air-gapped deployments

- [ ] **Mirror every image to a local registry**, including the ones that do not follow the
      registry setting. Helm `global.imageRegistry` and `imagePullSecrets` · Compose
      `DOCKER_REGISTRY_PREFIX` (the Matrix add-on images keep their own registries).
- [ ] **Turn off calls home**: usage telemetry (Helm `waldur.telemetry.enabled` · Compose
      `WALDUR_TELEMETRY_ENABLED`) and the update check (the `CHECK_FOR_UPDATES` setting).
- [ ] **Issue certificates from your own CA**, since Let's Encrypt cannot reach the site, and make
      Waldur trust that CA for its outgoing calls.
- [ ] **SAML: provide federation metadata locally**, or turn off the metadata sync.

## Go-live day

Run these on production, with real accounts, right before you announce the service.

- [ ] Sign in through each identity provider, as a new user and as an existing one.
- [ ] Create an organization and a project, and invite a second user.
- [ ] Order a resource from a test offering, and terminate it.
- [ ] The notification email for the order arrives, with links to the right host.
- [ ] Sentry receives an event from this environment, and the external probe reports the site up.

## After go-live

- [ ] **Repeat the restore test on a schedule**, for example every quarter, and after changing
      the backup setup.
- [ ] **Rotate the credentials shared during setup**, and remove accounts that were only needed
      for it.
- [ ] **Review Sentry and the event log** for failed orders, failing integrations and sign-in
      lockouts in the first weeks.
- [ ] **Do the first upgrade through your written procedure**, and fix the procedure where it
      was wrong.
