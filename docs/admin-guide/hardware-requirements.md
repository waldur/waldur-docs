# Hardware requirements

## Docker-compose deployment (on a single server)

- Docker version: 1.13+
- Minimal configuration: 4 vCPU, 8 GB RAM

## Helm-based deployment

- Kubernetes version: 1.18+
- Minimal namespace limits:
  - CPU: **6750m**
    - Waldur: 2750m
    - PostgreSQL: 4000m
  - RAM: **9500Mi**
    - Waldur: 5500Mi
    - PostgreSQL: 4000Mi
  - Storage: **20Gi** (PostgreSQL DB)
- Recommended namespace limits:
  - CPU: **10850m**
    - Waldur: 2750m
    - PostgreSQL: 4000m
  - RAM: **13700Mi**
    - Waldur: 5500Mi
    - PostgreSQL: 4000Mi
  - Storage: **40Gi** (PostgreSQL DB)

## Component specific requirements

### Waldur Mastermind (API)

By default 4 uWSGI processes are started.

- Minimum requirements: 1 CPU, 1GB RAM for every node
- Recommended setup: 2 CPU or more, 2 GB RAM or more

### Waldur Mastermind (Celery worker)

By default a single worker with 10 threads is started.

- Minimum requirements: 2 CPU, 1 GB RAM
- Recommended setup: 4 CPU or more, 8 GB RAM or more

**More memory should be added if more Celery worker processes are running on the same host (512 MB for each 4 Celery workers).**

### Waldur Mastermind (Celery beat)

A single Celery beat process is started.

- Minimum and recommended requirements: 1 CPU, 1 GB RAM

### PostgreSQL

- Minimum requirements: 1 CPU, 1 GB RAM
- Recommended setup: 2 CPU or more, 2 GB RAM or more

### Redis

- Minimum requirements: 1 CPU, 512 MB RAM
- Recommended setup: 2 CPU or more, 1 GB RAM or more

## Waldur HomePort (Nginx)

- Minimum and recommended requirements: 1 CPU and 512MB RAM
