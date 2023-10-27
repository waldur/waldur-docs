# Message templates

## waldur_core.logging

### email.html (waldur_core.logging)

``` html
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>Notifications from waldur_core</title>
</head>
<body>
<ul>
    {% for event in events %}
    <li>
        {{ event.message }}
        <div>{{ event.created|date:"M d H:i e"}}</div>
    </li>
    {% endfor %}
</ul>
</body>
</html>
```

## waldur_core.permissions

## waldur_core.structure

### notifications_profile_changes_operator_subject.txt (waldur_core.structure)

``` txt
Owner details have been updated
```

### notifications_profile_changes.html (waldur_core.structure)

``` html
User {{user.full_name}} (id={{ user.id }}) profile has been updated:

{% for f in fields %}
    {{ f.name }} from {{ f.old_value }} to {{ f.new_value }}{% if not forloop.last %}, {% else %}.{% endif %}
{% endfor %}
```

### change_email_request_subject.txt (waldur_core.structure)

``` txt
Verify new email address.
```

### notifications_profile_changes_operator_message.html (waldur_core.structure)

``` html
Owner of
{% for o in organizations %}
    {{ o.name }} {% if o.abbreviation %} ({{ o.abbreviation }}){% endif %}{% if not forloop.last %}, {% endif %}
{% endfor %}

{{user.full_name}} (id={{ user.id }}) has changed

{% for f in fields %}
    {{ f.name }} from {{ f.old_value }} to {{ f.new_value }}{% if not forloop.last %}, {% else %}.{% endif %}
{% endfor %}
```

### structure_role_granted_message.txt (waldur_core.structure)

``` txt
Role {{ permission.role }}  for {{ structure }} has been granted.
```

### structure_role_granted_subject.txt (waldur_core.structure)

``` txt
Role granted.
```

### change_email_request_message.html (waldur_core.structure)

``` html
<p>To confirm the change of email address from {{ request.user.email }} to {{ request.email }}, follow the <a href="{{ link }}">link</a>.</p>
```

### change_email_request_message.txt (waldur_core.structure)

``` txt
To confirm the change of email address from {{ request.user.email }} to {{ request.email }}, follow the {{ link }}.
```

### notifications_profile_changes_operator_message.txt (waldur_core.structure)

``` txt
Owner of
{% for o in organizations %}
    {{ o.name }} {% if o.abbreviation %} ({{ o.abbreviation }}){% endif %}{% if not forloop.last %}, {% endif %}
{% endfor %}

{{user.full_name}} (id={{ user.id }}) has changed

{% for f in fields %}
    {{ f.name }} from {{ f.old_value }} to {{ f.new_value }}{% if not forloop.last %}, {% else %}.{% endif %}
{% endfor %}
```

### service_settings_description.html (waldur_core.structure)

``` html
{% for name, service in services %}
    <div id="id_{{ name }}" class="service-fields">
    <h4>{{ name }}</h4>

    {% if service.fields.items %}
        <p>Fields:</p>
        <ul>
            {% for name, field in service.fields.items %}
                <li>
                    <code>{{ name }}</code>
                    {% if field.label or field.help_text %} — {% endif %}
                    {% if field.label %} {{ field.label }} {% endif %}
                    {% if field.help_text %} {{ field.help_text }} {% endif %}
                </li>
            {% endfor %}
        </ul>
    {% endif %}

    {% if service.extra_fields.items %}
        <p>Options:</p>
        <ul>
            {% for name, field in service.extra_fields.items %}
                <li>
                    <code>{{ name }}</code>
                    {% if field.label or field.help_text %} — {% endif %}
                    {% if not field.required %} (optional) {% endif %}
                    {% if field.label %} {{ field.label }} {% endif %}
                    {% if field.help_text %} {{ field.help_text }} {% endif %}
                </li>
            {% endfor %}
        </ul>
    {% endif %}
    </div>
{% endfor %}
```

### structure_role_granted_message.html (waldur_core.structure)

``` html
<p>Role {{ permission.role }}  for {{ structure }} has been granted.</p>
```

## waldur_core.users

### invitation_approved_subject.txt (waldur_core.users)

