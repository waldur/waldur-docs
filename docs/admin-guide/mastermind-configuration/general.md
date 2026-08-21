# General Configuration

Outline:

- [General Configuration](#general-configuration)
  - [Introduction](#introduction)
  - [Quick access links](#quick-access-links)
  - [Outgoing email](#outgoing-email)
  - [Custom templates configuration](#custom-templates-configuration)
  - [Local time zone configuration](#local-time-zone-configuration)

## Introduction

Waldur is a [Django](https://www.djangoproject.com)-based application, so configuration is done by modifying `settings.py` file.

If you want to configure options related to Django, such as tune caches, database connection, configure custom logging, etc, please refer to [Django documentation](https://docs.djangoproject.com/en/6.0/).

Please consult [configuration guide](configuration-guide.md) to learn more.

## Quick access links

The **Quick access** panel on the HomePort dashboard can carry custom links to systems outside
Waldur — a status page, a ticketing system, an institutional wiki.

These are managed through the user interface rather than through settings: open
**Administration → User interface → Navigation shortcuts** and click **Add**. Each shortcut
takes a name, an optional description, an optional icon and the target URL, and is stored via
the `/api/external-links/` endpoint.

## Outgoing email

SMTP transport, sender addresses and notification enablement are covered separately in
[Email configuration](email.md). Note that the SMTP settings have no `GLOBAL_*` environment
variable equivalent — they can only be set in `/etc/waldur/override.conf.py`.

## Custom templates configuration

To overwrite default templates you should use [django-dbtemplates](https://github.com/jazzband/django-dbtemplates). It allows creation of templates through `/admin`.

## Local time zone configuration

Set `TIME_ZONE` setting in `/etc/waldur/override.conf.py` to use local time zone. By default it is set to UTC. See the [list of time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for possible options.
