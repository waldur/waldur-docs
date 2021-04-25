# Checklist for launching Waldur in production

## General

- [ ] Make sure that privacy policy and terms of use are updated to the site specific ones.
- [ ] Make sure that SMTP server and outgoing email address are configured and emails are sent out.
- [ ] Reboot test: restart all the nodes where Waldur components are running, application should recover automatically.

## Security

- [ ] Remove or disable default staff accounts.
- [ ] Generate a new random secret key.

## Backups

- [ ] Assure that backups are performed, i.e. backups are created when manually triggering. 
- [ ] Assure that backups files are on a persistent storage, preferably outside the storage used for Waldur's database.

## Air-gapped deployments

- [ ] Make sure that Waldur docker images are mirrored to a local registry.