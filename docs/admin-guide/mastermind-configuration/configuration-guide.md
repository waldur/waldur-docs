# Configuration guide

## WALDUR_ATLASSIAN plugin

Default value:

```python
WALDUR_ATLASSIAN = {'DEFAULT_OFFERING_ISSUE_TYPE': 'Service Request',
 'EMAIL': '',
 'EXCLUDED_ATTACHMENT_TYPES': [],
 'ISSUE': {'caller_field': 'Caller',
           'impact_field': 'Impact',
           'reporter_field': 'Original Reporter',
           'request_feedback': 'Request feedback',
           'satisfaction_field': 'Customer satisfaction',
           'sla_field': 'Time to first response',
           'type_of_linked_issue': 'Relates',
           'types': ['Informational',
                     'Service Request',
                     'Change Request',
                     'Incident']},
 'MAP_WALDUR_USERS_TO_SERVICEDESK_AGENTS': False,
 'PASSWORD': 'PASSWORD',
 'PROJECT': {'key': 'PROJECT'},
 'PULL_PRIORITIES': True,
 'SERVER': 'http://example.com/',
 'STRANGE_SETTING': 1,
 'TOKEN': '',
 'USERNAME': 'USERNAME',
 'USE_AUTOMATIC_REQUEST_MAPPING': True,
 'USE_OLD_API': False,
 'USE_TEENAGE_API': False,
 'VERIFY_SSL': False}
```

### DEFAULT_OFFERING_ISSUE_TYPE

Type: str

Issue type

### EMAIL

Type: str

Email for access user

### EXCLUDED_ATTACHMENT_TYPES

Type: list

List of attachment types

### ISSUE

Type: dict

Issue-related settings

### MAP_WALDUR_USERS_TO_SERVICEDESK_AGENTS

Type: bool

Toggler for mapping between waldur user and service desk agents

### PASSWORD

Type: str

Password for access user

### PROJECT

Type: dict

Project-related settings

### PULL_PRIORITIES

Type: bool

Pull priorities

### SERVER

Type: str

Atlassian server URL

### STRANGE_SETTING

Type: int

### TOKEN

Type: str

Token for access user

### USERNAME

Type: str

Username for access user

### USE_AUTOMATIC_REQUEST_MAPPING

Type: bool

Toggler for automatic request mapping

### USE_OLD_API

Type: bool

Toggler for legacy API usage

### USE_TEENAGE_API

Type: bool

Toggler for teenage API usage

### VERIFY_SSL

Type: bool

Toggler for SSL verification

## WALDUR_AUTH_SAML2 plugin

Default value:

```python
WALDUR_AUTH_SAML2 = {'ALLOW_TO_SELECT_IDENTITY_PROVIDER': True,
 'ATTRIBUTE_MAP_DIR': '/etc/waldur/saml2/attributemaps',
 'AUTHN_REQUESTS_SIGNED': 'true',
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
 'MANAGEMENT_URL': '',
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

### MANAGEMENT_URL

Type: str

The endpoint for user details management.

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
WALDUR_AUTH_SOCIAL = {'ENABLE_EDUTEAMS_SYNC': False,
 'REMOTE_EDUTEAMS_CLIENT_ID': '',
 'REMOTE_EDUTEAMS_ENABLED': False,
 'REMOTE_EDUTEAMS_REFRESH_TOKEN': '',
 'REMOTE_EDUTEAMS_SECRET': '',
 'REMOTE_EDUTEAMS_TOKEN_URL': 'https://proxy.acc.researcher-access.org/OIDC/token',
 'REMOTE_EDUTEAMS_USERINFO_URL': 'https://proxy.acc.researcher-access.org/api/userinfo'}
```

### ENABLE_EDUTEAMS_SYNC

Type: bool

Enable eduTEAMS synchronization with remote Waldur.

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

## WALDUR_CORE plugin

Default value:

