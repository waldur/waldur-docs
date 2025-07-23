# Notifications

## WALDUR_CORE.STRUCTURE

### structure.change_email_request

A notification sent out when an email change is requested. Recipient is the old email address.

#### Templates

=== "structure/change_email_request_subject.txt"

```txt
    Verify new email address.

```

=== "structure/change_email_request_message.txt"

```txt
    To confirm the change of email address from {{ request.user.email }} to {{ request.email }}, follow the {{ link }}.

```

=== "structure/change_email_request_message.html"

```txt
    <p>To confirm the change of email address from {{ request.user.email }} to {{ request.email }}, follow the <a href="{{ link }}">link</a>.</p>

```

### structure.notifications_profile_changes_operator

A notification sent out to notify about profile changes. The recipients are Waldur operators.

#### Templates

=== "structure/notifications_profile_changes_operator_subject.txt"

```txt
    Owner details have been updated

```

=== "structure/notifications_profile_changes_operator_message.txt"

```txt
    Owner of
    {% for o in organizations %}
        {{ o.name }} {% if o.abbreviation %} ({{ o.abbreviation }}){% endif %}{% if not forloop.last %}, {% endif %}
    {% endfor %}

    {{user.full_name}} (id={{ user.id }}) has changed

    {% for f in fields %}
        {{ f.name }} from {{ f.old_value }} to {{ f.new_value }}{% if not forloop.last %}, {% else %}.{% endif %}
    {% endfor %}

```

=== "structure/notifications_profile_changes_operator_message.html"

```txt
    Owner of
    {% for o in organizations %}
        {{ o.name }} {% if o.abbreviation %} ({{ o.abbreviation }}){% endif %}{% if not forloop.last %}, {% endif %}
    {% endfor %}

    {{user.full_name}} (id={{ user.id }}) has changed

    {% for f in fields %}
        {{ f.name }} from {{ f.old_value }} to {{ f.new_value }}{% if not forloop.last %}, {% else %}.{% endif %}
    {% endfor %}

```

### structure.structure_role_granted

A notification sent out when a role is granted. The recipient is the user who received the role.

#### Templates

=== "structure/structure_role_granted_subject.txt"

```txt
    Role granted.

```

=== "structure/structure_role_granted_message.txt"

```txt
    Role {{ permission.role }}  for {{ structure }} has been granted.

```

=== "structure/structure_role_granted_message.html"

```txt
    <p>Role {{ permission.role }}  for {{ structure }} has been granted.</p>

```

## WALDUR_CORE.USERS

### users.invitation_approved

A notification sent to notify the user that his invitation has been approved. The recipient is the user who's being invited.

#### Templates

=== "users/invitation_approved_subject.txt"

```txt
    Account has been created

```

=== "users/invitation_approved_message.txt"

```txt
    Hello!

    {{ sender }} has invited you to join {{ name }} {{ type }} in {{ role }} role.
    Please visit the link below to sign up and accept your invitation:
    {{ link }}

    Your credentials are as following.

    Username is {{ username }}

    Your password is {{ password }}

```

=== "users/invitation_approved_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Account has been created</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        {{ sender }} has invited you to join {{ name }} {{ type }} in {{ role }} role.<br>
        Please visit <a href="{{ link }}">this page</a> to sign up and accept your invitation.
    </p>
    <p>
      Your credentials are as following.
    </p>
    <p>
      Your username is {{ username }}
    </p>
    <p>
      Your password is {{ password }}
    </p>
    </body>
    </html>

```

### users.invitation_created

A notification sent to the user so that he can accept it and receive permissions. The recipient is the user who's being invited.

#### Templates

=== "users/invitation_created_subject.txt"

```txt
    {% if reminder %}
    REMINDER: Invitation to {{ name }} {{ type }}
    {% else %}
    Invitation to {{ name }} {{ type }}
    {% endif %}

```

=== "users/invitation_created_message.txt"

```txt
    Hello!

    {{ sender }} has invited you to join {{ name }} {{ type }} in {{ role }} role.
    Please visit the link below to sign up and accept your invitation:
    {{ link }}
    {{ extra_invitation_text }}

```

=== "users/invitation_created_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Invitation to {{ name }} {{ type }}</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        {{ sender }} has invited you to join {{ name }} {{ type }} in {{ role }} role.<br>
        Please visit <a href="{{ link }}">this page</a> to sign up and accept your invitation.
        Please note: this invitation expires at {{ invitation.get_expiration_time|date:'d.m.Y H:i' }}!
    </p>
    <p>
        {{ extra_invitation_text }}
    </p>
    </body>
    </html>

```

### users.invitation_expired

A notification sent out to notify the user that his invitation has expired. The recipient is the user who's being invited.

#### Templates

=== "users/invitation_expired_subject.txt"

```txt
    Invitation has expired

```

=== "users/invitation_expired_message.txt"

```txt
    Hello!

    An invitation to {{ invitation.email }} has expired.
    This invitation expires at {{ invitation.get_expiration_time|date:'d.m.Y H:i' }}.

```

=== "users/invitation_expired_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Invitation to {{ invitation.email }} has expired</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        An invitation to {{ invitation.email }} has expired <br>
        An invitation to {{ invitation.email }} has expired at {{ invitation.get_expiration_time|date:'d.m.Y H:i' }}.

    </p>
    </body>
    </html>

```

### users.invitation_rejected

A notification sent to notify the user that his invitation has been rejected. The recipient is the user who's being invited.

#### Templates

=== "users/invitation_rejected_subject.txt"

```txt
    Invitation has been rejected