``` txt
Account has been created
```

### invitation_created_message.html (waldur_core.users)

``` html
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

### permission_request_submitted_message.html (waldur_core.users)

``` html
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

### invitation_approved_message.txt (waldur_core.users)

``` txt
Hello!

{{ sender }} has invited you to join {{ name }} {{ type }} in {{ role }} role.
Please visit the link below to sign up and accept your invitation:
{{ link }}

Your credentials are as following.

Username is {{ username }}

Your password is {{ password }}
```

### invitation_created_message.txt (waldur_core.users)

``` txt
Hello!

{{ sender }} has invited you to join {{ name }} {{ type }} in {{ role }} role.
Please visit the link below to sign up and accept your invitation:
{{ link }}
{{ extra_invitation_text }}
```

### invitation_expired_message.html (waldur_core.users)

``` html
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

### invitation_approved_message.html (waldur_core.users)

``` html
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

### invitation_expired_subject.txt (waldur_core.users)

``` txt
Invitation has expired
```

### invitation_expired_message.txt (waldur_core.users)

``` txt
Hello!

An invitation to {{ invitation.email }} has expired.
This invitation expires at {{ invitation.get_expiration_time|date:'d.m.Y H:i' }}.
```

### invitation_rejected_message.txt (waldur_core.users)

``` txt
Hello!

The following invitation has been rejected.

Full name: {{ invitation.full_name }}

Target: {{ name }} {{ type }}

Role: {{ role }}
```

### invitation_rejected_subject.txt (waldur_core.users)

``` txt
Invitation has been rejected
```

### invitation_created_subject.txt (waldur_core.users)

``` txt
{% if reminder %}
REMINDER: Invitation to {{ name }} {{ type }}
{% else %}
Invitation to {{ name }} {{ type }}
{% endif %}
```

### permission_request_submitted_subject.txt (waldur_core.users)

``` txt
Permission request has been submitted.
```

### invitation_requested_message.txt (waldur_core.users)

``` txt
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

### invitation_rejected_message.html (waldur_core.users)

``` html
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

### permission_request_submitted_message.txt (waldur_core.users)

``` txt
Hello!

User {{ permission_request.created_by }} with email {{ permission_request.created_by.email }} created permission request for {{ permission_request.invitation }}.

Please visit the link below to approve or reject permission request: {{ requests_link }}.
```

### invitation_requested_message.html (waldur_core.users)

``` html
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

### invitation_requested_subject.txt (waldur_core.users)

``` txt
Invitation request
```

## waldur_mastermind.booking

### notification_message.txt (waldur_mastermind.booking)

``` txt
Hello!

Please do not forget about upcoming booking:
{% for resource in resources %}
    {{ resource.name }}{% if not forloop.last %}, {% endif %}
{% endfor %}.
```

### notification_message.html (waldur_mastermind.booking)

``` html
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

### notification_subject.txt (waldur_mastermind.booking)

``` txt
Reminder about upcoming booking.
```

## waldur_mastermind.invoices

### monthly_invoicing_reports.html (waldur_mastermind.invoices)

