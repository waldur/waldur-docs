# Notifications

## WALDUR_CORE.STRUCTURE

### structure.change_email_request

A notification of an email change request

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

A notification of changing a profile

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

A notification of a granted role

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

A notification of invitation approval

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

A notification of invitation creation

#### Templates

=== "users/invitation_created_subject.txt"

```txt
    Invitation to {{ name }} {{ type }}

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

### users.invitation_rejected

A notification of invitation rejection

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

A notification of invitation request

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

    {% if invitation.tax_number %}
    Tax number: {{ invitation.tax_number }}
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

    {% if invitation.tax_number %}
      <p>
        Tax number: {{ invitation.tax_number }}
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

A notification of a submitted invitation request

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

A notification about upcoming bookings

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

A notification of invoice

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

A notification about upcoming ends

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

A notification of a scheduled resource termination

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

A notification of a resource termination

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

A notification of a successful resource limit update

#### Templates

=== "marketplace/marketplace_resource_update_limits_succeeded_subject.txt"

```txt
    Resource {{ resource_name }} limits have been updated.

```

=== "marketplace/marketplace_resource_update_limits_succeeded_message.txt"

```txt
    Hello!

    Following request from {{ order_item_user }}, resource {{ resource_name }} limits have been updated from:
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
        Following request from {{ order_item_user }}, resource {{ resource_name }} limits have been updated from:<br>
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

A notification of a successful resource update

#### Templates

=== "marketplace/marketplace_resource_update_succeeded_subject.txt"

```txt
    Resource {{ resource_name }} has been updated.

```

=== "marketplace/marketplace_resource_update_succeeded_message.txt"

```txt
    Hello!

    Following request from {{ order_item_user }}, resource {{ resource_name }} has been updated.

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
        Following request from {{ order_item_user }}, resource {{ resource_name }} has been updated.
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

A notification about project ending

#### Templates

=== "marketplace/notification_about_project_ending_subject.txt"

```txt
    Project {{ project.name }} will be deleted.

```

=== "marketplace/notification_about_project_ending_message.txt"

```txt
    Dear {{ user.full_name }},

    Your project {{ project.name }} is ending {% if delta == 1 %} tomorrow {% else %} in {{ delta }} days{% endif %}. End of the project will lead to termination of all resources in the project.
    If you are aware of that, then no actions are needed from your side.
    If you need to update project end date, please update it in project details {{ project_url }}.

    Thank you!

```

=== "marketplace/notification_about_project_ending_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Project {{ project.name }} will be deleted.</title>
    </head>
    <body>
    <p>Dear {{ user.full_name }},</p>

    <p>Your project {{ project.name }} is ending
        {% if delta == 1 %} tomorrow {% else %} in {{ delta }} days{% endif %}.
        End of the project will lead to termination of all resources in the project. <br />
        If you are aware of that, then no actions are needed from your side. <br />
        If you need to update project end date, please update it in project details {{ project_url }}.
    </p>

    <p>Thank you!</p>
    </body>
    </html>

```

### marketplace.notification_about_stale_resources

A notification about stale resources

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

### marketplace.notification_approval

A notification of order approval

#### Templates

=== "marketplace/notification_approval_subject.txt"

```txt
    A new order by {{ order.created_by.get_full_name }} is waiting for approval.

```

=== "marketplace/notification_approval_message.txt"

```txt
    Hello!

    A new order by {{ order.created_by.get_full_name }} is waiting for approval.

```

=== "marketplace/notification_approval_message.html"

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

### marketplace.notification_service_provider_approval

A notification to provider about pending order item approval

#### Templates

=== "marketplace/notification_service_provider_approval_subject.txt"

```txt
    A new order by {{ order.created_by.get_full_name }} is waiting for approval.

```

=== "marketplace/notification_service_provider_approval_message.txt"

```txt
    Hello!

    A new order by {{ order.created_by.get_full_name }} is waiting for approval.

```

=== "marketplace/notification_service_provider_approval_message.html"

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
        Please visit <a href="{{ order_item_url }}">{{ site_name }}</a> to find out more details.
    </p>
    </body>
    </html>

```

### marketplace.notification_usages

A notification about usages

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

## WALDUR_MASTERMIND.MARKETPLACE_FLOWS

### marketplace_flows.flow_rejected

A notification for a rejected marketplace flow

#### Templates

=== "marketplace_flows/flow_rejected_subject.txt"

```txt
    {% load i18n %}
    {% trans 'Your submission has been rejected' %}

