# Credit management

Credit management stablishes credit limits for organizations that can be used for purchasing eligible services.
The credit can optional be sub-allocated to projects and used in [cost policies](cost-and-usage-policies.md).

## Credit management configuration for staff

Users with staff roles can allocate credit points to organizations. This can be done by selecting Administration from the left side menu and then Organizations -> Credit management from the top menu.

![Credit management policies](img/Credit_management_overall.png)

This page provides an overview of already assigned credit policies. To create a new one, click on "Add" from the right. A popup opens with different configuration fields.

![Credit management new policy](img/Credit_management_new.png)

1. Select an organization to which you would like to assign credits.
2. Select an offering for which credits can be used.
3. Set the credit value. This is the maximum value.
4. Consumption logic defines, how credits are used:

    - Fixed means that it is possible to define minimal monthly value and overall credit will be reduced by the monthly value, even if the usage has been less than minimal consumption.
    - Linear means that by setting the end date, the total value of the credit will be divided evenly across the period until the end date and the overall value will be reduced monthly by the calculated value even if the consumption is less than the calculated value.

5. If all set, click "Create".

## Credit management for organization owners

Organization owners can distribute allocated credits to projects. Projects can use credits for specific resource, overused resource is invoiced according to the pricing plan. Organization owners can use credit management together with the [cost and usage policies](cost-and-usage-policies.md) not to allow overconsumption.

To see current credit management policies, open the organization dashboard and then Accounting -> Credit management from the top menu.

![Customer credit policies](img/Customer_credit_management_list.png)

To create a new one, click "Add" on the right. A popup opens with configuration fields:

1. Project - select the project, which can use the credits.
2. Allocate credit - set the maximum amount of credits.
3. Use organization credit after exceeding allocated amount - Enable, if project can use organization credits after running out of project credits. If disabled, resource usage will be invoiced according to the pricing plan.
4. If all set, click "Create".

![New project credit policy](img/Project_credit_new.png)