``` html
{% load i18n %}
{% load static %}
{% load humanize %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style type="text/css">
        {% include "./style.css" %}
    </style>
</head>
<body>
<h2>{% trans 'Fixed price contracts:' %}</h2>
{% if contracts %}
    <table class="invoice-table">
        <thead>
            <tr>
                <th></th>
                <th>{% trans 'Organization' %}</th>
                <th>{% trans 'Contract end date' %}</th>
                <th>{% trans 'Till the end of contract. [days]' %}</th>
                <th>{% trans 'Contract sum' %}</th>
                <th>{% trans 'Payment sum' %}</th>
            </tr>
        </thead>
        <tbody>
            {% for contract in contracts %}
                <tr>
                    <th>{{ forloop.counter }}</th>
                    <td>{{ contract.name }}</td>
                    <td>{{ contract.end|date:"Y-m-d"|default_if_none:"" }}</td>
                    <td {% if contract.end_date_alarm %} class="text-danger" {% endif %}>{{ contract.till_end|default_if_none:"" }}</td>
                    <td {% if contract.payments_alarm %} class="text-danger" {% endif %}>
                        {{ contract.contract_sum|default_if_none:0|floatformat:"2"|intcomma }}
                    </td>
                    <td {% if contract.payments_alarm %} class="text-danger" {% endif %}>
                        {{ contract.payments_sum|default_if_none:0|floatformat:"2"|intcomma }}
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% else %}
    <p>{% trans 'Contracts do not exist.' %}</p>
{% endif %}

<h2>{% blocktrans %}Invoices for month {{ month }}-{{ year }}:{% endblocktrans %}</h2>

<table class="invoice-table">
    <thead>
        <tr>
            <th></th>
            <th>{% trans 'Organization' %}</th>
            <th>{% trans 'Invoice date' %}</th>
            <th>{% trans 'Invoice sum' %}</th>
        </tr>
    </thead>
    <tbody>
        {% for invoice in invoices %}
            <tr>
                <th>{{ forloop.counter }}</th>
                <td>{% if invoice.customer.abbreviation %}
                        {{ invoice.customer.abbreviation }}
                    {% else %}
                        {{ invoice.customer.name }}
                    {% endif %}</td>
                <td>{{ invoice.invoice_date|date:"Y-m-d" }}</td>
                <td>{{ invoice.total|floatformat:"2"|intcomma }}</td>
            </tr>
        {% endfor %}
    </tbody>
</table>

</body>
</html>
```

### report_body.txt (waldur_mastermind.invoices)

``` txt
Attached is an accounting report for {{ month }}/{{ year }}.
```

### invoice.html (waldur_mastermind.invoices)

``` html
{% load i18n %}
{% load humanize %}

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Invoice</title>
    <style type="text/css">
      {% include "waldur_core/font.css" %}
      {% include "./style.css" %}
    </style>
  </head>
  <body>
      {% if deployment_logo %}
      <div id="logo">
        <img src="data:image/png;base64,{{ deployment_logo }}">
      </div>
      {% endif %}
      <h1>{% trans "Invoice No." %} {{ invoice.number|upper }}</h1>
      <br>
      <div class="text-right">
          <strong>{% trans "Invoice date" %}:</strong> {% if invoice.invoice_date %}
        {{ invoice.invoice_date|date:"Y-m-d" }} {% else %} {% trans "Pending" %} {% endif %}<br/>
          {% if invoice.due_date %}<strong>{% trans "Due date" %}:</strong> {{ invoice.due_date|date:"Y-m-d" }}<br/>{% endif %}
          <strong>{% trans "Invoice period" %}:</strong> {{ invoice.year }}-{{ invoice.month }}<br/>
      </div>

      <div>
        <h3 class="name">From</h3>
        <div><strong>{{ issuer_details.company }}</strong></div>
        <div>{{ issuer_details.address }}</div>
        <div>{{ issuer_details.country }}, {{ issuer_details.postal }}</div>
        <div><abbr>P:</abbr> ({{ issuer_details.phone.country_code }}) {{ issuer_details.phone.national_number }}</div>
        <div>{{ issuer_details.bank }}, {{ issuer_details.account }}</div>
        <div><abbr>{% trans "VAT" %}:</abbr>{{ issuer_details.vat_code }}</div>
        <div>{{ issuer_details.email }}</div>
      </div>
      <div>
        <h3 class="name">To</h3>
        <div><strong>{{ invoice.customer.name }}</strong></div>

        {% if invoice.customer.address %}
          <div>{{ invoice.customer.address }}</div>
        {% endif %}

        {% if invoice.customer.country and invoice.customer.postal %}
          <div>{{ invoice.customer.country }}, {{ invoice.customer.postal }}</div>
        {% endif %}

        {% if invoice.customer.phone_number %}
          <div><abbr>P:</abbr> {{ invoice.customer.phone_number }}</div>
        {% endif %}

        {% if invoice.customer.bank_name and invoice.customer.bank_account %}
          <div>{{ invoice.customer.bank_name }}, {{ invoice.customer.bank_account }}</div>
        {% endif %}

        {% if customer.vat_code %}
          <div><abbr>{% trans "VAT" %}:</abbr> {{ customer.vat_code }}</div>
        {% endif %}

        <div>{{ invoice.customer.email }}</div>

      </div>
      <div class="m-t">
        <table class="invoice-table">
          <tr>
            <th>Item</th>
            <th>Quantity</th>
            <th>Unit price</th>
            <th>Total price</th>
          </tr>

          {% regroup items|dictsort:"project_name" by project_name as project_list %}
          {% for project in project_list %}
          <tr>
              <td colspan="4"><h3>{{ project.grouper }}</h3></td>
          </tr>
            {% for item in project.list %}
              <tr>
                <td>
                  <strong>{{ item.name }}</strong>
                  <div>
                    <small>
                      {% trans "Start time" %}: {{ item.start | date:"Y-m-d H:i" }}.
                      {% trans "End time" %}: {{ item.end | date:"Y-m-d H:i" }}.
                    </small>
                  </div>
                </td>
                <td>{{ item.quantity }}</td>
                <td>{{ currency }} {{ item.unit_price | floatformat:2 | intcomma }}</td>
                <td>{{ currency }} {{ item.total | floatformat:2 | intcomma }}</td>
              </tr>
            {% endfor %}
          {% endfor %}
        </table>
      </div>
      <table class="m-t invoice-total">
        <tr>
          <td><strong>{% trans "Subtotal" %}</strong></td>
          <td>{{ currency }} {{ invoice.price | floatformat:2 | intcomma}}</td>
        </tr>
        {% if invoice.tax %}
          <tr>
            <td><strong>{% trans "VAT" %}</strong></td>
            <td>{{ currency }} {{ invoice.tax | floatformat:2 | intcomma}}</td>
          </tr>
        {% endif %}
        <tr>
          <td><strong>{% trans "TOTAL" %}</strong></td>
          <td>{{ currency }} {{ invoice.total | floatformat:2 | intcomma}}</td>
      </tr>
      </table>
  </body>
</html>
```

