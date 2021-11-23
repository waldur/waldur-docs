# Configuration guide

## WALDUR_AUTH_SAML2 plugin

Default value:

```python
WALDUR_AUTH_SAML2 = {'ALLOW_TO_SELECT_IDENTITY_PROVIDER': True,
 'ATTRIBUTE_MAP_DIR': '',
 'AUTHN_REQUESTS_SIGNED': 'true',
 'BASE_URL': '',
 'CATEGORIES': ['http://www.geant.net/uri/dataprotection-code-of-conduct/v1'],
 'CERT_FILE': '',
 'DEBUG': False,
 'DEFAULT_BINDING': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST',
 'DESCRIPTION': 'Service provider description',
 'DIGEST_ALGORITHM': None,
 'DISCOVERY_SERVICE_LABEL': None,
 'DISCOVERY_SERVICE_URL': None,
 'DISPLAY_NAME': 'Service provider display name',
 'ENABLE_SINGLE_LOGOUT': False,
 'IDENTITY_PROVIDER_LABEL': None,
 'IDENTITY_PROVIDER_URL': None,
 'IDP_METADATA_LOCAL': [],
 'IDP_METADATA_REMOTE': [],
 'KEY_FILE': '',
 'LOGOUT_REQUESTS_SIGNED': 'true',
 'LOG_FILE': '',
 'LOG_LEVEL': 'INFO',
 'NAME': 'saml2',
 'NAMEID_FORMAT': None,
 'OPTIONAL_ATTRIBUTES': [],
 'ORGANIZATION': {},
 'PRIVACY_STATEMENT_URL': 'http://example.com/privacy-policy/',
 'REGISTRATION_AUTHORITY': 'http://example.com/registration-authority/',
 'REGISTRATION_INSTANT': '2017-01-01T00:00:00',
 'REGISTRATION_POLICY': 'http://example.com/registration-policy/',
 'REQUIRED_ATTRIBUTES': [],
 'SAML_ATTRIBUTE_MAPPING': {},
 'SIGNATURE_ALGORITHM': None,
 'XMLSEC_BINARY': '/usr/bin/xmlsec1'}
```

### ALLOW_TO_SELECT_IDENTITY_PROVIDER

Type: bool

### ATTRIBUTE_MAP_DIR

Type: str

Directory with attribute mapping

### AUTHN_REQUESTS_SIGNED

Type: str

Indicates if the authentication requests sent should be signed by default

### BASE_URL

Type: str

URL required for assertion consumer, single logout services and entity ID

### CATEGORIES

Type: list

Links to the entity categories

### CERT_FILE

Type: str

PEM formatted certificate chain file

### DEBUG

Type: bool

Set to True to output debugging information

### DEFAULT_BINDING

Type: str

### DESCRIPTION

Type: str

Service provider description (required by CoC)

### DIGEST_ALGORITHM

Type: Optional[str]

Identifies the Message Digest algorithm URL according to the XML Signature specification (SHA1 is used by default)

### DISCOVERY_SERVICE_LABEL

Type: Optional[str]

### DISCOVERY_SERVICE_URL

Type: Optional[str]

### DISPLAY_NAME

Type: str

Service provider display name (required by CoC)

### ENABLE_SINGLE_LOGOUT

Type: bool

### IDENTITY_PROVIDER_LABEL

Type: Optional[str]

### IDENTITY_PROVIDER_URL

Type: Optional[str]

### IDP_METADATA_LOCAL

Type: list

IdPs metadata XML files stored locally

### IDP_METADATA_REMOTE

Type: list

IdPs metadata XML files stored remotely

### KEY_FILE

Type: str

PEM formatted certificate key file

### LOGOUT_REQUESTS_SIGNED

Type: str

Indicates if the entity will sign the logout requests

### LOG_FILE

Type: str

Empty to disable logging SAML2-related stuff to file

### LOG_LEVEL

Type: str

Log level for SAML2

### NAME

Type: str

Name used for assigning the registration method to the user

### NAMEID_FORMAT

Type: Optional[str]

Identified NameID format to use. None means default, empty string ("") disables addition of entity

### OPTIONAL_ATTRIBUTES

Type: list

SAML attributes that may be useful to have but not required

### ORGANIZATION

Type: dict

Organization responsible for the service (you can set multilanguage information here)

### PRIVACY_STATEMENT_URL

Type: str

URL with privacy statement (required by CoC)

