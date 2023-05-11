# Waldur Keycloak mapper

Custom Keycloak client mapper for Waldur OfferingUser usernames.

## Installation and setup

Custom mapper setup includes the following steps:

1. Download the jar file to your machine, e.g. from [this release](https://code.opennodecloud.com/waldur/waldur-keycloak-mapper/-/releases/v1.0.1)

2. Add the jar file to the providers directory. Given a Keycloak server is running in a Docker container via Docker Compose, you can mount the file as a volume:

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

3. Restart the deployment to apply the changes

4. You can find the mapper in client menu under "Mappers" section. The title is "Waldur preferred username mapper"
