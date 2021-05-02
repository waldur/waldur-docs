# FreeIPA

!!! tip
    For integrating FreeIPA as source of identities, please see [LDAP](LDAP.md).
    This module is about synchronising users from Waldur to FreeIPA

For situations when you would like to provide access to services based on the Linux usernames, e.g. for SLURM
deployments, you might want to map users from Waldur (e.g. created through eduGAIN) to an external FreeIPA service.

To do that, you need to enable module and define settings for accessing FreeIPA REST APIs. See
[Waldur configuration guide](../mastermind-configuration/configuration-guide.md) for the list of supported FreeIPA
settings.

At the moment at most one deployment of FreeIPA per Waldur is supported.