### REGISTRATION_AUTHORITY

Type: str

Registration authority required by mdpi

### REGISTRATION_INSTANT

Type: str

Registration instant time required by mdpi

### REGISTRATION_POLICY

Type: str

Registration policy required by mdpi

### REQUIRED_ATTRIBUTES

Type: list

SAML attributes that are required to identify a user

### SAML_ATTRIBUTE_MAPPING

Type: dict

Mapping between SAML attributes and User fields

### SIGNATURE_ALGORITHM

Type: Optional[str]

Identifies the Signature algorithm URL according to the XML Signature specification (SHA1 is used by default)

### XMLSEC_BINARY

Type: str

Full path to the xmlsec1 binary program

## WALDUR_AUTH_SOCIAL plugin

Default value:

```python
WALDUR_AUTH_SOCIAL = {'EDUTEAMS_AUTH_URL': 'https://proxy.acc.eduteams.org/saml2sp/OIDC/authorization',
 'EDUTEAMS_CLIENT_ID': '',
 'EDUTEAMS_LABEL': 'eduTEAMS',
 'EDUTEAMS_SECRET': '',
 'EDUTEAMS_TOKEN_URL': 'https://proxy.acc.eduteams.org/OIDC/token',
 'EDUTEAMS_USERINFO_URL': 'https://proxy.acc.eduteams.org/OIDC/userinfo',
 'ENABLE_EDUTEAMS_SYNC': False,
 'KEYCLOAK_AUTH_URL': '',
 'KEYCLOAK_CLIENT_ID': '',
 'KEYCLOAK_LABEL': 'Keycloak',
 'KEYCLOAK_SECRET': '',
 'KEYCLOAK_TOKEN_URL': '',
 'KEYCLOAK_USERINFO_URL': '',
 'KEYCLOAK_VERIFY_SSL': True,
 'REMOTE_EDUTEAMS_CLIENT_ID': '',
 'REMOTE_EDUTEAMS_ENABLED': False,
 'REMOTE_EDUTEAMS_REFRESH_TOKEN': '',
 'REMOTE_EDUTEAMS_SECRET': '',
 'REMOTE_EDUTEAMS_TOKEN_URL': 'https://proxy.acc.researcher-access.org/OIDC/token',
 'REMOTE_EDUTEAMS_USERINFO_URL': 'https://proxy.acc.researcher-access.org/api/userinfo',
 'SMARTIDEE_CLIENT_ID': '',
 'SMARTIDEE_SECRET': '',
 'TARA_CLIENT_ID': '',
 'TARA_LABEL': 'Riigi Autentimisteenus',
 'TARA_SANDBOX': True,
 'TARA_SECRET': ''}
```

### EDUTEAMS_AUTH_URL

Type: str

The authorization endpoint performs authentication of the end-user. This is done by redirecting the user agent to this endpoint.

### EDUTEAMS_CLIENT_ID

Type: str

ID of application used for OAuth authentication.

### EDUTEAMS_LABEL

Type: str

Label is used by HomePort for rendering login button.

### EDUTEAMS_SECRET

Type: str

Application secret key.

### EDUTEAMS_TOKEN_URL

Type: str

The token endpoint is used to obtain tokens.

### EDUTEAMS_USERINFO_URL

Type: str

The userinfo endpoint returns standard claims about the authenticated user, and is protected by a bearer token.

### ENABLE_EDUTEAMS_SYNC

Type: bool

Enable eduTEAMS synchronization with remote Waldur.

### KEYCLOAK_AUTH_URL

Type: str

The authorization endpoint performs authentication of the end-user. This is done by redirecting the user agent to this endpoint.

### KEYCLOAK_CLIENT_ID

Type: str

ID of application used for OAuth authentication.

### KEYCLOAK_LABEL

Type: str

Label is used by HomePort for rendering login button.

### KEYCLOAK_SECRET

Type: str

Application secret key.

### KEYCLOAK_TOKEN_URL

Type: str

The token endpoint is used to obtain tokens.

### KEYCLOAK_USERINFO_URL

Type: str

The userinfo endpoint returns standard claims about the authenticated user, and is protected by a bearer token.

### KEYCLOAK_VERIFY_SSL

Type: bool

Validate TLS certificate of Keycloak REST API

### REMOTE_EDUTEAMS_CLIENT_ID

Type: str

ID of application used for OAuth authentication.

### REMOTE_EDUTEAMS_ENABLED

Type: bool

