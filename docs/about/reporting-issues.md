# Reporting issues

No software is perfect and issues are to be expected. If you observe something that you think needs fixing, please
provide issue report, which includes:

From **HomePort**:

1. HAR request that has failed or that contains data required for rendering of the data.
    - [What is HAR](https://www.keycdn.com/support/what-is-a-har-file)
    - [Zendesk instructions for generating a HAR](https://support.zendesk.com/hc/en-us/articles/204410413-Generating-a-HAR-file-for-troubleshooting)
    - [Box instructions for generating a HAR](https://support.box.com/hc/en-us/articles/360043696054-How-to-Generate-Network-Captures-for-Troubleshooting)
2. Screenshot of the error in a high enough resolution.

From **MasterMind**:

1. Affected Mastermind URL(s)
2. Details of affected Waldur objects: customer name, project name, resource name, etc.
3. Details of environment: Waldur instance hostname, deployment type one of:
   1. Docker-compose
   2. Helm
   3. ArgoCD
4. In case issue is user specific, details of user facing the issue: roles in different scopes (project, organization, call, offering, etc), if user has global role (staff or support). If issue is reproducible in test environment, concrete username.
5. Latest mastermind stdout logs that include stacktrace of the error
   1. For docker-compose: [link](/docs/admin-guide/deployment/docker-compose/#logs)
   2. For Helm: [link](/docs/admin-guide/debugging.md#helm-1)

!!! warning
    Logs may contain sensitive data, please make sure that you either cleanup the data or share it with a trusted
    party before sharing the actual data.
