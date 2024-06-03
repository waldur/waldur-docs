# Debug instructions for Waldur Mastermind

## Filter logs for email-related events

Upon sending an email, Waldur logs an event to the Celery output.

### Docker Compose

A dedicated container `logger` collects all the logs from other Waldur containers.
All you need is to:

1. Go to the logs directory. It should be in the same directory where Compose runs:

    ```sh
    $ cd ./logs
    $ ls -lh waldur-mastermind-worker.log
    -rw-r--r--. 1 root root 39M Jun  3 08:53 waldur-mastermind-worker.log
    ```

2. Check the logs in the corresponding file:

    ```sh
    $ cat waldur-mastermind-worker.log | grep -i "about to send"
    ...
    [2024-05-31 08:09:46,569: INFO/ForkPoolWorker-1] About to send notify_provider_about_pending_order notification to email1@example.com
    [2024-05-31 08:09:48,706: INFO/ForkPoolWorker-1] About to send notify_provider_about_pending_order notification to email2@example.com
    [2024-05-31 08:09:49,524: INFO/ForkPoolWorker-8] About to send notify_provider_about_pending_order notification to email3@example.com
    [2024-05-31 09:17:05,673: INFO/ForkPoolWorker-8] About to send invitation_created notification to email1@example.com
    [2024-05-31 09:56:55,144: INFO/ForkPoolWorker-8] About to send notify_provider_about_pending_order notification to email2@example.com
    ```

### Helm

In this case, you can use the same approach, but execute `kubectl` instead of `docker` command:

```bash
kubectl logs -l app=waldur-mastermind-worker --tail=-1 | grep -i "about to send"
```
