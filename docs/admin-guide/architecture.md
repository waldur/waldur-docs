# Architecture

Waldur is composed of several runtime components that work together to provide a
comprehensive cloud-management platform. For the higher-level data model — users,
organizations, projects, and roles — see [Platform](../about/concepts/platform.md).

## Components

- **Homeport** (web client) — React single-page application.
- **Mastermind API server** — Django + Django REST Framework application implementing the business logic.
- **Celery workers** — background processing of tasks.
- **Celery beat** — scheduler for periodic tasks.
- **PostgreSQL** — persistent storage; also serves as the Celery result store in Kubernetes deployments.
- **RabbitMQ** — task queue and result store for Celery.
- **Waldur site agent** — remote agent that manages provider resources and synchronises data on the provider side.

## Runtime topology

```d2
direction: down
classes: {
  frontend:      { style: { fill: "#d5e8d4"; stroke: "#82b366" } }
  backend:       { style: { fill: "#dae8fc"; stroke: "#6c8ebf" } }
  infra:         { style: { fill: "#fff2cc"; stroke: "#d6b656" } }
  agent:         { style: { fill: "#f8cecc"; stroke: "#b85450" } }
}

user: User { class: frontend; shape: person }
browser: Web browser { class: frontend }
homeport: Homeport\n(React SPA) { class: frontend }
api: Mastermind API\n(Django + DRF) { class: backend }
worker: Celery worker { class: backend }
beat: Celery beat { class: backend }
db: PostgreSQL { class: infra; shape: cylinder }
queue: RabbitMQ { class: infra; shape: queue }
agent: Waldur site agent\n(remote) { class: agent }

user -> browser
browser -> homeport: serves SPA
homeport -> api: REST calls
agent -> api: REST calls
api -> db: persist
api -> queue: enqueue tasks
worker -> queue: pull
worker -> db: write results
beat -> queue: enqueue periodic
```
