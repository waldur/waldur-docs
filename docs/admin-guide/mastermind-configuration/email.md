# Email configuration

Outline:

- [Email configuration](#email-configuration)
    - [The two halves of email](#the-two-halves-of-email)
    - [1. SMTP transport](#1-smtp-transport)
    - [2. Sender addresses](#2-sender-addresses)
    - [3. Enabling notifications](#3-enabling-notifications)
    - [Branding outgoing mail](#branding-outgoing-mail)
    - [Verifying delivery](#verifying-delivery)
    - [Troubleshooting](#troubleshooting)

## The two halves of email

Getting mail out of Waldur requires configuring **two independent things**. Each is necessary and
neither is sufficient:

1. **SMTP transport** — where Waldur hands the message to. Configured in
   `/etc/waldur/override.conf.py`.
2. **Notification enablement** — which notification types are allowed to produce a message. Every
   notification type ships **disabled**.

!!! warning "The most common failure"
    A correctly configured SMTP relay with no notifications enabled sends nothing at all, and logs
    nothing to explain it. If you have configured SMTP and see complete silence, check
    [Enabling notifications](#3-enabling-notifications) before you debug the relay.

## 1. SMTP transport

These are standard [Django email settings](https://docs.djangoproject.com/en/4.2/ref/settings/#email-host).
Unlike most Waldur configuration, they have **no `GLOBAL_*` environment variable equivalent** — they
must be set in `/etc/waldur/override.conf.py`.

| Setting | Default | Purpose |
|---|---|---|
| `EMAIL_HOST` | `localhost` | Hostname of the SMTP relay |
| `EMAIL_PORT` | `25` | Relay port — commonly `587` for STARTTLS, `465` for implicit TLS |
| `EMAIL_HOST_USER` | `""` | Username for SMTP authentication; leave unset for an anonymous relay |
| `EMAIL_HOST_PASSWORD` | `""` | Password for SMTP authentication |
| `EMAIL_USE_TLS` | `False` | Use STARTTLS — upgrade a plaintext connection. Pair with port `587` |
| `EMAIL_USE_SSL` | `False` | Use implicit TLS from the first byte. Pair with port `465` |
| `EMAIL_TIMEOUT` | `None` | Socket timeout in seconds. Worth setting so a stalled relay cannot block a worker |

!!! danger "`EMAIL_USE_TLS` and `EMAIL_USE_SSL` are mutually exclusive"
    Setting both to `True` raises an error at send time. Pick the one your relay speaks.

### Authenticated relay over STARTTLS

The most common production setup:

```python
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'waldur@example.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_TIMEOUT = 30
```

Reading the password from the environment keeps it out of the configuration file. Whether the
variable reaches the process depends on your deployment method — see
[Deployment-specific notes](#deployment-specific-notes).

### Implicit TLS

```python
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'waldur@example.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
```

### Unauthenticated internal relay

Typical when an MTA on the same network accepts mail from Waldur's address range:

```python
EMAIL_HOST = 'mail-relay.internal'
EMAIL_PORT = 25
```

Leave `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` unset. Django only attempts `SMTP.login()` when
both are non-empty, so an anonymous session is the default.

### Deployment-specific notes

**Docker image.** The base image ships an `/etc/waldur/override.conf.py` containing a single
placeholder line, `EMAIL_HOST = "waldur-smtp"`. That hostname does not resolve in any shipped
stack — you must replace the file with your own.

**Helm.** The chart renders `override.conf.py` from `waldur.mail.*` values into the
`api-override-config` ConfigMap:

```yaml
waldur:
  mail:
    host: "smtp.example.com"
    port: "587"
    useTLS: "true"
    from: "waldur@example.com"
    replyTo: "support@example.com"
```

**Docker Compose.** The stack mounts `config/waldur-mastermind/override.conf.py` over the image's
copy, so add the settings to that file and restart the `waldur-mastermind-api`,
`waldur-mastermind-worker` and `waldur-mastermind-beat` services. Note that the compose stack
ships no SMTP relay of its own.

### Redirecting mail during testing

To inspect what Waldur would send without delivering it, point `EMAIL_BACKEND` at a non-SMTP
backend:

```python
# Write each message to the console instead of sending it
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Or drop messages silently while still recording them in the email log
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
```

Both leave the [email log](#verifying-delivery) intact, so you can still confirm which messages
were generated.

## 2. Sender addresses

These control the headers on the message rather than its delivery. Each has a `GLOBAL_*`
environment variable, so they can be set without touching `override.conf.py`.

| Setting | Environment variable | Purpose |
|---|---|---|
| `DEFAULT_FROM_EMAIL` | `GLOBAL_DEFAULT_FROM_EMAIL` | `From` address on all automated correspondence |
| `DEFAULT_REPLY_TO_EMAIL` | `GLOBAL_DEFAULT_REPLY_TO_EMAIL` | `Reply-To` header, applied to every message |
| `EMAIL_HOOK_FROM_EMAIL` | `GLOBAL_EMAIL_HOOK_FROM_EMAIL` | Alternative `From` used **only** by event-logging email hooks, so hook traffic can be filtered separately from user notifications |

!!! note "`SITE_EMAIL` is something else"
    The `SITE_EMAIL` setting under **Administration → Configuration** is a contact address rendered
    in the UI footer and in marketplace order headers. It is not used as an envelope sender and has
    no effect on delivery.

Whichever domain you put in `DEFAULT_FROM_EMAIL` must authorise your relay in its SPF record, and
ideally sign with DKIM. A large share of "Waldur does not send email" reports are messages that
were sent, accepted, and then dropped by the recipient's spam filter.

The subject of event-logging hook emails is set separately, via
`WALDUR_CORE['NOTIFICATION_SUBJECT']` (default `Notifications from Waldur`). It does not affect
regular notifications, which carry their own subject templates.

## 3. Enabling notifications

**All notification types are disabled by default.** This is deliberate — a fresh deployment should
not start mailing users while it is being configured — but it means an otherwise complete email
setup produces nothing until notifications are turned on.

There are two ways to enable them.

### Through the UI

Navigate to **Administration → Notifications** and toggle the notification types you need. See
[Notification management](../../user-guide/staff-users/notification-management.md) for the full
list and the template editor.

### Through configuration

Declare the desired state in `/etc/waldur/notifications.json` (JSON or YAML) and load it:

```json
{
    "users.invitation_created": true,
    "users.invitation_approved": true,
    "marketplace.notification_usages": true,
    "invoices.notification": false
}
```

```bash
waldur load_notifications /etc/waldur/notifications.json
```

Only keys present in the file are changed; anything omitted keeps its current value. The container
image runs this command automatically at startup against `/etc/waldur/notifications.json`, so
mounting the file is enough.

In Helm, set the same mapping under `waldur.notifications` in `values.yaml`:

```yaml
waldur:
  notifications:
    users.invitation_created: true
    users.invitation_approved: true
```

To see the available notification keys and their templates, consult the
[Notifications reference](notifications.md) or run `waldur print_notifications`.

## Branding outgoing mail

A common footer can be appended to every outgoing message. Both are set under
**Administration → Configuration → Notifications**:

| Setting | Purpose |
|---|---|
| `COMMON_FOOTER_TEXT` | Appended to the plain-text body of every email |
| `COMMON_FOOTER_HTML` | Appended to the HTML alternative, when one exists |

Message bodies themselves are Django templates and can be replaced wholesale — either through the
template editor in **Administration → Notifications**, or in bulk from a YAML file:

```yaml
users/invitation_created_subject.txt: |
  Invitation to {{ customer.name }}

users/invitation_created_message.html: |
  <p>Hello {{ user.full_name }}, you have been invited to {{ customer.name }}.</p>
```

```bash
waldur override_templates /etc/waldur/notifications-templates.yaml
```

Add `--clean` to remove any stored template not named in the file. See
[Templates](templates.md) for the full catalogue of overridable templates.

## Verifying delivery

Work outwards from the transport.

**1. Send a test message.** This bypasses the notification system entirely, so it isolates the SMTP
half:

```bash
# Docker Compose
docker exec -it waldur-mastermind-api waldur sendtestemail you@example.org

# Kubernetes
kubectl -n waldur exec -it $(kubectl -n waldur get pods -l app=waldur-mastermind-api -o name | head -1) \
  -- waldur sendtestemail you@example.org
```

A connection error here means the transport settings are wrong. Success with no message in your
inbox means the relay accepted it and something downstream — SPF, DKIM, a spam filter — discarded
it.

**2. Check the email log.** A message is recorded once the relay has *accepted* it: Waldur writes
the log row after the send returns, so a message the relay refuses raises first and is never
logged. `sendtestemail` uses Django's own send path and never appears here either. Browse the log
under **Support → Email logs** in the UI, or query `/api/email-logs/` directly. Each entry carries
the subject, body and recipient list.

An empty log therefore has two readings, and the worker logs distinguish them: SMTP errors there
mean the transport is at fault; silence means no message was ever generated — go back to
[Enabling notifications](#3-enabling-notifications).

**3. Check the worker logs.** Notifications are sent from Celery workers, not from the API process.
Each dispatch logs an `about to send` line:

```bash
# Kubernetes
kubectl logs -n waldur -l app=waldur-mastermind-worker --tail=1000 | grep -i "about to send"
```

See [Debugging](../debugging.md) for the Docker Compose equivalent and broader log filtering.

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| Email log empty, worker logs silent | Notifications are disabled — see [step 3](#3-enabling-notifications) |
| Email log empty, worker logs show SMTP errors | Transport is failing — the log row is only written after the relay accepts |
| `sendtestemail` fails with "connection refused" | `EMAIL_HOST` unset, still the `waldur-smtp` placeholder, or unreachable from the pod/container |
| Relay rejects the session as unauthenticated | `EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD` did not reach the process |
| `SMTPServerDisconnected` or a TLS handshake error | `EMAIL_USE_TLS` used against an implicit-TLS port, or `EMAIL_USE_SSL` against a STARTTLS port — match the flag to the port |
| Both TLS flags set, error at send time | `EMAIL_USE_TLS` and `EMAIL_USE_SSL` are mutually exclusive |
| Log shows the message was sent, recipient never receives it | SPF/DKIM missing for the `DEFAULT_FROM_EMAIL` domain, or recipient-side filtering |
| Email log is populated but nothing arrives | The relay accepted and dropped the message — inspect the relay's own logs |
| Templates edited on disk have no effect | Stored templates take precedence — edit them under **Administration → Notifications** or via `override_templates` |
