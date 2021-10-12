# Keycloak

Waldur supports integration with [Keycloak](http://keycloak.org/) identity manager.

To enable it, please register a new client for Waldur deployment and set configuration settings for Keycloak.
Check [configuration guide](../mastermind-configuration/configuration-guide.md) for available settings.

## Configuring Keycloak

Instructions below are aimed to provide a basic configuration of Keycloak, please refer to Keycloak documentation for full details.

1. Login to admin interface of Keycloak.
1. Create a new realm (or use existing)
 [![New realm](img/keycloak-add-realm.png)](img/keycloak-add-realm.png)
1. Open a menu with a list of clients.
 [![List clients](img/keycloak-client-list.png)](img/keycloak-client-list.png)
1. Add a new client for Waldur.
 [![Add client](img/keycloak-add-client.png)](img/keycloak-add-client.png)
1. Change client's access type to "confidential".
 [![Set access type](img/keycloak-client-access-type.png)](img/keycloak-client-access-type.png)
1. You can get secret code for the client configuratio
 [![Secret code](img/keycloak-client-secret.png)](img/keycloak-client-secret.png)
1. You can find the settings required for configuration of Waldur under the following path on your Keycloak deployment (change `test-waldur` to the realm that you are using):  `/auth/realms/test-waldur/.well-known/openid-configuration`.