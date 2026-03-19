# Order management

## Order lifecycle

When a customer requests a resource from your offering, an order is created. Orders progress through several states:

| State | Description |
|-------|-------------|
| **Pending consumer** | Waiting for consumer approval |
| **Pending provider** | Waiting for provider approval |
| **Executing** | Resource provisioning in progress |
| **Done** | Order completed successfully |
| **Erred** | Order failed with errors |
| **Canceled** | Order was canceled |
| **Rejected** | Order was rejected by provider |

## Managing orders

As a service provider (organization owner, offering owner, or offering manager), you can manage orders for your offerings from the **Provider** dashboard under the **Orders** section.

### Approving and rejecting orders

When an order is in **Pending provider** state, you can:

- **Approve** the order to start resource provisioning
- **Reject** the order with a reason that will be communicated to the customer

### Marking orders as done

For offerings that are managed manually (Basic and SLURM offerings), you can mark an executing order as **Done** once the resource has been provisioned on the backend.

### Retrying erred orders

When an order fails during processing, it enters the **Erred** state. If the failure was caused by a transient issue (e.g., temporary backend unavailability, network timeout), authorized users can retry the order instead of asking the customer to create a new one.

#### Who can retry

- Platform staff
- Organization owners of the service provider
- Offering managers

#### How to retry

1. Navigate to the order details page. The order state will show as **Erred** with an error message describing what went wrong.

    ![Order in erred state with error details](../img/order-retry-erred-state.png)

2. Click the **Error details** tab to review what went wrong before retrying.

    ![Error details tab showing error message and traceback](../img/order-retry-error-details.png)

3. Click the **Actions** dropdown button and select **Retry**.

    ![Actions dropdown showing the Retry option](../img/order-retry-actions-dropdown.png)

4. A confirmation dialog will appear explaining that the order and its resource will be reset to an active processing state. Click **Yes** to confirm.

    ![Confirmation dialog for retrying an erred order](../img/order-retry-confirmation-dialog.png)

5. After confirming, the order transitions back to **Executing** and a success notification appears.

    ![Order successfully retried, now in Executing state](../img/order-retry-success.png)

!!! warning
    Retrying an order clears the previous error message and traceback. If you need to preserve error details for investigation, note them down before retrying.

!!! note
    Retry is currently supported for **Basic** and **SLURM** (site agent) offering types. Other offering types do not support this action.

#### What happens during retry

| Order type | Resource state after retry |
|------------|---------------------------|
| Create | Creating |
| Update | Updating |
| Terminate | Terminating |

The order's error message, error traceback, and completion timestamp are cleared. The order is then resubmitted for processing through the normal provisioning pipeline.