Enable remote eduTEAMS extension.

### REMOTE_EDUTEAMS_REFRESH_TOKEN

Type: str

Token is used to authenticate against user info endpoint.

### REMOTE_EDUTEAMS_SECRET

Type: str

Application secret key.

### REMOTE_EDUTEAMS_TOKEN_URL

Type: str

The token endpoint is used to obtain tokens.

### REMOTE_EDUTEAMS_USERINFO_URL

Type: str

It allows to get user data based on userid aka CUID.

### SMARTIDEE_CLIENT_ID

Type: str

ID of application used for OAuth authentication.

### SMARTIDEE_SECRET

Type: str

Application secret key.

### TARA_CLIENT_ID

Type: str

ID of application used for OAuth authentication.

### TARA_LABEL

Type: str

You may set it to eIDAS, SmartID or MobileID make it more clear to the user which exact identity provider is configured or preferred for service provider.

### TARA_SANDBOX

Type: bool

You should set it to False in order to switch to production mode.

### TARA_SECRET

Type: str

Application secret key.

## WALDUR_CORE plugin

Default value:

```python
WALDUR_CORE = {'ATTACHMENT_LINK_MAX_AGE': datetime.timedelta(seconds=3600),
 'AUTHENTICATION_METHODS': ['LOCAL_SIGNIN'],
 'BACKEND_FIELDS_EDITABLE': True,
 'BRAND_COLOR': '#3a8500',
 'COUNTRIES': ['AL',
               'AT',
               'BA',
               'BE',
               'BG',
               'CH',
               'CY',
               'DE',
               'DK',
               'EE',
               'ES',
               'EU',
               'FI',
               'FR',
               'GB',
               'GE',
               'GR',
               'HR',
               'HU',
               'IE',
               'IS',
               'IT',
               'LT',
               'LU',
               'LV',
               'MC',
               'MK',
               'MT',
               'NL',
               'NO',
               'PL',
               'PT',
               'RO',
               'RS',
               'SE',
               'SI',
               'UA'],
 'CREATE_DEFAULT_PROJECT_ON_ORGANIZATION_CREATION': False,
 'CURRENCY_NAME': 'EUR',
 'DOCS_URL': '',
 'EMAIL_CHANGE_MAX_AGE': datetime.timedelta(days=1),
 'ENABLE_ACCOUNTING_START_DATE': False,
 'ENABLE_GEOIP': True,
 'EXTENSIONS_AUTOREGISTER': True,
 'EXTERNAL_LINKS': [],
 'FULL_PAGE_TITLE': 'Waldur | Cloud Service Management',
 'GOOGLE_ANALYTICS_ID': '',
 'GROUP_INVITATION_LIFETIME': datetime.timedelta(days=7),
 'HERO_IMAGE': None,
 'HERO_LINK_LABEL': None,
 'HERO_LINK_URL': None,
 'HOMEPORT_SENTRY_DSN': None,
 'HOMEPORT_URL': 'https://example.com/',
 'HTTP_CHUNK_SIZE': 50,
 'INITIAL_CUSTOMER_AGREEMENT_NUMBER': 4000,
 'INVITATIONS_ENABLED': True,
 'INVITATION_CIVIL_NUMBER_HELP_TEXT': 'Must start with a country prefix ie '
                                      'EE34501234215',
 'INVITATION_CIVIL_NUMBER_LABEL': '',
 'INVITATION_CREATE_MISSING_USER': False,
 'INVITATION_DISABLE_MULTIPLE_ROLES': False,
 'INVITATION_LIFETIME': datetime.timedelta(days=7),
 'INVITATION_MAX_AGE': None,
 'INVITATION_TAX_NUMBER_LABEL': '',
 'LOGGING_REPORT_DIRECTORY': '/var/log/waldur',
 'LOGGING_REPORT_INTERVAL': datetime.timedelta(days=7),
 'NATIVE_NAME_ENABLED': False,
 'NOTIFICATIONS_PROFILE_CHANGES': {'ENABLED': True,
                                   'FIELDS': ('email',
                                              'phone_number',
                                              'job_title')},
 'NOTIFICATION_SUBJECT': 'Notifications from Waldur',
 'ONLY_STAFF_CAN_INVITE_USERS': False,
 'ONLY_STAFF_MANAGES_SERVICES': False,
 'OWNERS_CAN_MANAGE_OWNERS': False,
 'OWNER_CAN_MANAGE_CUSTOMER': False,
 'POWERED_BY_LOGO': None,
 'PROTECT_USER_DETAILS_FOR_REGISTRATION_METHODS': [],
 'SELLER_COUNTRY_CODE': None,
 'SHORT_PAGE_TITLE': 'Waldur',
 'SHOW_ALL_USERS': False,
 'SIDEBAR_LOGO': None,
 'SITE_ADDRESS': '',
 'SITE_DESCRIPTION': 'Your single pane of control for managing projects, teams '
                     'and resources in a self-service manner.',
 'SITE_EMAIL': '',
 'SITE_LOGO': None,
 'SITE_NAME': 'Waldur',
 'SITE_PHONE': '',
 'SUPPORT_PORTAL_URL': '',
 'TOKEN_KEY': 'x-auth-token',
 'TOKEN_LIFETIME': datetime.timedelta(seconds=3600),
 'TRANSLATION_DOMAIN': '',
 'USER_MANDATORY_FIELDS': ['full_name', 'email'],
 'USER_REGISTRATION_HIDDEN_FIELDS': ['registration_method',
                                     'job_title',
                                     'phone_number',
                                     'organization'],
 'USE_ATOMIC_TRANSACTION': True,
 'VALIDATE_INVITATION_EMAIL': False}
```

