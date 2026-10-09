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

## Matrix chat

With Matrix chat on, the homeserver is a third component to back up: it keeps
the chat rooms, their messages and the users' Matrix accounts in its own
storage, the `tuwunel_data` volume with docker-compose and the
`data-matrix-homeserver-0` PVC with Helm. Back it up together with Waldur's
database, so a restore brings both back to the same point, and stop the
homeserver while you copy it (with Helm, scale the `matrix-homeserver`
StatefulSet to zero). With docker-compose, also back up the
`waldur_matrix_secrets` volume, which holds the tokens Waldur and the
homeserver share.

After restoring an older Waldur dump, or resetting Waldur's database, against
the same homeserver, the users provisioned since have a Matrix account that
Waldur no longer knows, and Waldur refuses to take it over: their chat stays
unavailable. Link them all with `waldur link_matrix_account --all`; see
[Existing Matrix accounts](../developer-guide/admin-guide/matrix-appservice-setup.md#existing-matrix-accounts).
