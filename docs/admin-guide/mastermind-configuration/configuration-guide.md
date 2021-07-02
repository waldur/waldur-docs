## WALDUR_AUTH_SOCIAL plugin

Default value: 
```python
WALDUR_AUTH_SOCIAL = {'EDUTEAMS_AUTH_URL': 'https://proxy.acc.eduteams.org/saml2sp/OIDC/authorization',
 'EDUTEAMS_CLIENT_ID': '',
 'EDUTEAMS_LABEL': 'Eduteams',
 'EDUTEAMS_SECRET': '',
 'EDUTEAMS_TOKEN_URL': 'https://proxy.acc.eduteams.org/OIDC/token',
 'EDUTEAMS_USERINFO_URL': 'https://proxy.acc.eduteams.org/OIDC/userinfo',
 'ENABLE_EDUTEAMS_SYNC': False,
 'FACEBOOK_CLIENT_ID': '',
 'FACEBOOK_SECRET': '',
 'KEYCLOAK_AUTH_URL': '',
 'KEYCLOAK_CLIENT_ID': '',
 'KEYCLOAK_LABEL': 'Keycloak',
 'KEYCLOAK_SECRET': '',
 'KEYCLOAK_TOKEN_URL': '',
 'KEYCLOAK_USERINFO_URL': '',
 'REMOTE_EDUTEAMS_ACCESS_TOKEN': '',
 'REMOTE_EDUTEAMS_TOKEN_URL': 'https://proxy.acc.researcher-access.org/OIDC/token',
 'REMOTE_EDUTEAMS_USERINFO_URL': 'https://proxy.acc.researcher-access.org/api/userinfo',
 'SMARTIDEE_CLIENT_ID': '',
 'SMARTIDEE_SECRET': '',
 'TARA_CLIENT_ID': '',
 'TARA_LABEL': 'Riigi Autentimisteenus',
 'TARA_SANDBOX': True,
 'TARA_SECRET': ''}
```

#### EDUTEAMS_AUTH_URL

Type: str

The authorization endpoint performs authentication of the end-user. This is done by redirecting the user agent to this endpoint.

#### EDUTEAMS_CLIENT_ID

Type: str

ID of application used for OAuth authentication.

#### EDUTEAMS_LABEL

Type: str

Label is used by HomePort for rendering login button.

#### EDUTEAMS_SECRET

Type: str

Application secret key.

#### EDUTEAMS_TOKEN_URL

Type: str

The token endpoint is used to obtain tokens.

#### EDUTEAMS_USERINFO_URL

Type: str

The userinfo endpoint returns standard claims about the authenticated user, and is protected by a bearer token.

#### ENABLE_EDUTEAMS_SYNC

Type: bool

Enable EduTeams synchronization with remote Waldur.

#### FACEBOOK_CLIENT_ID

Type: str

ID of application used for OAuth authentication.

#### FACEBOOK_SECRET

Type: str

Application secret key.

#### KEYCLOAK_AUTH_URL

Type: str

The authorization endpoint performs authentication of the end-user. This is done by redirecting the user agent to this endpoint.

#### KEYCLOAK_CLIENT_ID

Type: str

ID of application used for OAuth authentication.

#### KEYCLOAK_LABEL

Type: str

Label is used by HomePort for rendering login button.

#### KEYCLOAK_SECRET

Type: str

Application secret key.

#### KEYCLOAK_TOKEN_URL

Type: str

The token endpoint is used to obtain tokens.

#### KEYCLOAK_USERINFO_URL

Type: str

The userinfo endpoint returns standard claims about the authenticated user, and is protected by a bearer token.

#### REMOTE_EDUTEAMS_ACCESS_TOKEN

Type: str

Token is used to authenticate against user info endpoint.

#### REMOTE_EDUTEAMS_TOKEN_URL

Type: str

The token endpoint is used to obtain tokens.

#### REMOTE_EDUTEAMS_USERINFO_URL

Type: str

It allows to get user data based on userid aka CUID.

#### SMARTIDEE_CLIENT_ID

Type: str

ID of application used for OAuth authentication.

#### SMARTIDEE_SECRET

