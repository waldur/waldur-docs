# Adding an offering

Waldur supports a number of different types of service providers when creating a shared offering. A common way of
creating an offering is through a HomePort.

1. Select organization, which will provide the offering.

2. Make sure that organization is a service provider. Make it one with a staff user if the flag is not set.

    [![Register provider](img/provider-manage.png)](img/provider-manage.png)

3. Go to Provider dashboard and click on "Add new offering":

    [![Adding an offering](img/add-offering.png)](img/add-offering.png)

4. Fill in the name for the offering, category and type:

    [![Adding details](img/add-offering-name.png)](img/add-offering-name.png)

5. From the offerings' list, select offering and click on "Actions"->"Edit"

    [![Adding details](img/offering-edit.png)](img/offering-edit.png)

6. Fill in the details of the offering and click "Activate" to make it visible to everybody.

    [![Activate offering](img/add-offering-details.png)](img/add-offering-details.png)

!!! tip
    For more advanced cases of management of offerings, take a look at how a SLURM offering can be managed using
   [Ansible module](https://github.com/waldur/ansible-waldur-module/blob/develop/waldur_batch_offering.py).