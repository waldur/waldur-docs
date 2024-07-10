# Adding an offering

Waldur supports a number of different types of service providers when creating a shared offering. A common way of
creating an offering is through a HomePort.

1. Select organization, which will provide the offering.

2. Make sure that organization is a service provider. Make it one with a staff user if the flag is not set.

    [![Register provider](img/service-provider-reg.png)](img/service-provider-reg.png)

3. Go to Provider dashboard and click on "Marketplace" -> "Offerings" -> "Add new offering":

    [![Adding an offering](img/offering-add-new.png)](img/offering-add-new.png)

4. Fill in the name for the offering, category and type:

    [![Adding details](img/offering-name.png)](img/offering-name.png)

5. Offering details page opens, where you can add additional information:

    [![Offering details](img/offering-general-details.png)](img/offering-general-details.png)

6. To add accounting components, select "Accounting components" from the top menu and then "Add component" from the right side. Accounting component is a measurable unit of a resource. For example, it can be CPU hours, GPU hours, storage hours, RAM etc.

    [![Accounting components](img/offering-accounting-components.png)](img/offering-accounting-components.png)

7. A popup opens with possibility to configure fields and select the accounting type (whether the component is billed by the usage, max limit or it has a fixed price).

    - Usage-based - billing is applied according to the actual usage of the resource during the billing period defined in the accounting plan after the submission of a usage report;
    - Limit-based - billing is applied according to the requested/updated limits of a resource, actual usage can be below the limits and it is not the basis of the billing;
    - Fixed price - billing is applied according to the exact values defined by the service provider in the accounting plan, limits and usage are not the basis for the accounting;
    - One-time - billing is applied once on resource activation;
    - One-time on plan switch - billing is applied once on resource activation and everytime a plan has changed, using pricing of a new plan.

    [![Accounting component details](img/offering-accounting-component-details.png)](img/offering-accounting-component-details.png)

8. To configure accoutning frequency and prices, select "Accounting plans" from the top menu and then "Add plan" from the right:

    [![Accounting plans](img/offering-accounting-plans.png)](img/offering-accounting-plans.png)

9. Select a name for the plan and accounting frequency:

    [![Accounting frequency](img/offering-accounting-plan-freq.png)](img/offering-accounting-plan-freq.png)

10. To define prices for the components, select "Actions" and then "Edit prices". Set new price and save. If there is a need to provide higher priority access to resources with different prices, then it is advised to create another offering for this kind of cases.

    [![Offering prices](img/offering-accounting-plan-actions.png)](img/offering-accounting-plan-actions.png)

    [![Offering prices](img/offering-accounting-plan-prices.png)](img/offering-accounting-plan-prices.png)

11. If all set, click "Activate" on the top-right side to make it visible to everybody.

    [![Activate offering](img/offering-activation.png)](img/offering-activation.png)

!!! tip
    For more advanced cases of management of offerings, take a look at how a SLURM offering can be managed using
   [Ansible module](https://github.com/waldur/ansible-waldur-module/blob/develop/waldur_batch_offering.py).