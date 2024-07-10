# MyAccessID

Waldur supports integration with [MyAccessID](https://wiki.geant.org/display/MyAccessID/MyAccessID+Home) identity service.

The MyAccessID Identity and Access Management Service is provided by GEANT with the purpose of offering  a common
Identity Layer for Infrastructure Service Domains (ISDs).

The AAI proxy of MyAccessID connects Identity Providers from eduGAIN, specific IdPs which are delivered in context of
ISDs such as HPC IdPs, eIDAS eIDs and potentially other IdPs as requested by ISDs.

MyAccessID delivers the Discovery Service used during the user authentication process for users to choose their IdP.
It enables the user to register an account in the Account Registry, to link different identities and it guarantees
the uniqueness and persistence of the user identifier towards connected ISDs.

To enable MyAccessID, please [register a new client](https://wiki.geant.org/display/MyAccessID/Registering+Relying+Parties)
for Waldur deployment and set configuration settings for MyAccessID.
Check [configuration guide](../mastermind-configuration/configuration-guide.md) for available settings.

## Fetch user data using CUID of a user

You can use CUID of user in order to fetch user permissions from MyAccessID registry.
[This document](../waldur-shell.md) describes how to perform it via Waldur shell.
