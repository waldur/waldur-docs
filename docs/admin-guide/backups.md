# Backups

Waldur keeps state in 2 components:

- Database - main persistency layer.
- Message queue - contains transient data mostly about scheduled jobs and cache.

Of these, only the database needs to be backed up. Uploaded files — organization logos,
attachments and the like — are stored in the database too
(`waldur_core.media.storage.DatabaseStorage`), so a database dump captures them as well.

A typical approach to a backup is:

## 1. Create a DB dump

1. An entire db dump

```bash
docker exec -t waldur-db pg_dump -U waldur waldur | gzip -9 > waldur-$(date +'%Y%m%dT%H%M%S').sql.gz
```

1. An entire db dump with cleanup commands:

```bash
docker exec -t waldur-db pg_dump --clean -U waldur waldur | gzip -9 > waldur-$(date +'%Y%m%dT%H%M%S').sql.gz
```

1. A db dump containing only data

```bash
docker exec -t waldur-db pg_dump -a -U waldur waldur | gzip -9 > waldur-$(date +'%Y%m%dT%H%M%S').sql.gz
```

## 2. Copy backup to a remote location

Using rsync / scp or more specialised tools.

## 3. Restore the created backup

The dumps above are gzipped, so decompress them on the way in:

```bash
zcat waldur-20260819T101500.sql.gz | docker exec -i waldur-db psql -U waldur waldur
```

We suggest to make sure that backups are running regularly, e.g. using cron.
