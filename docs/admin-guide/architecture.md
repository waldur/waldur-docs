# Architecture

Waldur is composed of a several components.

- Homeport (web client, graphical interface) - React application
- Mastermind API server - Django/Django REST Framework application implementing the core business logic
- Celery workers - Background processing of tasks
- Celery beat - Scheduling of periodic tasks for background processing
- PostgreSQL database - Storing persistent data, also serves as Celery result store in Kubernetes deployment
- RabbitMQ - Tasks queue and result store for Celery

![diagram](../assets/components.svg)
