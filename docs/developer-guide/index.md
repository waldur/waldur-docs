# Developer documentation

## Overview

Waldur is a multi-tenant cloud service management platform built with Django and React. This developer documentation
provides comprehensive guidance for contributors, plugin developers, and anyone looking to extend or modify
Waldur's functionality.

Waldur follows a service-oriented architecture where the backend (Waldur Mastermind) exposes a REST API that is consumed by the frontend (HomePort).

## Core architecture

Waldur's architecture is built around several key concepts:

- **Managed Entities**: Resources that Waldur manages through its database as the authoritative source of information
- **Role-Based Access Control**: A permission system that determines what users can do based on roles
- **Background Processing**: Uses Celery for executing heavier requests and background tasks
- **Event System**: Comprehensive event logging and notification system, including MQTT-based event notifications
- **Quotas**: Resource tracking functionality that stores and queries resource limits and usages

## Development environment

Waldur can be set up for development using two main approaches:

- Dev Containers (for VS Code or GitHub Codespaces)
- Manual installation from source

The development workflow follows git flow principles, with feature branches created from the develop branch and merged via pull requests after testing and review.

Whether you're implementing new features, fixing bugs, or developing plugins, this documentation provides the necessary information to effectively contribute to the Waldur ecosystem.