```

=== "users/invitation_rejected_message.txt"

```txt
    Hello!

    The following invitation has been rejected.

    Full name: {{ invitation.full_name }}

    Target: {{ name }} {{ type }}

    Role: {{ role }}

```

=== "users/invitation_rejected_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Invitation to {{ name }} {{ type }}</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
      The following invitation has been rejected.
    </p>

    <p>
      Full name: {{ invitation.full_name }}
    </p>

    <p>
      Target: {{ name }} {{ type }}
    </p>

    <p>
      Role: {{ role }}
    </p>
    </body>
    </html>

```

### users.invitation_requested

A notification sent to staff users so that they can approve or reject invitation. The recipients are active staff users.

#### Templates

=== "users/invitation_requested_subject.txt"

```txt
    Invitation request

```

=== "users/invitation_requested_message.txt"

```txt
    Hello!

    {{ sender }} has created invitation request for the following user
    to join {{ name }} {{ type }} in {{ role }} role.

    {% if invitation.civil_number %}
    Civil number: {{ invitation.civil_number }}
    {% endif %}

    {% if invitation.phone_number %}
    Phone number: {{ invitation.phone_number }}
    {% endif %}

    E-mail: {{ invitation.email }}

    {% if invitation.full_name %}
    Full name: {{ invitation.full_name }}
    {% endif %}

    {% if invitation.native_name %}
    Native name: {{ invitation.native_name }}
    {% endif %}

    {% if invitation.organization %}
    Organization: {{ invitation.organization }}
    {% endif %}

    {% if invitation.job_title %}
    Job title: {{ invitation.job_title }}
    {% endif %}

    Please visit the link below to approve invitation: {{ approve_link }}

    Alternatively, you may reject invitation: {{ reject_link }}

```

=== "users/invitation_requested_message.html"

```txt
    <html>
    <head lang="en">
      <meta charset="UTF-8">
      <title>Invitation request</title>
    </head>
    <body>
    <p>
      Hello!
    </p>
    <p>
      {{ sender }} has created invitation request for the following user
      to join {{ name }} {{ type }} in {{ role }} role.
    </p>

    {% if invitation.civil_number %}
      <p>
        Civil number: {{ invitation.civil_number }}
      </p>
    {% endif %}

    {% if invitation.phone_number %}
      <p>
        Phone number: {{ invitation.phone_number }}
      </p>
    {% endif %}

    <p>
      E-mail: {{ invitation.email }}
    </p>

    {% if invitation.full_name %}
      <p>
        Full name: {{ invitation.full_name }}
      </p>
    {% endif %}

    {% if invitation.native_name %}
      <p>
        Native name: {{ invitation.native_name }}
      </p>
    {% endif %}

    {% if invitation.organization %}
      <p>
        Organization: {{ invitation.organization }}
      </p>
    {% endif %}

    {% if invitation.job_title %}
      <p>
        Job title: {{ invitation.job_title }}
      </p>
    {% endif %}

    <p>
      Please <a href="{{ approve_link }}">approve</a> or <a href="{{ reject_link }}">reject</a> invitation.
    </p>
    </body>
    </html>

```

### users.permission_request_submitted

A notification sent out to notify about submitted permission request. The recipients are active staff users or customer owners.

#### Templates

=== "users/permission_request_submitted_subject.txt"

```txt
    Permission request has been submitted.

```

=== "users/permission_request_submitted_message.txt"

```txt
    Hello!

    User {{ permission_request.created_by }} with email {{ permission_request.created_by.email }} created permission request for {{ permission_request.invitation }}.

    Please visit the link below to approve or reject permission request: {{ requests_link }}.

```

=== "users/permission_request_submitted_message.html"

```txt
    <html>
    <head lang="en">
      <meta charset="UTF-8">
      <title>Permission request has been submitted.</title>
    </head>
    <body>
    <p>
      Hello!
    </p>
    <p>
      User {{ permission_request.created_by }} with email {{ permission_request.created_by.email }} created permission request for {{ permission_request.invitation }}.
    </p>
    <p>
      Please visit the <a href="{{ requests_link }}">link</a> to approve or reject permission request.
    </p>
    </body>
    </html>

```

## WALDUR_MASTERMIND.BOOKING

### booking.notification

A notification sent out to notify about upcoming bookings. The recipients are users who have upcoming bookings.

#### Templates

=== "booking/notification_subject.txt"

```txt
    Reminder about upcoming booking.

```

=== "booking/notification_message.txt"

```txt
    Hello!

    Please do not forget about upcoming booking:
    {% for resource in resources %}
        {{ resource.name }}{% if not forloop.last %}, {% endif %}
    {% endfor %}.

```

=== "booking/notification_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Reminder about upcoming booking.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        Please do not forget about upcoming booking: <br />
        {% for resource in resources %}
            {{ resource.name }}
            {% if not forloop.last %}
                <br />
            {% endif %}
        {% endfor %}
    </p>
    </body>
    </html>

```

## WALDUR_MASTERMIND.INVOICES

### invoices.notification

A notification of invoice. The recipients are organization owners.

#### Templates

=== "invoices/notification_subject.txt"

```txt
    {{ customer }}'s invoice for {{ month }}/{{ year }}

```

=== "invoices/notification_message.txt"

```txt
    Hello,

    Please follow the link below to see {{ customer }}'s accounting information for {{ month }}/{{ year }}:
    {{ link }}

```

=== "invoices/notification_message.html"

```txt
    <html xmlns="http://www.w3.org/1999/html">
    <head lang="en">
        <meta charset="UTF-8">
        <title>{{ customer }}'s invoice for {{ month }}/{{ year }}</title>
    </head>
    <body>
    <p>
        Dear Sir or Madam,
    </p>
    <p>
        Attached is invoice for services consumed by {{ customer }}'s during {{ month }}/{{ year }}.
    </p>
    </body>
    </html>

