# Hardware Requirements

This document outlines the recommended hardware requirements for deploying Waldur in different environments.

## Deployment Methods

| Deployment Method | Minimum Requirements | Recommended Configuration | Notes |
|-------------------|----------------------|---------------------------|-------|
| **Docker Compose** | • 4 vCPU<br>• 12 GB RAM<br>• 20 GB storage | • 8 vCPU<br>• 16 GB RAM<br>• 40 GB storage | Single server deployment, fastest to set up |
| **Kubernetes (Helm)** | See detailed component breakdown below | See detailed component breakdown below | Production-grade, scalable deployment |

## Kubernetes Resource Requirements

### Namespace Totals

| Requirement Level | CPU | Memory | Storage |
|-------------------|-----|--------|---------|
| **Minimal** | 8000m (8 vCPU) | 10000Mi (10 GB) | 20Gi for PostgreSQL |
| **Recommended** | 12000m (12 vCPU) | 14000Mi (14 GB) | 40Gi for PostgreSQL |

### Per-Component Requirements

| Component | CPU Requests | CPU Limits | Memory Requests | Memory Limits | Notes |
|-----------|--------------|------------|-----------------|---------------|-------|
| **Waldur Mastermind API** | 500m | 1000m | 2000Mi | 4000Mi | Serves API requests, increase for high traffic |
| **Waldur Mastermind Worker** | 1000m | 2000m | 2000Mi | 4000Mi | Processes background tasks, critical for performance |
| **Waldur Mastermind Beat** | 250m | 500m | 500Mi | 1000Mi | Schedules periodic tasks |
| **Waldur HomePort** | 250m | 500m | 500Mi | 1000Mi | Serves web interface |
| **PostgreSQL (Single)** | 500m | 1000m | 1024Mi | 2048Mi | Main database, persistent storage |
| **PostgreSQL (HA)** | 1000m per replica | 2000m per replica | 2048Mi per replica | 4096Mi per replica | For high availability (3 replicas recommended) |
| **RabbitMQ** | 500m | 1000m | 512Mi | 1000Mi | Message broker |

### Storage Requirements

| Component | Minimal Size | Recommended Size | Notes |
|-----------|--------------|------------------|-------|
| **PostgreSQL** | 10Gi | 40Gi | Main database storage, grows with user and resource count |
| **RabbitMQ** | 2Gi | 5Gi | Message queue persistence |
| **Backups** | 20Gi | 50Gi | Separate storage for database backups |

## Scaling Recommendations

| User Scale | API Replicas | Worker Replicas | PostgreSQL Configuration | Additional Notes |
|------------|--------------|-----------------|--------------------------|------------------|
| **Small** (<100 users) | 1 | 1 | Single instance | Default values sufficient |
| **Medium** (100-500 users) | 2 | 2 | Single instance with increased resources | Enable HPA for API |
| **Large** (500+ users) | 3+ | 3+ | HA with 3 replicas | Enable HPA for all components, increase resource limits |

## Performance Factors

Consider increasing resources beyond the recommended values if your deployment includes:

- High number of concurrent users (>50 simultaneous active sessions)
- Large number of resources being managed (>1000 total resources)
- Complex marketplace offerings with many components
- Frequent reporting or billing operations
- Integration with multiple external systems

## Hardware Recommendations for Production

| Component | vCPU | RAM | Storage | Network |
|-----------|------|-----|---------|---------|
| **Control Plane Nodes** | 4 cores | 8 GB | 100 GB SSD | 1 Gbps |
| **Worker Nodes** | 8 cores | 16 GB | 200 GB SSD | 1 Gbps |
| **Database Nodes** | 4 cores | 8 GB | 100 GB SSD | 1 Gbps |
| **Load Balancer** | 2 cores | 4 GB | 20 GB | 1 Gbps |
