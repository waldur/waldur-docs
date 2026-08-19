# eduTEAMS

Waldur supports integration with the [eduTEAMS](https://eduteams.org/) identity service.

To enable it, please [register a new client](https://wiki.geant.org/display/eduTEAMS/Registering+services+on+the+eduTEAMS+Service)
for Waldur deployment and set configuration settings for eduTEAMS.
Check [configuration guide](../mastermind-configuration/configuration-guide.md) for available settings.

## Fetch user data using CUID of a user

A user's CUID is stored as their Waldur username, so you can fetch their permissions by
filtering on it: `GET /api/user-permissions/?username=<CUID>`. See
[permissions](../../integrator-guide/APIs/permissions.md) for the response shape and the
other filters available.