```

### invoices.upcoming_ends_notification

A notification about upcoming contract ending. The recipients are organization owners.

#### Templates

=== "invoices/upcoming_ends_notification_subject.txt"

```txt
    {{ organization_name }}'s fixed price contract {{ contract_number }} is coming to an end

```

=== "invoices/upcoming_ends_notification_message.txt"

```txt
    Hello,

    this is a reminder that {{ organization_name }}'s fixed price contract {{ contract_number }} is ending on {{ end }}.

```

=== "invoices/upcoming_ends_notification_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>{{ organization_name }}'s fixed price contract {{ contract_number }} is coming to an end.</title>
    </head>
    <body>
    <p>
        Hello,
        <br/>
        this is a reminder that {{ organization_name }}'s fixed price contract {{ contract_number }} is ending on {{ end }}.
    </p>
    </body>
    </html>

```

## WALDUR_MASTERMIND.MARKETPLACE

### marketplace.marketplace_resource_create_failed

A notification of a failed resource creation

#### Templates

=== "marketplace/marketplace_resource_create_failed_subject.txt"

```txt
    Resource {{ resource_name }} creation has failed.

```

=== "marketplace/marketplace_resource_create_failed_message.txt"

```txt
    Hello!

    Resource {{ resource_name }} creation has failed.

```

=== "marketplace/marketplace_resource_create_failed_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Resource {{ resource_name }} creation has failed.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        Resource {{ resource_name }} creation has failed.
    </p>
    </body>
    </html>

```

### marketplace.marketplace_resource_create_succeeded

A notification of a successful resource creation

#### Templates

=== "marketplace/marketplace_resource_create_succeeded_subject.txt"

```txt
    Resource {{ resource_name }} has been created.

```

=== "marketplace/marketplace_resource_create_succeeded_message.txt"

```txt
    Hello!

    Resource {{ resource_name }} has been created.

```

=== "marketplace/marketplace_resource_create_succeeded_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Resource {{ resource_name }} has been created.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        Resource {{ resource_name }} has been created.
    </p>
    </body>
    </html>

```

### marketplace.marketplace_resource_terminate_failed

A notification of a failed resource termination

#### Templates

=== "marketplace/marketplace_resource_terminate_failed_subject.txt"

```txt
    Resource {{ resource_name }} deletion has failed.

```

=== "marketplace/marketplace_resource_terminate_failed_message.txt"

```txt
    Hello!

    Resource {{ resource_name }} deletion has failed.

```

=== "marketplace/marketplace_resource_terminate_failed_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Resource {{ resource_name }} deletion has failed.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        Resource {{ resource_name }} deletion has failed.
    </p>
    </body>
    </html>

```

### marketplace.marketplace_resource_terminate_succeeded

A notification of a successful resource termination

#### Templates

=== "marketplace/marketplace_resource_terminate_succeeded_subject.txt"

```txt
    Resource {{ resource_name }} has been deleted.

```

=== "marketplace/marketplace_resource_terminate_succeeded_message.txt"

```txt
    Hello!

    Resource {{ resource_name }} has been deleted.

```

=== "marketplace/marketplace_resource_terminate_succeeded_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Resource {{ resource_name }} has been deleted.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        Resource {{ resource_name }} has been deleted.
    </p>
    </body>
    </html>

```

### marketplace.marketplace_resource_termination_scheduled

A notification of a scheduled resource termination. The recipients are project administrators and managers

#### Templates

=== "marketplace/marketplace_resource_termination_scheduled_subject.txt"

```txt
    Resource {{ resource.name }} termination has been scheduled.

```

=== "marketplace/marketplace_resource_termination_scheduled_message.txt"

```txt
    Hello!

    The resource you have - {{ resource.name }} has not been used for the past 3 months. {{ user.full_name }} has scheduled termination of that resource on {{ resource.end_date|date:"SHORT_DATE_FORMAT" }}. If you feel that you still want to keep it, please remove the resource end date {{ resource_url }}.

```

=== "marketplace/marketplace_resource_termination_scheduled_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Resource {{ resource.name }} termination has been scheduled.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        The resource you have - <a href="{{ resource_url }}">{{ resource.name }}</a> has not been used for the past 3 months. {{ user.full_name }} has scheduled termination of that resource on {{ resource.end_date|date:"SHORT_DATE_FORMAT" }}.
        If you feel that you still want to keep it, please <a href="{{ resource_url }}"></a>remove the resource end date</a>.
    </p>
    </body>
    </html>

```

### marketplace.marketplace_resource_termination_scheduled_staff

A notification of a resource termination. The recipients are project administrators and managers.

#### Templates

=== "marketplace/marketplace_resource_termination_scheduled_staff_subject.txt"

```txt
    Resource {{ resource.name }} termination has been scheduled.

```

=== "marketplace/marketplace_resource_termination_scheduled_staff_message.txt"

```txt
    Hello!

    The resource you have - {{ resource.name }} has not been used for the past 3 months. {{ user.full_name }} has scheduled termination of that resource on {{ resource.end_date|date:"SHORT_DATE_FORMAT" }}. If you feel that you still want to keep it, please remove the resource end date {{ resource_url }}.

