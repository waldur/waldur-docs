# Get started

Pick the path that matches what you want to do.

## Try Waldur on your machine

Run a local instance with Docker Compose and look around the UI.
→ [Try Waldur locally](try-waldur.md)

## Use a Waldur deployment

You have an account on a Waldur portal run by your organization, HPC centre or cloud provider.

- [Interface introduction](../user-guide/end-users/interface.md) — how the portal is laid out
- [Create an organization](../user-guide/customer-organization/creat_an_organization.md) and [manage projects](../user-guide/customer-organization/project-management.md)
- [Order and manage resources](../user-guide/customer-organization/resource_management.md)
- [How you reach services](../user-guide/end-users/service-access-modes.md) once they are provisioned

The [user guide](../user-guide/index.md) covers the rest, by role.

## Call the API

Make your first request with curl, the Python SDK or TypeScript.
→ [Make your first API call](first-api-call.md)

## Deploy Waldur for production

1. Check the [hardware requirements](../admin-guide/hardware-requirements.md).
2. Install with [Docker Compose](../admin-guide/deployment/docker-compose/index.md) on a single server, or with [Helm](../admin-guide/deployment/helm/index.md) on Kubernetes.
3. Configure Waldur: the [configuration guide](../admin-guide/mastermind-configuration/configuration-guide.md) lists every setting, and most deployments start with [identity providers](../admin-guide/identities/summary.md).
4. Let service providers [add offerings](../user-guide/service-provider-organization/adding-an-offering.md).

!!! danger
    Before going to production, complete the [go-live checklist](../admin-guide/checklist-for-production.md).

## Contribute to Waldur

Set up a development environment and open your first merge request.
→ [Contribute to Waldur](contribute.md)

## Learn the concepts

The [platform overview](../about/concepts/platform.md) explains Waldur's three building blocks — users, organizations and projects — and how everything else, from orders to invoices, attaches to them.