Type: str

Application secret key.

#### TARA_CLIENT_ID

Type: str

ID of application used for OAuth authentication.

#### TARA_LABEL

Type: str

You may set it to eIDAS, SmartID or MobileID make it more clear to the user which exact identity provider is configured or preferred for service provider.

#### TARA_SANDBOX

Type: bool

You should set it to False in order to switch to production mode.

#### TARA_SECRET

Type: str

Application secret key.

## WALDUR_CORE plugin

Default value: 
```python
WALDUR_CORE = {'ALLOW_SIGNUP_WITHOUT_INVITATION': True,
 'ATTACHMENT_LINK_MAX_AGE': datetime.timedelta(seconds=3600),
 'AUTHENTICATION_METHODS': ['LOCAL_SIGNIN'],
 'BACKEND_FIELDS_EDITABLE': True,
 'COUNTRIES': ['EE', 'LV', 'LT'],
 'CREATE_DEFAULT_PROJECT_ON_ORGANIZATION_CREATION': False,
 'CURRENCY_NAME': 'EUR',
 'EMAIL_CHANGE_MAX_AGE': datetime.timedelta(days=1),
 'ENABLE_ACCOUNTING_START_DATE': False,
 'ENABLE_GEOIP': True,
 'EXTENSIONS_AUTOREGISTER': True,
 'HOMEPORT_URL': 'https://example.com/',
 'HTTP_CHUNK_SIZE': 50,
 'INITIAL_CUSTOMER_AGREEMENT_NUMBER': 4000,
 'INVITATIONS_ENABLED': True,
 'INVITATION_CREATE_MISSING_USER': False,
 'INVITATION_DISABLE_MULTIPLE_ROLES': False,
 'INVITATION_LIFETIME': datetime.timedelta(days=7),
 'INVITATION_MAX_AGE': None,
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
 'PROTECT_USER_DETAILS_FOR_REGISTRATION_METHODS': [],
 'SELLER_COUNTRY_CODE': None,
 'SHOW_ALL_USERS': False,
 'SITE_ADDRESS': 'Default address',
 'SITE_EMAIL': 'Default email',
 'SITE_LOGO': None,
 'SITE_NAME': 'Waldur MasterMind',
 'SITE_PHONE': 'Default phone',
 'TOKEN_KEY': 'x-auth-token',
 'TOKEN_LIFETIME': datetime.timedelta(seconds=3600),
 'USE_ATOMIC_TRANSACTION': True,
 'VALIDATE_INVITATION_EMAIL': False}
```

#### ALLOW_SIGNUP_WITHOUT_INVITATION

Type: bool

Allow to signup without an invitation.

#### ATTACHMENT_LINK_MAX_AGE

Type: timedelta

Max age of secure token for media download.

#### AUTHENTICATION_METHODS

Type: List[str]

List of enabled authentication methods.

#### BACKEND_FIELDS_EDITABLE

Type: bool

Allows to control /admin writable fields. If this flag is disabled it is impossible to edit any field that corresponds to backend value via /admin. Such restriction allows to save information from corruption.

#### COUNTRIES

Type: List[str]

It is used in organization creation dialog in order to limit country choices to predefined set.

#### CREATE_DEFAULT_PROJECT_ON_ORGANIZATION_CREATION

Type: bool

Enables generation of the first project on organization creation.

#### CURRENCY_NAME

Type: str

It is used in marketplace order details and invoices for currency formatting.

#### EMAIL_CHANGE_MAX_AGE

Type: timedelta

Max age of change email request.

#### ENABLE_ACCOUNTING_START_DATE

Type: bool

Allows to enable accounting for organizations using value of accounting_start_date field.

#### ENABLE_GEOIP

Type: bool

Enable detection of coordinates of virtual machines.

#### EXTENSIONS_AUTOREGISTER

Type: bool

Defines whether extensions should be automatically registered.

#### HOMEPORT_URL

Type: str

It is used for rendering callback URL in HomePort.

#### HTTP_CHUNK_SIZE

Type: int

Chunk size for resource fetching from backend API. It is needed in order to avoid too long HTTP request error.