```python
WALDUR_CORE = {'ATTACHMENT_LINK_MAX_AGE': datetime.timedelta(seconds=3600),
 'AUTHENTICATION_METHODS': ['LOCAL_SIGNIN'],
 'BACKEND_FIELDS_EDITABLE': True,
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
 'EMAIL_CHANGE_MAX_AGE': datetime.timedelta(days=1),
 'ENABLE_ACCOUNTING_START_DATE': False,
 'ENABLE_GEOIP': True,
 'EXTENSIONS_AUTOREGISTER': True,
 'EXTERNAL_LINKS': [],
 'GOOGLE_ANALYTICS_ID': '',
 'GROUP_INVITATION_LIFETIME': datetime.timedelta(days=7),
 'HOMEPORT_SENTRY_DSN': None,
 'HOMEPORT_SENTRY_ENVIRONMENT': 'waldur-production',
 'HOMEPORT_SENTRY_TRACES_SAMPLE_RATE': 0.01,
 'HOMEPORT_URL': 'https://example.com/',
 'HTTP_CHUNK_SIZE': 50,
 'INVITATIONS_ENABLED': True,
 'INVITATION_CIVIL_NUMBER_LABEL': '',
 'INVITATION_CREATE_MISSING_USER': False,
 'INVITATION_DISABLE_MULTIPLE_ROLES': False,
 'INVITATION_LIFETIME': datetime.timedelta(days=7),
 'INVITATION_MAX_AGE': None,
 'INVITATION_TAX_NUMBER_LABEL': '',
 'LOCAL_IDP_LABEL': 'Local DB',
 'LOCAL_IDP_MANAGEMENT_URL': '',
 'LOCAL_IDP_NAME': 'Local DB',
 'LOCAL_IDP_PROTECTED_FIELDS': [],
 'LOGGING_REPORT_DIRECTORY': '/var/log/waldur',
 'LOGGING_REPORT_INTERVAL': datetime.timedelta(days=7),
 'MASTERMIND_URL': '',
 'NATIVE_NAME_ENABLED': False,
 'NOTIFICATIONS_PROFILE_CHANGES': {'ENABLE_OPERATOR_OWNER_NOTIFICATIONS': False,
                                   'FIELDS': ('email',
                                              'phone_number',
                                              'job_title'),
                                   'OPERATOR_NOTIFICATION_EMAILS': []},
 'NOTIFICATION_SUBJECT': 'Notifications from Waldur',
 'ONLY_STAFF_CAN_INVITE_USERS': False,
 'ONLY_STAFF_MANAGES_SERVICES': False,
 'OWNERS_CAN_MANAGE_OWNERS': False,
 'OWNER_CAN_MANAGE_CUSTOMER': False,
 'PROTECT_USER_DETAILS_FOR_REGISTRATION_METHODS': [],
 'SELLER_COUNTRY_CODE': None,
 'SHOW_ALL_USERS': False,
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

### COUNTRIES

Type: List[str]

It is used in organization creation dialog in order to limit country choices to predefined set.

### CREATE_DEFAULT_PROJECT_ON_ORGANIZATION_CREATION

Type: bool

Enables generation of the first project on organization creation.

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

### GOOGLE_ANALYTICS_ID

Type: str

Identifier associated with your account and used by Google Analytics to collect the data.

### GROUP_INVITATION_LIFETIME

Type: timedelta

Defines for how long group invitation remains valid.

### HOMEPORT_SENTRY_DSN

Type: Optional[str]

Sentry Data Source Name for Waldur HomePort project.

### HOMEPORT_SENTRY_ENVIRONMENT

Type: str

Sentry environment name for Waldur Homeport.

### HOMEPORT_SENTRY_TRACES_SAMPLE_RATE

Type: float

Percentage of transactions sent to Sentry for tracing.

### HOMEPORT_URL

Type: str

It is used for rendering callback URL in HomePort.

### HTTP_CHUNK_SIZE

Type: int

Chunk size for resource fetching from backend API. It is needed in order to avoid too long HTTP request error.

### INVITATIONS_ENABLED

Type: bool

Allows to disable invitations feature.

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

### LOCAL_IDP_LABEL

Type: str

The label of local auth.

### LOCAL_IDP_MANAGEMENT_URL

Type: str

The URL for management of local user details.

### LOCAL_IDP_NAME

Type: str

The name of local auth.

### LOCAL_IDP_PROTECTED_FIELDS

Type: List[str]

The list of protected fields for local IdP.

### LOGGING_REPORT_DIRECTORY

Type: str

Directory where log files are located.

### LOGGING_REPORT_INTERVAL

Type: timedelta

Files older that specified interval are filtered out.

### MASTERMIND_URL

Type: str

It is used for rendering callback URL in MasterMind.

### NATIVE_NAME_ENABLED

Type: bool

Allows to render native name field in customer and user forms.

### NOTIFICATIONS_PROFILE_CHANGES

Type: dict

Configure notifications about profile changes of organization owners.

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

### PROTECT_USER_DETAILS_FOR_REGISTRATION_METHODS

Type: List[str]

List of authentication methods which are not allowed to update user details.

### SELLER_COUNTRY_CODE

Type: Optional[str]

Specifies seller legal or effective country of registration or residence as an ISO 3166-1 alpha-2 country code. It is used for computing VAT charge rate.

### SHOW_ALL_USERS

Type: bool

Indicates whether user can see all other users in `api/users/` endpoint.

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
 'EXTERNAL_LIMITS': {},
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

### EXTERNAL_LIMITS

Type: dict

Overrided default values for SLURM offering to be created for users belonging to external organization.

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
WALDUR_MARKETPLACE = {'ANONYMOUS_USER_CAN_VIEW_OFFERINGS': True,
 'ANONYMOUS_USER_CAN_VIEW_PLANS': True,
 'DISABLE_SENDING_NOTIFICATIONS_ABOUT_RESOURCE_UPDATE': True,
 'ENABLE_RESOURCE_END_DATE': True,
 'ENABLE_STALE_RESOURCE_NOTIFICATIONS': False,
 'NOTIFY_ABOUT_RESOURCE_CHANGE': True,
 'NOTIFY_STAFF_ABOUT_APPROVALS': False,
 'OWNER_CAN_REGISTER_SERVICE_PROVIDER': False,
 'TELEMETRY_ENABLED': True,
 'TELEMETRY_URL': 'https://telemetry.waldur.com/',
 'TELEMETRY_VERSION': 1,
 'THUMBNAIL_SIZE': (120, 120)}
```