### ATTACHMENT_LINK_MAX_AGE

Type: timedelta

Max age of secure token for media download.

### AUTHENTICATION_METHODS

Type: List[str]

List of enabled authentication methods.

### BACKEND_FIELDS_EDITABLE

Type: bool

Allows to control /admin writable fields. If this flag is disabled it is impossible to edit any field that corresponds to backend value via /admin. Such restriction allows to save information from corruption.

### BRAND_COLOR

Type: Optional[str]

Hex color definition is used in HomePort landing page for login button.

### COUNTRIES

Type: List[str]

It is used in organization creation dialog in order to limit country choices to predefined set.

### CREATE_DEFAULT_PROJECT_ON_ORGANIZATION_CREATION

Type: bool

Enables generation of the first project on organization creation.

### CURRENCY_NAME

Type: str

It is used in marketplace order details and invoices for currency formatting.

### DOCS_URL

Type: str

Renders link to docs in header

### EMAIL_CHANGE_MAX_AGE

Type: timedelta

Max age of change email request.

### ENABLE_ACCOUNTING_START_DATE

Type: bool

Allows to enable accounting for organizations using value of accounting_start_date field.

### ENABLE_GEOIP

Type: bool

Enable detection of coordinates of virtual machines.

### EXTENSIONS_AUTOREGISTER

Type: bool

Defines whether extensions should be automatically registered.

### EXTERNAL_LINKS

Type: List[ExternalLink]

Render external links in dropdown in header. Each item should be object with label and url fields. For example: {"label": "Helpdesk", "url": "`https://example.com/`"}

### FULL_PAGE_TITLE

Type: str

It is used as default page title if it's not specified explicitly.

### GOOGLE_ANALYTICS_ID

Type: str

Identifier associated with your account and used by Google Analytics to collect the data.

### GROUP_INVITATION_LIFETIME

Type: timedelta

Defines for how long group invitation remains valid.

### HERO_IMAGE

Type: Optional[str]

Relative path to image rendered at hero section of HomePort landing page.

### HERO_LINK_LABEL

Type: Optional[str]

Label for link in hero section of HomePort landing page. It can be lead to support site or blog post.

### HERO_LINK_URL

Type: Optional[str]

Link URL in hero section of HomePort landing page.

### HOMEPORT_SENTRY_DSN

Type: Optional[str]

Sentry Data Source Name for Waldur HomePort project.

### HOMEPORT_URL

Type: str

It is used for rendering callback URL in HomePort.

### HTTP_CHUNK_SIZE

Type: int

Chunk size for resource fetching from backend API. It is needed in order to avoid too long HTTP request error.

### INITIAL_CUSTOMER_AGREEMENT_NUMBER

Type: int

Allows to tweak initial value of agreement number. It is assumed that organization owner should accept terms of services when organization is registered via Waldur HomePort.

### INVITATIONS_ENABLED

Type: bool

Allows to disable invitations feature.

### INVITATION_CIVIL_NUMBER_HELP_TEXT

Type: str

Help text for civil number field in invitation creation dialog.

### INVITATION_CIVIL_NUMBER_LABEL

Type: str

