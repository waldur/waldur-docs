# VPNaaS custom script - Provisioning VPN as a Service based on Firezone

![Firezone login screen](/preview.png "Login Screen")

This python script provisions VPN as a Service based on [Firezone](https://github.com/firezone/firezone) in OpenStack in Waldur.
It uses [Flatcar Linux](https://www.flatcar.org/) and a butane binary that the user needs to provide inside a Docker container used for running Waldur custom scripts.

An additional requirement is an OpenID Connect provider for end-user authentication in Firezone.
Default VPN port: UDP/51820.

## System requirements

* Keycloak with admin access for OpenID Connect client creation
* [Butane](https://coreos.github.io/butane/) for converting Flarcar Linux yaml config into json
* OpenStack nova for running the Firezone VM
* OpenStack designate for the VM FQDN generation. Firezone will use that FQDN for HTTPS certificate generation.

Firezone VM needs Internet connection for Let's Encrypt certificate generation and Github access for script download.

## Setup guide

1. Prepare waldur custom script runner container to have [Butane](https://coreos.github.io/butane/) and [required Python packages](https://raw.githubusercontent.com/waldur/waldur-custom-offerings/main/firezone/custom-scripts/requirements.txt)
1. Paste the create.py into the creation script and terminate.py into the termination script
1. Populate environment variables
1. Add user input field with internal name "tenant" and type - "Select OpenStack tenant", make it a required field

## Environment Variables

The following environment variables need to be provided in the Waldur custom script:

- `WALDUR_API_URL` - API URL of Waldur that holds OpenStack
- `WALDUR_API_TOKEN` - Waldur API token
- `KEYCLOAK_URL` - Keycloak address for creating OpenID connect clients
- `KEYCLOAK_USERNAME` - Keycloak admin username
- `KEYCLOAK_PASSWORD` - Keycloak admin password
- `KEYCLOAK_REALM` - Keycloak realm
- `CREATOR_EMAIL` - Email of the user, that created the VPN instance
- `IMAGE` - OpenStack image
- `FLAVOR` - OpenStack flavor
- `SYSTEM_VOLUME_SIZE` - Size of the system volume for OpenStack VM
- `RUN_BUTANE_IN_DOCKER` - When set to True - run butane in docker container instead of just binary