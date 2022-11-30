# Overriding notification templates via admin panel

An admin can override(edit the content) the templates of notifications with the following sequence of actions:

* Go to admin panel (e.g. `http://localhost:8080/admin/`)

* Open Templates: `Utilities` -> `Database templates` -> `Templates`

![Go to admin panel](img/notification_templates_step_1.png)

* Click on `Add template` on the right side.

![Go to admin panel](img/notification_templates_step_2.png)

* Enter the path to the template file into the `Name` input field as shown below.

    The name should have a `<waldur_application_name>/<event_name>_<postfix>.<extension>` format, where `<postfix>` can be either `message` or `subject`, and `<extension>` - either `txt` or `html`.

    You can find a list of all notification templates [here](notifications.md)

![Go to admin panel](img/notification_templates_step_3.png)

* Scroll down and click on `Save and continue editing` and you should have the content of the template loaded automatically

![Go to admin panel](img/notification_templates_step_4.png)

* Edit the `Content` field as you like and `Save` the changes.

![Go to admin panel](img/notification_templates_step_5.png)