### ANONYMOUS_USER_CAN_VIEW_OFFERINGS

Type: bool

Allow anonymous users to see shared offerings in active, paused and archived states

### ANONYMOUS_USER_CAN_VIEW_PLANS

Type: bool

Allow anonymous users to see plans

### DISABLE_SENDING_NOTIFICATIONS_ABOUT_RESOURCE_UPDATE

Type: bool

Disable only resource update events.

### ENABLE_RESOURCE_END_DATE

Type: bool

Allow to view and update resource end date.

### ENABLE_STALE_RESOURCE_NOTIFICATIONS

Type: bool

Enable reminders to owners about resources of shared offerings that have not generated any cost for the last 3 months.

### NOTIFY_ABOUT_RESOURCE_CHANGE

Type: bool

If true, notify users about resource changes from Marketplace perspective. Can generate duplicate events if plugins also log

### NOTIFY_STAFF_ABOUT_APPROVALS

Type: bool

If true, users with staff role are notified when request for order approval is generated

### OWNER_CAN_REGISTER_SERVICE_PROVIDER

Type: bool

Allow organization owner to request or mark its organization as service provider

### TELEMETRY_ENABLED

Type: bool

Enable telemetry.

### TELEMETRY_URL

Type: str

URL for sending telemetry data.

### TELEMETRY_VERSION

Type: int

Telemetry service version.

### THUMBNAIL_SIZE

Type: tuple

Size of the thumbnail to generate when screenshot is uploaded for an offering.

## WALDUR_MARKETPLACE_REMOTE_SLURM plugin

Default value:

```python
WALDUR_MARKETPLACE_REMOTE_SLURM = {'USE_WALDUR_USERNAMES': True}
```

### USE_WALDUR_USERNAMES

Type: bool

Fetch usernames from Waldur rather then FreeIPA profiles.

