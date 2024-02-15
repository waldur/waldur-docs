# Data processing disclaimer

Waldur developers would like to inform that we do not assume any responsibility for processing data generated or handled by the software.

Users (e.g platform operators, platform users) are solely responsible for ensuring that the data processed through our software complies with applicable laws, regulations, and industry standards. Waldur developers disclaim any liability for loss, damage, or unauthorized access to data from our software.

Our role is limited to the development of software solution. We do not control, manage, or take responsibility for our software processes' specific deployments and data, including but not limited to data storage, transmission, or any associated security measures.

Users are encouraged to implement data protection and security measures to secure their information. By using Waldur software, users acknowledge and agree that Waldur developers are not liable for any issues related to data processing.

## Some highlights to keep in mind regarding user data processing in Waldur

- Platform operator should have a DPA (Data Processing Agreement) with every Service Provider connected to the platform because, in case of a service request from a Service Provider, the latter gets the ability to see members of the project whereas service is to be provisioned. For example, an HPC service gets access to project member information only when the project is requesting access to the service. The access is revoked once the service is terminated.
- Staff users (usually platform operators) can see all users personal information.
- User profile modifications are logged, including modifier network address and changes for auditing and tracing abilities. Additionally, operations connected with the user, e.g. adding or removing SSH key, are also logged.
- The authentication system is designed around the federated AAI solution, where a user is expected to conform explicitly to personal data propagation from the Identity Provider (IdP) to Waldur.
- In cases when policy allows, it is possible to create a non-personalized group or robot account to act on behalf of the user, e.g. for CICD types of workflows.
- All event logs contain references to a user - by UUID - if they are connected with the user. This allows the platform operator to have an easy information cleanup for user data according to specific deployment policies (e.g. removing data of deactivated users after two years) and to disclose user data easily collected about them.

## Some suggestions to ensure that the data is securely protected

- Waldur is pretty configurable, this means that the Waldur deployment operator can configure user profiles in a way that the information requested about the users is as minimal as possible.
- User information is visible to all project members, so make sure that you include only these users in the project, who are allowed to see each other's information. In addition to that, organization managers can see the user information about users connected to that organization.