Custom label for civil number field in invitation creation dialog.

### INVITATION_CREATE_MISSING_USER

Type: bool

Allow to create FreeIPA user using details specified in invitation if user does not exist yet.

### INVITATION_DISABLE_MULTIPLE_ROLES

Type: bool

Do not allow user to grant multiple roles in the same project or organization using invitation.

### INVITATION_LIFETIME

Type: timedelta

Defines for how long invitation remains valid.

### INVITATION_MAX_AGE

Type: Optional[timedelta]

Max age of invitation token. It is used in approve and reject actions.

### INVITATION_TAX_NUMBER_LABEL

Type: str

Custom label for tax number field in invitation creation dialog.

### LOGGING_REPORT_DIRECTORY

Type: str

Directory where log files are located.

### LOGGING_REPORT_INTERVAL

Type: timedelta

Files older that specified interval are filtered out.

### NATIVE_NAME_ENABLED

Type: bool

Allows to render native name field in customer and user forms.

### NOTIFICATIONS_PROFILE_CHANGES

Type: dict

Allows enabling notifications about profile changes of organization owners.

### NOTIFICATION_SUBJECT

Type: str

It is used as a subject of email emitted by event logging hook.

### ONLY_STAFF_CAN_INVITE_USERS

Type: bool

Allow to limit invitation management to staff only.

### ONLY_STAFF_MANAGES_SERVICES

Type: bool

Allows to restrict provider management only to staff users.

### OWNERS_CAN_MANAGE_OWNERS

Type: bool

Enables organization owners to manage other organization owners.

### OWNER_CAN_MANAGE_CUSTOMER

Type: bool

Enables organization owners to create an organization.

### POWERED_BY_LOGO

Type: Optional[str]

Relative path to image rendered at the bottom of login menu in HomePort.

### PROTECT_USER_DETAILS_FOR_REGISTRATION_METHODS

Type: List[str]

List of authentication methods which are not allowed to update user details.

### SELLER_COUNTRY_CODE

Type: Optional[str]

Specifies seller legal or effective country of registration or residence as an ISO 3166-1 alpha-2 country code. It is used for computing VAT charge rate.

### SHORT_PAGE_TITLE

Type: str

it is used as prefix for page title.

### SHOW_ALL_USERS

Type: bool

Indicates whether user can see all other users in `api/users/` endpoint.

### SIDEBAR_LOGO

Type: Optional[str]

Relative path to image rendered at the top of sidebar menu in HomePort.

### SITE_ADDRESS

Type: str

It is used in marketplace order header.

### SITE_DESCRIPTION

Type: str

Description of the Waldur deployment.

### SITE_EMAIL

Type: str

It is used in marketplace order header and UI footer.

### SITE_LOGO

Type: Optional[str]

It is used in marketplace order header.

### SITE_NAME

Type: str

Human-friendly name of the Waldur deployment.

### SITE_PHONE

Type: str

It is used in marketplace order header and UI footer.

### SUPPORT_PORTAL_URL

Type: str

Support portal URL is rendered as a shortcut on dashboard

### TOKEN_KEY

Type: str

Header for token authentication.

### TOKEN_LIFETIME

Type: timedelta

Defines for how long user token should remain valid if there was no action from user.

### TRANSLATION_DOMAIN

Type: str

Identifier of translation domain applied to current deployment.

### USER_MANDATORY_FIELDS

Type: List[str]

List of user profile attributes that would be required for filling in HomePort. Note that backend will not be affected. If a mandatory field is missing in profile, a profile edit view will be forced upon user on any HomePort logged in action. Possible values are: description, email, full_name, job_title, organization, phone_number

### USER_REGISTRATION_HIDDEN_FIELDS

Type: List[str]

List of user profile attributes that would be concealed on registration form in HomePort. Possible values are: job_title, registration_method, phone_number

### USE_ATOMIC_TRANSACTION

Type: bool

Wrap action views in atomic transaction.

### VALIDATE_INVITATION_EMAIL

Type: bool

Ensure that invitation and user emails match.

## WALDUR_FREEIPA plugin

Default value:

```python
WALDUR_FREEIPA = {'BLACKLISTED_USERNAMES': ['root'],
 'ENABLED': False,
 'GROUPNAME_PREFIX': 'waldur_',
 'GROUP_SYNCHRONIZATION_ENABLED': True,
 'HOSTNAME': 'ipa.example.com',
 'PASSWORD': 'secret',
 'USERNAME': 'admin',
 'USERNAME_PREFIX': 'waldur_',
 'VERIFY_SSL': True}
```

