# Project management

Project creation is allowed for organization owners in their organizations and staff users.

!!! note
    User must have an account in Waldur instance to create projects.

1. Select your home organization.
2. Under the **Project** tab, click on **Add**.
3. Fill the necessary fields (fields marked with * are mandatory) and click **Create**.

    - **Project name** - The original title of the project.
    - **Project description** - A brief description about the project.
    - **OECD FoS code** - OECD science field code ([more info](https://joinup.ec.europa.eu/collection/eu-semantic-interoperability-catalogue/solution/field-science-and-technology-classification/about))
    - **Start date** - once reached, marks the date when prepared user invitations are sent out and triggers the processing of previously made resource orders.
    - **End date** – once reached, triggers the creation of termination orders for the existing resources. If the resources have already been terminated by this time, the project will be removed. The date is inclusive.

4. If you need to edit project details later, open your project and select the **Edit** tab.

!!! note
    1. If a resource has a termination date that comes after the project's end date, the project's end date will automatically become that resource's termination date.
    2. If a resource has a termination date that comes before the project's end date, we'll use the resource's original termination date.
    3. Important: Setting any end date (either the project's or a resource's) only creates a termination request. The resource remains active in the project until the termination process is fully completed.

![type:video](../img/create_project.mp4)