## WALDUR_MARKETPLACE_SCRIPT plugin

Default value:

```python
WALDUR_MARKETPLACE_SCRIPT = {'DOCKER_CLIENT': {'base_url': 'unix://var/run/docker.sock'},
 'DOCKER_IMAGES': {'python': {'command': 'python',
                              'image': 'python:3.8-alpine'},
                   'shell': {'command': 'sh', 'image': 'alpine:3'}},
 'DOCKER_REMOVE_CONTAINER': True,
 'DOCKER_RUN_OPTIONS': {'mem_limit': '512m'},
 'DOCKER_SCRIPT_DIR': None,
 'K8S_CONFIG_PATH': '~/.kube/config',
 'K8S_JOB_TIMEOUT': 1800,
 'K8S_NAMESPACE': 'default',
 'SCRIPT_RUN_MODE': 'docker'}
```

### DOCKER_CLIENT

Type: dict

Options for docker client. See also: <https://docker-py.readthedocs.io/en/stable/client.html#docker.client.DockerClient>

### DOCKER_IMAGES

Type: dict

Key is command to execute script, value is a dictionary of image name and command.

### DOCKER_REMOVE_CONTAINER

Type: bool

Remove Docker container after script execution

### DOCKER_RUN_OPTIONS

Type: dict

Options for docker runtime. See also: <https://docker-py.readthedocs.io/en/stable/containers.html#docker.models.containers.ContainerCollection.run>

### DOCKER_SCRIPT_DIR

Type: Optional[str]

Path to folder on executor machine where to create temporary submission scripts. If None uses OS-dependent location. OS X users, see <https://github.com/docker/for-mac/issues/1532>

### K8S_CONFIG_PATH

Type: str

Path to Kubernetes configuration file

### K8S_JOB_TIMEOUT

Type: int

Timeout for execution of one Kubernetes job in seconds

### K8S_NAMESPACE

Type: str

Kubernetes namespace where jobs will be executed

### SCRIPT_RUN_MODE

Type: str

Type of jobs deployment. Valid values: "docker" for simple docker deployment, "k8s" for Kubernetes-based one

## WALDUR_OPENSTACK plugin

Default value:

```python
WALDUR_OPENSTACK = {'DEFAULT_BLACKLISTED_USERNAMES': ['admin', 'service'],
 'DEFAULT_SECURITY_GROUPS': ({'description': 'Security group for any access',
                              'name': 'allow-all',
                              'rules': ({'cidr': '0.0.0.0/0',
                                         'icmp_code': -1,
                                         'icmp_type': -1,
                                         'protocol': 'icmp'},
                                        {'cidr': '0.0.0.0/0',
                                         'from_port': 1,
                                         'protocol': 'tcp',
                                         'to_port': 65535})},
                             {'description': 'Security group for secure shell '
                                             'access',
                              'name': 'ssh',
                              'rules': ({'cidr': '0.0.0.0/0',
                                         'from_port': 22,
                                         'protocol': 'tcp',
                                         'to_port': 22},)},
                             {'description': 'Security group for ping',
                              'name': 'ping',
                              'rules': ({'cidr': '0.0.0.0/0',
                                         'icmp_code': -1,
                                         'icmp_type': -1,
                                         'protocol': 'icmp'},)},
                             {'description': 'Security group for remove '
                                             'desktop access',
                              'name': 'rdp',
                              'rules': ({'cidr': '0.0.0.0/0',
                                         'from_port': 3389,
                                         'protocol': 'tcp',
                                         'to_port': 3389},)},
                             {'description': 'Security group for http and '
                                             'https access',
                              'name': 'web',
                              'rules': ({'cidr': '0.0.0.0/0',
                                         'from_port': 80,
                                         'protocol': 'tcp',
                                         'to_port': 80},
                                        {'cidr': '0.0.0.0/0',
                                         'from_port': 443,
                                         'protocol': 'tcp',
                                         'to_port': 443})}),
 'SUBNET': {'ALLOCATION_POOL_END': '{first_octet}.{second_octet}.{third_octet}.200',
            'ALLOCATION_POOL_START': '{first_octet}.{second_octet}.{third_octet}.10'},
 'TENANT_CREDENTIALS_VISIBLE': False}
```

