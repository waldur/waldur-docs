# Impersonation functionality

Waldur provides Impersonation functionality to allow the support team to debug and resolve user-related issues more efficiently. This feature enables support users to view the user interface (UI) as though they were the user they are impersonating.

## Prerequisites

1. The impersonator must have a staff role in the Waldur deployment.
2. The user being impersonated must have an active session (users cannot be logged out).

## Process guide

1. Log in to the Waldur deployment using a staff account.
2. Navigate to the Administration menu, then go to Accounts → Users from the top menu.

    ![Impersionation](../img/Admin_Users.png)

3. Locate the user you wish to impersonate and select Impersonate from the Actions options.

    ![Impersionation](../img/User_impersionate.png)

## Logging

All actions performed on behalf of a user are logged with additional context in the audit logs, including the impersonator's UUID, full name, and username. This is primarily for security purposes.



