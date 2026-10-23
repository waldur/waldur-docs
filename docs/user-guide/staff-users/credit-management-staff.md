# Credit management configuration for staff

Credit management establishes credit limits for organizations that can be used for purchasing eligible services.
The credit can optional be sub-allocated to projects and used in [cost policies](../customer-organization/cost-and-usage-policies.md).

Users with staff role can allocate credit to organizations. Open **Administration** in the
sidebar, then **Organizations & compliance → Credits & cost policies**. The **Credits** tab lists
the credits already assigned; the **Cost policies** tab holds the organization
[cost policies](../customer-organization/cost-and-usage-policies.md#cost-policies-for-organizations).

![Credits of organizations](../img/credit-organization-list.png)

To assign a credit, click **Add**. A dialog opens with these fields.

![Add allocation credit dialog](../img/credit-organization-new.png)

1. Select an organization to which you would like to assign credits.
2. Select the offerings the credit may be spent on. **Leave this empty to allow all offerings** —
   an empty list means unrestricted, not "none". Cost on any other offering is invoiced
   normally and is never drawn from the credit.
3. Set the credit value. This is the total value that the organization will be able to spent.
4. Optionally set an end date. On that date the remaining credit is set to 0. It must be the
   first day of a month.
5. Minimal consumption logic defines, how minimal monthly consumption is calculated:

    - Fixed means that it is possible to define minimal monthly value and overall credit will be reduced by the monthly value, even if the usage has been less than minimal consumption.
    - Linear means that by setting the end date, the total value of the credit will be divided evenly across the period until the end date and the overall value will be reduced monthly by the calculated value even if the consumption is less than the calculated value.

6. **Expected consumption** is the monthly amount for the fixed logic. It is only charged as a
   minimum when **Apply as minimal consumption** is on. The **Grace coefficient** lowers that
   minimum by a percentage: with an expected consumption of 1 000 and a grace coefficient of
   10 %, at least 900 is deducted each month. In the month of the end date, the full expected
   consumption is deducted.
7. If all set, click **Create**.

!!! warning
    Restricting the offerings is not the same as excluding cost from the organization.
    Resources on offerings outside the list are still bought and still invoiced — the
    credit simply never covers them. Because that cost is never compensated, it counts
    towards [cost policies](../customer-organization/cost-and-usage-policies.md)
    immediately, while the credit balance still looks untouched.