### notification_message.txt (waldur_mastermind.invoices)

``` txt
Hello,

Please follow the link below to see {{ customer }}'s accounting information for {{ month }}/{{ year }}:
{{ link }}
```

### upcoming_ends_notification_message.txt (waldur_mastermind.invoices)

``` txt
Hello,

this is a reminder that {{ organization_name }}'s fixed price contract {{ contract_number }} is ending on {{ end }}.
```

### upcoming_ends_notification_subject.txt (waldur_mastermind.invoices)

``` txt
{{ organization_name }}'s fixed price contract {{ contract_number }} is coming to an end
```

### report_subject.txt (waldur_mastermind.invoices)

``` txt
Waldur accounting report for {{ month }}/{{ year }}
```

### notification_message.html (waldur_mastermind.invoices)

``` html
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

### upcoming_ends_notification_message.html (waldur_mastermind.invoices)

``` html
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

### notification_subject.txt (waldur_mastermind.invoices)

``` txt
{{ customer }}'s invoice for {{ month }}/{{ year }}
```

## waldur_mastermind.marketplace

### notification_about_project_ending_subject.txt (waldur_mastermind.marketplace)

``` txt
Project {{ project.name }} will be deleted.
```

### marketplace_resource_update_limits_succeeded_message.txt (waldur_mastermind.marketplace)

``` txt
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

### notification_approval_subject.txt (waldur_mastermind.marketplace)

``` txt
A new order by {{ order.created_by.get_full_name }} is waiting for approval.
```

### marketplace_resource_update_limits_succeeded_subject.txt (waldur_mastermind.marketplace)

``` txt
Resource {{ resource_name }} limits have been updated.
```

### notification_about_stale_resources_message.txt (waldur_mastermind.marketplace)

``` txt
Hello!

We noticed that you have stale resources that have not cost you anything for the last 3 months.
Perhaps some of them are not needed any more?

The resource names are:
{% for resource in resources %}
    {{ resource.resource.name }} {{ resource.resource_url }}
{% endfor %}
Thank you!
```

### marketplace_plan_template.txt (waldur_mastermind.marketplace)

``` txt
Plan: {{ plan.name }}{% for component in components %}
{{component.name}}; amount: {{component.amount}}; price: {{component.price|floatformat }};
{% endfor %}
```

### notification_usages_message.txt (waldur_mastermind.marketplace)

``` txt
Hello!