```

=== "marketplace/marketplace_resource_termination_scheduled_staff_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Resource {{ resource.name }} termination has been scheduled.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        The resource you have - <a href="{{ resource_url }}">{{ resource.name }}</a> has not been used for the past 3 months. {{ user.full_name }} has scheduled termination of that resource on {{ resource.end_date|date:"SHORT_DATE_FORMAT" }}.
        If you feel that you still want to keep it, please <a href="{{ resource_url }}"></a>remove the resource end date</a>.
    </p>
    </body>
    </html>

```

### marketplace.marketplace_resource_update_failed

A notification of failed resource update

#### Templates

=== "marketplace/marketplace_resource_update_failed_subject.txt"

```txt
    Resource {{ resource_name }} update has failed.

```

=== "marketplace/marketplace_resource_update_failed_message.txt"

```txt
    Hello!

    Resource {{ resource_name }} update has failed.

```

=== "marketplace/marketplace_resource_update_failed_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Resource {{ resource_name }} update has failed.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        Resource {{ resource_name }} update has failed.
    </p>
    </body>
    </html>

```

### marketplace.marketplace_resource_update_limits_failed

A notification of failed resource limits update

#### Templates

=== "marketplace/marketplace_resource_update_limits_failed_subject.txt"

```txt
    Resource {{ resource_name }} limits update has failed.

```

=== "marketplace/marketplace_resource_update_limits_failed_message.txt"

```txt
    Hello!

    Resource {{ resource_name }} limits update has failed.

```

=== "marketplace/marketplace_resource_update_limits_failed_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Resource {{ resource_name }} limits update has failed.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        Resource {{ resource_name }} limits update has failed.
    </p>
    </body>
    </html>

```

### marketplace.marketplace_resource_update_limits_succeeded

A notification of a successful resource limit update. The recipients are all the users in the project.

#### Templates

=== "marketplace/marketplace_resource_update_limits_succeeded_subject.txt"

```txt
    Resource {{ resource_name }} limits have been updated.

```

=== "marketplace/marketplace_resource_update_limits_succeeded_message.txt"

```txt
    Hello!

    Following request from {{ order_user }}, resource {{ resource_name }} limits have been updated from:
        {{ resource_old_limits }}
    to:
        {{ resource_limits }}.

    {% if support_email or support_phone %}
    If you have any additional questions, please contact support.
    {% if support_email %}
    Email: {{ support_email }}
    {% endif %}
    {% if support_phone %}
    Phone: {{ support_phone }}
    {% endif %}
    {% endif %}

```

=== "marketplace/marketplace_resource_update_limits_succeeded_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Resource {{ resource_name }} limits have been updated.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        Following request from {{ order_user }}, resource {{ resource_name }} limits have been updated from:<br>
        <blockquote>
            {{ resource_old_limits }}
        </blockquote>
        to:
        <blockquote>
            {{ resource_limits }}
        </blockquote>
    </p>
    {% if support_email or support_phone %}
    <p>
        If you have any additional questions, please contact support.
    </p>
    {% if support_email %}
    <p>
        Email: {{ support_email }}
    </p>
    {% endif %}
    {% if support_phone %}
    <p>
        Phone: {{ support_phone }}
    </p>
    {% endif %}
    {% endif %}
    </body>
    </html>

```

### marketplace.marketplace_resource_update_succeeded

A notification of a successful resource update. The recipients are all the users in the project.

#### Templates

=== "marketplace/marketplace_resource_update_succeeded_subject.txt"

```txt
    Resource {{ resource_name }} has been updated.

```

=== "marketplace/marketplace_resource_update_succeeded_message.txt"

```txt
    Hello!

    Following request from {{ order_user }}, resource {{ resource_name }} has been updated.

    {% if resource_old_plan %}
    The plan has been changed from {{ resource_old_plan }} to {{ resource_plan }}.
    {% endif %}

    {% if support_email or support_phone %}
    If you have any additional questions, please contact support.
    {% if support_email %}
    Email: {{ support_email }}
    {% endif %}
    {% if support_phone %}
    Phone: {{ support_phone }}
    {% endif %}
    {% endif %}

```

=== "marketplace/marketplace_resource_update_succeeded_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Resource {{ resource_name }} has been updated.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        Following request from {{ order_user }}, resource {{ resource_name }} has been updated.
    </p>
    {% if resource_old_plan %}
    <p>
        The plan has been changed from {{ resource_old_plan }} to {{ resource_plan }}.
    </p>
    {% endif %}
    {% if support_email or support_phone %}
    <p>
        If you have any additional questions, please contact support.
    </p>
    {% if support_email %}
    <p>
        Email: {{ support_email }}
    </p>
    {% endif %}
    {% if support_phone %}
    <p>
        Phone: {{ support_phone }}
    </p>
    {% endif %}
    {% endif %}
    </body>
    </html>

```

### marketplace.notification_about_project_ending

A notification about project ending. The recipients are project managers and customer owners.

#### Templates

=== "marketplace/notification_about_project_ending_subject.txt"

```txt
    {% if count_projects > 1 %}Your {{ count_projects }} projects{% else %} Project{% endif %} will be deleted on {{ end_date|date:'d/m/Y' }}.

```

=== "marketplace/notification_about_project_ending_message.txt"

```txt
    Hello {{ user.full_name }}!

    The following projects are ending {% if delta == 1 %} tomorrow {% else %} in {{ delta }} days{% endif %}:

    {% for project in projects %}
        - {{ project.name }} ({{ project.url }})
    {% endfor %}

    End of the project will lead to termination of all resources in the project.
    If you are aware of that, then no actions are needed from your side.
    If you need to update project end date, please update it in project details.

    Thank you!

```

