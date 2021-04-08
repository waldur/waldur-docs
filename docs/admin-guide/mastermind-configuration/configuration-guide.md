| **Name** | **Type** | **Description** | **Default value** |
| -------- | -------- | --------------- | ----------------- |
| IPSTACK_ACCESS_KEY | Optional[str] | Unique authentication key used to gain access to the ipstack API. | None | 
| WALDUR_CORE.AUTHENTICATION_METHODS | List[str] | List of enabled authentication methods. | ['LOCAL_SIGNIN'] | 
| WALDUR_CORE.SITE_LOGO | Optional[str] | It is used in marketplace order header. | None | 
| WALDUR_CORE.COUNTRIES | List[str] | It is used in organization creation dialog in order to limit country choices to predefined set. | ['EE', 'LV', 'LT'] | 
| WALDUR_CORE.INVITATION_MAX_AGE | Optional[timedelta] | Max age of invitation token. It is used in approve and reject actions. | None | 
| WALDUR_CORE.PROTECT_USER_DETAILS_FOR_REGISTRATION_METHODS | List[str] | List of authentication methods which are not allowed to update user details. | [] | 
| WALDUR_CORE.SELLER_COUNTRY_CODE | Optional[str] | Specifies seller legal or effective country of registration or residence as an ISO 3166-1 alpha-2 country code. It is used for computing VAT charge rate. | None | 
| WALDUR_CORE.EXTENSIONS_AUTOREGISTER | bool | Defines whether extensions should be automatically registered. | True | 
| WALDUR_CORE.TOKEN_KEY | str | Header for token authentication. | x-auth-token | 
| WALDUR_CORE.INVITATIONS_ENABLED | bool | Allows to disable invitations feature. | True | 
| WALDUR_CORE.ALLOW_SIGNUP_WITHOUT_INVITATION | bool | Allow to signup without an invitation. | True | 
| WALDUR_CORE.VALIDATE_INVITATION_EMAIL | bool | Ensure that invitation and user emails match. | False | 
| WALDUR_CORE.TOKEN_LIFETIME | timedelta | Defines for how long user token should remain valid if there was no action from user. | 1:00:00 | 
| WALDUR_CORE.INVITATION_LIFETIME | timedelta | Defines for how long invitation remains valid. | 7 days, 0:00:00 | 
| WALDUR_CORE.OWNERS_CAN_MANAGE_OWNERS | bool | Enables organization owners to manage other organization owners. | False | 
| WALDUR_CORE.OWNER_CAN_MANAGE_CUSTOMER | bool | Enables organization owners to create an organization. | False | 
| WALDUR_CORE.BACKEND_FIELDS_EDITABLE | bool | Allows to control /admin writable fields. If this flag is disabled it is impossible to edit any field that corresponds to backend value via /admin. Such restriction allows to save information from corruption. | True | 
| WALDUR_CORE.INITIAL_CUSTOMER_AGREEMENT_NUMBER | int | Allows to tweak initial value of agreement number. It is assumed that organization owner should accept terms of services when organization is registered via Waldur HomePort. | 4000 | 
| WALDUR_CORE.CREATE_DEFAULT_PROJECT_ON_ORGANIZATION_CREATION | bool | Enables generation of the first project on organization creation. | False | 
| WALDUR_CORE.ONLY_STAFF_MANAGES_SERVICES | bool | Allows to restrict provider management only to staff users. | False | 
| WALDUR_CORE.NATIVE_NAME_ENABLED | bool | Allows to render native name field in customer and user forms. | False | 
| WALDUR_CORE.SITE_NAME | str | It is used in email notifications in order to refer to the current deployment in user-friendly way. | Waldur MasterMind | 
| WALDUR_CORE.SITE_ADDRESS | str | It is used in marketplace order header. | Default address | 
| WALDUR_CORE.SITE_EMAIL | str | It is used in marketplace order header. | Default email | 
| WALDUR_CORE.SITE_PHONE | str | It is used in marketplace order header. | Default phone | 
| WALDUR_CORE.CURRENCY_NAME | str | It is used in marketplace order details and invoices for currency formatting. | EUR | 
| WALDUR_CORE.NOTIFICATIONS_PROFILE_CHANGES | dict | Allows enabling notifications about profile changes of organization owners. | {'ENABLED': True, 'FIELDS': ('email', 'phone_number', 'job_title')} | 
| WALDUR_CORE.ENABLE_ACCOUNTING_START_DATE | bool | Allows to enable accounting for organizations using value of accounting_start_date field. | False | 
| WALDUR_CORE.USE_ATOMIC_TRANSACTION | bool | Wrap action views in atomic transaction. | True | 
| WALDUR_CORE.NOTIFICATION_SUBJECT | str | It is used as a subject of email emitted by event logging hook. | Notifications from Waldur | 
| WALDUR_CORE.LOGGING_REPORT_DIRECTORY | str | Directory where log files are located. | /var/log/waldur | 
| WALDUR_CORE.LOGGING_REPORT_INTERVAL | timedelta | Files older that specified interval are filtered out. | 7 days, 0:00:00 | 
| WALDUR_CORE.HTTP_CHUNK_SIZE | int | Chunk size for resource fetching from backend API. It is needed in order to avoid too long HTTP request error. | 50 | 
| WALDUR_CORE.ONLY_STAFF_CAN_INVITE_USERS | bool | Allow to limit invitation management to staff only. | False | 
| WALDUR_CORE.INVITATION_CREATE_MISSING_USER | bool | Allow to create FreeIPA user using details specified in invitation if user does not exist yet. | False | 
| WALDUR_CORE.INVITATION_DISABLE_MULTIPLE_ROLES | bool | Do not allow user to grant multiple roles in the same project or organization using invitation. | False | 
| WALDUR_CORE.ATTACHMENT_LINK_MAX_AGE | timedelta | Max age of secure token for media download. | 1:00:00 | 
| WALDUR_CORE.EMAIL_CHANGE_MAX_AGE | timedelta | Max age of change email request. | 1 day, 0:00:00 | 
| WALDUR_CORE.HOMEPORT_URL | str | It is used for rendering callback URL in HomePort. | https://example.com/ | 
| WALDUR_CORE.ENABLE_GEOIP | bool | Enable detection of coordinates of virtual machines. | True | 
| WALDUR_CORE.SHOW_ALL_USERS | bool | Indicates whether user can see all other users in `api/users/` endpoint. | False | 
| WALDUR_AUTH_SOCIAL.FACEBOOK_SECRET | str | Application secret key. |  | 
| WALDUR_AUTH_SOCIAL.FACEBOOK_CLIENT_ID | str | ID of application used for OAuth authentication. |  | 
| WALDUR_AUTH_SOCIAL.SMARTIDEE_SECRET | str | Application secret key. |  | 
| WALDUR_AUTH_SOCIAL.SMARTIDEE_CLIENT_ID | str | ID of application used for OAuth authentication. |  | 
| WALDUR_AUTH_SOCIAL.TARA_SECRET | str | Application secret key. |  | 
| WALDUR_AUTH_SOCIAL.TARA_CLIENT_ID | str | ID of application used for OAuth authentication. |  | 
| WALDUR_AUTH_SOCIAL.TARA_SANDBOX | bool | You should set it to False in order to switch to production mode. | True | 
| WALDUR_AUTH_SOCIAL.TARA_LABEL | str | You may set it to eIDAS, SmartID or MobileID make it more clear to the user which exact identity provider is configured or preferred for service provider. | Riigi Autentimisteenus | 
| WALDUR_AUTH_SOCIAL.KEYCLOAK_LABEL | str | Label is used by HomePort for rendering login button. | Keycloak | 
| WALDUR_AUTH_SOCIAL.KEYCLOAK_CLIENT_ID | str | ID of application used for OAuth authentication. |  | 
| WALDUR_AUTH_SOCIAL.KEYCLOAK_SECRET | str | Application secret key. |  | 
| WALDUR_AUTH_SOCIAL.KEYCLOAK_AUTH_URL | str | The authorization endpoint performs authentication of the end-user. This is done by redirecting the user agent to this endpoint. |  | 
| WALDUR_AUTH_SOCIAL.KEYCLOAK_TOKEN_URL | str | The token endpoint is used to obtain tokens. |  | 
| WALDUR_AUTH_SOCIAL.KEYCLOAK_USERINFO_URL | str | The userinfo endpoint returns standard claims about the authenticated user, and is protected by a bearer token. |  | 
| WALDUR_AUTH_SOCIAL.EDUTEAMS_LABEL | str | Label is used by HomePort for rendering login button. | Eduteams | 
| WALDUR_AUTH_SOCIAL.EDUTEAMS_CLIENT_ID | str | ID of application used for OAuth authentication. |  | 
| WALDUR_AUTH_SOCIAL.EDUTEAMS_SECRET | str | Application secret key. |  | 
| WALDUR_AUTH_SOCIAL.EDUTEAMS_AUTH_URL | str | The authorization endpoint performs authentication of the end-user. This is done by redirecting the user agent to this endpoint. | https://proxy.acc.eduteams.org/saml2sp/OIDC/authorization | 
| WALDUR_AUTH_SOCIAL.EDUTEAMS_TOKEN_URL | str | The token endpoint is used to obtain tokens. | https://proxy.acc.eduteams.org/OIDC/token | 
| WALDUR_AUTH_SOCIAL.EDUTEAMS_USERINFO_URL | str | The userinfo endpoint returns standard claims about the authenticated user, and is protected by a bearer token. | https://proxy.acc.eduteams.org/OIDC/userinfo | 
| WALDUR_AUTH_SOCIAL.REMOTE_EDUTEAMS_ACCESS_TOKEN | str | Token is used to authenticate against user info endpoint. |  | 
| WALDUR_AUTH_SOCIAL.REMOTE_EDUTEAMS_USERINFO_URL | str | It allows to get user data based on userid aka CUID. |  | 
| USE_PROTECTED_URL | bool | Protect media URLs using signed token. | False | 
| VERIFY_WEBHOOK_REQUESTS | bool | When webook is processed, requests verifies SSL certificates for HTTPS requests, just like a web browser. | True | 
| DEFAULT_FROM_EMAIL | str | Default email address to use for automated correspondence from Waldur. | webmaster@localhost | 
| CONVERT_MEDIA_URLS_TO_MASTERMIND_NETLOC | bool | None | False | 
| IMPORT_EXPORT_USE_TRANSACTIONS | bool | Controls if resource importing should use database transactions. Using transactions makes imports safer as a failure during import won’t import only part of the data set. | True | 
