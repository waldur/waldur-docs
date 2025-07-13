# Waldur Keycloak mapper

This repository contains custom Keycloak OIDC protocol mappers that integrate with Waldur (cloud platform) to provide dynamic user authentication and authorization capabilities. The mappers enable seamless integration between Keycloak identity provider and Waldur's permission system.

## Waldur OfferingUser username mapper

### Goal

Maps Keycloak users to their corresponding usernames in Waldur offerings, enabling consistent user identification across systems.

### Capabilities

- **Dynamic Username Resolution**: Retrieves the preferred username for a user from Waldur's marketplace offering users API
- **Token Integration**: Adds the resolved username as a custom claim in OIDC tokens (ID token, access token, and user info)
- **Offering-Specific Mapping**: Configurable per offering UUID to support different username schemes across offerings
- **Secure API Communication**: Supports both TLS-validated and non-validated connections to Waldur API
- **Error Handling**: Graceful handling of API failures with comprehensive logging

### Configuration Parameters

- **Waldur API URL**: Base URL to Waldur API (e.g., `https://waldur.example.com/api/`)
- **Offering UUID**: Specific offering identifier in Waldur
- **API Token**: Authentication token for Waldur API access
- **TLS Validation**: Enable/disable TLS certificate validation
- **Claim Name**: Custom name for the token claim containing the username

## Waldur Offering access mapper

### Goal

Dynamically manages Keycloak group memberships and role assignments based on user access permissions in Waldur offerings.

### Capabilities

- **Dynamic Access Control**: Checks user access to specific Waldur offerings in real-time
- **Group Management**: Automatically adds/removes users from Keycloak groups based on offering access
- **Role Assignment**: Grants or revokes Keycloak roles based on offering permissions
- **Bidirectional Sync**: Both grants access when user has permissions and revokes when access is lost
- **Flexible Username Sources**: Supports both Keycloak user ID and username for Waldur API calls
- **Token Claims**: Optionally adds group information to OIDC tokens

### Configuration Parameters

- **Waldur API URL**: Base URL to Waldur API
- **Offering UUID**: Target offering identifier for access checks
- **API Token**: Waldur API authentication token
- **Username Source**: Choose between Keycloak user ID or username (`id` or `username`)
- **Group Management**:
  - Group name to manage
  - Enable/disable automatic group addition
- **Role Management**:
  - Role name to grant/revoke
  - Enable/disable automatic role assignment
- **Claim Name**: Custom token claim for group information

### Use Cases

- **Service Access Control**: Automatically grant access to services based on Waldur offering subscriptions
- **Team Management**: Sync team memberships between Waldur and Keycloak
- **Resource Permissions**: Map Waldur resource access to Keycloak authorization

## Waldur MinIO mapper

### Goal

Generates MinIO-compatible policy claims for object storage access control based on user permissions in Waldur.

### Capabilities

- **Permission Aggregation**: Collects user permissions from Waldur across different scope types
- **Policy Generation**: Creates comma-separated lists of resource UUIDs for MinIO policies
- **Scope-Based Filtering**: Supports both `customer` and `project` scope types for permission queries
- **Role-Based Access**: Filters permissions by user roles (owner, manager, etc.) within each scope
- **Token Integration**: Embeds policy information directly in OIDC tokens for MinIO consumption
- **Flexible Username Sources**: Supports both Keycloak user ID and username for API authentication
- **Secure Communication**: Configurable TLS validation for API calls

### Configuration Parameters

- **Waldur API URL**: Base URL to Waldur API
- **API Token**: Waldur API authentication token
- **Permission Scope**: Choose between `customer` or `project` scope types
- **TLS Validation**: Enable/disable certificate validation
- **Username Source**: Use Keycloak user ID or username for API calls
- **Claim Name**: Token claim name for the policy data

### Example Output

For a user who is an owner in customers C1, C2 and manager in projects P1, P2:

**Customer scope**: `policy=c1-uuid-here,c2-uuid-here`
**Project scope**: `policy=p1-uuid-here,p2-uuid-here`

### MinIO Integration

The generated policy claims can be used by MinIO to:
- **Bucket Access Control**: Grant access to buckets based on customer/project membership
- **Object-Level Permissions**: Control file access within buckets
- **Dynamic Policy Updates**: Automatically update access as Waldur permissions change

## Building from Source

### Prerequisites

- **Java 8 or higher**: The project is compiled with Java 8 target compatibility
- **Apache Maven 3.6+**: Required for building and dependency management
- **Git**: For cloning the repository

### Build Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/waldur/waldur-keycloak-mapper.git
   cd waldur-keycloak-mapper
   ```

2. **Build the JAR file:**

   ```bash
   mvn clean install
   ```

   This will:
   - Download all required dependencies
   - Compile the Java source code
   - Run any tests (if present)
   - Create a shaded JAR with all dependencies included
   - Place the built JAR in the `target/` directory

3. **Locate the built JAR:**

   The compiled JAR file will be available at:

   ```text
   target/waldur-keycloak-mapper-{version}.jar
   ```

### Build Options

- **Clean build:** Remove previous build artifacts before building

  ```bash
  mvn clean install
  ```

- **Skip tests:** Build without running tests (if any)

  ```bash
  mvn clean install -DskipTests
  ```

- **Custom version:** Build with a specific version number

  ```bash
  mvn clean install -Drevision=1.2.3
  ```

### Development Environment

For development, you can use any Java IDE that supports Maven projects:

- **IntelliJ IDEA**: Import as Maven project
- **Eclipse**: Import existing Maven project
- **VS Code**: Use Java Extension Pack with Maven support

The project uses Maven's standard directory layout:
- `src/main/java/`: Java source files
- `src/main/resources/`: Resource files and service registration
- `target/`: Build output directory

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
