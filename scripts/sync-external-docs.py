#!/usr/bin/env python3
"""
Pull-based external documentation synchronization script.
Pulls documentation from remote repositories and syncs with local directories.
"""

import os
import sys
import shutil
import subprocess
import yaml
import fnmatch
from pathlib import Path
from datetime import datetime
import re
import argparse

class ExternalDocSyncer:
    def __init__(self, config_file='external-sources.yml', dry_run=False):
        self.config = self.load_config(config_file)
        self.settings = self.config.get('settings', {})
        self.temp_base = Path(self.settings.get('temp_dir', '.temp_clones'))
        self.external_marker = self.settings.get('external_marker_template', '')
        self.preserve_local = self.settings.get('preserve_local', [])
        self.dry_run = dry_run

    def load_config(self, config_file):
        """Load the external sources configuration."""
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)

    def get_auth_token(self, source):
        """Get authentication token for a source repository."""
        auth_config = source.get('auth', {})
        token_env = auth_config.get('token_env')

        if token_env:
            token = os.getenv(token_env)
            if not token:
                print(f"Warning: Authentication token {token_env} not found in environment")
                return None
            return token
        return None

    def clone_repository(self, source, source_key):
        """Clone a repository to a temporary directory."""
        repo_url = source['repository']
        branch = source['branch']

        # Create authenticated URL if token is available
        token = self.get_auth_token(source)
        if token and repo_url.startswith('https://'):
            # Insert token into URL: https://token@gitlab.com/...
            repo_url = repo_url.replace('https://', f'https://oauth2:{token}@')

        temp_dir = self.temp_base / source_key

        # Remove existing clone if present
        if temp_dir.exists():
            shutil.rmtree(temp_dir)

        temp_dir.parent.mkdir(parents=True, exist_ok=True)

        print(f"Cloning {source['name']} from {source['repository']}")

        try:
            # Clone with depth=1 for faster cloning
            subprocess.run([
                'git', 'clone',
                '--branch', branch,
                '--depth', '1',
                repo_url, str(temp_dir)
            ], check=True, capture_output=True)

            return temp_dir

        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e}")
            print(f"Stdout: {e.stdout.decode()}")
            print(f"Stderr: {e.stderr.decode()}")
            return None

    def should_exclude(self, file_path, excludes):
        """Check if a file should be excluded based on exclude patterns."""
        file_name = os.path.basename(file_path)
        rel_path = str(file_path)

        for pattern in excludes:
            if fnmatch.fnmatch(file_name, pattern) or fnmatch.fnmatch(rel_path, pattern):
                return True
        return False

    def is_in_excluded_subdir(self, file_rel_path, excluded_subdirs):
        """Check if a file is within any of the excluded subdirectories."""
        file_path = Path(file_rel_path)
        for excluded_subdir in excluded_subdirs:
            try:
                # Check if file_path is relative to excluded_subdir
                file_path.relative_to(excluded_subdir)
                return True
            except ValueError:
                # Not in this subdirectory
                continue
        return False

    def is_binary_file(self, file_path):
        """Check if a file is binary by checking its extension."""
        # Common binary file extensions
        binary_extensions = {
            '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.svg',
            '.pdf', '.zip', '.tar', '.gz', '.bz2',
            '.exe', '.dll', '.so', '.dylib',
            '.mp3', '.mp4', '.avi', '.mov',
            '.woff', '.woff2', '.ttf', '.eot'
        }

        return file_path.suffix.lower() in binary_extensions

    def has_external_marker(self, file_path):
        """Check if a file has an external document marker."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(500)  # Just read first 500 chars
                return '<!-- EXTERNAL DOCUMENT' in content
        except (IOError, UnicodeDecodeError):
            return False

    def add_external_marker(self, content, source, mapping, remote_file, temp_dir):
        """Add external document marker to file content."""
        # Calculate the relative path from the temp_dir's remote path
        remote_base = temp_dir / mapping['remote']
        rel_file_path = remote_file.relative_to(remote_base)

        # Construct the clean remote path
        clean_remote_path = f"{mapping['remote']}/{rel_file_path}".replace('\\', '/')

        marker = self.external_marker.format(
            repository=source['repository'],
            branch=source['branch'],
            remote_path=clean_remote_path,
            local_path=mapping['local'],
            sync_time=datetime.now().isoformat()
        )

        # Remove existing marker if present
        if '<!-- EXTERNAL DOCUMENT' in content:
            pattern = r'<!-- EXTERNAL DOCUMENT.*?-->\s*'
            content = re.sub(pattern, '', content, flags=re.DOTALL)

        return marker + '\n\n' + content

    def get_subdirectory_mappings(self, source, current_mapping):
        """Get subdirectories that have their own mappings with different targets."""
        subdirs_to_exclude = []
        current_remote = Path(current_mapping['remote'])
        current_local = Path(current_mapping['local'])

        for mapping in source.get('mappings', []):
            if mapping == current_mapping:
                continue

            other_remote = Path(mapping['remote'])
            other_local = Path(mapping['local'])

            # Check if other mapping is a subdirectory of current mapping
            try:
                # If other_remote is relative to current_remote, it's a subdirectory
                rel_path = other_remote.relative_to(current_remote)

                # Check if the local targets are different (not a subdirectory relationship)
                try:
                    other_local.relative_to(current_local)
                    # If we get here, the local path is a subdirectory, so targets are aligned
                except ValueError:
                    # Local targets are different, so we should exclude this subdirectory
                    subdirs_to_exclude.append(rel_path)

            except ValueError:
                # Not a subdirectory, skip
                continue

        return subdirs_to_exclude

    def sync_mapping(self, source, mapping, temp_dir):
        """Sync a single mapping from remote to local."""
        remote_path = temp_dir / mapping['remote']
        local_path = Path(mapping['local'])

        if not remote_path.exists():
            print(f"  Warning: Remote path {mapping['remote']} does not exist")
            return {'synced': 0, 'removed': 0, 'warnings': 1}

        stats = {'synced': 0, 'removed': 0, 'warnings': 0}
        excludes = source.get('excludes', [])

        # Get subdirectories that should be excluded from this sync
        excluded_subdirs = self.get_subdirectory_mappings(source, mapping)
        if excluded_subdirs:
            print(f"    Excluding subdirectories with separate mappings: {', '.join(str(s) for s in excluded_subdirs)}")

        # Track which local files should remain (those from remote)
        expected_files = set()

        # Check if this is a file-to-file mapping (e.g., README.md -> index.md)
        is_file_mapping = remote_path.is_file()

        if is_file_mapping:
            # Single file mapping
            if self.should_exclude(remote_path, excludes):
                print(f"    File excluded by pattern: {mapping['remote']}")
                return stats

            # Create parent directory for the destination file
            if not self.dry_run:
                local_path.parent.mkdir(parents=True, exist_ok=True)
                print(f"    Ensured directory exists: {local_path.parent}")
            else:
                if not local_path.parent.exists():
                    print(f"    [DRY RUN] Would create directory: {local_path.parent}")

            expected_files.add(local_path)

            # Process file based on whether it's binary or text
            try:
                is_binary = self.is_binary_file(remote_path)

                if is_binary:
                    # Handle binary files - just copy them
                    if self.dry_run:
                        if local_path.exists():
                            # Compare binary content
                            with open(remote_path, 'rb') as f:
                                remote_content = f.read()
                            with open(local_path, 'rb') as f:
                                local_content = f.read()
                            if remote_content != local_content:
                                print(f"    [DRY RUN] Would update binary: {local_path.name}")
                            else:
                                print(f"    [DRY RUN] No change: {local_path.name}")
                        else:
                            print(f"    [DRY RUN] Would create binary: {local_path.name}")
                    else:
                        shutil.copy2(remote_path, local_path)
                        print(f"    Synced binary: {local_path.name}")
                else:
                    # Handle text files
                    with open(remote_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Add external marker for markdown files
                    if remote_path.suffix.lower() == '.md':
                        content = self.add_external_marker(content, source, mapping, remote_path, temp_dir)

                    # Write to local file (or simulate in dry-run mode)
                    if self.dry_run:
                        if local_path.exists():
                            with open(local_path, 'r', encoding='utf-8') as f:
                                existing_content = f.read()
                            if existing_content != content:
                                print(f"    [DRY RUN] Would update: {local_path.name}")
                            else:
                                print(f"    [DRY RUN] No change: {local_path.name}")
                        else:
                            print(f"    [DRY RUN] Would create: {local_path.name}")
                    else:
                        with open(local_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"    Synced: {local_path.name}")

                stats['synced'] += 1

            except (IOError, UnicodeDecodeError) as e:
                print(f"    Error processing {local_path.name}: {e}")
                stats['warnings'] += 1

            return stats

        # Directory mapping - create local directory if it doesn't exist
        if not self.dry_run:
            local_path.mkdir(parents=True, exist_ok=True)
            print(f"    Ensured directory exists: {local_path}")
        else:
            if not local_path.exists():
                print(f"    [DRY RUN] Would create directory: {local_path}")

        # Copy files from remote to local
        for remote_file in remote_path.rglob('*'):
            if remote_file.is_file():
                if self.should_exclude(remote_file, excludes):
                    continue

                rel_path = remote_file.relative_to(remote_path)

                # Skip files in subdirectories that have their own mappings with different targets
                if self.is_in_excluded_subdir(rel_path, excluded_subdirs):
                    continue

                local_file = local_path / rel_path
                expected_files.add(local_file)

                # Create directory if needed
                if not self.dry_run:
                    local_file.parent.mkdir(parents=True, exist_ok=True)
                else:
                    if not local_file.parent.exists():
                        print(f"    [DRY RUN] Would create directory: {local_file.parent}")

                # Process file based on whether it's binary or text
                try:
                    is_binary = self.is_binary_file(remote_file)

                    if is_binary:
                        # Handle binary files - just copy them
                        if self.dry_run:
                            if local_file.exists():
                                # Compare binary content
                                with open(remote_file, 'rb') as f:
                                    remote_content = f.read()
                                with open(local_file, 'rb') as f:
                                    local_content = f.read()
                                if remote_content != local_content:
                                    print(f"    [DRY RUN] Would update binary: {rel_path}")
                                else:
                                    print(f"    [DRY RUN] No change: {rel_path}")
                            else:
                                print(f"    [DRY RUN] Would create binary: {rel_path}")
                        else:
                            shutil.copy2(remote_file, local_file)
                            print(f"    Synced binary: {rel_path}")
                    else:
                        # Handle text files
                        with open(remote_file, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # Add external marker for markdown files
                        if remote_file.suffix.lower() == '.md':
                            content = self.add_external_marker(content, source, mapping, remote_file, temp_dir)

                        # Write to local file (or simulate in dry-run mode)
                        if self.dry_run:
                            # Check if file exists and content differs
                            if local_file.exists():
                                with open(local_file, 'r', encoding='utf-8') as f:
                                    existing_content = f.read()
                                if existing_content != content:
                                    print(f"    [DRY RUN] Would update: {rel_path}")
                                else:
                                    print(f"    [DRY RUN] No change: {rel_path}")
                            else:
                                print(f"    [DRY RUN] Would create: {rel_path}")
                        else:
                            with open(local_file, 'w', encoding='utf-8') as f:
                                f.write(content)
                            print(f"    Synced: {rel_path}")

                    stats['synced'] += 1

                except (IOError, UnicodeDecodeError) as e:
                    print(f"    Error processing {rel_path}: {e}")
                    stats['warnings'] += 1

        # Check for local files that should be removed
        for local_file in local_path.rglob('*'):
            if local_file.is_file() and local_file not in expected_files:
                # Check if this file should be preserved
                should_preserve = False
                for preserve_pattern in self.preserve_local:
                    if fnmatch.fnmatch(local_file.name, preserve_pattern):
                        should_preserve = True
                        break

                if should_preserve:
                    print(f"    Preserved local file: {local_file.relative_to(local_path)}")
                    continue

                # Check if file has external marker (indicating it was previously synced)
                # Only check markdown files for markers
                if self.has_external_marker(local_file):
                    if self.dry_run:
                        print(f"    [DRY RUN] Would remove obsolete file: {local_file.relative_to(local_path)}")
                    else:
                        print(f"    Removed obsolete external file: {local_file.relative_to(local_path)}")
                        local_file.unlink()
                    stats['removed'] += 1
                elif local_file.suffix.lower() == '.md':
                    print(f"    Warning: Local file without external marker: {local_file.relative_to(local_path)}")
                    stats['warnings'] += 1

        # Remove empty directories (skip in dry-run mode)
        if not self.dry_run:
            self.remove_empty_dirs(local_path)

        return stats

    def remove_empty_dirs(self, path):
        """Recursively remove empty directories."""
        for child in path.iterdir():
            if child.is_dir():
                self.remove_empty_dirs(child)
                try:
                    child.rmdir()  # Only removes if empty
                except OSError:
                    pass  # Directory not empty

    def sync_source(self, source_key, source):
        """Sync all mappings for a source repository."""
        print(f"\n{'='*60}")
        print(f"Syncing: {source['name']}")
        print(f"{'='*60}")

        # Clone repository
        temp_dir = self.clone_repository(source, source_key)
        if not temp_dir:
            return {'synced': 0, 'removed': 0, 'warnings': 1}

        total_stats = {'synced': 0, 'removed': 0, 'warnings': 0}

        try:
            # Process each mapping
            for mapping in source.get('mappings', []):
                print(f"\n  Mapping: {mapping['remote']} -> {mapping['local']}")
                print(f"  Description: {mapping['description']}")

                stats = self.sync_mapping(source, mapping, temp_dir)

                # Accumulate stats
                for key in total_stats:
                    total_stats[key] += stats[key]

                print(f"    Files synced: {stats['synced']}, removed: {stats['removed']}, warnings: {stats['warnings']}")

        finally:
            # Cleanup temporary directory
            if temp_dir.exists():
                shutil.rmtree(temp_dir)

        return total_stats

    def sync_all(self, source_filter=None):
        """Sync all configured sources."""
        print("External Documentation Sync")
        if self.dry_run:
            print("DRY RUN MODE - No changes will be made")
        print(f"Config: {len(self.config['sources'])} sources configured")

        total_stats = {'synced': 0, 'removed': 0, 'warnings': 0}

        for source_key, source in self.config['sources'].items():
            if source_filter and source_key not in source_filter:
                continue

            stats = self.sync_source(source_key, source)

            # Accumulate total stats
            for key in total_stats:
                total_stats[key] += stats[key]

        # Print summary
        print(f"\n{'='*60}")
        if self.dry_run:
            print("DRY RUN SUMMARY")
        else:
            print("SYNC SUMMARY")
        print(f"{'='*60}")

        if self.dry_run:
            print(f"Files that would be synced: {total_stats['synced']}")
            print(f"Files that would be removed: {total_stats['removed']}")
        else:
            print(f"Total files synced: {total_stats['synced']}")
            print(f"Total files removed: {total_stats['removed']}")
        print(f"Total warnings: {total_stats['warnings']}")

        if total_stats['warnings'] > 0:
            print(f"\n⚠️  {total_stats['warnings']} warnings encountered. Review the output above.")
            return 1

        if self.dry_run:
            print("\n✅ Dry run completed successfully! No actual changes were made.")
        else:
            print("\n✅ Sync completed successfully!")
        return 0

    def list_sources(self):
        """List all configured sources."""
        print("Configured External Sources:")
        print(f"{'='*60}")

        for source_key, source in self.config['sources'].items():
            print(f"\n{source_key}:")
            print(f"  Name: {source['name']}")
            print(f"  Repository: {source['repository']}")
            print(f"  Branch: {source['branch']}")
            print(f"  Mappings: {len(source.get('mappings', []))}")

            for mapping in source.get('mappings', []):
                print(f"    {mapping['remote']} -> {mapping['local']}")

def main():
    parser = argparse.ArgumentParser(description='Sync external documentation')
    parser.add_argument('--config', '-c', default='external-sources.yml',
                        help='Configuration file path')
    parser.add_argument('--sources', '-s', nargs='*',
                        help='Specific sources to sync (default: all)')
    parser.add_argument('--list', '-l', action='store_true',
                        help='List configured sources and exit')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help='Show what would be synced without making changes')

    args = parser.parse_args()

    try:
        syncer = ExternalDocSyncer(args.config, dry_run=args.dry_run)

        if args.list:
            syncer.list_sources()
            return 0

        return syncer.sync_all(args.sources)

    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())