---
mentions:
  - setting:PAT_ENABLED
---

# Personal access tokens

Personal access tokens (PATs) provide a secure way to authenticate with the Waldur API for programmatic access. Unlike session-based authentication, PATs are scoped, time-limited, and can be revoked independently.

## Prerequisites

- Your account must be active.
- Your account must be allowed personal access tokens. That is the case when either:
    - staff have turned them on for every user (`PAT_ENABLED`, under **Administration > Configuration > Personal access tokens**), or
    - while they are not on for every user, staff have turned on the **Personal access tokens** option on your account, when editing the user.

Staff accounts follow the same rule. If **Personal access tokens** is missing under **Profile > Credentials**, your account is not allowed them: ask your administrator.

When an account stops being allowed tokens (staff turn `PAT_ENABLED` off and the account does not have the option), its existing tokens stop working but are not deleted. They work again if the account is allowed tokens before they expire.

## Creating a token

1. Navigate to **Profile > Credentials > Personal access tokens**.

    ![PAT list](../img/pat-list-with-token.png)

2. Click **Create token**.

3. Fill in the form:
    - **Token name** — a descriptive name (e.g., "CI/CD pipeline token").
    - **Scopes** — select the permissions this token should have. Only permissions you currently hold are available.
    - **Expiration date** — the token will stop working after this date.

    ![Create dialog](../img/pat-create-dialog.png)

    Scopes are displayed with human-readable labels organized by category:

    ![Scopes dropdown](../img/pat-scopes-dropdown.png)

4. Click **Create token**. A dialog shows your new token:

    ![Secret dialog](../img/pat-secret-dialog.png)

!!! warning
    Copy your token immediately. It will not be shown again. Use the copy button or copy the curl example directly.

## Using a token

Authenticate API requests by passing the token in the `Authorization` header:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" https://waldur.example.com/api/customers/
```

The token respects the **scope ceiling model**: effective permissions are the intersection of the token's scopes and your current roles. A token cannot grant more access than you have.

## Managing tokens

### Viewing token details

Click on a token row to expand it and see:

- **Scopes** — human-readable list of granted permissions.
- **Last used from IP** — the IP address of the most recent API call.
- **Total usage count** — how many times the token has been used.

![Expanded details](../img/pat-expanded-details.png)

### Rotating a token

Open the row actions menu and select **Rotate**. This atomically revokes the current token and generates a new one with the same scopes and expiration. The old token stops working immediately.

![Row actions](../img/pat-row-actions.png)

### Revoking a token

Open the row actions menu and select **Revoke**. The token is permanently deactivated. Revoked tokens remain visible in the list with a red "Revoked" badge for audit purposes.

## Security notes

- Tokens are stored as SHA-256 hashes — Waldur never stores the plaintext.
- Expired tokens are automatically deactivated by a background process.
- If your account is deactivated, all your tokens are revoked automatically.
- You cannot create, rotate, or revoke tokens when authenticated via a PAT (session authentication required).
