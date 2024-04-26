# Cookie policy and Telemetry

## Cookie policy

Waldur can save data about the user in a browser. Data type and policy depends on the component.

### HomePort

- Saving of the latest view point of the user.
- Saving redirect information, i.e. where to forward from a certain state.
- Saving which authentication method was used by user for logging in.
- Saving user session token.
- Saving user language preference.

### MasterMind

- Saving authentication token (cookie) when a user logs into /admin management interface.

## Telemetry

Waldur can send telemetry metrics to the telemetry server. Metrics are sent only if the feature is enabled and the telemetry server is configured in the Waldur settings.
To toggle the feature on or off, navigate to `Administration -> Settings -> Features` in HomePort and enable or disable the `Send telemetry metrics` feature.
![](img/telemetry-feature.png)

An **example** of telemetry metrics is shown below:

```bash
Deployment ID: 0f115db062b7c0dd030b16878c7
Deployment type: other
Helpdesk backend: zammad
Helpdesk integration status: true
Number of users: 1555
Number of offerings: 796
Types of offering:
    Waldur.RemoteOffering
    Marketplace.Booking
    Marketplace.Rancher
    OpenStackTenant.Volume
    VMware.VirtualMachine
    Marketplace.Basic
Version: 6.6.5+3.g6491c9dab.dirty
Installation date: 2022-06-10 11:28:50.585100+0000
```
