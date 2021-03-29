# Hardware requirements

## Waldur Mastermind

### Celery workers
By default 3 Celery workers and one Celery beat process are started.

- Minimum requirements: 2 CPU, 2 GB RAM
- Recommended setup: 4 CPU or more, 8 GB RAM or more

**More memory should be added if more Celery worker processes are running on the same host (512 MB for each 4 Celery workers).**

### PostgreSQL
- Minimum requirements: 1 CPU, 1 GB RAM
- Recommended setup: 2 CPU or more, 2 GB RAM or more

### Redis
- Minimum requirements: 1 CPU, 512 MB RAM
- Recommended setup: 2 CPU or more, 1 GB RAM or more

### uWSGI
By default 4 uWSGI processes are started.
- Minimum requirements: 1 CPU, 1GB RAM for every node
- Recommended setup: 2 CPU or more, 2 GB RAM or more

## Waldur HomePort
Minimum web server capable to serve static files is enough. HomePort should work just fine with Nginx on 1 CPU and 512 MB RAM.

## All-in-one
It is possible to run Celery, PostgreSQL, Redis and uWSGI services on one machine. This setup is not recommended for production environments but can be useful for demonstration and evaluation purposes.

- Recommended setup: 4 CPU, 10 GB RAM
- Operating system: CentOS7 or RHEL7