### DEFAULT_BLACKLISTED_USERNAMES

Type: list

Usernames that cannot be created by Waldur in OpenStack

### DEFAULT_SECURITY_GROUPS

Type: tuple

Default security groups and rules created in each of the provisioned OpenStack tenants

### SUBNET

Type: dict

Default allocation pool for auto-created internal network

### TENANT_CREDENTIALS_VISIBLE

Type: bool

If true, generated credentials of a tenant are exposed to project users

## WALDUR_OPENSTACK_TENANT plugin

Default value:

```python
WALDUR_OPENSTACK_TENANT = {'ALLOW_CUSTOMER_USERS_OPENSTACK_CONSOLE_ACCESS': True,
 'ALLOW_DIRECT_EXTERNAL_NETWORK_CONNECTION': False,
 'MAX_CONCURRENT_PROVISION': {'OpenStackTenant.Instance': 4,
                              'OpenStackTenant.Snapshot': 4,
                              'OpenStackTenant.Volume': 4},
 'REQUIRE_AVAILABILITY_ZONE': False}
```

### ALLOW_CUSTOMER_USERS_OPENSTACK_CONSOLE_ACCESS

Type: bool

If true, customer users would be offered actions for accessing OpenStack Console

### ALLOW_DIRECT_EXTERNAL_NETWORK_CONNECTION

Type: bool

If true, allow connecting of Instances directly to external networks

### MAX_CONCURRENT_PROVISION

Type: dict

Maximum parallel executions of provisioning operations for OpenStackTenant resources

### REQUIRE_AVAILABILITY_ZONE

Type: bool

If true, specification of availability zone during provisioning will become mandatory

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

## WALDUR_SUPPORT plugin

Default value:

```python
WALDUR_SUPPORT = {'ACTIVE_BACKEND_TYPE': 'atlassian',
 'DISPLAY_REQUEST_TYPE': True,
 'ENABLED': False}
```

### ACTIVE_BACKEND_TYPE

Type: str

Type of support backend. Possible values: atlassian, zammad

### DISPLAY_REQUEST_TYPE

Type: bool

Toggler for request type displaying

### ENABLED

Type: bool

Toggler for Support plugin

## WALDUR_ZAMMAD plugin

Default value:

```python
WALDUR_ZAMMAD = {'COMMENT_COOLDOWN_DURATION': 5,
 'ZAMMAD_API_URL': '',
 'ZAMMAD_ARTICLE_TYPE': 'email',
 'ZAMMAD_COMMENT_MARKER': 'Created by Waldur',
 'ZAMMAD_COMMENT_PREFIX': 'User: {name}',
 'ZAMMAD_GROUP': '',
 'ZAMMAD_TOKEN': ''}
```

### COMMENT_COOLDOWN_DURATION

Type: int

Time in minutes. Time in minutes while comment deletion is available <https://github.com/zammad/zammad/issues/2687/>, <https://github.com/zammad/zammad/issues/3086/>

### ZAMMAD_API_URL

Type: str

Address of Zammad server. For example <http://localhost:8080/>

### ZAMMAD_ARTICLE_TYPE

Type: str

Type of a comment.Default is email because it allows support to reply to tickets directly in Zammad<https://docs.zammad.org/en/latest/api/ticket/articles.html#articles/>

### ZAMMAD_COMMENT_MARKER

Type: str

Marker for comment.Used for separating comments made via Waldur from natively added comments.

### ZAMMAD_COMMENT_PREFIX

Type: str

Comment prefix with user info.

### ZAMMAD_GROUP

Type: str

The name of the group to which the ticket will be added. If not specified, the first group will be used.

### ZAMMAD_TOKEN

Type: str

Authorization token.

## Other variables

### DEFAULT_FROM_EMAIL

Type: str, default value: webmaster@localhost

Default email address to use for automated correspondence from Waldur.

### DEFAULT_REPLY_TO_EMAIL

Type: str

Default email address to use for email replies.

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

