# OfferingUser management

OfferingUser is a model in Waldur, which represents a link between an offering available in marketplace and a user.
A service provider can utilize it to create an account for a service visible for all the offering resources, for example: a user account in a SLURM cluster.
As an account, an OfferingUser can have a custom username different from user's one.

This feature is available for all offering types.

For Basic, SLURM remote and Custom script offerings, offering-users are created automatically when a user is added to the project with active offering resources or when a new offering resource is created.

In case of Rancher, offering-users are created when users are imported from a Rancher cluster.

In case of SLURM, offering-users are created when association are imported from a SLURM cluster.

## Defining the OfferingUser management policy

A service provider can define the policy via User Interface:

1. Select the particular offering and go to **Edit** section.
2. Select **Integration** and then **User management** from the top menu.

    ![OfferingUser management](img/offeringUser.png)

3. Here it is possible to enable the automatic creation of offering users and define how it is done exactly.

    - **Enable automatic creation of offering users**: Enable/disable automatic creation of offering users;
    - **Shared user password**: Set common password for all offering users;
    - **Username generation policy**: Define how usernames are generated:

        - `Service provider`: a service provider should manually set usernames for the offering users (default strategy);
        - `Anonymized`: usernames are generated with `<prefix>_<number>`, e.g. "anonym_00001"; the prefix must be specified in the plugin options of the offering as `username_anonymized_prefix`;
        - `Full name`: usernames are constructed using first and last name of users with numerical suffix, e.g. "john_doe_01";
        - `Waldur username`: uses a Waldur instance username of a user;
        - `FreeIPA`: uses the username field of a corresponding FreeIPA profile;
        - `Identity claim`: uses dedicated attribute released by the IdP as a username.

    - **Initial UID number**: refers to the lowest numerical user ID (UID) assigned to regular users;
    - **Initial primary group number**: refers to Group ID (GID) assigned to a user when they are created;
    - **Home directory prefix**: Allows to define home directory prefix for the offering users.

4. After this, the usernames are regenerated for all the linked offering users.

## Granting user access to resource

An access to a resource can be granted by service provider for a particular user with specification of username. A result is represented by triplet [user, resource, username]. For this purpose, `create_remote_offering_user` should be invoked. This method requires the following arguments:

- **offering** - UUID or URL of a target offering;
- **user** - UUID or URL of a target user;
- **username** - username for the user.

```bash
  result = client.create_remote_offering_user(
      offering='<offering-uuid-or-url>',
      user='<user-uuid-or-url>',
      username='<username>'
  )

  # result => {
  #  'created': '2021-08-12T15:22:18.993586Z',
  #  'offering': 'http://localhost:8000/api/marketplace-provider-offerings/d47ca5bce71144579df29da3c290027e/',
  #  'offering_name': 'Remote offering (really)',
  #  'offering_uuid': 'd47ca5bce71144579df29da3c290027e',
  #  'user': 'http://localhost:8000/api/users/db157a5cf7f247eba161cd90eba9ac63/',
  #  'user_uuid': 'db157a5cf7f247eba161cd90eba9ac63',
  #  'username': 'abc'
  # }
```

In case if SDK usage is not possible, HTTP request can be sent:

```bash
  POST <API-URL>/marketplace-offering-users/

  {
      "offering": "<offering-uuid-or-url>",
      "user": "<user-uuid-or-url>",
      "username": "<username>"
  }

  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

  {
      "created": "2021-08-12T15:22:18.993586Z",
      "offering": "http://localhost:8000/api/marketplace-provider-offerings/d47ca5bce71144579df29da3c290027e/",
      "offering_name": "Remote offering (really)",
      "offering_uuid": "d47ca5bce71144579df29da3c290027e",
      "user": "http://localhost:8000/api/users/db157a5cf7f247eba161cd90eba9ac63/",
      "user_uuid": "db157a5cf7f247eba161cd90eba9ac63",
      "username": "abc"
  }
```

## Granting user access to corresponding resources in batch manner

A service provider can grant access mentioned in the previous section to all resources used in projects including a target user. For such access creation or update, `set_offerings_username` is used. The method requires the following arguments:

- **service_provider_uuid** - UUID of a target service provider;
- **user_uuid** - UUID of a target user;
- **username** - the new username.

```bash
  result = client.set_offerings_username(
      service_provider_uuid='<service-provider-uuid>',
      user_uuid='<user-uuid>',
      username='<username>',
  )

  # result =>  {
  #  'detail': 'Offering users have been set.'
  # }
```

