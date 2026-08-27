# Notification management

Waldur includes a configurable notification system for managing email communications. Administrators can enable/disable notifications, customize email templates, and manage notification delivery.

## Overview

Waldur has 70+ notification types organized by module. Each notification has:

- **Subject template**: Email subject line
- **Text template**: Plain text email body
- **HTML template**: Rich HTML email body
- **Context variables**: Dynamic data available in templates

## Managing notifications

**Performed by:** Staff users

1. Navigate to **Support** → **User management** → **Notifications**
2. View the list of all notification types with their current status

Each row shows the notification code, when it was created, and whether it is enabled.
A pencil icon next to the code marks a notification whose template has been
customised, and a question mark icon reveals its description.

!!! note
    The actions described below are available to staff users only. Other users
    can open the list but see no actions on it.

### Enabling and disabling notifications

1. Open the **actions menu** at the end of the notification's row
2. Select **Enable** or **Disable**

Disabled notifications will not send any emails.

!!! warning
    All notifications are disabled by default. Enable the notifications relevant to your deployment before going live.

    Enabling a notification only decides whether a message is *composed*. Delivery additionally
    requires a configured SMTP relay — see
    [Email configuration](../../admin-guide/mastermind-configuration/email.md).

### Viewing templates

Expand a notification's row to read its templates without editing them. Each
template is shown on its own tab, with a **Copy** button for its content.

### Editing email templates

1. Open the **actions menu** at the end of the notification's row and select **Edit**
2. The editor shows one tab per template — the subject line, the plain text body
   and the HTML body — named after the underlying template file
3. Open the **Available variables** tab for a table of the variables this
   notification provides, with their types and descriptions
4. Edit the template in the code editor
5. Click **Confirm** to apply changes

Changes take effect on the next email sent; no restart is required.

### Template syntax

Templates use Django template syntax:

```django
Dear {{ user.full_name }},

Your proposal "{{ proposal.name }}" has been {{ proposal.state }}.

{% if proposal.state == "accepted" %}
Congratulations! Your project has been created.
{% endif %}

Best regards,
{{ call.name }} Team
```

### Reverting a customised template

There is no reset action in the interface. A customised template is marked with a
pencil icon in the list and on its tab; to return it to the shipped wording,
replace its content with the original text. Clearing the editor shows the
original as a placeholder, and it is also returned by the API as
`original_content`.

## Proposal notifications

The following notifications are available for call management:

| Notification | Recipients | Trigger |
|---|---|---|
| New proposal submitted | Call managers | Researcher submits a proposal |
| New review submitted | Call managers | Reviewer submits evaluation |
| Proposal cancelled | Proposal creator | Round cutoff passes (auto-cancel) |
| Proposal state changed | Proposal creator | Any state transition |
| Submission deadline approaching | Draft proposers | 3 days before round cutoff |
| Review assigned | Reviewer | Manager assigns a review |
| Review deadline approaching | Reviewers | 3 days before review deadline |
| Review rejected | Call managers | Reviewer rejects assignment |
| Round closing | Call managers | Round ends |
| Round opening | Reviewers | New round becomes active |
| Reviews complete | Call managers | All required reviews submitted |
| Proposal decision (reviewer) | Reviewers | After accept/reject decision |
| Requested offering decision | Call manager | Decision on offering request |

## Broadcasting

For one-time communications to groups of users, use the [Broadcasting](broadcasting.md) feature instead of notification templates.

## Configuration via management commands

Administrators can manage notifications via CLI:

```bash
# Load notification configuration from file
waldur load_notifications /etc/waldur/notifications.json

# Override templates from YAML file
waldur override_templates /etc/waldur/custom_templates.yaml

# Generate notification documentation
waldur print_notifications
```