#### INITIAL_CUSTOMER_AGREEMENT_NUMBER

Type: int

Allows to tweak initial value of agreement number. It is assumed that organization owner should accept terms of services when organization is registered via Waldur HomePort.

#### INVITATIONS_ENABLED

Type: bool

Allows to disable invitations feature.

#### INVITATION_CREATE_MISSING_USER

Type: bool

Allow to create FreeIPA user using details specified in invitation if user does not exist yet.

#### INVITATION_DISABLE_MULTIPLE_ROLES

Type: bool

Do not allow user to grant multiple roles in the same project or organization using invitation.

#### INVITATION_LIFETIME

Type: timedelta

Defines for how long invitation remains valid.

#### INVITATION_MAX_AGE

Type: Optional[timedelta]

Max age of invitation token. It is used in approve and reject actions.

#### LOGGING_REPORT_DIRECTORY

Type: str

Directory where log files are located.

#### LOGGING_REPORT_INTERVAL

Type: timedelta

Files older that specified interval are filtered out.

#### NATIVE_NAME_ENABLED

Type: bool

Allows to render native name field in customer and user forms.

#### NOTIFICATIONS_PROFILE_CHANGES

Type: dict

Allows enabling notifications about profile changes of organization owners.

#### NOTIFICATION_SUBJECT

Type: str

It is used as a subject of email emitted by event logging hook.

#### ONLY_STAFF_CAN_INVITE_USERS

Type: bool

Allow to limit invitation management to staff only.

#### ONLY_STAFF_MANAGES_SERVICES

Type: bool

Allows to restrict provider management only to staff users.

#### OWNERS_CAN_MANAGE_OWNERS

Type: bool

Enables organization owners to manage other organization owners.

#### OWNER_CAN_MANAGE_CUSTOMER

Type: bool

Enables organization owners to create an organization.

#### PROTECT_USER_DETAILS_FOR_REGISTRATION_METHODS

Type: List[str]

List of authentication methods which are not allowed to update user details.

#### SELLER_COUNTRY_CODE

Type: Optional[str]

Specifies seller legal or effective country of registration or residence as an ISO 3166-1 alpha-2 country code. It is used for computing VAT charge rate.

#### SHOW_ALL_USERS

Type: bool

Indicates whether user can see all other users in `api/users/` endpoint.

#### SITE_ADDRESS

Type: str

It is used in marketplace order header.

#### SITE_EMAIL

Type: str

It is used in marketplace order header.

#### SITE_LOGO

Type: Optional[str]

It is used in marketplace order header.

#### SITE_NAME

Type: str

It is used in email notifications in order to refer to the current deployment in user-friendly way.

#### SITE_PHONE

Type: str

It is used in marketplace order header.

#### TOKEN_KEY

Type: str

Header for token authentication.

#### TOKEN_LIFETIME

Type: timedelta

Defines for how long user token should remain valid if there was no action from user.

#### USE_ATOMIC_TRANSACTION

Type: bool

Wrap action views in atomic transaction.

#### VALIDATE_INVITATION_EMAIL

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

#### BLACKLISTED_USERNAMES

Type: list

List of username that users are not allowed to select

#### ENABLED

Type: bool

Enable integration of identity provisioning in configured FreeIPA

#### GROUPNAME_PREFIX

Type: str

Prefix to be appended to all group names created in FreeIPA by Waldur

#### GROUP_SYNCHRONIZATION_ENABLED

Type: bool

Optionally disable creation of user groups in FreeIPA matching Waldur structure

#### HOSTNAME

Type: str

Hostname of FreeIPA server

#### PASSWORD

Type: str

Password of FreeIPA user with administrative privileges

#### USERNAME

Type: str

Username of FreeIPA user with administrative privileges

#### USERNAME_PREFIX

Type: str

Prefix to be appended to all usernames created in FreeIPA by Waldur

#### VERIFY_SSL

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

#### ENABLED

Type: bool

Enable HPC-specific hooks in Waldur deployment

#### EXTERNAL_AFFILIATIONS

Type: List[str]

List of user affiliations (eduPersonScopedAffiliation fields) that define if the user belongs to external organization.

