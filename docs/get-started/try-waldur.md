# Try Waldur locally

Run Waldur on your own machine with Docker Compose: the web UI (HomePort), the API (MasterMind), and the services they need.

## What you need

- Docker with the Compose plugin
- At least 8 GB of RAM available to Docker
- Ports 80 and 443 free on `localhost`

## 1. Get the Compose files

```bash
git clone https://github.com/waldur/waldur-docker-compose.git
cd waldur-docker-compose
cp .env.example .env
```

The defaults in `.env` work for a local trial. To reach the instance from another machine, set `WALDUR_DOMAIN`.

## 2. Start the stack

```bash
docker compose up -d
docker compose ps
```

The first start pulls the images and runs the database migrations. Wait until the services report as running or healthy.

## 3. Create an admin user

```bash
docker exec -t waldur-mastermind-worker waldur createstaffuser -u admin -p <password> -e admin@example.com
```

Optionally, create demo marketplace categories for OpenStack (Virtual Private Cloud, VMs and Storage):

```bash
docker exec -t waldur-mastermind-worker waldur load_categories vpc vm storage
```

## 4. Log in

Open <https://localhost>, accept the self-signed certificate, and sign in as `admin` with the password from step 3.

The API is at <https://localhost/api/> and the Django admin at <https://localhost/admin/>.

## What to try next

- [Create an organization](../user-guide/customer-organization/creat_an_organization.md) and [a project](../user-guide/customer-organization/project-management.md) in it.
- [Publish an offering](../user-guide/service-provider-organization/adding-an-offering.md) as a service provider, then order it from the marketplace. The demo categories stay empty until an offering is published in them.
- [Make your first API call](first-api-call.md) against your instance.

## Clean up

```bash
docker compose down -v
```

`-v` also removes the volumes, so the database is deleted.

## Going further

This setup is for trying Waldur out. For a real deployment, read the full [Docker Compose guide](../admin-guide/deployment/docker-compose/index.md) or the [Helm guide](../admin-guide/deployment/helm/index.md), and the [go-live checklist](../admin-guide/checklist-for-production.md).
