# Organization and project management

## User guide for adding organizations

!!! note
    Organization creation is only allowed for users in Staff role!

Organization in Waldur context means whatever grouping platform owner would like to have.
This can mean for example research group, institution, department or working group. Organization has an owner who can manage the organization, projects and users connected to that project.

## Create a new organization

1. Login to Waldur and select "Organizations" from the left-side menu and then select "Add" from the right.
2. Fill the form and click "Create organization":

    - Name - Name of the organization
    - Contact email - email of the person, who is responsible for the organization

3. Organization edit page opens, where it is possible to add additional information, like policies, contact information. It is beneficial to assign a predefined category group (like private company, university, government, individial person etc) to organization.

![type:video](img/create_organization.mp4)

## Creation of projects

Project creation is allowed for organization owners in their organizations and staff users.

Prerequisites for creating projects:

    - User must have an account in Waldur instance.

1. Select your home organization.
2. Under the "Project" tab, click on "Add project".
3. Fill the necessary fields (fields marked with * are mandatory).

    - Project name - The original title of the project.
    - Project description - A brief description about the project.
    - OECD FoS code - OECD science field code ([more info](https://joinup.ec.europa.eu/collection/eu-semantic-interoperability-catalogue/solution/field-science-and-technology-classification/about))
    - Start date - once reached, marks the date when prepared user invitations are sent out and triggers the processing of previously made resource orders.
    - End date – once reached, triggers the creation of termination orders for the existing resources. If the resources have already been terminated by this time, the project will be removed. The date is inclusive.

![type:video](img/create_project.mp4)