# Ad-hoc scripts

This section describes different ad-hoc scripts used by Waldur developers.

## Usage-related scripts

### Restore CPU/GPU/RAM usages for a month

Sometimes, Waldur can have issues with data correctness. They can be caused by different circumstansies, e.g. problems with data syncronization between Waldur backend and service provider software. In order to resolve these issues, a user can restore usage data with [restore_usages.py](scripts/update_usages.py) script.

### Generate openmetrics file with usages for serveral months

If a user needs to create openmetrics file with usages, e.g. for [historical data backfilling in Prometheus](https://medium.com/tlvince/prometheus-backfilling-a92573eb712c), the [generate_openmetrics_usages.py](scripts/generate_openmetrics_usages.py) can be used.