Please do not forget to add usage for the resources you provide:
{% regroup resources by offering as offering_list %}{% for offering in offering_list %}
{{forloop.counter}}. {{ offering.grouper.name }}:{% for resource in offering.list %}
    - {{ resource.name }}
{% endfor %}{% endfor %}
You can submit resource usage via API or do it manually at {{ public_resources_url }}.
```

### marketplace_resource_termination_scheduled_staff_message.html (waldur_mastermind.marketplace)

``` html
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

### marketplace_resource_update_succeeded_message.html (waldur_mastermind.marketplace)

``` html
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

### notification_approval_message.txt (waldur_mastermind.marketplace)

``` txt
Hello!

A new order by {{ order.created_by.get_full_name }} is waiting for approval.
```

### marketplace_resource_update_failed_subject.txt (waldur_mastermind.marketplace)

``` txt
Resource {{ resource_name }} update has failed.
```

### marketplace_resource_terminate_failed_subject.txt (waldur_mastermind.marketplace)

``` txt
Resource {{ resource_name }} deletion has failed.
```

### marketplace_resource_update_succeeded_message.txt (waldur_mastermind.marketplace)

``` txt
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

### marketplace_resource_update_failed_message.txt (waldur_mastermind.marketplace)

``` txt
Hello!

Resource {{ resource_name }} update has failed.
```

### notification_about_stale_resources_message.html (waldur_mastermind.marketplace)

``` html
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

### marketplace_resource_create_failed_message.html (waldur_mastermind.marketplace)

``` html
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

### marketplace_resource_create_succeeded_message.html (waldur_mastermind.marketplace)

``` html
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

### marketplace_resource_update_limits_failed_message.html (waldur_mastermind.marketplace)

``` html
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

### marketplace_resource_update_limits_succeeded_message.html (waldur_mastermind.marketplace)

``` html
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

### marketplace_resource_update_failed_message.html (waldur_mastermind.marketplace)

``` html
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

### notification_about_project_ending_message.html (waldur_mastermind.marketplace)

``` html
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

### marketplace_resource_create_failed_subject.txt (waldur_mastermind.marketplace)

``` txt
Resource {{ resource_name }} creation has failed.
```

### marketplace_resource_update_limits_failed_subject.txt (waldur_mastermind.marketplace)

``` txt
Resource {{ resource_name }} limits update has failed.
```

### marketplace_resource_terminate_failed_message.html (waldur_mastermind.marketplace)

``` html
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

### notification_usages_message.html (waldur_mastermind.marketplace)

``` html
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

### marketplace_resource_terminate_succeeded_message.html (waldur_mastermind.marketplace)

``` html
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

### notification_service_provider_approval_message.html (waldur_mastermind.marketplace)

``` html
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

### marketplace_resource_termination_scheduled_staff_subject.txt (waldur_mastermind.marketplace)

``` txt
Resource {{ resource.name }} termination has been scheduled.
```

### notification_about_stale_resources_subject.txt (waldur_mastermind.marketplace)

``` txt
Reminder about stale resources.
```

### marketplace_resource_terminate_succeeded_subject.txt (waldur_mastermind.marketplace)

``` txt
Resource {{ resource_name }} has been deleted.
```

### marketplace_resource_termination_scheduled_message.txt (waldur_mastermind.marketplace)

``` txt
Hello!

The resource you have - {{ resource.name }} has not been used for the past 3 months. {{ user.full_name }} has scheduled termination of that resource on {{ resource.end_date|date:"SHORT_DATE_FORMAT" }}. If you feel that you still want to keep it, please remove the resource end date {{ resource_url }}.
```

### notification_about_project_ending_message.txt (waldur_mastermind.marketplace)

``` txt
Dear {{ user.full_name }},

Your project {{ project.name }} is ending {% if delta == 1 %} tomorrow {% else %} in {{ delta }} days{% endif %}. End of the project will lead to termination of all resources in the project.
If you are aware of that, then no actions are needed from your side.
If you need to update project end date, please update it in project details {{ project_url }}.

