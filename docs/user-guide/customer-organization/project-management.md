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

!!! note
    If a resource's termination date is beyond the project end date, the project end date will be used instead for that resource as a termination date. However, if a resource's termination date is earlier than the project end date, the resource's own termination date will apply. Setting end dates only triggers the creation of a termination order. Resources continue to exist in the project until the termination order is fully processed.

4. If you need to edit project details later, open your project and select the **Edit** tab.

![type:video](../img/create_project.mp4)
