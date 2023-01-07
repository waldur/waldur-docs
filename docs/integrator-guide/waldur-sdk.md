# Waldur SDK

Waldur SDK is a [python wrapper](https://github.com/waldur/ansible-waldur-module/blob/develop/waldur_client.py)
for typical REST operations.
You can use it, if you want to send requests to Waldur REST API directly from Python.
SDK is represented by Python module called `waldur_client.py` from `ansible-waldur-module` repository.

## Installation

Due to frequent SDK updates, installation from the public GitHub repository is highly recommended:

```bash
pip install https://github.com/waldur/python-waldur-client/archive/master.zip
```

In order to perform operations, a user needs to create an instance of `WaldurClient` class:

```python
from waldur_client import WaldurClient

client = WaldurClient('<api-url>', '<api-token>')
```

This instance provides interface for further interaction with Waldur and will be used across examples in related documentation.

## Error handling

If the client fails to perform an operation, it raises `WaldurClientException`. This can be handled using `try...except` block.
Example:

```python
from waldur_client import WaldurClient, WaldurClientException
import pprint

client = WaldurClient('https://abc.example.com/api', 'some-token')

try:
    client.list_marketplace_resources()
except WaldurClientException as e:
    pprint.pprint(e)

# WaldurClientException("HTTPSConnectionPool(host='abc.example.com', port=443):
# Max retries exceeded with url: /api/marketplace-resources/?page_size=200
# (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x110636430>:
# Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))")
```

## Disabling TLS validation (not recommended!)

If you are running your commands against Waldur deployment with broken TLS certificates (e.g. in development),
the trick below can be used to disable validation of certificates by SDK.

```python
import os
import requests

os.environ['CURL_CA_BUNDLE']=""
session = requests.Session()
session.verify = False

...
```

## Air gapped installation

If your machine from where you run SDK is not connected to the public Internet, you can use the following method
to transfer required libraries.

On the machine with access to the Internet:

```shell
echo "https://github.com/waldur/python-waldur-client/archive/master.zip" > requirements.txt
mkdir dependencies
pip3 download -r requirements.txt -d dependencies/
```

Now transfer content of the dependencies folder and requirements.txt to a machine without public Internet and
run.

```shell
pip3 install --no-index --find-links dependencies/  -r requirements.txt
```
