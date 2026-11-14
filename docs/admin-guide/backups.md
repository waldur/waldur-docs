# Backups

Waldur keeps state in 2 components:

- Database - main persistency layer.
- Message queue - contains transient data mostly about scheduled jobs and cache.

Of these, only the database needs to be backed up. Uploaded files — organization logos,
attachments and the like — are stored in the database too
(`waldur_core.media.storage.DatabaseStorage`), so a database dump captures them as well.

The commands below are for [Docker Compose](deployment/docker-compose/index.md); with Helm,
see [Kubernetes](#kubernetes) further down. A typical approach to a backup is:

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

Run the dump on a schedule, for example from cron, and copy it off the server each time.

## Kubernetes

The Helm chart can run the dump for you: `postgresBackup` schedules a `pg_dump` CronJob that
uploads to S3-compatible storage configured in `backupStorage`, and rotates old dumps. The
[backup management](deployment/helm/docs/postgres-backup-management.md) guide covers the
settings and the restore. With a PostgreSQL operator, prefer its own backups: CloudNativePG and
Zalando archive the write-ahead log continuously, so you can restore to any point in time, not
only to the last dump ([PostgreSQL operators](deployment/helm/docs/postgres-operator.md)).

## Test the restore

A backup you have not restored is not yet a backup. Restore into a separate environment on a
schedule, for example every quarter, and after any change to the backup setup:

1. Start an environment of the same Waldur version, with the same encryption key (see below),
   but with outgoing email disabled and no access to the service providers' APIs, so the copy
   cannot mail real users or act on real resources.
2. Restore the newest backup into it, and time the restore: that time is what an outage would
   cost you.
3. Sign in, and check that the newest records you expect are there, and that stored credentials
   can be read (for example, an offering's integration settings open without errors).
4. Delete the environment, and note the date and the result.

## Keep the encryption key

A dump does not hold the key Waldur encrypts credentials in the database with:
`FIELD_ENCRYPTION_KEY`, or, while that is unset, `SECRET_KEY` (`GLOBAL_SECRET_KEY`
with docker-compose, `waldur.secretKey` with Helm), which the key is then derived from.
During a key rotation, `FIELD_ENCRYPTION_KEY_FALLBACKS` holds the old ones. Back
them up as carefully as the dumps, but separately: restored without them, the
encrypted columns cannot be read, and nothing recovers them. See
[Field encryption at rest](../developer-guide/field-encryption.md#backups).

## Matrix chat

With Matrix chat on, the homeserver is a third component to back up: it keeps
the chat rooms, their messages and the users' Matrix accounts in its own
storage, the `tuwunel_data` volume with docker-compose and the
`data-matrix-homeserver-0` PVC with Helm. Back it up together with Waldur's
database, so a restore brings both back to the same point, and stop the
homeserver while you copy it (with Helm, scale the `matrix-homeserver`
StatefulSet to zero). Also back up the tokens Waldur and the homeserver
share: with docker-compose, the `waldur_matrix_secrets` volume; with Helm, the
`matrix-appservice-secret` Secret, unless `setup.existingSecret` keeps it in
your secret manager. Both also hold the bootstrap password.

Chat depends on the encryption key above too. Users' escrowed recovery keys,
the bot's encryption keys and access token, every history export's key and the
appservice tokens in Waldur's settings are encrypted with it. Restored with
another key, the bot refuses to start, the appservice stops working, and no
recovery key or history export can be read. The
[Helm](deployment/helm/docs/matrix-chat.md#backup-and-restore) and
[docker-compose](deployment/docker-compose/matrix-chat-add-on.md#backup-and-restore)
guides have the full backup and restore steps.

After restoring an older Waldur dump, or resetting Waldur's database, against
the same homeserver, the users provisioned since have a Matrix account that
Waldur no longer knows, and Waldur refuses to take it over: their chat stays
unavailable. Link them all with `waldur link_matrix_account --all`; see
[Existing Matrix accounts](../developer-guide/admin-guide/matrix-appservice-setup.md#existing-matrix-accounts).