### BLACKLISTED_USERNAMES

Type: list

List of username that users are not allowed to select

### ENABLED

Type: bool

Enable integration of identity provisioning in configured FreeIPA

### GROUPNAME_PREFIX

Type: str

Prefix to be appended to all group names created in FreeIPA by Waldur

### GROUP_SYNCHRONIZATION_ENABLED

Type: bool

Optionally disable creation of user groups in FreeIPA matching Waldur structure

### HOSTNAME

Type: str

Hostname of FreeIPA server

### PASSWORD

Type: str

Password of FreeIPA user with administrative privileges

### USERNAME

Type: str

Username of FreeIPA user with administrative privileges

### USERNAME_PREFIX

Type: str

Prefix to be appended to all usernames created in FreeIPA by Waldur

### VERIFY_SSL

Type: bool

Validate TLS certificate of FreeIPA web interface / REST API

## WALDUR_HPC plugin

Default value:

```python
WALDUR_HPC = {'ENABLED': False,
 'EXTERNAL_AFFILIATIONS': [],
 'EXTERNAL_CUSTOMER_UUID': '',
 'EXTERNAL_EMAIL_PATTERNS': [],
 'INTERNAL_AFFILIATIONS': [],
 'INTERNAL_CUSTOMER_UUID': '',
 'INTERNAL_EMAIL_PATTERNS': [],
 'INTERNAL_LIMITS': {},
 'OFFERING_UUID': '',
 'PLAN_UUID': ''}
```

### ENABLED

Type: bool

Enable HPC-specific hooks in Waldur deployment

### EXTERNAL_AFFILIATIONS

Type: List[str]

List of user affiliations (eduPersonScopedAffiliation fields) that define if the user belongs to external organization.

### EXTERNAL_CUSTOMER_UUID

Type: str

UUID of a Waldur organization (aka customer) where new external users would be added

### EXTERNAL_EMAIL_PATTERNS

Type: List[str]

List of user email patterns (as regex) that define if the user belongs to external organization.

### INTERNAL_AFFILIATIONS

Type: List[str]

List of user affiliations (eduPersonScopedAffiliation fields) that define if the user belongs to internal organization.

### INTERNAL_CUSTOMER_UUID

Type: str

UUID of a Waldur organization (aka customer) where new internal users would be added

### INTERNAL_EMAIL_PATTERNS

Type: List[str]

List of user email patterns (as regex) that define if the user belongs to internal organization.

### INTERNAL_LIMITS

Type: dict

Overrided default values for SLURM offering to be created for users belonging to internal organization.

### OFFERING_UUID

Type: str

UUID of a Waldur SLURM offering, which will be used for creating allocations for users

### PLAN_UUID

Type: str

UUID of a Waldur SLURM offering plan, which will be used for creating allocations for users

## WALDUR_KEYCLOAK plugin

Default value:

```python
WALDUR_KEYCLOAK = {'BASE_URL': 'http://localhost:8080/auth',
 'CLIENT_ID': 'waldur',
 'CLIENT_SECRET': 'UUID',
 'ENABLED': False,
 'PASSWORD': 'secret',
 'REALM': 'waldur',
 'USERNAME': 'admin'}
```

### BASE_URL

Type: str

Base URL of Keycloak server

### CLIENT_ID

Type: str

Identification of Waldur client app

### CLIENT_SECRET

Type: str

Credentials are generated in Keycloak admin console

### ENABLED

Type: bool

Enable integration of group provisioning in configured Keycloak

### PASSWORD

Type: str

Password of Keycloak user with administrative privileges

### REALM

Type: str

Realm used by Waldur

### USERNAME

Type: str

Username of Keycloak user with administrative privileges

## WALDUR_MARKETPLACE plugin

Default value:

```python
WALDUR_MARKETPLACE = {'ADMIN_CAN_APPROVE_ORDER': False,
 'ANONYMOUS_USER_CAN_VIEW_OFFERINGS': True,
 'DISABLE_SENDING_NOTIFICATIONS_ABOUT_RESOURCE_UPDATE': True,
 'ENABLE_STALE_RESOURCE_NOTIFICATIONS': False,
 'MANAGER_CAN_APPROVE_ORDER': False,
 'NOTIFY_ABOUT_RESOURCE_CHANGE': True,
 'NOTIFY_STAFF_ABOUT_APPROVALS': False,
 'OWNER_CAN_APPROVE_ORDER': True,
 'OWNER_CAN_REGISTER_SERVICE_PROVIDER': False,
 'THUMBNAIL_SIZE': (120, 120)}
```

