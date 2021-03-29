# General Architecture

- [Modules Diagram](#modules-diagram)

## Modules Diagram
#### TODO: add changed diagram
## Physical Architecture
#### TODO: add changed diagram
### Backend
- uWSGI (web server)
- Django REST API server
- Celery workers (backend processing)
- PostgreSQL (operational database)
- Redis (message queue and cache)

### Frontend
- HTTP web server; frontend is a JavaScript application written in ReactJS
