# Credit management configuration for staff

Credit management establishes credit limits for organizations that can be used for purchasing eligible services.
The credit can optional be sub-allocated to projects and used in [cost policies](cost-and-usage-policies.md).

Users with staff role can allocate credit points to organizations. This can be done by selecting Administration from the left side menu and then Organizations -> Credit management from the top menu.

![Credit management policies](img/Credit_management_overall.png)

This page provides an overview of already assigned credit policies. To create a new one, click on "Add" from the right. A popup opens with different configuration fields.

![Credit management new policy](img/Credit_management_new.png)

1. Select an organization to which you would like to assign credits.
2. Select an offering for which credits can be used.
3. Set the credit value. This is the total value that the organization will be able to spent.
4. Minimal consumption logic defines, how minimal monthly consumption is calculated:

    - Fixed means that it is possible to define minimal monthly value and overall credit will be reduced by the monthly value, even if the usage has been less than minimal consumption.
    - Linear means that by setting the end date, the total value of the credit will be divided evenly across the period until the end date and the overall value will be reduced monthly by the calculated value even if the consumption is less than the calculated value.

5. If all set, click "Create".