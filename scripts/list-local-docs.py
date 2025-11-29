#!/usr/bin/env python3
"""
List local documentation files that are not imported from external sources.
Identifies purely local content vs. externally synced documentation.
"""

import sys
import yaml
import re
from pathlib import Path
import argparse
import fnmatch

class LocalDocsLister:
    def __init__(self, config_file='external-sources.yml'):
        self.config = self.load_config(config_file)
        self.settings = self.config.get('settings', {})
        self.preserve_local = self.settings.get('preserve_local', [])
        
    def load_config(self, config_file):
        """Load the external sources configuration."""
        try:
            with open(config_file, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            return {'sources': {}}

    def has_external_marker(self, file_path):
        """Check if a file has an external document marker."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(500)  # Just read first 500 chars
                return '<!-- EXTERNAL DOCUMENT' in content
        except (IOError, UnicodeDecodeError):
            return False

    def get_all_external_paths(self):
        """Get all local paths that are managed by external sources."""
        external_paths = set()
        
        for source_key, source in self.config.get('sources', {}).items():
            for mapping in source.get('mappings', []):
                local_path = Path(mapping['local'])
                external_paths.add(local_path)
                
        return external_paths

    def is_under_external_path(self, file_path, external_paths):
        """Check if a file is under any external source path."""
        for external_path in external_paths:
            try:
                file_path.relative_to(external_path)
                return True, external_path
            except ValueError:
                continue
        return False, None

    def is_preserved_local_file(self, file_path, base_path):
        """Check if a file matches preserved local patterns."""
        # Try both relative path from base and just filename
        try:
            rel_path = file_path.relative_to(base_path)
            rel_path_str = str(rel_path)
        except ValueError:
            rel_path_str = file_path.name
            
        for pattern in self.preserve_local:
            if (fnmatch.fnmatch(file_path.name, pattern) or 
                fnmatch.fnmatch(rel_path_str, pattern) or
                rel_path_str == pattern):
                return True
        return False

    def scan_directory(self, docs_path, include_patterns=None, exclude_patterns=None):
        """Scan documentation directory for local files."""
        docs_path = Path(docs_path)
        if not docs_path.exists():
            print(f"Error: Documentation directory {docs_path} does not exist")
            return {'local': [], 'external': [], 'preserved': []}

        external_paths = self.get_all_external_paths()
        
        results = {
            'local': [],
            'external': [],
            'preserved': []
        }

        # Default patterns if none specified
        if include_patterns is None:
            include_patterns = ['*.md']
        if exclude_patterns is None:
            exclude_patterns = ['.*']

        for pattern in include_patterns:
            for file_path in docs_path.rglob(pattern):
                # Skip if matches exclude patterns
                if any(fnmatch.fnmatch(file_path.name, exp) for exp in exclude_patterns):
                    continue
                    
                # Skip directories
                if file_path.is_dir():
                    continue

                # Check if file has external marker
                has_marker = self.has_external_marker(file_path)
                
                # Check if under external path
                under_external, external_path = self.is_under_external_path(file_path, external_paths)
                
                # Check if preserved local file
                is_preserved = self.is_preserved_local_file(file_path, docs_path)

                if has_marker:
                    results['external'].append({
                        'path': file_path,
                        'relative': file_path.relative_to(docs_path),
                        'external_path': external_path,
                        'type': 'external'
                    })
                elif is_preserved:
                    results['preserved'].append({
                        'path': file_path,
                        'relative': file_path.relative_to(docs_path),
                        'external_path': external_path if under_external else None,
                        'type': 'preserved_local'
                    })
                elif under_external:
                    # File is under external path but doesn't have marker
                    # This could be a local file that should be reviewed
                    results['local'].append({
                        'path': file_path,
                        'relative': file_path.relative_to(docs_path),
                        'external_path': external_path,
                        'type': 'potentially_orphaned',
                        'note': f"Under external path {external_path} but no external marker"
                    })
                else:
                    # Purely local file
                    results['local'].append({
                        'path': file_path,
                        'relative': file_path.relative_to(docs_path),
                        'external_path': None,
                        'type': 'local'
                    })

        return results

    def print_results(self, results, output_format='summary', show_paths=True):
        """Print results in the specified format."""
        
        if output_format == 'summary':
            print("Documentation File Analysis")
            print("=" * 60)
            print(f"Total local files: {len(results['local'])}")
            print(f"Total external files: {len(results['external'])}")
            print(f"Total preserved files: {len(results['preserved'])}")
            print()
            
            if results['local']:
                print("LOCAL FILES (not imported from external sources):")
                print("-" * 50)
                for item in sorted(results['local'], key=lambda x: x['relative']):
                    if show_paths:
                        print(f"  {item['relative']}")
                        if item.get('note'):
                            print(f"    Note: {item['note']}")
                    else:
                        print(f"  {item['relative'].name}")
                print()
                
            if results['preserved'] and show_paths:
                print("PRESERVED LOCAL FILES (local files in external directories):")
                print("-" * 58)
                for item in sorted(results['preserved'], key=lambda x: x['relative']):
                    print(f"  {item['relative']}")
                    if item['external_path']:
                        print(f"    (In external path: {item['external_path']})")
                print()

        elif output_format == 'paths':
            # Just print local file paths, one per line
            for item in sorted(results['local'], key=lambda x: x['relative']):
                print(item['relative'])
                
        elif output_format == 'detailed':
            print("DETAILED DOCUMENTATION ANALYSIS")
            print("=" * 60)
            
            print("\n1. LOCAL DOCUMENTATION FILES:")
            print("-" * 40)
            if not results['local']:
                print("  None found")
            else:
                by_type = {}
                for item in results['local']:
                    file_type = item['type']
                    if file_type not in by_type:
                        by_type[file_type] = []
                    by_type[file_type].append(item)
                
                for file_type, items in by_type.items():
                    print(f"\n  {file_type.replace('_', ' ').title()} ({len(items)} files):")
                    for item in sorted(items, key=lambda x: x['relative']):
                        print(f"    {item['relative']}")
                        if item.get('note'):
                            print(f"      → {item['note']}")

            print(f"\n2. EXTERNAL DOCUMENTATION FILES ({len(results['external'])}):")
            print("-" * 45)
            if show_paths:
                external_by_path = {}
                for item in results['external']:
                    ext_path = item['external_path'] or 'Unknown'
                    if ext_path not in external_by_path:
                        external_by_path[ext_path] = []
                    external_by_path[ext_path].append(item)
                
                for ext_path, items in external_by_path.items():
                    print(f"\n  From {ext_path} ({len(items)} files):")
                    for item in sorted(items, key=lambda x: x['relative'])[:5]:  # Show first 5
                        print(f"    {item['relative']}")
                    if len(items) > 5:
                        print(f"    ... and {len(items) - 5} more files")
            else:
                print(f"  {len(results['external'])} files imported from external sources")

            print(f"\n3. PRESERVED LOCAL FILES ({len(results['preserved'])}):")
            print("-" * 42)
            if not results['preserved']:
                print("  None found")
            else:
                for item in sorted(results['preserved'], key=lambda x: x['relative']):
                    print(f"  {item['relative']}")
                    if item['external_path']:
                        print(f"    (Preserved in external path: {item['external_path']})")

        elif output_format == 'stats':
            # Just print statistics
            total = len(results['local']) + len(results['external']) + len(results['preserved'])
            print(f"Local: {len(results['local'])}")
            print(f"External: {len(results['external'])}")
            print(f"Preserved: {len(results['preserved'])}")
            print(f"Total: {total}")
            
            if total > 0:
                local_pct = (len(results['local']) / total) * 100
                external_pct = (len(results['external']) / total) * 100
                print(f"Local %: {local_pct:.1f}%")
                print(f"External %: {external_pct:.1f}%")

def main():
    parser = argparse.ArgumentParser(description='List local documentation files')
    parser.add_argument('--config', '-c', default='external-sources.yml',
                        help='Configuration file path')
    parser.add_argument('--docs-path', '-d', default='docs',
                        help='Documentation directory path')
    parser.add_argument('--format', '-f', choices=['summary', 'detailed', 'paths', 'stats'],
                        default='summary', help='Output format')
    parser.add_argument('--include', '-i', nargs='*', default=['*.md'],
                        help='File patterns to include (default: *.md)')
    parser.add_argument('--exclude', '-e', nargs='*', default=['.*'],
                        help='File patterns to exclude (default: .*)')
    parser.add_argument('--no-paths', action='store_true',
                        help='Hide detailed path information in summary')

    args = parser.parse_args()

    try:
        lister = LocalDocsLister(args.config)
        results = lister.scan_directory(
            args.docs_path, 
            include_patterns=args.include,
            exclude_patterns=args.exclude
        )
        
        lister.print_results(
            results, 
            output_format=args.format, 
            show_paths=not args.no_paths
        )
        
        return 0

    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())