=== "marketplace/notification_about_project_ending_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Projects will be deleted.</title>
    </head>
    <body>
    <p>Hello {{ user.full_name }}!</p>
    <p>The following projects are ending {% if delta == 1 %} tomorrow {% else %} in {{ delta }} days{% endif %}:</p>
    <ul>
    {% for project in projects %}
        <li><a href="{{ project.url }}">{{ project.name }}</a></li>
    {% endfor %}
    </ul>
    <p>
        End of the project will lead to termination of all resources in the project. <br />
        If you are aware of that, then no actions are needed from your side. <br />
        If you need to update project end date, please update it in project details.
    </p>
    <p>Thank you!</p>
    </body>
    </html>

```

### marketplace.notification_about_resource_ending

A notification about resource ending. The recipients are project managers and customer owners.

#### Templates

=== "marketplace/notification_about_resource_ending_subject.txt"

```txt
    Resource {{ resource.name }} will be deleted.

```

=== "marketplace/notification_about_resource_ending_message.txt"

```txt
    Dear {{ user.full_name }},

    Termination date of your {{ resource.name }} is approaching and it will be deleted{% if delta == 1 %} tomorrow {% else %} in {{ delta }} days{% endif %}.
    If you are aware of that, then no actions are needed from your side.
    If you need to update resource end date, please update it in resource details {{ resource_url }}.

    Thank you!

```

=== "marketplace/notification_about_resource_ending_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Resource {{ resource.name }} will be deleted.</title>
    </head>
    <body>
    <p>Dear {{ user.full_name }},</p>

    <p>
        Termination date of your {{ resource.name }} is approaching and it will be
        deleted{% if delta == 1 %} tomorrow {% else %} in {{ delta }} days{% endif %}.<br />
        If you are aware of that, then no actions are needed from your side. <br />
        If you need to update resource end date, please update it in resource details {{ resource_url }}.
    </p>

    <p>Thank you!</p>
    </body>
    </html>

```

### marketplace.notification_about_stale_resources

A notification about stale resources. The recipients are organization owners.

#### Templates

=== "marketplace/notification_about_stale_resources_subject.txt"

```txt
    Reminder about stale resources.

```

=== "marketplace/notification_about_stale_resources_message.txt"

```txt
    Hello!

    We noticed that you have stale resources that have not cost you anything for the last 3 months.
    Perhaps some of them are not needed any more?

    The resource names are:
    {% for resource in resources %}
        {{ resource.resource.name }} {{ resource.resource_url }}
    {% endfor %}
    Thank you!

```

=== "marketplace/notification_about_stale_resources_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Reminder about stale resources.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        We noticed that you have stale resources that have not cost you anything for the last 3 months. <br />
        Perhaps some of them are not needed any more?<br />

        The resource names are:
        <ul>
            {% for resource in resources %}
                <li><a href='{{ resource.resource_url }}'>{{ resource.resource.name }}</a></li>
            {% endfor %}
        </ul>
        Thank you!
    </p>
    </body>
    </html>

```

### marketplace.notification_to_user_that_order_been_rejected

Notification to user whose order been rejected.

#### Templates

=== "marketplace/notification_to_user_that_order_been_rejected_subject.txt"

```txt
    Your order to {{ order_type }} a resource {{ order.resource.name }} has been rejected.

```

=== "marketplace/notification_to_user_that_order_been_rejected_message.txt"

```txt
    Hello!

    Your order {{ link }} to {{ order_type }} a resource {{ order.resource.name }} has been rejected.

```

=== "marketplace/notification_to_user_that_order_been_rejected_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Your order has been rejected.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        Your <a href="{{ link }}">order</a> to {{ order_type }} a resource {{ order.resource.name }} has been rejected.
    </p>
    </body>
    </html>

```

### marketplace.notification_usages

A notification about usages. The recipients are organization owners.

#### Templates

=== "marketplace/notification_usages_subject.txt"

```txt
    Reminder about missing usage reports.

```

=== "marketplace/notification_usages_message.txt"

```txt
    Hello!

    Please do not forget to add usage for the resources you provide:
    {% regroup resources by offering as offering_list %}{% for offering in offering_list %}
    {{forloop.counter}}. {{ offering.grouper.name }}:{% for resource in offering.list %}
        - {{ resource.name }}
    {% endfor %}{% endfor %}
    You can submit resource usage via API or do it manually at {{ public_resources_url }}.

```

=== "marketplace/notification_usages_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Reminder about missing usage reports.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>Please do not forget to add usage for the resources you provide:</p>
    {% regroup resources by offering as offering_list %}

    <ol>
    {% for offering in offering_list %}
        <li>
            {{ offering.grouper.name }}:
            <ul>
                {% for resource in offering.list %}
                <li>{{ resource.name }}</li>
                {% endfor %}
            </ul>
        </li>
    {% endfor %}
    </ol>

    <p>
        You can submit resource usage via API or do it <a href='{{ public_resources_url }}'>manually</a>.
    </p>
    </body>
    </html>

```

### marketplace.notify_consumer_about_pending_order

A notification for consumer about pending order. The recipients are users that have permissions to approve the order.

#### Templates

=== "marketplace/notify_consumer_about_pending_order_subject.txt"

```txt
    A new order by {{ order.created_by.get_full_name }} is waiting for approval.

```

=== "marketplace/notify_consumer_about_pending_order_message.txt"

```txt
    Hello!

    A new order by {{ order.created_by.get_full_name }} is waiting for approval.

```

=== "marketplace/notify_consumer_about_pending_order_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>A new order by {{ order.created_by.get_full_name }} is waiting for approval.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        Please visit <a href="{{ order_link }}">{{ site_name }}</a> to find out more details.
    </p>
    </body>
    </html>

```

