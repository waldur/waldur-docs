# Your POSIX identity on Linux and HPC offerings

When you get access to a Linux or HPC offering — for example a SLURM cluster
or a storage service that provisions a Unix account for you — the service
provider assigns you two numeric identifiers:

- a **UID** (user id), which identifies your personal account, and
- a **primary GID** (group id), which identifies your default group.

These numbers are how the underlying systems track file ownership, disk
quotas and job scheduling. You normally never type them yourself: you log in
with your username and SSH key, and the cluster maps you to your UID and GID
behind the scenes.

## What to expect

- **They are stable.** Your UID and primary GID stay the same for the lifetime
    of your account, so files you create keep their ownership and your jobs are
    accounted to you consistently.
- **They are unique within a provider.** Each service provider keeps its own
    pool of identifiers, so no two people on that provider's systems share a
    UID, and a user's id never collides with a project or role group id.
- **They are managed for you.** You do not request or change these numbers —
    the provider allocates them automatically from a reserved pool when your
    account is created.

Your service provider can look up the UID and primary GID that were assigned to
your account, which is useful when you open a support request about file
permissions or scheduling.

![Assigned UID and GID of offering users](../img/posix-offering-users-uid-gid.png)

!!! note
    If you have accounts with more than one service provider, your UID and GID
    may differ between them — each provider numbers its own users
    independently. Within a single provider they stay consistent across all of
    that provider's offerings.
