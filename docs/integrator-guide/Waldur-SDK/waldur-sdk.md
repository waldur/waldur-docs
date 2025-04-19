# Waldur SDK

Waldur SDK is a [python wrapper](https://github.com/waldur/py-client)
for typical REST operations.
You can use it, if you want to send requests to Waldur REST API directly from Python.
SDK is represented by Python module called `waldur_api_client`.

## Installation

Due to frequent SDK updates, installation from the public GitHub repository is highly recommended:

```bash
pip install https://github.com/waldur/py-client/archive/master.zip
```

In order to perform operations, a user needs to create an instance of `AuthenticatedClient` class:

```python
from waldur_api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.example.com", token="SuperSecretToken", prefix="Token")
```

This instance provides interface for further interaction with Waldur and will be used across examples in related documentation.

## Error handling

If the API call fails or returns an unexpected status code, it may raise `UnexpectedStatus` exception if the client is configured with `raise_on_unexpected_status=True`. This can be handled using a `try...except` block. The exception contains both the status code and the response content for debugging purposes.

Example:

```python
from waldur_api_client.api.marketplace_resources import marketplace_resources_list
from waldur_api_client.errors import UnexpectedStatus
import pprint

try:
    result = marketplace_resources_list.sync(client=client)
except UnexpectedStatus as e:
    print(f"Status code: {e.status_code}")
    print("Response content:")
    pprint.pprint(e.content)
```

The `UnexpectedStatus` exception is raised when:

- The API returns a status code that is not documented in the OpenAPI specification
- The `raise_on_unexpected_status` client setting is enabled (default is disabled)


## Disabling TLS validation (not recommended!)

If you are running your commands against Waldur deployment with broken TLS certificates (e.g. in development),
the trick below can be used to disable validation of certificates by SDK, beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken", 
    verify_ssl=False
)
```

Sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

## Installation with Poetry

The recommended way to install the SDK is using Poetry, a modern Python dependency management tool. In order to install Poetry, visit [Poetry](https://python-poetry.org/docs/#installation).

After Poetry is installed, follow these steps:

Download the project:

```shell
git clone https://github.com/waldur/py-client.git
cd py-client
```

Install the SDK:

```shell
poetry install
```

This will automatically create a virtual environment, install the SDK and its dependencies.

## Air gapped installation

If your machine from where you run SDK is not connected to the public Internet, you can use the following method
to transfer required libraries.

On the machine with access to the Internet:

```shell
echo "https://github.com/waldur/py-client/archive/master.zip" > requirements.txt
mkdir dependencies
pip3 download -r requirements.txt -d dependencies/
```

Now transfer content of the dependencies folder and requirements.txt to a machine without public Internet and
run.

```shell
pip3 install --no-index --find-links dependencies/  -r requirements.txt
```