### marketplace.notify_provider_about_pending_order

A notification for provider about pending order. The recipients are users that have permissions to approve the order.

#### Templates

=== "marketplace/notify_provider_about_pending_order_subject.txt"

```txt
    A new order by {{ order.created_by.get_full_name }} is waiting for approval.

```

=== "marketplace/notify_provider_about_pending_order_message.txt"

```txt
    Hello!

    A new order by {{ order.created_by.get_full_name }} is waiting for approval.

```

=== "marketplace/notify_provider_about_pending_order_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>A new order by {{ order.created_by.get_full_name }} is waiting for approval.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        Please visit <a href="{{ order_url }}">{{ site_name }}</a> to find out more details.
    </p>
    </body>
    </html>

```

## WALDUR_MASTERMIND.MARKETPLACE_REMOTE

### marketplace_remote.notification_about_pending_project_updates

A notification about pending project updates. The recipients are customer owners

#### Templates

=== "marketplace_remote/notification_about_pending_project_updates_subject.txt"

```txt
    Reminder about pending project updates.

```

=== "marketplace_remote/notification_about_pending_project_updates_message.txt"

```txt
    Hello!

    We noticed that you have pending project update requests.
    Perhaps you would like to have a look at them?

    The project is:
        {{ project_update_request.project.name }} {{ project_url }}
    Thank you!

```

=== "marketplace_remote/notification_about_pending_project_updates_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Reminder about pending project updates.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        We noticed that you have pending project update requests.<br />
        Perhaps you would like to have a look at them?<br />

        The project is:
        <ul>
            <li><a href='{{ project_url }}'>{{ project_update_request.project.name }}</a></li>
        </ul>
        Thank you!
    </p>
    </body>
    </html>

```

### marketplace_remote.notification_about_project_details_update

A notification about project details update. The recipients the user who requested project details update and the user that reviewed it.

#### Templates

=== "marketplace_remote/notification_about_project_details_update_subject.txt"

```txt
    A notification about project details update.

```

=== "marketplace_remote/notification_about_project_details_update_message.txt"

```txt
    Hello!

    We would like to notify you about recent updates in project details.
    Perhaps you would like to have a look at them?

    The project is:
        {{ new_name }} {{ project_url }}

        Details after the update are below:
            {% if new_description %}
                Old description: {{ old_description }}
                New description: {{ new_description }}
            {% endif %}

            {% if new_name %}
                Old name: {{ old_name }}
                New name: {{ new_name }}
            {% endif %}

            {% if new_end_date %}
               Old end date: {{ old_end_date }}
               New end date: {{ new_end_date }}
            {% endif %}

            {% if new_oecd_fos_2007_code %}
               Old OECD FOS 2007 code: {{ old_oecd_fos_2007_code }}
               New OECD FOS 2007 code: {{ new_oecd_fos_2007_code }}
            {% endif %}

            {% if new_is_industry %}
               Old is_industry: {{ old_is_industry }}
               New is_industry: {{ new_is_industry }}
            {% endif %}

        Reviewed by: {{ reviewed_by }}
    Thank you!

```

=== "marketplace_remote/notification_about_project_details_update_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>A notification about project details update.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        We would like to notify you about recent updates in project details.<br />
        Perhaps you would like to have a look at them?<br />

        The project is:
        <ul>
            <li><a href='{{ project_url }}'>{{ new_name }}</a></li>
        </ul>

        <div>
            Details after the update are below:
            <ul>
                {% if new_description %}
                    <li>Old description: {{ old_description }}</li>
                    <li>New description: {{ new_description }}</li>
                {% endif %}

                {% if new_name %}
                    <li>Old name: {{ old_name }}</li>
                    <li>New name: {{ new_name }}</li>
                {% endif %}

                {% if new_end_date %}
                    <li>Old end date: {{ old_end_date }}</li>
                    <li>New end date: {{ new_end_date }}</li>
                {% endif %}

                {% if new_oecd_fos_2007_code %}
                    <li>Old OECD FOS 2007 code: {{ old_oecd_fos_2007_code }}</li>
                    <li>New OECD FOS 2007 code: {{ new_oecd_fos_2007_code }}</li>
                {% endif %}

                {% if new_is_industry %}
                    <li>Old is_industry: {{ old_is_industry }}</li>
                    <li>New is_industry: {{ new_is_industry }}</li>
                {% endif %}
                <li>Reviewed by: {{ reviewed_by }}</li>
            </ul>

        </div>
        Thank you!
    </p>
    </body>
    </html>

```

### marketplace_policy.notification_about_project_cost_exceeded_limit

Notification about project cost exceeded limit. The recipients are all customer owners of the project.

#### Templates

=== "marketplace_policy/notification_about_project_cost_exceeded_limit_subject.txt"

```txt
    {{ scope_class }} {{ scope_name }} cost has exceeded the limit.

```

=== "marketplace_policy/notification_about_project_cost_exceeded_limit_message.txt"

```txt
    Hello!
    {{ scope_class }} {{ scope_name }} ({{ scope_url }}) cost has exceeded the limit of {{ limit }}.

```

=== "marketplace_policy/notification_about_project_cost_exceeded_limit_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>{{ scope_class }} {{ scope_name }} cost has exceeded the limit.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        {{ scope_class }} <a href='{{ scope_url }}'>{{ scope_name }}</a> cost has exceeded the limit of {{ limit }}.
    </p>
    </body>
    </html>

```

## WALDUR_MASTERMIND.SUPPORT

### support.description

A notification used for issue creation.

#### Templates

=== "support/description.txt"

