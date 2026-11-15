# Waldur Python SDK

Waldur SDK is a thin Python wrapper for common REST operations.
It allows you to interact with the Waldur REST API directly from your Python code.
The SDK is provided as a Python module named `waldur_api_client`.

## Installation

The Waldur SDK is available on PyPI as `waldur-api-client` and requires Python 3.9 or newer.
Install the version that matches your Waldur server, so that the client knows the same endpoints and fields:

```bash
pip install "waldur-api-client==<waldur-version>"
uv add "waldur-api-client==<waldur-version>"
poetry add "waldur-api-client==<waldur-version>"
```

In order to perform operations, a user needs to create an instance of `AuthenticatedClient` class:

```python
from waldur_api_client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://api.example.com",
    token="SuperSecretToken",
)
```

This instance provides interface for further interaction with Waldur and will be used across examples in related documentation.

## Calling an endpoint

Each endpoint is a module under `waldur_api_client.api.<tag>`, named after the endpoint's operation, for example
`waldur_api_client.api.marketplace_resources.marketplace_resources_list`. A module offers up to four functions:

- `sync(...)` returns the parsed response: a model object, a list of them, or `None`.
- `sync_detailed(...)` returns a `Response` with `status_code`, `headers`, raw `content` and `parsed`.
- `asyncio(...)` and `asyncio_detailed(...)` are the `async` versions of the two above.

Endpoints whose response has no body, such as most actions that only change state, have only
`sync_detailed` and `asyncio_detailed`. List endpoints also have `sync_all` and `asyncio_all`, which follow the
pagination and return every page.

The fields of returned objects are the attributes of the model classes in `waldur_api_client.models`.

## Error handling

If the API returns a status code that the endpoint does not document, for example `400` for invalid input or `403`
for missing permissions, the SDK raises `UnexpectedStatus`. The exception carries the status code, the raw response
content and the URL.

```python
from waldur_api_client.api.marketplace_resources import marketplace_resources_list
from waldur_api_client.errors import UnexpectedStatus

try:
    result = marketplace_resources_list.sync(client=client)
except UnexpectedStatus as e:
    print(f"Status code: {e.status_code}")
    print(f"Response content: {e.content.decode(errors='ignore')}")
```

`sync_detailed` raises `UnexpectedStatus` in the same cases. Use it when a successful call needs more than the
parsed body, for example the response headers or the raw content:

```python
from waldur_api_client.api.marketplace_resources import marketplace_resources_list

response = marketplace_resources_list.sync_detailed(client=client)
print(response.headers.get("x-result-count"))
resources = response.parsed
```

## Disabling TLS validation (not recommended!)

If you are running your commands against Waldur deployment with broken TLS certificates (e.g. in development),
the trick below can be used to disable validation of certificates by SDK, beware that **this is a security risk**.

```python
from waldur_api_client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://internal_api.example.com",
    token="SuperSecretToken",
    verify_ssl=False,
)
```

Sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
from waldur_api_client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://internal_api.example.com",
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```


## Air gapped installation

If your machine from where you run SDK is not connected to the public Internet, you can use the following method
to transfer required libraries.

On a machine with access to the Internet and the same Python version and platform, download the client and its
dependencies:

```shell
echo "waldur-api-client==<waldur-version>" > requirements.txt
mkdir dependencies
pip3 download -r requirements.txt -d dependencies/
```

Now transfer content of the dependencies folder and requirements.txt to a machine without public Internet and
run.

```shell
pip3 install --no-index --find-links dependencies/  -r requirements.txt
```