Thank you!
```

### marketplace_resource_update_succeeded_subject.txt (waldur_mastermind.marketplace)

``` txt
Resource {{ resource_name }} has been updated.
```

### marketplace_resource_update_limits_failed_message.txt (waldur_mastermind.marketplace)

``` txt
Hello!

Resource {{ resource_name }} limits update has failed.
```

### marketplace_resource_termination_scheduled_subject.txt (waldur_mastermind.marketplace)

``` txt
Resource {{ resource.name }} termination has been scheduled.
```

### marketplace_resource_terminate_failed_message.txt (waldur_mastermind.marketplace)

``` txt
Hello!

Resource {{ resource_name }} deletion has failed.
```

### marketplace_resource_termination_scheduled_message.html (waldur_mastermind.marketplace)

``` html
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

### notification_service_provider_approval_message.txt (waldur_mastermind.marketplace)

``` txt
Hello!

A new order by {{ order.created_by.get_full_name }} is waiting for approval.
```

### notification_service_provider_approval_subject.txt (waldur_mastermind.marketplace)

``` txt
A new order by {{ order.created_by.get_full_name }} is waiting for approval.
```

### marketplace_resource_create_failed_message.txt (waldur_mastermind.marketplace)

``` txt
Hello!

Resource {{ resource_name }} creation has failed.
```

### marketplace_resource_termination_scheduled_staff_message.txt (waldur_mastermind.marketplace)

``` txt
Hello!

The resource you have - {{ resource.name }} has not been used for the past 3 months. {{ user.full_name }} has scheduled termination of that resource on {{ resource.end_date|date:"SHORT_DATE_FORMAT" }}. If you feel that you still want to keep it, please remove the resource end date {{ resource_url }}.
```

### marketplace_resource_create_succeeded_subject.txt (waldur_mastermind.marketplace)

``` txt
Resource {{ resource_name }} has been created.
```

### marketplace_resource_terminate_succeeded_message.txt (waldur_mastermind.marketplace)

``` txt
Hello!

Resource {{ resource_name }} has been deleted.
```

### notification_approval_message.html (waldur_mastermind.marketplace)

``` html
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

### marketplace_resource_create_succeeded_message.txt (waldur_mastermind.marketplace)

``` txt
Hello!

Resource {{ resource_name }} has been created.
```

### notification_usages_subject.txt (waldur_mastermind.marketplace)

``` txt
Reminder about missing usage reports.
```

## waldur_mastermind.marketplace_flows

### flow_rejected_message.html (waldur_mastermind.marketplace_flows)

``` html
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

### flow_submitted_message.html (waldur_mastermind.marketplace_flows)

``` html
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

### flow_submitted_subject.txt (waldur_mastermind.marketplace_flows)

``` txt
{% load i18n %}
{% trans 'Resource creation request has been submitted' %}
```

### flow_rejected_subject.txt (waldur_mastermind.marketplace_flows)

``` txt
{% load i18n %}
{% trans 'Your submission has been rejected' %}
```

### flow_submitted_message.txt (waldur_mastermind.marketplace_flows)

``` txt
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

### flow_rejected_message.txt (waldur_mastermind.marketplace_flows)

``` txt
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

## waldur_mastermind.marketplace_remote

### notification_about_pending_project_updates_message.txt (waldur_mastermind.marketplace_remote)

``` txt
Hello!

We noticed that you have pending project update requests.
Perhaps you would like to have a look at them?

The project is:
    {{ project_update_request.project.name }} {{ project_url }}
Thank you!
```

### notification_about_pending_project_updates_subject.txt (waldur_mastermind.marketplace_remote)

``` txt
Reminder about pending project updates.
```

### notification_about_project_details_update_message.txt (waldur_mastermind.marketplace_remote)

``` txt
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

### notification_about_project_details_update_message.html (waldur_mastermind.marketplace_remote)

``` html
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

### notification_about_pending_project_updates_message.html (waldur_mastermind.marketplace_remote)

``` html
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

### notification_about_project_details_update_subject.txt (waldur_mastermind.marketplace_remote)

``` txt
A notification about project details update.
```

## waldur_mastermind.marketplace_support