```txt
    {{issue.description}}

    Additional Info:
    {% if issue.customer %}- Organization: {{issue.customer.name}}{% endif %}
    {% if issue.project %}- Project: {{issue.project.name}}{% endif %}
    {% if issue.resource %}
        {% if issue.resource.service_settings %}
            {% if issue.resource.service_settings.type %}- Service type: {{issue.resource.service_settings.type}}{% endif %}
            - Offering name: {{ issue.resource.service_settings.name }}
            - Offering provided by: {{ issue.resource.service_settings.customer.name }}
        {% endif %}
        - Affected resource: {{issue.resource}}
        - Backend ID: {{issue.resource.backend_id}}
    {% endif %}
    - Site name: {{ settings.WALDUR_CORE.SITE_NAME }}
    - Site URL: {{ config.HOMEPORT_URL }}

```

### support.notification_comment_added

Notification about a new comment in the issue. The recipient is issue caller.

#### Templates

=== "support/notification_comment_added.txt"

```txt
    Hello!

    The issue you have created has a new comment. Please go to {{issue_url}} to see it.

```

=== "support/notification_comment_added.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>The issue you have created ({{ issue.key }}) has a new comment</title>
    </head>
    <body>
    <p>
        {% if is_system_comment %}
            Added a new comment.
        {% else %}
            {{ comment.author.name }} added a new comment.
        {% endif %}
    </p>
    <p>
        <a href="{{ issue_url }}">[{{ issue.key }}] {{ issue.summary }}</a>
    </p>
    <div>
        {{ description|safe }}
    </div>
    </body>
    </html>

```

=== "support/notification_comment_added_subject.txt"

```txt
    The issue ({{ issue.key }}) you have created has a new comment

```

### support.notification_comment_updated

Notification about an update in the issue comment. The recipient is issue caller.

#### Templates

=== "support/notification_comment_updated.txt"

```txt
    Hello!

    The comment has been updated. Please go to {{issue_url}} to see it.

```

=== "support/notification_comment_updated.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>The comment has been updated ({{ issue.key }})</title>
    </head>
    <body>
    <p>
        {{ comment.author.name }} updated comment.
    </p>
    <p>
        <a href="{{ issue_url }}">[{{ issue.key }}] {{ issue.summary }}</a>
    </p>
    <p>
        Old comment:
    </p>
    <p>
        {{ old_description|safe }}
    </p>
    <p>
        New comment:
    </p>
    <p>
        {{ description|safe }}
    </p>
    </body>
    </html>

```

=== "support/notification_comment_updated_subject.txt"

```txt
    Issue {{ issue.key }}. The comment has been updated

```

### support.notification_issue_feedback

Notification about a feedback related to the issue. The recipient is issue caller.

#### Templates

=== "support/notification_issue_feedback.txt"

```txt
    Hello, {{issue.caller.full_name}}!

    We would like to hear your feedback regarding your recent experience with support for {{issue_url}}.

    Click on the evaluations below to provide the feedback.

    {% for link in feedback_links%}
        {{link.label}}: {{link.link}}
    {% endfor %}

```

=== "support/notification_issue_feedback.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>The issue you have ({{ issue.key }}) has been updated</title>

        <style>
            * {
              font-family: sans-serif;
            }
            .rating {
              unicode-bidi: bidi-override;
              direction: rtl;
              width: 500px;
            }
            .rating > a {
              display: inline-block;
              position: relative;
              width: 1.1em;
              text-decoration: none;
              font-size: xx-large;
              color: rgba(180, 179, 178, 1);
            }
            .rating > a:hover:before,
            .rating > a:hover ~ a:before {
               content: "\2605";
               position: absolute;
               color: rgba(224, 194, 75, 1);
            }
        </style>

    </head>
    <body>
    <p>Hello, {{issue.caller.full_name}}!</p>
    <p>We would like to hear your feedback regarding your recent experience with support for
        <a href='{{issue_url}}'>{{ issue.summary }}</a>.
    </p>
    <p>Click the stars below to provide your feedback:</p>
    <div class="rating">
        {% for link in feedback_links reversed %}
            <a href='{{link.link}}'>☆</a>
        {% endfor %}
    </div>
    </body>
    </html>

```

=== "support/notification_issue_feedback_subject.txt"

```txt
    Please share your feedback: {{issue.key}} {{issue.summary}}

```

### support.notification_issue_updated

Notification about an update in the issue. The recipient is issue caller.

#### Templates

=== "support/notification_issue_updated.txt"

```txt
    Hello!

    The issue you have has been updated.

    {% if changed.status %}
    Status has been changed from {{ changed.status }} to {{ issue.status }}.
    {% endif %}
    {% if changed.description %}
    Description has been changed from {{ changed.description }} to {{ issue.description }}.
    {% endif %}
    {% if changed.summary %}
    Summary has been changed from {{ changed.summary }} to {{ issue.summary }}.
    {% endif %}
    {% if changed.priority %}
    Priority has been changed from {{ changed.priority }} to {{ issue.priority }}.
    {% endif %}

    Please go to {{issue_url}} to see it.

```

=== "support/notification_issue_updated.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>The issue you have ({{ issue.key }}) has been updated</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    {% if changed.status %}
    <p>
        Status has been changed from <strong>{{ changed.status }}</strong> to <strong>{{ issue.status }}</strong>.
    </p>
    {% endif %}
    {% if old_description %}
    <p>
        Description has been changed from <strong>{{ old_description|safe }}</strong> to <strong>{{ description|safe }}</strong>.
    </p>
    {% endif %}
    {% if changed.summary %}
    <p>
        Summary has been changed from <strong>{{ changed.summary }}</strong> to <strong>{{ issue.summary }}</strong>.
    </p>
    {% endif %}
    {% if changed.priority %}
    <p>
        Priority has been changed from <strong>{{ changed.priority }}</strong> to <strong>{{ issue.priority }}</strong>.
    </p>
    {% endif %}
    <p>
        Please visit <a href="{{ issue_url }}">{{ site_name }}</a> to find out more details.
    </p>
    </body>
    </html>

```