### ADMIN_CAN_APPROVE_ORDER

Type: bool

If true, orders for resource can be approved by admin of the customer project

### ANONYMOUS_USER_CAN_VIEW_OFFERINGS

Type: bool

Allow anonymous users to see shared offerings in active, paused and archived states

### DISABLE_SENDING_NOTIFICATIONS_ABOUT_RESOURCE_UPDATE

Type: bool

Disable only resource update events.

### ENABLE_STALE_RESOURCE_NOTIFICATIONS

Type: bool

Enable reminders to owners about resources of shared offerings that have not generated any cost for the last 3 months.

### MANAGER_CAN_APPROVE_ORDER

Type: bool

If true, orders for resource can be approved by manager of the customer project

### NOTIFY_ABOUT_RESOURCE_CHANGE

Type: bool

If true, notify users about resource changes from Marketplace perspective. Can generate duplicate events if plugins also log

### NOTIFY_STAFF_ABOUT_APPROVALS

Type: bool

If true, users with staff role are notified when request for order approval is generated

### OWNER_CAN_APPROVE_ORDER

Type: bool

If true, orders for resource can be approved by custom organization owner.

### OWNER_CAN_REGISTER_SERVICE_PROVIDER

Type: bool

Allow organization owner to request or mark its organization as service provider

### THUMBNAIL_SIZE

Type: tuple

Size of the thumbnail to generate when screenshot is uploaded for an offering.

## WALDUR_PID plugin

Default value:

```python
WALDUR_PID = {'DATACITE': {'API_URL': 'https://example.com',
              'COLLECTION_DOI': '',
              'PASSWORD': '',
              'PREFIX': '',
              'PUBLISHER': 'Waldur',
              'REPOSITORY_ID': ''}}
```

### DATACITE

Type: dict

Settings for integration of Waldur with Datacite PID service. Collection DOI is used to aggregate generated DOIs.

## WALDUR_SLURM plugin

Default value:

```python
WALDUR_SLURM = {'ALLOCATION_PREFIX': 'waldur_allocation_',
 'CUSTOMER_PREFIX': 'waldur_customer_',
 'DEFAULT_LIMITS': {'CPU': 16000, 'GPU': 400, 'RAM': 102400000},
 'ENABLED': False,
 'PRIVATE_KEY_PATH': '/etc/waldur/id_rsa',
 'PROJECT_PREFIX': 'waldur_project_'}
```

### ALLOCATION_PREFIX

Type: str

Prefix for SLURM account name corresponding to Waldur allocation

### CUSTOMER_PREFIX

Type: str

Prefix for SLURM account name corresponding to Waldur organization.

### DEFAULT_LIMITS

Type: dict

Default limits of account that are set when SLURM account is provisioned.

### ENABLED

Type: bool

Enable support for SLURM plugin in a deployment

### PRIVATE_KEY_PATH

Type: str

Path to private key file used as SSH identity file for accessing SLURM master.

### PROJECT_PREFIX

Type: str

Prefix for SLURM account name corresponding to Waldur project.

## Other variables

### DEFAULT_FROM_EMAIL

Type: str, default value: webmaster@localhost

Default email address to use for automated correspondence from Waldur.

### IMPORT_EXPORT_USE_TRANSACTIONS

Type: bool, default value: True

Controls if resource importing should use database transactions. Using transactions makes imports safer as a failure during import won’t import only part of the data set.

### IPSTACK_ACCESS_KEY

Type: Optional[str]

Unique authentication key used to gain access to the ipstack API.

### LANGUAGES

Type: List[Tuple[str, str]], default value: (('en', 'English'), ('et', 'Eesti'))

The list is a list of two-tuples in the format (language code, language name) – for example, ('ja', 'Japanese'). This specifies which languages are available for language selection.

### LANGUAGE_CODE

Type: str, default value: en

Represents the name of a default language.

### USE_PROTECTED_URL

Type: bool, default value: False

Protect media URLs using signed token.

### VERIFY_WEBHOOK_REQUESTS

Type: bool, default value: True

When webook is processed, requests verifies SSL certificates for HTTPS requests, just like a web browser.

