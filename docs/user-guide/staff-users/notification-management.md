# Notification management

Waldur includes a configurable notification system for managing email communications. Administrators can enable/disable notifications, customize email templates, and manage notification delivery.

## Overview

Waldur has 40+ notification types organized by module. Each notification has:

- **Subject template**: Email subject line
- **Text template**: Plain text email body
- **HTML template**: Rich HTML email body
- **Context variables**: Dynamic data available in templates

## Managing notifications

**Performed by:** Staff users

1. Navigate to **Administration** → **Notifications**
2. View the list of all notification types with their current status (enabled/disabled)

### Enabling and disabling notifications

- Click the **toggle** next to any notification to enable or disable it
- Disabled notifications will not send any emails

!!! warning
    All notifications are disabled by default. Enable the notifications relevant to your deployment before going live.

### Editing email templates

1. Click on a notification to open the template editor
2. The editor shows three tabs:
    - **Subject**: Plain text subject line template
    - **Message (text)**: Plain text body template
    - **Message (HTML)**: Rich HTML body template
3. Use the **Variables** pane on the right to see available template variables
4. Edit the template using the Monaco code editor
5. Click **Save** to apply changes

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

### Resetting templates

To restore a template to its default:

1. Open the notification template editor
2. Click **Reset to default**
3. The template reverts to the system default version

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
