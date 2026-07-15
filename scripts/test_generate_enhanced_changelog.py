import unittest
import tempfile
import shutil
import sys
from pathlib import Path

# Add current directory to path to resolve import
sys.path.append(str(Path(__file__).parent))

from . import generate_enhanced_changelog_multi_repo as changelog_script
MultiRepoChangelogGenerator = changelog_script.MultiRepoChangelogGenerator


class TestMultiRepoChangelogGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = MultiRepoChangelogGenerator()
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_commit_categorization(self):
        """Test if commits are correctly categorized based on subject keywords"""
        commits = [
            {'subject': 'feat: support openstack floating ip resource', 'hash': 'a1b2c3d', 'author': 'Dev', 'date': '2026-07-14'},
            {'subject': 'fix: resolve race condition in volume deletion', 'hash': 'e5f6g7h', 'author': 'Dev', 'date': '2026-07-14'},
            {'subject': 'BREAKING CHANGE: rename structure_project endpoint to project', 'hash': 'i9j0k1l', 'author': 'Dev', 'date': '2026-07-14'},
            {'subject': 'security: patch input sanitization CVE-2026-1234', 'hash': 'm3n4o5p', 'author': 'Dev', 'date': '2026-07-14'},
            {'subject': 'refactor: simplify request client auth header checks', 'hash': 'q7r8s9t', 'author': 'Dev', 'date': '2026-07-14'},
            {'subject': 'docs: add release orchestration instructions to developer guide', 'hash': 'u1v2w3x', 'author': 'Dev', 'date': '2026-07-14'},
            {'subject': 'chore: bump waldur mastermind to v8.0.10', 'hash': 'y5z6a7b', 'author': 'Dev', 'date': '2026-07-14'},
            {'subject': 'random cleanup commit without prefix', 'hash': 'c9d0e1f', 'author': 'Dev', 'date': '2026-07-14'},
        ]

        cats = self.generator.analyze_commit_categories(commits)

        self.assertEqual(len(cats['features']), 1)
        self.assertEqual(cats['features'][0]['hash'], 'a1b2c3d')

        self.assertEqual(len(cats['fixes']), 1)
        self.assertEqual(cats['fixes'][0]['hash'], 'e5f6g7h')

        self.assertEqual(len(cats['breaking']), 1)
        self.assertEqual(cats['breaking'][0]['hash'], 'i9j0k1l')

        self.assertEqual(len(cats['security']), 1)
        self.assertEqual(cats['security'][0]['hash'], 'm3n4o5p')

        self.assertEqual(len(cats['refactor']), 1)
        self.assertEqual(cats['refactor'][0]['hash'], 'q7r8s9t')

        self.assertEqual(len(cats['docs']), 1)
        self.assertEqual(cats['docs'][0]['hash'], 'u1v2w3x')

        self.assertEqual(len(cats['chore']), 1)
        self.assertEqual(cats['chore'][0]['hash'], 'y5z6a7b')

        self.assertEqual(len(cats['other']), 1)
        self.assertEqual(cats['other'][0]['hash'], 'c9d0e1f')

    def test_subject_cleaning(self):
        """Test if commit prefixes and issue codes are correctly stripped, formatted and capitalized"""
        # Test cleaning with matching categories (prefixes should be stripped)
        self.assertEqual(
            self.generator._clean_commit_subject('feat: add support for project quotas', 'features'),
            'Add support for project quotas.'
        )
        self.assertEqual(
            self.generator._clean_commit_subject('fix(core): resolve ssh key whitespace bug', 'fixes'),
            'Resolve ssh key whitespace bug.'
        )
        self.assertEqual(
            self.generator._clean_commit_subject('refactor: optimize database indices', 'refactor'),
            'Optimize database indices.'
        )

        # Test cleaning with general category (non-matching prefixes are capitalized but kept)
        test_cases_general = [
            ('feat: add support for project quotas', 'Feat: add support for project quotas.'),
            ('[WALDUR-412] improve performance of marketplace queries', 'Improve performance of marketplace queries.'),
            ('WAL-1982: implement token rotation', 'Implement token rotation.'),
            ('docs: update readmes', 'Update readmes.'),
            ('Chore: bump python client', 'Bump python client.'),
            ('non-prefixed sentence already ending with period.', 'Non-prefixed sentence already ending with period.'),
            ('sh', 'Sh.'),
        ]

        for input_subject, expected in test_cases_general:
            cleaned = self.generator._clean_commit_subject(input_subject, 'general')
            self.assertEqual(cleaned, expected)

    def test_file_exclusion(self):
        """Test if files are properly excluded according to repository configurations"""
        # SDK exclusion checks
        self.assertTrue(self.generator.should_exclude_file('waldur_client/models.py', 'py-client'))
        self.assertTrue(self.generator.should_exclude_file('docs/index.md', 'py-client'))
        self.assertFalse(self.generator.should_exclude_file('pyproject.toml', 'py-client'))

        self.assertTrue(self.generator.should_exclude_file('lib/client.js', 'js-client'))
        self.assertTrue(self.generator.should_exclude_file('package-lock.json', 'js-client'))
        self.assertFalse(self.generator.should_exclude_file('package.json', 'js-client'))

        self.assertTrue(self.generator.should_exclude_file('waldur/provider.go', 'go-client'))
        self.assertFalse(self.generator.should_exclude_file('go.mod', 'go-client'))

        # Ansible & Terraform exclusion checks
        self.assertTrue(self.generator.should_exclude_file('ansible_waldur_module/ansible_collections/waldur/core/README.md', 'ansible-waldur-module-next'))
        self.assertFalse(self.generator.should_exclude_file('Makefile', 'ansible-waldur-module-next'))

        self.assertTrue(self.generator.should_exclude_file('internal/provider/resource_project.go', 'terraform-provider-waldur'))
        self.assertTrue(self.generator.should_exclude_file('services/core/resource_ssh_public_key.go', 'terraform-provider-waldur'))
        self.assertTrue(self.generator.should_exclude_file('provider-manifest.json', 'terraform-provider-waldur'))
        self.assertFalse(self.generator.should_exclude_file('main.go', 'terraform-provider-waldur'))

    def test_terraform_changelog_extraction(self):
        """Test if the script correctly extracts the requested version block from CHANGELOG.md"""
        repo_path = Path(self.temp_dir)
        changelog_file = repo_path / "CHANGELOG.md"

        # Test case: missing file
        self.assertEqual(self.generator._extract_terraform_changelog(repo_path, "v8.0.9"), "")

        # Test case: populated file
        mock_content = """# Changelog

## v8.0.9

### ⚠️ Breaking changes

- `core_ssh_public_key`: attribute `fingerprint_md5` type changed from `types.Int64` to `types.String`
- `customer_permission`: attribute `role` is now required

## v8.0.8

### Added
- New resource `structure_project`
"""
        changelog_file.write_text(mock_content)

        # Extraction for matching version (with 'v')
        extracted_v = self.generator._extract_terraform_changelog(repo_path, "v8.0.9")
        expected_v = (
            "### ⚠️ Breaking changes\n\n"
            "- `core_ssh_public_key`: attribute `fingerprint_md5` type changed from `types.Int64` to `types.String`\n"
            "- `customer_permission`: attribute `role` is now required"
        )
        self.assertEqual(extracted_v, expected_v)

        # Extraction for matching version (without 'v')
        extracted_no_v = self.generator._extract_terraform_changelog(repo_path, "8.0.9")
        self.assertEqual(extracted_no_v, expected_v)

        # Extraction for another existing version in the file
        extracted_other = self.generator._extract_terraform_changelog(repo_path, "v8.0.8")
        self.assertEqual(extracted_other, "### Added\n- New resource `structure_project`")

        # Extraction for a non-existing version
        self.assertEqual(self.generator._extract_terraform_changelog(repo_path, "v8.0.10"), "")

    def test_ansible_changelog_extraction(self):
        """Test if the script extracts breaking changes section from multiple collections READMEs"""
        repo_path = Path(self.temp_dir)
        collections_dir = repo_path / "ansible_waldur_module" / "ansible_collections"
        collections_dir.mkdir(parents=True)

        # Create two mock collections
        core_readme = collections_dir / "waldur" / "core"
        core_readme.mkdir(parents=True)
        (core_readme / "README.md").write_text("""# Waldur Core Ansible Collection

## Breaking Changes for 8.0.9
- `waldur_client`: credential field is removed in favor of token authentication.

## Breaking Changes for 8.0.8
- Old changes...
""")

        marketplace_readme = collections_dir / "waldur" / "marketplace"
        marketplace_readme.mkdir(parents=True)
        (marketplace_readme / "README.md").write_text("""# Waldur Marketplace Ansible Collection

## Breaking Changes for 8.0.9
- `waldur_marketplace_resource`: state changes.

# Waldur Ansible Collection
General boilerplate docs.
""")

        # Call extraction
        extracted = self.generator._extract_ansible_changelog(repo_path, "8.0.9")
        
        # Verify both collections are parsed and output matches expected formatting
        self.assertIn("#### Collection `waldur.core`", extracted)
        self.assertIn("- `waldur_client`: credential field is removed in favor of token authentication.", extracted)
        self.assertIn("#### Collection `waldur.marketplace`", extracted)
        self.assertIn("- `waldur_marketplace_resource`: state changes.", extracted)
        self.assertNotIn("## Breaking Changes for 8.0.8", extracted)
        self.assertNotIn("General boilerplate docs", extracted)

        # Verify empty output on non-matching version
        self.assertEqual(self.generator._extract_ansible_changelog(repo_path, "8.0.10"), "")


