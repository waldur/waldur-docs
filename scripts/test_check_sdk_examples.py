"""Tests for check_sdk_examples.py. Needs waldur-api-client installed."""

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "check_sdk_examples.py"
spec = importlib.util.spec_from_file_location("check_sdk_examples", SCRIPT)
check_sdk_examples = importlib.util.module_from_spec(spec)
# Registered before exec: @dataclass looks its module up in sys.modules.
sys.modules["check_sdk_examples"] = check_sdk_examples
spec.loader.exec_module(check_sdk_examples)


def check(source: str):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "page.md"
        path.write_text(f"Intro\n\n```python\n{source}```\n", encoding="utf-8")
        return [p.message for p in check_sdk_examples.check_file(path)]


class CheckSdkExamplesTest(unittest.TestCase):
    def test_valid_example_passes(self):
        self.assertEqual(
            check(
                "from waldur_api_client.api.users import users_list\n"
                "users = users_list.sync_all(client=client)\n"
            ),
            [],
        )

    def test_missing_import_is_reported(self):
        messages = check("from waldur_api_client.models import NoSuchModel\n")
        self.assertEqual(len(messages), 1)
        self.assertIn("cannot import NoSuchModel", messages[0])

    def test_missing_function_is_reported(self):
        messages = check(
            "from waldur_api_client.api.users import users_list\n"
            "users_list.no_such_function(client=client)\n"
        )
        self.assertIn("users_list.no_such_function does not exist", messages[0])

    def test_unknown_and_missing_arguments_are_reported(self):
        messages = check(
            "from waldur_api_client.api.marketplace_resources import marketplace_resources_team_list\n"
            "marketplace_resources_team_list.sync(client=client, bogus=1)\n"
        )
        self.assertTrue(
            any("unexpected keyword arguments ['bogus']" in m for m in messages)
        )
        self.assertTrue(
            any("missing required arguments ['uuid']" in m for m in messages)
        )

    def test_model_arguments_are_checked(self):
        messages = check(
            "from waldur_api_client.models import SetOfferingsUsernameRequest\n"
            "SetOfferingsUsernameRequest(username='u', bogus=1)\n"
        )
        self.assertTrue(
            any("unexpected keyword arguments ['bogus']" in m for m in messages)
        )
        self.assertTrue(
            any("missing required arguments ['user_uuid']" in m for m in messages)
        )

    def test_syntax_error_reports_markdown_line(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "page.md"
            path.write_text(
                'Intro\n\n```python\nx = "unterminated\n```\n', encoding="utf-8"
            )
            problems = check_sdk_examples.check_file(path)
        self.assertEqual(problems[0].line, 4)
        self.assertIn("syntax error", problems[0].message)


if __name__ == "__main__":
    unittest.main()