=== "support/notification_issue_updated_subject.txt"

```txt
    Updated issue: {{issue.key}} {{issue.summary}}

```

### support.summary

A notification used for issue creation.

#### Templates

=== "support/summary.txt"

```txt
    {% if issue.customer.abbreviation %}{{issue.customer.abbreviation}}: {% endif %}{{issue.summary}}

```

## WALDUR_MASTERMIND.PROPOSAL

### proposal.proposal_state_changed

A notification about the proposal state changes (submitted → in review → accepted/rejected).

#### Templates

=== "proposal/proposal_state_changed_message.txt"

```txt
    Dear {{ proposal_creator_name }},

    The state of your proposal "{{ proposal_name }}" in call "{{ call_name }}" has been updated.

    State change:
    - Previous state: {{ previous_state }}
    - New state: {{ new_state }}
    - Updated on: {{ update_date }}

    {% if new_state == 'accepted' %}
    Project created: {{ project_name }}
    Allocation start date: {{ allocation_date }}
    Duration: {{ duration }} days
    {% endif %}

    {% if new_state == 'rejected' %}
    Feedback: {{ rejection_feedback }}
    {% endif %}

    {% if new_state == 'submitted' %}
    Your proposal has been successfully submitted and will be reviewed according to the review process for this call. You will receive further notifications as your proposal progresses through the review process.
    {% endif %}

    {% if new_state == 'in_review' %}
    Your proposal is now under review. Reviewers will evaluate your proposal based on the criteria specified in the call. This process may take {{ review_period }} days according to the round's review period.
    {% endif %}

    {% if new_state == 'accepted' %}
    Congratulations! Your proposal has been accepted. Resources have been allocated based on your request and a new project has been created. You can access your project by clicking the link below.
    {% endif %}

    {% if new_state == 'rejected' %}
    We regret to inform you that your proposal has not been accepted at this time. Please review any feedback provided above. You may have the opportunity to submit a revised proposal in future rounds.
    {% endif %}

    View Proposal: {{ proposal_url }}
    {% if new_state == 'accepted' and project_url %}
    View Project: {{ project_url }}
    {% endif %}

    This is an automated message from the {{ site_name }}. Please do not reply to this email.

```

=== "proposal/proposal_state_changed_message.html"

```txt
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Proposal Status Update</title>
        <style>
            body {
                color: #333;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }
            .header {
                margin-bottom: 20px;
            }
            .state-change {
                background-color: #f9f9f9;
                padding: 15px;
                border-radius: 5px;
                margin-bottom: 20px;
            }
            .message-box {
                padding: 15px;
                margin: 15px 0;
            }
            .footer {
                margin-top: 30px;
                color: #777;
                border-top: 1px solid #eee;
                padding-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <p>Dear {{ proposal_creator_name }},</p>
            <p>The state of your proposal "<strong>{{ proposal_name }}</strong>" in call "<strong>{{ call_name }}</strong>" has been updated.</p>
        </div>

        <div class="state-change">
            <h3>State change:</h3>
            <ul>
                <li><strong>Previous state:</strong> {{ previous_state }}</li>
                <li><strong>New state:</strong> {{ new_state }}</li>
                <li><strong>Updated on:</strong> {{ update_date }}</li>
            </ul>

            {% if new_state == 'accepted' %}
            <ul>
                <li><strong>Project created:</strong> {{ project_name }}</li>
                <li><strong>Allocation start date:</strong> {{ allocation_date }}</li>
                <li><strong>Duration:</strong> {{ duration }} days</li>
            </ul>
            {% endif %}

            {% if new_state == 'rejected' %}
            <p><strong>Feedback:</strong> {{ rejection_feedback }}</p>
            {% endif %}
        </div>

        <div class="message-box">
            {% if new_state == 'submitted' %}
            <p>Your proposal has been successfully submitted and will be reviewed according to the review process for this call. You will receive further notifications as your proposal progresses through the review process.</p>
            {% endif %}

            {% if new_state == 'in_review' %}
            <p>Your proposal is now under review. Reviewers will evaluate your proposal based on the criteria specified in the call. This process may take {{ review_period }} days according to the round's review period.</p>
            {% endif %}

            {% if new_state == 'accepted' %}
            <p>Congratulations! Your proposal has been accepted. Resources have been allocated based on your request and a new project has been created. You can access your project by clicking the link below.</p>
            {% endif %}

            {% if new_state == 'rejected' %}
            <p>We regret to inform you that your proposal has not been accepted at this time. Please review any feedback provided above. You may have the opportunity to submit a revised proposal in future rounds.</p>
            {% endif %}
        </div>

        <a href="{{ proposal_url }}">View Proposal</a>
        <br>
        {% if new_state == 'accepted' and project_url %}
        <a href="{{ project_url }}">View Project</a>
        {% endif %}

        <div class="footer">
            <p>This is an automated message from the {{ site_name }}. Please do not reply to this email.</p>
        </div>
    </body>
    </html>

```

=== "proposal/proposal_state_changed_subject.txt"

```txt
    Proposal state update: {{ proposal_name }} - {{ new_state }}

```

