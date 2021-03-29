# General Configuration

Outline:

- [Introduction](#introduction)
- [Waldur Core settings](#waldur-core-settings)
- [Admin dashboard configuration](#admin-dashboard-configuration)
- [Custom templates configuration](#custom-templates-configuration)
- [Local time zone configuration](#local-time-zone-configuration)

## Introduction
Waldur is a [Django](https://www.djangoproject.com)-based application, so configuration is done by modifying `settings.py` file.

If you want to configure options related to Django, such as tune caches, database connection, configure custom logging, etc, please refer to [Django documentation](https://docs.djangoproject.com/en/2.2/).

Configuration for Waldur Core is namespaced inside a single Django setting, named `WALDUR_CORE`. Usually each plugin's settings are namespaced, so please refer to plugin documentation for details.

Basic configuration might look like this:
```python
WALDUR_CORE = {
   'ENABLE_GEOIP': True,
   'EXTENSIONS_AUTOREGISTER': True,
   'GOOGLE_API': {
        'Android': {
            'server_key': 'AIzaSyA2_7UaVIxXfKeFvxTjQNZbrzkXG9OTCkg',
        },
        'iOS': {
             'server_key': 'AIzaSyA34zlG_y5uHOe2FmcJKwfk2vG-3RW05vk',
        }
    },
    'SHOW_ALL_USERS': False,
    'OWNER_CAN_MANAGE_CUSTOMER': False,
    'CREATE_DEFAULT_PROJECT_ON_ORGANIZATION_CREATION': False,
    'TOKEN_KEY': 'x-auth-token',
    'TOKEN_LIFETIME': timedelta(hours=1),
    'SITE_NAME': 'Waldur MasterMind',
    'COUNTRIES': ['EE', 'LV', 'LT'],
    'NOTIFICATIONS_PROFILE_CHANGES': {
        'ENABLED': True,
        'FIELDS': ('email', 'phone_number', 'job_title')
    },
}
```

Waldur will send notifications from email address specified in `DEFAULT_FROM_EMAIL` variable. for example,
```python
DEFAULT_FROM_EMAIL = 'noreply@example.com'
```

## Waldur Core settings
- `ALLOW_SIGNUP_WITHOUT_INVITATION` is disabled by default. Set to `True` to enable signup by invitation only.

- `AUTHENTICATION_METHODS` is a list of enabled authentication methods. It allows you to restrict enabled authentication methods.

- `BACKEND_FIELDS_EDITABLE` allows to control `/admin` writable fields. If this flag is disabled, it is impossible to edit any field that corresponds to backend value via `/admin`. Such restriction allows to save information from corruption. Flag is enabled by default.

- `COMPANY_TYPES` specifies list of available company types, it is used in organization creation dialog. By default *Ministry*, *Private company*, *Public company*, *Government owned company* are available.

- `COUNTRIES` list is used in organization creation dialog in order to limit country choices to predefined set.

- `CREATE_DEFAULT_PROJECT_ON_ORGANIZATION_CREATION` enables generation of the first project on organization creation.

- `CURRENCY_NAME` is used in marketplace order details and invoice for currency formatting.

- `ENABLE_ACCOUNTING_START_DATE` allows to enable accounting only for organizations using value of `accounting_start_date` field. Disabled by default.

- `ENABLE_GEOIP` indicates whether geolocation is enabled (boolean). Enabled by default.

- `EXTENSIONS_AUTOREGISTER` defines whether extensions should be automatically registered (boolean).

- `GOOGLE_API` is settings dictionary for Google Cloud Messaging:
    - `Android` specifies settings for Android devices.
server_key is Google Cloud messaging server key.
    - `IOS` specifies settings for IOS devices.
server_key is Google Cloud messaging server key.

- `NOTIFICATION_TITLE` is string to be displayed in the notification pop-up title.

- `INITIAL_CUSTOMER_AGREEMENT_NUMBER` allows to tweak initial value of agreement number (`4000` by default). It is assumed that organization owner should accept terms of services when organization is registered via Waldur HomePort.

- `INVITATION_LIFETIME` defines for how long invitation remains valid. Default value - `1` week.

- `INVITATIONS_ENABLED` allows to enable invitations feature. Enabled by default.

- `NATIVE_NAME_ENABLED` allows to render native name field in customer and user forms. Disabled by default.

- `NOTIFICATIONS_PROFILE_CHANGES` allows enabling notifications about profile changes of organization owners and allows selecting, which fields of profile should be tracked.

- `OWNER_CAN_MANAGE_CUSTOMER` enables organization owners to create an organization (boolean).

- `OWNERS_CAN_MANAGE_OWNERS` enables organization owners to manage other organization owners, enabled by default.

- `ONLY_STAFF_MANAGES_SERVICES` allows to restrict provider management only to staff users, disabled by default.
Please also note, that if this flag is enabled, OpenStack tenant provision & modification would be available for staff users only. It means that organization owners wouldn't be able to manage virtual private clouds.

- `SELLER_COUNTRY_CODE` specifies seller legal or effective country of registration or residence as an ISO 3166-1 alpha-2 country code. It is used for computing VAT charge rate.

- `SHOW_ALL_USERS` indicates whether user can see all other users in `api/users/` endpoint (boolean).

- `SITE_NAME` is used in email notifications in order to refer to the current deployment in user-friendly way.

- `SITE_ADDRESS` is used in marketplace order header.

- `SITE_EMAIL` is used in marketplace order header.

- `SITE_PHONE` is used in marketplace order header.

- `SITE_LOGO` is used in marketplace order header.

- `TOKEN_KEY` is header for token authentication. For example, 'x-auth-token'.

- `TOKEN_LIFETIME` defines for how long user token should remain valid if there was no action from user (`timedelta` value, for example `timedelta(hours=1)`).

- `VALIDATE_INVITATION_EMAIL` allows to ensure that invitation and user emails match. Disabled by default.

## Admin dashboard configuration
An admin dashboard supports custom links on Quick access panel. For instance, a panel below was configured with one additional link to **https://waldur.com**:

![admin example](img/admin-example.png)

Configuration of custom links is stored under `FLUENT_DASHBOARD_QUICK_ACCESS_LINKS` settings key and for current example has following structure:
```python
FLUENT_DASHBOARD_QUICK_ACCESS_LINKS = [
  {
   'title': '[Custom] Waldur - Cloud Service',
   'url': 'https://waldur.com',
   'external': True, # adds an icon specifying that this link is external,
   'description': 'Open-source Cloud Brokerage Platform',
   'attrs': {'target': '_blank'} # add an attribute to generated anchor element which will open link in a new tab.
  },
]
```
Here is a short description of link parameters:

| **Name** | **Type** | **Required** | **Description** |
| -------- | -------- | ------------ | --------------- |
| description | string | No | Tool tip on the link |
| external | boolean | No | Specifies whether additional icon indicating an external URL has to be added |
|url | URL | Yes | A URL of the link|
| title | string | Yes | A title of the generated link |
| attrs | dict | No | A dictionary of anchor attributes to be added to generated element |

It is also possible to omit optional fields and add links by specifying only a title and a URL to the generated link.

```python
FLUENT_DASHBOARD_QUICK_ACCESS_LINKS = [
  ['[Custom] Waldur - Cloud Service', 'https://waldur.com'],
  ['Find us on GitHub', 'https://github.com/opennode/waldur-core'],
]
```

## Custom templates configuration
To overwrite default templates you should use [django-dbtemplates](https://github.com/jazzband/django-dbtemplates). It allows creation of templates through `/admin`.

## Local time zone configuration
Set `TIME_ZONE` setting in `/etc/waldur/override.conf.py` to use local time zone. By default it is set to UTC. See the [list of time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for possible options.
