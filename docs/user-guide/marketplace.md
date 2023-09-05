# Marketplace introduction

Marketplace is a central module for provisioning of Waldur resources. Marketplace contains Offerings that
belong to a special type of Organizations - Service Providers. Marketplace provides common functionality
for resource lifecycle management, accounting and invoicing. Specifics are implemented in the Marketplace plugins
(e.g. for OpenStack, SLURM, Rancher, etc).

## Diagram of concepts

![Diagram of marketplace concepts](img/marketplace-structure.png)

## Adding a new Offering

To create a new Offering in the Marketplace, you need to:

- Assure that categories are configured in the Marketplace.
- Create at least one service provider.
- Create and activate a public offering.

### Creating a Service Provider

Pick or create an organization that will be used as a service provider. Mark it a such in the Management tab of the
organization using "Register as service provider":

![Mark as service provider](img/serviceprovider_reg.jpg)

### Creating Marketplace categories

To create a category, either use administrative interface of Waldur, hosted under ```/admin`` (can be accessed by staff users)
or use management command for loading the pre-defined categories.

- With Docker-compose deployment:

```bash
  docker exec -t waldur-mastermind-worker waldur load_categories  # vpc vm storage ...
```

- With Helm deployment

Open waldur-mastermind-worker shell and execute the following command:

1. Get waldur-mastermind-worker pod name

```bash
  # Example:
  kubectl get pods -A | grep waldur-mastermind-worker # -->
  # default       waldur-mastermind-worker-6d98cd98bd-wps8n   1/1     Running     0          9m9s
```

1. Connect to pod via shell

```bash
  # Example:
  kubectl exec -it waldur-mastermind-worker-6d98cd98bd-wps8n -- /bin/bash
```

1. Execute command to see available or add a category

```bash
  waldur load_categories  # vpc vm storage ...
```

### Creating public Offering

Once you have a service provider and at least one category defined, you can add a new service offering.

- Go to Provider -> Marketplace -> Offerings and click Add new offering.

![List offerings](img/add_offering.jpg)

- Fill in the name, category and type of the offering.

![Add offering](img/add_offering_2.jpg)

- Fill in additional information and click on Activate. After that, the offering is visible in the Marketplace.

![Activate offering](img/add_offering_3.jpg)