#### EXTERNAL_CUSTOMER_UUID

Type: str

UUID of a Waldur organization (aka customer) where new external users would be added

#### EXTERNAL_EMAIL_PATTERNS

Type: List[str]

List of user email patterns (as regex) that define if the user belongs to external organization.

#### INTERNAL_AFFILIATIONS

Type: List[str]

List of user affiliations (eduPersonScopedAffiliation fields) that define if the user belongs to internal organization.

#### INTERNAL_CUSTOMER_UUID

Type: str

UUID of a Waldur organization (aka customer) where new internal users would be added

#### INTERNAL_EMAIL_PATTERNS

Type: List[str]

List of user email patterns (as regex) that define if the user belongs to internal organization.

#### INTERNAL_LIMITS

Type: dict

Overrided default values for SLURM offering to be created for users belonging to internal organization.

#### OFFERING_UUID

Type: str

UUID of a Waldur SLURM offering, which will be used for creating allocations for users

#### PLAN_UUID

Type: str

UUID of a Waldur SLURM offering plan, which will be used for creating allocations for users

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

#### ADMIN_CAN_APPROVE_ORDER

Type: bool

If true, orders for resource can be approved by admin of the customer project

#### ANONYMOUS_USER_CAN_VIEW_OFFERINGS

Type: bool

Allow anonymous users to see shared offerings in active, paused and archived states

#### DISABLE_SENDING_NOTIFICATIONS_ABOUT_RESOURCE_UPDATE

Type: bool

Disable only resource update events.

#### ENABLE_STALE_RESOURCE_NOTIFICATIONS

Type: bool

Enable reminders to owners about resources of shared offerings that have not generated any cost for the last 3 months.

#### MANAGER_CAN_APPROVE_ORDER

Type: bool

If true, orders for resource can be approved by manager of the customer project

#### NOTIFY_ABOUT_RESOURCE_CHANGE

Type: bool

If true, notify users about resource changes from Marketplace perspective. Can generate duplicate events if plugins also log

#### NOTIFY_STAFF_ABOUT_APPROVALS

Type: bool

If true, users with staff role are notified when request for order approval is generated

#### OWNER_CAN_APPROVE_ORDER

Type: bool

If true, orders for resource can be approved by custom organization owner.

#### OWNER_CAN_REGISTER_SERVICE_PROVIDER

Type: bool

Allow organization owner to request or mark its organization as service provider

#### THUMBNAIL_SIZE

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

#### DATACITE

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

#### ALLOCATION_PREFIX

Type: str

Prefix for SLURM account name corresponding to Waldur allocation

#### CUSTOMER_PREFIX

Type: str

Prefix for SLURM account name corresponding to Waldur organization.

#### DEFAULT_LIMITS

Type: dict

Default limits of account that are set when SLURM account is provisioned.

#### ENABLED

Type: bool

Enable support for SLURM plugin in a deployment

#### PRIVATE_KEY_PATH

Type: str

Path to private key file used as SSH identity file for accessing SLURM master.

#### PROJECT_PREFIX

Type: str

Prefix for SLURM account name corresponding to Waldur project.

## Other variables

#### DEFAULT_FROM_EMAIL

Type: str, default value: webmaster@localhost

Default email address to use for automated correspondence from Waldur.

#### IMPORT_EXPORT_USE_TRANSACTIONS

Type: bool, default value: True

Controls if resource importing should use database transactions. Using transactions makes imports safer as a failure during import won’t import only part of the data set.

#### IPSTACK_ACCESS_KEY

Type: Optional[str]

Unique authentication key used to gain access to the ipstack API.

#### LANGUAGES

Type: List[Tuple[str, str]], default value: (('en', 'English'), ('et', 'Eesti'))

The list is a list of two-tuples in the format (language code, language name) – for example, ('ja', 'Japanese'). This specifies which languages are available for language selection.

#### USE_PROTECTED_URL

Type: bool, default value: False

Protect media URLs using signed token.

#### VERIFY_WEBHOOK_REQUESTS

Type: bool, default value: True

When webook is processed, requests verifies SSL certificates for HTTPS requests, just like a web browser.

