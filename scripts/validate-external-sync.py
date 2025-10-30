#!/usr/bin/env python3
"""
Validation script for external documentation synchronization.
Checks sync status and identifies issues with external documentation.
"""

import sys
import yaml
import re
from pathlib import Path
from datetime import datetime
import argparse

class ExternalSyncValidator:
    def __init__(self, config_file='external-sources.yml'):
        self.config = self.load_config(config_file)
        self.settings = self.config.get('settings', {})
        self.max_sync_age = self.settings.get('max_sync_age_hours', 24)
        self.preserve_local = self.settings.get('preserve_local', [])

    def load_config(self, config_file):
        """Load the external sources configuration."""
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)

    def extract_external_marker_info(self, content):
        """Extract information from external document marker."""
        marker_pattern = r'<!-- EXTERNAL DOCUMENT(.*?)-->'
        match = re.search(marker_pattern, content, re.DOTALL)

        if not match:
            return None

        marker_content = match.group(1)
        info = {}

        for line in marker_content.split('\n'):
            line = line.strip()
            if ':' in line:
                key, value = line.split(':', 1)
                info[key.strip()] = value.strip()

        return info

    def check_file_sync_status(self, file_path):
        """Check the sync status of a single file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(1000)  # Read first 1000 chars to find marker
        except (IOError, UnicodeDecodeError):
            return {'status': 'error', 'message': 'Could not read file'}

        marker_info = self.extract_external_marker_info(content)

        if not marker_info:
            return {'status': 'no_marker', 'message': 'No external marker found'}

        # Check sync timestamp
        last_sync = marker_info.get('Last Sync')
        if last_sync:
            try:
                sync_time = datetime.fromisoformat(last_sync.replace('Z', '+00:00'))
                age_hours = (datetime.now() - sync_time.replace(tzinfo=None)).total_seconds() / 3600

                if age_hours > self.max_sync_age:
                    return {
                        'status': 'stale',
                        'message': f'Last sync {age_hours:.1f} hours ago (max: {self.max_sync_age}h)',
                        'age_hours': age_hours,
                        'marker_info': marker_info
                    }
            except ValueError:
                return {'status': 'invalid_timestamp', 'message': 'Invalid sync timestamp format'}

        return {
            'status': 'ok',
            'message': 'File is properly synced',
            'marker_info': marker_info
        }

    def should_exclude_from_source(self, file_path, source_key, mapping, all_mappings):
        """
        Check if a file should be excluded from this mapping's validation because
        it belongs to a more specific mapping.

        This handles cases where:
        1. Different sources with overlapping paths:
           - Homeport docs are in docs/developer-guide/ui
           - Mastermind docs are in docs/developer-guide
           Files in ui/ should be validated against homeport-ui, not mastermind-api.

        2. Same source with multiple mappings to overlapping directories:
           - Mapping 1: docs/ -> docs/developer-guide
           - Mapping 2: docs/admin -> docs/developer-guide/admin
           Files in admin/ should only be validated by Mapping 2, not Mapping 1.
        """
        local_path = Path(mapping['local'])

        # Check all mappings (from all sources, including the same source)
        for other_source_key, other_mappings in all_mappings.items():
            for other_mapping in other_mappings:
                # Skip the current mapping itself
                if (other_source_key == source_key and
                    other_mapping.get('local') == mapping.get('local') and
                    other_mapping.get('remote') == mapping.get('remote')):
                    continue

                other_local_path = Path(other_mapping['local'])

                # Check if the other mapping is a subdirectory of this mapping
                try:
                    # If other_local_path is under local_path
                    other_local_path.relative_to(local_path)

                    # Check if the file is under the other mapping's path
                    try:
                        file_path.relative_to(other_local_path)
                        # File is under the more specific mapping, exclude it from this mapping
                        return True
                    except ValueError:
                        # File is not under other_local_path
                        continue
                except ValueError:
                    # other_local_path is not under local_path
                    continue

        return False

    def validate_mapping(self, source_key, source, mapping, all_mappings):
        """Validate a single mapping configuration."""
        local_path = Path(mapping['local'])

        if not local_path.exists():
            return {
                'status': 'missing_local',
                'files_checked': 0,
                'issues': [{'type': 'missing_directory', 'message': f"Local directory {mapping['local']} does not exist"}]
            }

        issues = []
        files_checked = 0
        external_files = 0
        local_files = 0

        for file_path in local_path.rglob('*.md'):
            if file_path.name.startswith('.'):
                continue

            # Skip files that belong to a more specific mapping from another source
            if self.should_exclude_from_source(file_path, source_key, mapping, all_mappings):
                continue

            files_checked += 1

            # Check if file should be preserved locally
            should_preserve = any(
                file_path.name == pattern or file_path.match(pattern)
                for pattern in self.preserve_local
            )

            sync_status = self.check_file_sync_status(file_path)
            relative_path = file_path.relative_to(local_path)

            if sync_status['status'] == 'no_marker':
                if should_preserve:
                    local_files += 1
                    # This is expected for preserved files
                    continue
                else:
                    issues.append({
                        'type': 'untracked_local_file',
                        'file': str(relative_path),
                        'message': 'Local file without external marker (may need manual review)'
                    })
                    local_files += 1

            elif sync_status['status'] == 'stale':
                external_files += 1
                issues.append({
                    'type': 'stale_sync',
                    'file': str(relative_path),
                    'message': sync_status['message'],
                    'age_hours': sync_status.get('age_hours', 0)
                })

            elif sync_status['status'] == 'error':
                issues.append({
                    'type': 'file_error',
                    'file': str(relative_path),
                    'message': sync_status['message']
                })

            elif sync_status['status'] == 'ok':
                external_files += 1
                # Verify the marker points to the correct source
                marker_info = sync_status.get('marker_info', {})
                expected_repo = source['repository']
                actual_repo = marker_info.get('Source', '')

                if expected_repo not in actual_repo:
                    issues.append({
                        'type': 'wrong_source',
                        'file': str(relative_path),
                        'message': f'Marker points to {actual_repo}, expected {expected_repo}'
                    })

        return {
            'status': 'ok' if not issues else 'issues',
            'files_checked': files_checked,
            'external_files': external_files,
            'local_files': local_files,
            'issues': issues
        }

    def validate_source(self, source_key, source, all_sources):
        """Validate all mappings for a source."""
        print(f"\n{'='*60}")
        print(f"Validating: {source['name']}")
        print(f"{'='*60}")

        total_stats = {
            'files_checked': 0,
            'external_files': 0,
            'local_files': 0,
            'issues': []
        }

        # Build all_mappings dict with source_key -> list of mappings
        all_mappings = {}
        for src_key, src_config in all_sources.items():
            all_mappings[src_key] = src_config.get('mappings', [])

        for mapping in source.get('mappings', []):
            print(f"\n  Checking mapping: {mapping['remote']} -> {mapping['local']}")

            result = self.validate_mapping(source_key, source, mapping, all_mappings)

            # Accumulate stats
            total_stats['files_checked'] += result['files_checked']
            total_stats['external_files'] += result.get('external_files', 0)
            total_stats['local_files'] += result.get('local_files', 0)
            total_stats['issues'].extend(result['issues'])

            # Print mapping summary
            print(f"    Files checked: {result['files_checked']}")
            if result.get('external_files', 0) > 0:
                print(f"    External files: {result['external_files']}")
            if result.get('local_files', 0) > 0:
                print(f"    Local files: {result['local_files']}")

            if result['issues']:
                print(f"    Issues found: {len(result['issues'])}")
                for issue in result['issues']:
                    print(f"      - {issue['type']}: {issue.get('file', '')} - {issue['message']}")
            else:
                print("    ✅ No issues found")

        return total_stats

    def validate_all(self, source_filter=None):
        """Validate all configured sources."""
        print("External Documentation Sync Validation")
        print(f"Config: {len(self.config['sources'])} sources configured")
        print(f"Max sync age: {self.max_sync_age} hours")

        total_stats = {
            'files_checked': 0,
            'external_files': 0,
            'local_files': 0,
            'issues': []
        }

        critical_issues = 0
        warning_issues = 0

        all_sources = self.config['sources']

        for source_key, source in all_sources.items():
            if source_filter and source_key not in source_filter:
                continue

            stats = self.validate_source(source_key, source, all_sources)

            # Accumulate total stats
            for key in ['files_checked', 'external_files', 'local_files']:
                total_stats[key] += stats[key]
            total_stats['issues'].extend(stats['issues'])

        # Categorize issues
        for issue in total_stats['issues']:
            if issue['type'] in ['missing_directory', 'file_error', 'wrong_source']:
                critical_issues += 1
            else:
                warning_issues += 1

        # Print overall summary
        print(f"\n{'='*60}")
        print("VALIDATION SUMMARY")
        print(f"{'='*60}")
        print(f"Total files checked: {total_stats['files_checked']}")
        print(f"External files: {total_stats['external_files']}")
        print(f"Local files: {total_stats['local_files']}")
        print(f"Critical issues: {critical_issues}")
        print(f"Warnings: {warning_issues}")

        # Print issue breakdown
        if total_stats['issues']:
            print(f"\nISSUE BREAKDOWN:")
            issue_types = {}
            for issue in total_stats['issues']:
                issue_type = issue['type']
                issue_types[issue_type] = issue_types.get(issue_type, 0) + 1

            for issue_type, count in issue_types.items():
                print(f"  {issue_type}: {count}")

        # Recommendations
        if critical_issues > 0:
            print(f"\n❌ {critical_issues} critical issues found. Run sync to fix:")
            print("   python scripts/sync-external-docs.py")
            return 2
        elif warning_issues > 0:
            print(f"\n⚠️  {warning_issues} warnings found. Consider running sync:")
            print("   python scripts/sync-external-docs.py")
            return 1
        else:
            print(f"\n✅ All external documentation is properly synchronized!")
            return 0

    def generate_report(self, output_file=None):
        """Generate a detailed validation report."""
        # This could be extended to generate HTML or markdown reports
        pass

def main():
    parser = argparse.ArgumentParser(description='Validate external documentation sync status')
    parser.add_argument('--config', '-c', default='external-sources.yml',
                        help='Configuration file path')
    parser.add_argument('--sources', '-s', nargs='*',
                        help='Specific sources to validate (default: all)')
    parser.add_argument('--report', '-r',
                        help='Generate detailed report to file')

    args = parser.parse_args()

    try:
        validator = ExternalSyncValidator(args.config)

        exit_code = validator.validate_all(args.sources)

        if args.report:
            validator.generate_report(args.report)

        return exit_code

    except Exception as e:
        print(f"Error: {e}")
        return 3

if __name__ == '__main__':
    sys.exit(main())