import consolidate_changelog


class TestConsolidateChangelog(unittest.TestCase):
    def test_get_previous_tag(self):
        content = """# Changelog

## 8.1.0-rc.1 - 2026-07-15
Test RC.

## 8.0.9 - 2026-07-14
Test stable.

## 8.0.8-rc.1 - 2026-07-13
"""
        tag = consolidate_changelog.get_previous_tag(content)
        self.assertEqual(tag, "8.0.9")

    def test_clean_rc_entries(self):
        content = """# Changelog

## 8.1.0-rc.2 - 2026-07-15
RC 2
---

## 8.1.0-rc.1 - 2026-07-14
RC 1
---

## 8.0.9 - 2026-07-13
Stable
---
"""
        cleaned = consolidate_changelog.clean_rc_entries(content, "8.1.0")
        self.assertNotIn("8.1.0-rc.2", cleaned)
        self.assertNotIn("8.1.0-rc.1", cleaned)
        self.assertIn("8.0.9", cleaned)
        self.assertIn("Stable\n---", cleaned)

    def test_rotate_changelog(self):
        entries = []
        for i in range(25):
            entries.append(f"## 8.0.{i} - 2026-07-{i}\nEntry {i}\n---")
        
        content = "\n\n".join(entries)
        rotated = consolidate_changelog.rotate_changelog(content, 20)
        
        self.assertIn("## 8.0.0", rotated)
        self.assertIn("## 8.0.19", rotated)
        self.assertNotIn("## 8.0.20", rotated)
        self.assertNotIn("## 8.0.24", rotated)


if __name__ == '__main__':
    unittest.main()
