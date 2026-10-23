# Make your first API call

Everything in the Waldur UI goes through the REST API, so anything you can do there you can script.

## 1. Get a token

Copy your API token from HomePort, as described in [Authentication](../integrator-guide/APIs/authentication.md#authentication-token-management). It is sent as `Authorization: Token <token>`.

For automation, prefer a [personal access token](../user-guide/end-users/personal-access-tokens.md): it can be limited to specific scopes and given an expiry date. It is sent as `Authorization: Bearer <token>`.

A token carries your permissions, so keep it out of shared scripts and repositories.

## 2. List the marketplace offerings

=== "curl"

    ```bash
    WALDUR_URL="https://waldur.example.com"
    WALDUR_TOKEN="<token>"

    curl -H "Authorization: Token $WALDUR_TOKEN" \
         -H "Accept: application/json" \
         "$WALDUR_URL/api/marketplace-public-offerings/"
    ```

=== "Python"

    ```bash
    pip install waldur-api-client
    ```

    ```python
    from waldur_api_client import AuthenticatedClient
    from waldur_api_client.api.marketplace_public_offerings import marketplace_public_offerings_list

    client = AuthenticatedClient(
        base_url="https://waldur.example.com",
        token="<token>",
    )

    offerings = marketplace_public_offerings_list.sync(client=client)
    for o in offerings:
        print(o.name, "—", o.uuid)
    ```

=== "TypeScript"

    ```ts
    const WALDUR_URL = "https://waldur.example.com";
    const TOKEN = process.env.WALDUR_TOKEN!;

    const res = await fetch(`${WALDUR_URL}/api/marketplace-public-offerings/`, {
      headers: {
        Authorization: `Token ${TOKEN}`,
        Accept: "application/json",
      },
    });
    console.log(await res.json());
    ```

The response is a JSON list of the offerings you can see. `401 Unauthorized` means the token is wrong or expired.

## 3. Order a resource

An order names the offering, the project to create the resource in, and a plan, each by its API URL:

```python
from waldur_api_client.api.marketplace_orders import marketplace_orders_create
from waldur_api_client.models import GenericOrderAttributes, OrderCreateRequest

WALDUR_URL = "https://waldur.example.com"

order = marketplace_orders_create.sync(
    client=client,
    body=OrderCreateRequest(
        offering=f"{WALDUR_URL}/api/marketplace-public-offerings/<offering-uuid>/",
        project=f"{WALDUR_URL}/api/projects/<project-uuid>/",
        plan=f"{WALDUR_URL}/api/marketplace-public-offerings/<offering-uuid>/plans/<plan-uuid>/",
        attributes=GenericOrderAttributes.from_dict({"name": "my-first-resource"}),
        accepting_terms_of_service=True,
    ),
)
print(order.uuid, order.state)
```

The order then moves through its states: one of the `pending-*` states while it waits for approval or a start date, `executing` while the resource is provisioned, and `done`. The new resource appears in the project.

## Where to go next

- [Python SDK](../integrator-guide/sdk.md) and [SDK examples](../integrator-guide/SDK-Examples/allocation-management-sp.md)
- [waldur-cli](../integrator-guide/waldur-cli/index.md), [Terraform](../integrator-guide/terraform.md) and [Ansible](../integrator-guide/ansible/index.md)
- [Service provider onboarding](../integrator-guide/service-provider-onboarding.md), to publish your own offerings through the API
- [API lifecycle](../integrator-guide/api-lifecycle.md): what stays stable between releases
- [REST API reference](https://api-docs.waldur.com/), every endpoint