```

=== "marketplace_flows/flow_rejected_message.txt"

```txt
    {% load i18n %}

    {% if flow.customer_create_request.is_rejected %}
    {% trans 'Customer creation request has been rejected.' %}

    {% if flow.customer_create_request.reviewed_by %}
    {% trans 'Reviewer name:' %} {{ flow.customer_create_request.reviewed_by.full_name }}
    {% endif %}

    {% if flow.customer_create_request.reviewed_at %}
    {% trans 'Reviewed at:' %}
    {{ flow.customer_create_request.reviewed_at|date:"SHORT_DATE_FORMAT" }}
    {{ flow.customer_create_request.reviewed_at|time:"H:i" }}
    {% endif %}

    {% if flow.customer_create_request.review_comment %}
    {% trans 'Comment:' %} {{ flow.customer_create_request.review_comment }}
    {% endif %}
    {% endif %}


    {% if flow.project_create_request.is_rejected %}
    {% trans 'Project creation request has been rejected.' %}

    {% if flow.project_create_request.reviewed_by %}
    {% trans 'Reviewer name:' %} {{ flow.project_create_request.reviewed_by.full_name }}
    {% endif %}

    {% if flow.project_create_request.reviewed_at %}
    {% trans 'Reviewed at:' %}
    {{ flow.project_create_request.reviewed_at|date:"SHORT_DATE_FORMAT" }}
    {{ flow.project_create_request.reviewed_at|time:"H:i" }}
    {% endif %}

    {% if flow.project_create_request.review_comment %}
    {% trans 'Comment:' %} {{ flow.project_create_request.review_comment }}
    {% endif %}
    {% endif %}

    {% if flow.resource_create_request.is_rejected %}
    {% trans 'Resource creation request has been rejected.' %}

    {% if flow.resource_create_request.reviewed_by %}
    {% trans 'Reviewer name:' %} {{ flow.resource_create_request.reviewed_by.full_name }}
    {% endif %}

    {% if flow.resource_create_request.reviewed_at %}
    {% trans 'Reviewed at:' %}
    {{ flow.resource_create_request.reviewed_at|date:"SHORT_DATE_FORMAT" }}
    {{ flow.resource_create_request.reviewed_at|time:"H:i" }}
    {% endif %}

    {% if flow.resource_create_request.review_comment %}
    {% trans 'Comment:' %} {{ flow.resource_create_request.review_comment }}
    {% endif %}
    {% endif %}

```

=== "marketplace_flows/flow_rejected_message.html"

```txt
    {% load i18n %}
    {% if flow.customer_create_request.is_rejected %}
    <p>{% trans 'Customer creation request has been rejected.' %}</p>

    {% if flow.customer_create_request.reviewed_by %}
    <p><b>{% trans 'Reviewer name:' %}</b> {{ flow.customer_create_request.reviewed_by.full_name }}</p>
    {% endif %}

    {% if flow.customer_create_request.reviewed_at %}
    <p><b>{% trans 'Reviewed at:' %}</b>
    {{ flow.customer_create_request.reviewed_at|date:"SHORT_DATE_FORMAT" }}
    {{ flow.customer_create_request.reviewed_at|time:"H:i" }}</p>
    {% endif %}

    {% if flow.customer_create_request.review_comment %}
    <p><b>{% trans 'Comment:' %}</b> {{ flow.customer_create_request.review_comment }}</p>
    {% endif %}
    {% endif %}


    {% if flow.project_create_request.is_rejected %}
    <p>{% trans 'Project creation request has been rejected.' %}</p>

    {% if flow.project_create_request.reviewed_by %}
    <p><b>{% trans 'Reviewer name:' %}</b> {{ flow.project_create_request.reviewed_by.full_name }}</p>
    {% endif %}

    {% if flow.project_create_request.reviewed_at %}
    <p><b>{% trans 'Reviewed at:' %}</b>
    {{ flow.project_create_request.reviewed_at|date:"SHORT_DATE_FORMAT" }}
    {{ flow.project_create_request.reviewed_at|time:"H:i" }}</p>
    {% endif %}

    {% if flow.project_create_request.review_comment %}
    <p><b>{% trans 'Comment:' %}</b> {{ flow.project_create_request.review_comment }}</p>
    {% endif %}
    {% endif %}

    {% if flow.resource_create_request.is_rejected %}
    <p>{% trans 'Resource creation request has been rejected.' %}</p>

    {% if flow.resource_create_request.reviewed_by %}
    <p><b>{% trans 'Reviewer name:' %}</b> {{ flow.resource_create_request.reviewed_by.full_name }}</p>
    {% endif %}

    {% if flow.resource_create_request.reviewed_at %}
    <p><b>{% trans 'Reviewed at:' %}</b>
    {{ flow.resource_create_request.reviewed_at|date:"SHORT_DATE_FORMAT" }}
    {{ flow.resource_create_request.reviewed_at|time:"H:i" }}</p>
    {% endif %}

    {% if flow.resource_create_request.review_comment %}
    <p><b>{% trans 'Comment:' %}</b> {{ flow.resource_create_request.review_comment }}</p>
    {% endif %}
    {% endif %}

