# Backups

Waldur keeps state in 2 components:

- Database - main persistency layer.
- Message queue - contains transient data mostly about scheduled jobs and cache.

Of these, only database needs to be backed up.

A typical approach to a backup is:

1. Create a database dump, e.g.
```bash
$ docker exec -t waldur-db pg_dump -U waldur waldur | gzip -9 > postgresql-backup/waldur-$(date +'%Y%m%dT%H%M%S').sql.gz
```

2. Copy backup to a remote location.

We suggest to make sure that backups are running regularly, e.g. using cron.