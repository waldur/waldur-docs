#!/usr/bin/env python3
"""
Regenerate a single changelog entry or update multiple entries
Usage: python3 regenerate-changelog-entry.py 7.9.0 7.8.9
       python3 regenerate-changelog-entry.py --update-recent 5
"""

import sys
import re
import subprocess
import argparse
from pathlib import Path

def get_enhanced_entry(version, prev_version):
    """Generate enhanced changelog entry for a single version"""
    try:
        print(f"Generating enhanced entry for {version} (since {prev_version})")
        result = subprocess.run([
            'python3', 'scripts/generate-enhanced-changelog-multiRepo.py', 
            version, prev_version
        ], capture_output=True, text=True, timeout=300)
        
        output = result.stdout
        
        # Extract just the changelog entry (between ## and ---)
        lines = output.split('\n')
        start_idx = -1
        end_idx = -1
        
        for i, line in enumerate(lines):
            if line.startswith('## ') and version in line:
                start_idx = i
            elif start_idx != -1 and line.strip() == '---':
                end_idx = i
                break
        
        if start_idx != -1 and end_idx != -1:
            entry = '\n'.join(lines[start_idx:end_idx+1])
            # Clean up any remaining debug info
            entry_lines = entry.split('\n')
            cleaned_lines = []
            for line in entry_lines:
                if not any(skip in line for skip in [
                    'Warning:', 'Using tags', 'Analyzing', 'Cloning', 'Command failed'
                ]):
                    cleaned_lines.append(line)
            return '\n'.join(cleaned_lines)
        
        print(f"Warning: Could not extract changelog entry for {version}")
        return None
        
    except subprocess.TimeoutExpired:
        print(f"Timeout generating entry for {version}")
        return None
    except Exception as e:
        print(f"Error generating entry for {version}: {e}")
        return None

def get_current_versions():
    """Get list of versions from current changelog"""
    changelog_path = Path('docs/about/CHANGELOG.md')
    if not changelog_path.exists():
        return []
    
    with open(changelog_path, 'r') as f:
        content = f.read()
    
    # Find all version headers
    version_matches = re.findall(r'^## ([0-9]+\.[0-9]+\.[0-9]+)', content, re.MULTILINE)
    return version_matches

def get_previous_version(current_version, all_versions):
    """Get the previous version from the list"""
    try:
        current_idx = all_versions.index(current_version)
        if current_idx + 1 < len(all_versions):
            return all_versions[current_idx + 1]
        else:
            # Generate a reasonable previous version
            parts = current_version.split('.')
            if len(parts) == 3:
                major, minor, patch = map(int, parts)
                if patch > 0:
                    return f"{major}.{minor}.{patch - 1}"
                elif minor > 0:
                    return f"{major}.{minor - 1}.9"
                else:
                    return f"{major - 1}.9.9"
    except ValueError:
        pass
    
    return f"{current_version}.prev"

def replace_changelog_entry(content, version, new_entry):
    """Replace a specific version entry in changelog content"""
    # Pattern to match from ## version to the next ## or end of file
    pattern = rf'## {re.escape(version)}.*?(?=## [0-9]+\.[0-9]+\.[0-9]+|## Archived|$)'
    
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, new_entry + '\n\n', content, flags=re.DOTALL)
        return new_content.rstrip() + '\n'
    else:
        print(f"Warning: Could not find entry for {version} to replace")
        return content

def update_single_entry(version, prev_version=None):
    """Update a single changelog entry"""
    changelog_path = Path('docs/about/CHANGELOG.md')
    
    if not changelog_path.exists():
        print("Error: CHANGELOG.md not found")
        return False
    
    # Determine previous version if not provided
    if not prev_version:
        all_versions = get_current_versions()
        prev_version = get_previous_version(version, all_versions)
    
    print(f"Updating changelog entry for {version} (since {prev_version})")
    
    # Generate enhanced entry
    enhanced_entry = get_enhanced_entry(version, prev_version)
    if not enhanced_entry:
        print(f"Failed to generate enhanced entry for {version}")
        return False
    
    # Read current changelog
    with open(changelog_path, 'r') as f:
        content = f.read()
    
    # Replace the entry
    new_content = replace_changelog_entry(content, version, enhanced_entry)
    
    # Write back
    with open(changelog_path, 'w') as f:
        f.write(new_content)
    
    print(f"Successfully updated changelog entry for {version}")
    return True

def update_recent_entries(count):
    """Update the most recent N entries"""
    all_versions = get_current_versions()
    
    if len(all_versions) < count:
        count = len(all_versions)
        
    print(f"Updating {count} most recent changelog entries")
    
    success_count = 0
    for i in range(count):
        version = all_versions[i]
        prev_version = get_previous_version(version, all_versions)
        
        if update_single_entry(version, prev_version):
            success_count += 1
        else:
            print(f"Skipping {version} due to errors")
    
    print(f"Successfully updated {success_count}/{count} entries")

def main():
    parser = argparse.ArgumentParser(description='Regenerate changelog entries with enhanced format')
    parser.add_argument('version', nargs='?', help='Version to regenerate (e.g., 7.9.0)')
    parser.add_argument('prev_version', nargs='?', help='Previous version (e.g., 7.8.9)')
    parser.add_argument('--update-recent', type=int, metavar='N', 
                       help='Update N most recent entries')
    parser.add_argument('--list-versions', action='store_true',
                       help='List all versions in current changelog')
    
    args = parser.parse_args()
    
    # Change to repo root
    script_dir = Path(__file__).parent
    import os
    os.chdir(script_dir.parent)
    
    if args.list_versions:
        versions = get_current_versions()
        print("Versions in current changelog:")
        for version in versions:
            print(f"  {version}")
        return
    
    if args.update_recent:
        update_recent_entries(args.update_recent)
    elif args.version:
        if not args.prev_version:
            all_versions = get_current_versions()
            args.prev_version = get_previous_version(args.version, all_versions)
            print(f"Auto-detected previous version: {args.prev_version}")
        
        success = update_single_entry(args.version, args.prev_version)
        sys.exit(0 if success else 1)
    else:
        parser.print_help()
        print("\nExamples:")
        print("  python3 regenerate-changelog-entry.py 7.9.0 7.8.9")
        print("  python3 regenerate-changelog-entry.py 7.9.0  # auto-detect previous version")
        print("  python3 regenerate-changelog-entry.py --update-recent 3")
        print("  python3 regenerate-changelog-entry.py --list-versions")

if __name__ == '__main__':
    main()