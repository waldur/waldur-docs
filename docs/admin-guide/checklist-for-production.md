# Checklist for Go live

## General

- [ ] Make sure that privacy policy and terms of use are updated to the site specific ones.
- [ ] Reboot test: restart all the nodes where Waldur components are running, application should recover automatically.

## Email

Outgoing email needs three separate things to be right. See
[Email configuration](mastermind-configuration/email.md) for the settings behind each item.

- [ ] SMTP transport is configured in `/etc/waldur/override.conf.py` and verified end to end with
      `waldur sendtestemail <your-address>`.
- [ ] Outgoing addresses are set (`DEFAULT_FROM_EMAIL`, `DEFAULT_REPLY_TO_EMAIL`), and the sending
      domain authorises the relay in its SPF record — ideally with DKIM signing as well.
- [ ] The notifications relevant to the deployment are enabled. **All notification types ship
      disabled**, so a correct SMTP setup on its own still sends nothing.

## Security

- [ ] Remove or disable default staff accounts.
- [ ] Generate a new random secret key.

## Backups

- [ ] Make sure that configuration of Waldur is backed up and versioned.
- [ ] Assure that DB backups are performed, i.e. backups are created when manually triggering
- [ ] Assure that DB backups files are on a persistent storage, preferably outside the storage used for Waldur's database.

## Air-gapped deployments

- [ ] Make sure that Waldur docker images are mirrored to a local registry.
