# Reporting issues

No software is perfect, and issues are to be expected. If you observe something that you think needs fixing, please provide a detailed issue report using the guidelines below.

## Where to report issues

Choose the appropriate channel to report your issue:

1. **Internal issue management (Atlassian JIRA)**
   - If you have access to the internal issue management system, please report the issue through Atlassian JIRA
   - Use the appropriate project for the component experiencing the issue
   - Follow your organization's internal guidelines for issue categorization

2. **GitHub Issues**
   - If you don't have access to internal issue management, report issues on GitHub
   - Visit the appropriate repository under the [Waldur organization](https://github.com/waldur)
   - Select the repository that corresponds to the component with the issue (e.g., HomePort, MasterMind)
   - Create a new issue using the provided templates when available

## Not sure which component has the issue?

If you're uncertain whether the issue is with HomePort or MasterMind, please provide:

1. **Description of the problem**
    - What you were trying to do
    - What happened instead
    - Any error messages you saw

2. **Screenshots** of the error at high resolution
    - Include the entire screen if possible to provide context
    - Ensure text is legible

3. **Basic environment information**
    - Browser type and version (if applicable)
    - URL where the issue occurred
    - Time and date when you encountered the issue
    - Waldur version (if known)

This information will help us determine which component is affected and guide you on additional details we might need.

## Required information for all issues

The following information is helpful for troubleshooting any issue:

1. **Environment details**
    - Waldur instance hostname
    - Deployment type (select one):
        - Docker-compose
        - Helm
        - ArgoCD

2. **Affected URL(s)**
    - Include the exact page where the issue occurs

3. **User-specific details** (if applicable)
    - User roles in different scopes (project, organization, call, offering, etc.)
    - Whether user has global role (staff or support)
    - If reproducible in test environment, provide the specific username

4. **Details of affected Waldur objects**
    - Customer name
    - Project name
    - Resource name
    - Any other relevant identifiers

## Homeport-specific issues

When reporting issues specifically with HomePort, please also include:

1. **HAR request file** that has failed or contains data required for rendering
    - [What is a HAR file](https://www.keycdn.com/support/what-is-a-har-file)
    - [How to generate a HAR file in Chrome/Firefox](https://support.zendesk.com/hc/en-us/articles/204410413-Generating-a-HAR-file-for-troubleshooting)
    - [Alternative HAR generation instructions](https://support.box.com/hc/en-us/articles/360043696054-How-to-Generate-Network-Captures-for-Troubleshooting)

## Mastermind-specific issues

When reporting issues specifically with MasterMind, please also include:

1. **Logs**
    - Include the latest MasterMind stdout logs with the error stacktrace
    - For different deployment types, retrieve logs using:
        - Docker-compose: [View logging instructions](../admin-guide/deployment/docker-compose.md#logs)
        - Helm: [View debugging instructions](../admin-guide/debugging.md#helm-1)

!!! warning
    Logs may contain sensitive data. Please ensure you either clean up the data or share it only with trusted parties before submitting.

## Best practices for issue reports

- Be specific about the steps to reproduce the issue
- Mention which browser and version you're using (for frontend issues)
- Include timing information (when did it start occurring, is it intermittent, etc.)
- Note any recent changes that might be related to the issue
- Provide as much context as possible to help with troubleshooting
- If possible, indicate if the issue can be consistently reproduced or occurs randomly