```

### marketplace_flows.flow_submitted

A notification for a submitted marketplace flow

#### Templates

=== "marketplace_flows/flow_submitted_subject.txt"

```txt
    {% load i18n %}
    {% trans 'Resource creation request has been submitted' %}

```

=== "marketplace_flows/flow_submitted_message.txt"

```txt
    {% load i18n %}
    {% load waldur_core %}

    {% trans 'Resource creation request has been submitted.' %}

    It has been requested by user {{ flow.requested_by.full_name }} with email {{ flow.requested_by.email }}.

    {% if flow.customer_create_request %}
    {% trans 'Customer create request details are:' %}

    * {% trans 'Organization name' %}: {{ flow.customer_create_request.name }}

    {% if flow.customer_create_request.native_name %}
    * {% trans 'Organization native name' %}: {{ flow.customer_create_request.native_name }}
    {% endif %}

    {% if flow.customer_create_request.abbreviation %}
    * {% trans 'Organization abbreviation' %}: {{ flow.customer_create_request.abbreviation }}
    {% endif %}

    {% if flow.customer_create_request.contact_details %}
    * {% trans 'Contact details' %}: {{ flow.customer_create_request.contact_details }}
    {% endif %}

    {% if flow.customer_create_request.agreement_number %}
    * {% trans 'Contact details' %}: {{ flow.customer_create_request.agreement_number }}
    {% endif %}

    {% if flow.customer_create_request.sponsor_number %}
    * {% trans 'External ID of the sponsor covering the costs' %}: {{ flow.customer_create_request.sponsor_number }}
    {% endif %}

    {% if flow.customer_create_request.email %}
    * {% trans 'Email address' %}: {{ flow.customer_create_request.email }}
    {% endif %}

    {% if flow.customer_create_request.phone_number %}
    * {% trans 'Phone number' %}: {{ flow.customer_create_request.phone_number }}
    {% endif %}

    {% if flow.customer_create_request.access_subnets %}
    * {% trans 'List of IPv4 or IPv6 CIDR addresses from where connection to self-service is allowed' %}: {{ flow.customer_create_request.access_subnets }}
    {% endif %}

    {% if flow.customer_create_request.registration_code %}
    * {% trans 'Registration code' %}: {{ flow.customer_create_request.registration_code }}
    {% endif %}

    {% if flow.customer_create_request.homepage %}
    * {% trans 'Homepage URL' %}: {{ flow.customer_create_request.homepage }}
    {% endif %}

    {% if flow.customer_create_request.domain %}
    * {% trans 'Organization domain' %}: {{ flow.customer_create_request.domain }}
    {% endif %}

    {% if flow.customer_create_request.address %}
    * {% trans 'Legal address' %}: {{ flow.customer_create_request.address }}
    {% endif %}

    {% if flow.customer_create_request.postal %}
    * {% trans 'Postal code' %}: {{ flow.customer_create_request.postal }}
    {% endif %}

    {% if flow.customer_create_request.bank_name %}
    * {% trans 'Bank name (for accounting)' %}: {{ flow.customer_create_request.bank_name }}
    {% endif %}

    {% if flow.customer_create_request.bank_account %}
    * {% trans 'Bank account number' %}: {{ flow.customer_create_request.bank_account }}
    {% endif %}

    {% else %}
    {% trans 'Organization name' %}: {{ flow.customer.name }}

    {% endif %}

    {% trans 'Project create request details are:' %}

    * {% trans 'Name' %}: {{ flow.project_create_request.name }}

    {% if flow.project_create_request.description %}
    * {% trans 'Description' %}: {{ flow.project_create_request.description }}
    {% endif %}

    {% if flow.project_create_request.end_date %}
    * {% trans 'End date' %}: {{ flow.project_create_request.end_date }}
    {% endif %}

    {% trans 'Resource create request details are:' %}

    * {% trans 'Name' %}: {{ flow.resource_create_request.name }}

    {% if flow.resource_create_request.description %}
    * {% trans 'Description' %}: {{ flow.resource_create_request.description }}
    {% endif %}

    {% if flow.resource_create_request.end_date %}
    * {% trans 'End date' %}: {{ flow.resource_create_request.end_date }}
    {% endif %}

    * {% trans 'Offering name' %}: {{ flow.resource_create_request.offering.name }}

    * {% trans 'Offering category' %}: {{ flow.resource_create_request.offering.category.title }}

    {% if flow.resource_create_request.plan %}
    * {% trans 'Plan' %}: {{ flow.resource_create_request.plan.name }}
    {% endif %}

    {% if flow.resource_create_request.attributes %}
    * {% trans 'Attributes' %}:

    {% for key, value in flow.resource_create_request.attributes.items|dictsort:"0.lower" %}
    {{ key }}: {{ value | pretty_json }}
    {% endfor %}

    {% endif %}

    {% if flow.resource_create_request.limits %}
    * {% trans 'Limits' %}:

    {% for key, value in flow.resource_create_request.limits.items|dictsort:"0.lower" %}
    {{ key }}: {{ value }}
    {% endfor %}

    {% endif %}