### terminate_resource_template.txt (waldur_mastermind.marketplace_support)

``` txt
{% load waldur_marketplace %}[Terminate resource {{order_item.resource.scope.name}}|{{request_url}}].
{% plan_details order_item.resource.plan %}
Marketplace resource UUID: {{order_item.resource.uuid.hex}}
```

### update_resource_template.txt (waldur_mastermind.marketplace_support)

``` txt
[Switch plan for resource {{order_item.resource.scope.name}}|{{request_url}}].
Switch from {{order_item.resource.plan.name}} plan to {{order_item.plan.name}}.
Marketplace resource UUID: {{order_item.resource.uuid.hex}}
```

### create_resource_template.txt (waldur_mastermind.marketplace_support)

``` txt
{% load waldur_marketplace %}[Order item|{{order_item_url}}].
Provider: {{order_item.offering.customer.name}}
Resource UUID: {{resource.uuid}}
Plan details:
    {% plan_details order_item.plan %}
Full name: {{order_item.order.created_by.full_name|default:"none"}}
Civil code:{{order_item.order.created_by.civil_number|default:"none"}}
Email: {{order_item.order.created_by.email}}
```

### update_limits_template.txt (waldur_mastermind.marketplace_support)

``` txt
[Update limits for resource {{order_item.resource.scope.name}}|{{request_url}}].
Marketplace resource UUID: {{order_item.resource.uuid.hex}}
Old limits: {{ old_limits }}.
New limits: {{ new_limits }}.
```

## waldur_mastermind.support

### notification_comment_updated.txt (waldur_mastermind.support)

``` txt
Hello!

The comment has been updated. Please go to {{issue_url}} to see it.
```

### notification_issue_feedback.txt (waldur_mastermind.support)

``` txt
Hello, {{issue.caller.full_name}}!

We would like to hear your feedback regarding your recent experience with support for {{issue_url}}.

Click on the evaluations below to provide the feedback.

{% for link in feedback_links%}
    {{link.label}}: {{link.link}}
{% endfor %}
```

### description.txt (waldur_mastermind.support)

``` txt
{{issue.description}}

---
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
- Site URL: {{ settings.WALDUR_CORE.HOMEPORT_URL }}
```

### summary.txt (waldur_mastermind.support)

``` txt
{% if issue.customer.abbreviation %}{{issue.customer.abbreviation}}: {% endif %}{{issue.summary}}
```

### notification_issue_updated_subject.txt (waldur_mastermind.support)

``` txt
Updated issue: {{issue.key}} {{issue.summary}}
```

### notification_comment_added.html (waldur_mastermind.support)

``` html
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>The issue you have created ({{ issue.key }}) has a new comment</title>
</head>
<body>
<p>
    {{ comment.author.name }} added a new comment.
</p>
<p>
    <a href="{{ issue_url }}">[{{ issue.key }}] {{ issue.summary }}</a>
</p>
<pre>
    {{ comment.description }}
</pre>
</body>
</html>
```

### notification_issue_updated.html (waldur_mastermind.support)

``` html
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
{% if changed.description %}
<p>
    Description has been changed from <strong>{{ changed.description }}</strong> to <strong>{{ issue.description }}</strong>.
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

### notification_comment_added.txt (waldur_mastermind.support)

``` txt
Hello!

The issue you have created has a new comment. Please go to {{issue_url}} to see it.
```

### notification_issue_feedback_subject.txt (waldur_mastermind.support)

``` txt
Please share your feedback: {{issue.key}} {{issue.summary}}
```

### notification_issue_feedback.html (waldur_mastermind.support)

``` html
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

### notification_comment_added_subject.txt (waldur_mastermind.support)

``` txt
The issue you have created has a new comment
```

### notification_issue_updated.txt (waldur_mastermind.support)

``` txt
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

### notification_comment_updated.html (waldur_mastermind.support)

``` html
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
    {{ old_description }}
</p>
<p>
    New comment:
</p>
<p>
    {{ comment.description }}
</p>
</body>
</html>
```

### notification_comment_updated_subject.txt (waldur_mastermind.support)

``` txt
The comment has been updated
```

