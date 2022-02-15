# eduTEAMS

Waldur supports integration with [eduTEAMS](http://keycloak.org/) identity service.

To enable it, please [register a new client](https://wiki.geant.org/display/eduTEAMS/Registering+services+on+the+eduTEAMS+Service)
for Waldur deployment and set configuration settings for eduTEAMS.
Check [configuration guide](../mastermind-configuration/configuration-guide.md) for available settings.

## Fetch user data using CUID of a user

You can use CUID of user in order to fetch user permissions. [This file](../../integrator-guide/APIs/permissions.md) describes how to perform it, you only need to provide CUID as a username.
