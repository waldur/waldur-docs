# Keycloak

Waldur supports integration with [Keycloak](http://keycloak.org/) identity manager.

Below is a guide to configure Keycloak OpenID Connect client and Waldur intergration.

## Configuring Keycloak

Instructions below are aimed to provide a basic configuration of Keycloak, please refer to Keycloak documentation for full details.

1. Login to admin interface of Keycloak.
2. Create a new realm (or use existing)
 [![New realm](img/keycloak-add-realm.png)](img/keycloak-add-realm.png)
3. Open a menu with a list of clients.
 [![List clients](img/keycloak-client-list.png)](img/keycloak-client-list.png)
4. Add a new client for Waldur.
 [![Add client](img/keycloak-add-client.png)](img/keycloak-add-client.png)
5. Change client's access type to "confidential".
 [![Set access type](img/keycloak-client-access-type.png)](img/keycloak-client-access-type.png)
6. Change client's Valid redirect URIs to "*".
 [![Valid redirect URIs](img/keycloak-client-redirect.png)](img/keycloak-client-redirect.png)
7. You can get secret code for the client configuration
 [![Secret code](img/keycloak-client-secret.png)](img/keycloak-client-secret.png)
8. You can find the settings required for configuration of Waldur under the following path on your Keycloak deployment (change `test-waldur` to the realm that you are using):  `/auth/realms/test-waldur/.well-known/openid-configuration`

## Configuring Waldur

1. Add Keycloak related configuration to Mastermind's `override.py`:

    ```python
    WALDUR_AUTH_SOCIAL.update({'KEYCLOAK_AUTH_URL': 'https://KEYCLOAK_ADDRESS:8080/auth/realms/test-waldur/.well-known/openid-configuration',
     'KEYCLOAK_CLIENT_ID': 'CLIENT_ID',
     'KEYCLOAK_SECRET': 'SECRET'
     'KEYCLOAK_TOKEN_URL': 'https://KEYCLOAK_ADDRESS:8080/auth/realms/test-waldur/protocol/openid-connect/token',
     'KEYCLOAK_USERINFO_URL': 'https://KEYCLOAK_ADDRESS:8080/auth/realms/test-waldur/protocol/openid-connect/userinfo'
    })
    ```

2. Make sure `SOCIAL_SIGNUP` is added to the list of available authentication methods:

    ```python
    WALDUR_CORE['AUTHENTICATION_METHODS'] = ["LOCAL_SIGNIN", "SOCIAL_SIGNUP"]
    ```

    Full Keycloak related configuration settings are available at [Mastermind configuration file reference](../mastermind-configuration/configuration-guide.md)
