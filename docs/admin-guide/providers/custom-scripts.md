# Custom scripts

`Custom scripts` is a type of plugin that allows defining custom scripts that are executed
at different lifecycle events of the resource. The scripts are executed in one time containers.
Depending on the deployment type, it can be either a docker container for docker-compose-based, or
Kubernetes Jobs for Helm-based deployments.

The following lifecycle events are supported:

- Creation;
- Update - change of plans or limits;
- Termination;
- Regular updates - executed once per hour, aka pull script.

## Script output format

It is possible to control certain aspects of resource management with outputs of the custom scripts.
Below we list currently supported conventions and their impact.

### Creation script

You can set the the backend_id of the created resource by passing a single string as the last
line of the output.

```python
# for python-based scripts
UUID = "12345abcd"
print(UUID)
```

If you want to save additional metadata, then last line of output should consist of 2 strings:

- ID of the created resource that will be saved as backend_id;
- Base64 encoded metadata object.

```python
# for python-based scripts
import base64

UUID = "12345abcd"
metadata = {"backend_metadata": {"cpu": 1}}
print(UUID + ' ' + base64.b64encode(metadata))
```

### Regular updates script

The script for regular updates allows to update usage information as well as provide updates of reporting.
In all cases the last line should include a base64-encoded string containing a dictionary with keywords:

- "usages" for usage reporting;
- "report" for updating resource report.

Examples of Python-based scripts are:

```python
# for python-based scripts
import base64

info = {
  "usages":
    {
      "type": "cpu",
      "amount": 10
    }
}
print(base64.b64encode(info))
```

```python
# for python-based scripts
import base64

info = {
  "report":
    {
      "header": "header",
      "body": "body"
    }
}
print(base64.b64encode(info))
```
