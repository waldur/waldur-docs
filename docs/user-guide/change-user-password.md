# Changing user passwords

This guide explains how administrators can change user passwords in Waldur.

## Important note

⚠️ **This guide only applies to local Waldur accounts**:
- For users authenticated via LDAP: Manage passwords in your LDAP directory
- For users authenticated via OIDC: Manage passwords in your OpenID provider
- For users authenticated via SAML: Manage passwords in your SAML identity provider

## Prerequisites

- Staff account access

## Steps to change user password

1. Access the admin panel
   - Navigate to `<your-waldur-instance>/admin/`
   - Log in with your staff account credentials

2. Locate user settings
   - Go to "Users" section
   - Select "Users" from the list

3. Find specific user
   - Use the search function to find the user
   - Click on the username to access their details

4. Change password
   - Locate the password field
   - Enter and confirm the new password
   - Save changes

## Important notes

⚠️ **Security warnings**:
- Only use this feature when absolutely necessary
- Ensure password changes comply with your organization's security policies
- Notify users when their passwords have been changed
- Document password changes according to your security protocols