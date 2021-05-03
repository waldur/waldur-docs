# Reporting issues

No software is perfect and issues are to be expected. If you observe something that you think needs fixing, please
provide issue report, which includes:

From **HomePort**:

1. HAR request that has failed or that contains data required for rendering of the data.
    - [What is HAR](https://www.keycdn.com/support/what-is-a-har-file)
    - [Zendesk instructions for generating a HAR](https://support.zendesk.com/hc/en-us/articles/204410413-Generating-a-HAR-file-for-troubleshooting)
    - [Box instructions for generating a HAR](https://support.box.com/hc/en-us/articles/360043696054-How-to-Generate-Network-Captures-for-Troubleshooting)
1. Screenshot of the error in a high enough resolution.

From **MasterMind**:

1. Latest mastermind logs that include stacktrace of the error, typically *core.log* and *celery-celery.log*.

!!! warning
    Logs may contain sensitive data, please make sure that you either cleanup the data or share it with a trusted
    party before sharing the actual data.
