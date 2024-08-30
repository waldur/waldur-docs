# Waldur Keycloak mapper

## Waldur OfferingUser username mapper

Custom Keycloak client mapper for Waldur OfferingUser usernames.

## Waldur Offering access mapper

Custom Keycloak client mapper for Waldur groups.

## Waldur MinIO mapper

Custom Keycloak client mapper for MinIO.
This mapper adds `policy` claim to a JSON token with a list of user permissions on a specified scope in Waldur.
For now, only `customer` and `project` are supported as a scope types for user permissions.
For example, if a user is an owner in customers C1, C2 and a manager in projects P1 and P2, the result would be:

1. For scope `customer`: `policy=<C1_UUID>,<C2_UUID>`
2. For scope `project`: `policy=<P1_UUID>,<P2_UUID>`

## Installation and setup

Custom mapper setup includes the following steps:

1. Download the jar file to your machine, e.g. one of [these releases](https://github.com/waldur/waldur-keycloak-mapper/releases/).

2. Add the jar file to the [providers](https://www.keycloak.org/server/configuration-provider#_installing_and_uninstalling_a_provider) directory.
   If a Keycloak server is running in a Docker container via Docker Compose, you can mount the file as a volume:

    ```yaml
    keycloak:
    image: "quay.io/keycloak/keycloak:18.0.2"
    container_name: keycloak
    command: start-dev --http-relative-path /auth
    ports:
        - "${KEYCLOAK_PORT:-8080}:8080"
    volumes:
        - waldur-keycloak-mapper-1.0.jar:/opt/keycloak/providers/waldur-keycloak-mapper-1.0.jar
    ```

3. Restart the deployment to apply the changes.

4. You can find the mapper in client menu under "Mappers" section. The title is "Waldur preferred username mapper"
