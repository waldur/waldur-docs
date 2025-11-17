# Test author guide

## End-to-End Testing with VCR

This project uses a powerful "record and replay" testing strategy for its end-to-end (E2E) tests, powered by
`pytest` and the `VCR.py` library. This allows us to create high-fidelity tests based on real API interactions
while ensuring our CI/CD pipeline remains fast, reliable, and completely independent of a live API server.

The E2E tests are located in the `ansible_waldur_generator/tests/e2e/` directory.

### Core Concept: Cassette-Based Testing

1. **Recording Mode:** The first time a test is run, it requires access to a live Waldur API. The test
   executes its workflow (e.g., creating a VM), and `VCR.py` records every single HTTP request and its
   corresponding response into a YAML file called a "cassette" (e.g., `ansible_waldur_generator/tests/e2e/cassettes/test_create_instance.yaml`).

2. **Replaying Mode:** Once a cassette file exists, all subsequent runs of the same test will be completely
   offline. `VCR.py` intercepts any outgoing HTTP call, finds the matching request in the cassette, and "replays"
   the saved response. The test runs instantly without any network activity.

This approach gives us the best of both worlds: the realism of integration testing and the speed and
reliability of unit testing.

### Running the E2E Tests

The E2E tests are designed to be run in two distinct modes.

#### Mode 1: Replaying (Standard CI/CD and Local Testing)

This is the default mode. If the cassette files exist in
`ansible_waldur_generator/tests/e2e/cassettes/`, the tests will run
offline. This is the fastest and most common way to run the tests.

```bash
# Run all E2E tests using their saved cassettes
poetry run pytest ansible_waldur_generator/tests/e2e/
```

This command should complete in a few seconds.

#### Mode 2: Recording (When Adding or Modifying Tests)

You only need to enter recording mode when you are:

- Creating a new E2E test.
- Modifying an existing E2E test in a way that changes its API interactions (e.g., adding a new parameter
  to a module call).

**Workflow for Recording a Test:**

1. **Prepare the Live Environment:** Ensure you have a live Waldur instance and that all the necessary
   prerequisite resources for your test exist (e.g., for creating a VM, you need a project, offering, flavor,
   image, etc.).

2. **Set Environment Variables:** Provide the test runner with the credentials for the live API. **Never
   hardcode these in the test files.**

    ```bash
    export WALDUR_API_URL="https://your-waldur-instance.com/api/"
    export WALDUR_ACCESS_TOKEN="<your_real_api_token>"
    ```

3. **Delete the Old Cassette:** To ensure a clean recording, delete the corresponding YAML file for the
   test you are re-recording. `pytest-vcr` names cassettes based on the test file and function name.

    ```bash
    # Example for the instance creation test
    rm ansible_waldur_generator/tests/e2e/cassettes/test_e2e_modules.py::TestInstanceModule::test_create_instance.yaml
    ```

4. **Run Pytest:** Execute the test. It will now connect to the live API specified by your environment
   variables.

    ```bash
    # Run a specific test to record its interactions
    poetry run pytest ansible_waldur_generator/tests/e2e/test_e2e_modules.py::TestInstanceModule::test_create_instance
    ```

    After the test passes, a new cassette file will be generated.

5. **Review and Commit:**
   - **CRITICAL:** Inspect the newly generated `.yaml` cassette file.
   - Verify that sensitive data, like the `Authorization` token, has been automatically scrubbed and
     replaced with a placeholder (e.g., `DUMMY_TOKEN`). This is configured in `pyproject.toml` or `pytest.ini`.
   - Commit the new or updated cassette file to your Git repository along with your test code changes.

### Writing a New E2E Test

Follow the pattern established in `ansible_waldur_generator/tests/e2e/`:

1. **Organize with Classes:** Group tests for a specific module into a class (e.g., `TestVolumeModule`).
2. **Use the `@pytest.mark.vcr` Decorator:** Add this decorator to your test class or individual test methods
   to enable VCR.
3. **Use the `auth_params` Fixture:** This fixture provides the standard `api_url` and `access_token`
   parameters, reading them from environment variables during recording and using placeholders during replay.
4. **Use the `run_module_harness`:** This generic helper function handles the boilerplate of mocking
   `AnsibleModule` and running the module's `main()` function.
5. **Write Your Test Logic:**
   - **Arrange:** Define the `user_params` dictionary that simulates the Ansible playbook input.
   - **Act:** Call the `run_module_harness`, passing it the imported module object and the `user_params`.
   - **Assert:** Check the `exit_result` and `fail_result` to verify that the module behaved as expected
     (e.g., `changed` is `True`, the returned `resource` has the correct data).

**Example Skeleton:**

```python
# In a test file within ansible_waldur_generator/tests/e2e/

import pytest
from ansible_collections.waldur.structure.plugins.modules import project as project_module
# ... import harness and fixtures ...

@pytest.mark.vcr
class TestProjectModule:
    def test_create_new_project(self, auth_params):
        # 1. Arrange: Define user input
        user_params = {
            "state": "present",
            "name": "E2E New Project",
            "customer": "Big Corp",
            **auth_params
        }

        # 2. Act: Run the module
        exit_result, fail_result = run_module_harness(project_module, user_params)

        # 3. Assert: Verify the outcome
        assert fail_result is None
        assert exit_result['changed'] is True
        assert exit_result['resource']['name'] == "E2E New Project"
```