```

=== "marketplace_flows/flow_submitted_message.html"

```txt
    {% load i18n %}
    {% load waldur_core %}

    <!DOCTYPE html>
    <html>

    <head>
      <meta charset="utf-8">
      <title>{% trans "Resource creation request details" %}</title>
    </head>
    <body>
    <p>It has been requested by user {{ flow.requested_by.full_name }} with email {{ flow.requested_by.email }}.</p>

    {% if flow.customer_create_request %}
    <h1>{% trans 'Customer create request details' %}</h1>

    <ul>
        <li><b>{% trans 'Organization name' %}</b>: {{ flow.customer_create_request.name }}</li>

    {% if flow.customer_create_request.native_name %}
        <li><b>{% trans 'Organization native name' %}</b>: {{ flow.customer_create_request.native_name }}</li>
    {% endif %}

    {% if flow.customer_create_request.abbreviation %}
        <li><b>{% trans 'Organization abbreviation' %}</b>: {{ flow.customer_create_request.abbreviation }}</li>
    {% endif %}

    {% if flow.customer_create_request.contact_details %}
        <li><b>{% trans 'Contact details' %}: {{ flow.customer_create_request.contact_details }}</b></li>
    {% endif %}

    {% if flow.customer_create_request.agreement_number %}
        <li><b>{% trans 'Contact details' %}: {{ flow.customer_create_request.agreement_number }}</b></li>
    {% endif %}

    {% if flow.customer_create_request.sponsor_number %}
        <li><b>{% trans 'External ID of the sponsor covering the costs' %}: {{ flow.customer_create_request.sponsor_number }}</b></li>
    {% endif %}

    {% if flow.customer_create_request.email %}
        <li><b>{% trans 'Email address' %}: {{ flow.customer_create_request.email }}</b></li>
    {% endif %}

    {% if flow.customer_create_request.phone_number %}
        <li><b>{% trans 'Phone number' %}: {{ flow.customer_create_request.phone_number }}</b></li>
    {% endif %}

    {% if flow.customer_create_request.access_subnets %}
        <li><b>{% trans 'List of IPv4 or IPv6 CIDR addresses from where connection to self-service is allowed' %}: {{ flow.customer_create_request.access_subnets }}</b></li>
    {% endif %}

    {% if flow.customer_create_request.registration_code %}
        <li><b>{% trans 'Registration code' %}: {{ flow.customer_create_request.registration_code }}</b></li>
    {% endif %}

    {% if flow.customer_create_request.homepage %}
        <li><b>{% trans 'Homepage URL' %}: {{ flow.customer_create_request.homepage }}</b></li>
    {% endif %}

    {% if flow.customer_create_request.domain %}
        <li><b>{% trans 'Organization domain' %}: {{ flow.customer_create_request.domain }}</b></li>
    {% endif %}

    {% if flow.customer_create_request.address %}
        <li><b>{% trans 'Legal address' %}: {{ flow.customer_create_request.address }}</b></li>
    {% endif %}

    {% if flow.customer_create_request.postal %}
        <li><b>{% trans 'Postal code' %}: {{ flow.customer_create_request.postal }}</b></li>
    {% endif %}

    {% if flow.customer_create_request.bank_name %}
        <li><b>{% trans 'Bank name (for accounting)' %}: {{ flow.customer_create_request.bank_name }}</b></li>
    {% endif %}

    {% if flow.customer_create_request.bank_account %}
        <li><b>{% trans 'Bank account number' %}: {{ flow.customer_create_request.bank_account }}</b></li>
    {% endif %}
    </ul>
    {% else %}
    <b>{% trans 'Organization name' %}</b>: {{ flow.customer.name }}
    {% endif %}

    <h1>{% trans 'Project create request details' %}</h1>

    <ul>
    <li><b>{% trans 'Name' %}: {{ flow.project_create_request.name }}</b></li>

    {% if flow.project_create_request.description %}
    <li><b>{% trans 'Description' %}: {{ flow.project_create_request.description }}</b></li>
    {% endif %}

    {% if flow.project_create_request.end_date %}
    <li><b>{% trans 'End date' %}: {{ flow.project_create_request.end_date }}</b></li>
    {% endif %}
    </ul>

    <h1>{% trans 'Resource create request details' %}</h1>

    <ul>
    <li><b>{% trans 'Name' %}: {{ flow.resource_create_request.name }}</b></li>

    {% if flow.resource_create_request.description %}
    <li><b>{% trans 'Description' %}: {{ flow.resource_create_request.description }}</b></li>
    {% endif %}

    {% if flow.resource_create_request.end_date %}
    <li><b>{% trans 'End date' %}: {{ flow.resource_create_request.end_date }}</b></li>
    {% endif %}

    <li><b>{% trans 'Offering name' %}: {{ flow.resource_create_request.offering.name }}</b></li>

    <li><b>{% trans 'Offering category' %}: {{ flow.resource_create_request.offering.category.title }}</b></li>

    {% if flow.resource_create_request.plan %}
    <li><b>{% trans 'Plan' %}: {{ flow.resource_create_request.plan.name }}</b></li>
    {% endif %}

    {% if flow.resource_create_request.attributes %}
    <li><b>{% trans 'Attributes' %}</b>:

    <table border="0" cellspacing="0" cellpadding="0">
    <tr>
      <th>#</th>
      <th>{% trans "NAME" %}</th>
      <th>{% trans "VALUE" %}</th>
    </tr>
    {% for key, value in flow.resource_create_request.attributes.items|dictsort:"0.lower" %}
      <tr>
        <td>{{ forloop.counter }}</td>
        <td>{{ key }}</td>
        <td>{{ value | pretty_json }}</td>
      </tr>
    {% endfor %}
    </table>
    </li>
    {% endif %}

    {% if flow.resource_create_request.limits %}
    <li><b>{% trans 'Limits' %}</b>:
    <table border="0" cellspacing="0" cellpadding="0">
    <tr>
      <th>#</th>
      <th>{% trans "NAME" %}</th>
      <th>{% trans "VALUE" %}</th>
    </tr>
    {% for key, value in flow.resource_create_request.limits.items|dictsort:"0.lower" %}
      <tr>
        <td>{{ forloop.counter }}</td>
        <td>{{ key }}</td>
        <td>{{ value }}</td>
      </tr>
    {% endfor %}
    </table>
    </li>
    {% endif %}
    </ul>
    </body>
    </html>

```

## WALDUR_RANCHER

### rancher.notification_create_user

A notification for created rancher user

#### Templates

=== "rancher/notification_create_user_subject.txt"

```txt
    New account has been created.

```

=== "rancher/notification_create_user_message.txt"

```txt
    Hello!

    User with login {{ user.username }} and temporary password {{ password }} has been created.
    Please go to management console {{ rancher_url }} to change the password.

```

=== "rancher/notification_create_user_message.html"

```txt
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>A new user account has been created for you.</title>
    </head>
    <body>
    <p>
        Hello!
    </p>
    <p>
        User with login {{ user.username }} and temporary password {{ password }} has been created.<br />
        Please go to <a href="{{ rancher_url }}">management console</a> to change the password.
    </p>
    </body>
    </html>

```

## WALDUR_MASTERMIND.MARKETPLACE_REMOTE

### marketplace_remote.notification_about_pending_project_updates

A notification about pending project updates

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

