# OfferingUser management

OfferingUser is a model in Waldur, which represents a link between an offering available in marketplace and a user.
A service provider can utilize it to create an account for a service visible for all the offering resources, for example: a user account in a SLURM cluster.
As an account, an OfferingUser can have a custom username different from user's one.

This feature is available for offerings of types:

* Basic
* SLURM
* SLURM remote
* Custom script
* Rancher

For Basic, SLURM remote and Custom script offerings, offering-users are created automatically when a user is added to the project with active offering resources or when a new offering resource is created.

In case of Rancher, offering-users are created when users are imported from a Rancher cluster.

In case of SLURM, offering-users are created when association are imported from a SLURM cluster.

## Username generation

The `username` field for the model can be generated via strategies:

1. `service_provider`: a service provider should manually set usernames for the offering users (default strategy);
2. `anonymized`: usernames are generated with `<prefix>_<number>`, e.g. "anonym_00001"; the prefix must be specified in the plugin options of the offering as `username_anonymized_prefix`;
3. `full_name`: usernames are constructed using first and last name of users with numerical suffix, e.g. "john_doe_01";
4. `waldur_username`: uses a username of a user;
5. `freeipa`: uses the username field of a corresponding FreeIPA profile.

A service provider can choose the policy via UI:

1. go to offering edit section in a service provider page;
2. open `Integration` tab;
3. click `Edit integration options`;
4. choose a username generation policy from the drop-down list;
5. click `Save` button.

After this, the usernames are regenerated for all the linked offering users.
