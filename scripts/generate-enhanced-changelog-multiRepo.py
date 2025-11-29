#!/usr/bin/env python3
"""
Enhanced changelog generator for Waldur - analyzes multiple repositories like GitLab CI
"""

import os
import sys
import subprocess
import re
import tempfile
import shutil
from datetime import datetime
from pathlib import Path
import json

class MultiRepoChangelogGenerator:
    def __init__(self):
        self.repositories = {
            'waldur-mastermind': 'https://github.com/waldur/waldur-mastermind.git',
            'waldur-homeport': 'https://github.com/waldur/waldur-homeport.git', 
            'waldur-helm': 'https://github.com/waldur/waldur-helm.git',
            'waldur-docker-compose': 'https://github.com/waldur/waldur-docker-compose.git',
            'waldur-prometheus-exporter': 'https://github.com/waldur/waldur-prometheus-exporter.git',
            'py-client': 'https://github.com/waldur/py-client.git',
            'js-client': 'https://github.com/waldur/js-client.git',
            'go-client': 'https://github.com/waldur/go-client.git'
        }
        # Define which repositories are core (not auto-generated)
        self.core_repositories = {
            'waldur-mastermind', 'waldur-homeport', 'waldur-helm', 
            'waldur-docker-compose', 'waldur-prometheus-exporter'
        }
        # SDK clients are auto-generated from MasterMind OpenAPI schema
        self.generated_repositories = {
            'py-client', 'js-client', 'go-client'
        }
        self.temp_dir = None
        
    def run_command(self, cmd, cwd=None):
        """Run command and return output"""
        try:
            result = subprocess.run(
                cmd, shell=True, cwd=cwd, 
                capture_output=True, text=True, check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {cmd}")
            print(f"Error: {e.stderr}")
            return ""

    def clone_repo(self, repo_name, repo_url, temp_dir):
        """Clone a repository to temp directory"""
        repo_path = temp_dir / repo_name
        if repo_path.exists():
            shutil.rmtree(repo_path)
            
        print(f"Cloning {repo_name}...")
        clone_cmd = f"git clone --depth 100 {repo_url} {repo_path}"
        self.run_command(clone_cmd)
        return repo_path

    def check_tag_exists(self, repo_path, tag):
        """Check if a tag exists in the repository"""
        try:
            result = self.run_command(f"git rev-parse {tag}", cwd=repo_path)
            return bool(result)
        except:
            return False
    
    def find_closest_tag(self, repo_path, target_tag):
        """Find closest available tag if target doesn't exist"""
        try:
            # Get all tags sorted by version
            all_tags = self.run_command("git tag --sort=version:refname", cwd=repo_path)
            if not all_tags:
                return None
                
            tags = [t.strip() for t in all_tags.split('\n') if t.strip()]
            
            # Try to find exact match first
            if target_tag in tags:
                return target_tag
            
            # Find closest tag (prefer earlier version)
            target_parts = target_tag.split('.')
            if len(target_parts) >= 3:
                try:
                    major, minor, patch = map(int, target_parts[:3])
                    
                    # Look for closest earlier version
                    best_match = None
                    best_distance = float('inf')
                    
                    for tag in tags:
                        tag_parts = tag.split('.')
                        if len(tag_parts) >= 3:
                            try:
                                t_major, t_minor, t_patch = map(int, tag_parts[:3])
                                # Calculate distance (prefer earlier versions)
                                version_num = t_major * 10000 + t_minor * 100 + t_patch
                                target_num = major * 10000 + minor * 100 + patch
                                
                                if version_num <= target_num:
                                    distance = abs(target_num - version_num)
                                    if distance < best_distance:
                                        best_distance = distance
                                        best_match = tag
                            except ValueError:
                                continue
                                
                    return best_match
                except ValueError:
                    pass
            
            return None
        except:
            return None

    def get_commits_between_tags(self, repo_path, prev_tag, current_tag):
        """Get commits between two tags with fallback handling"""
        # Handle missing tags
        actual_prev = prev_tag
        actual_current = current_tag
        
        if not self.check_tag_exists(repo_path, current_tag):
            actual_current = self.find_closest_tag(repo_path, current_tag)
            if not actual_current:
                print(f"    Warning: No suitable current tag found for {repo_path.name}")
                return []
                
        if not self.check_tag_exists(repo_path, prev_tag):
            actual_prev = self.find_closest_tag(repo_path, prev_tag)
            if not actual_prev:
                print(f"    Warning: No suitable previous tag found for {repo_path.name}, using commit history")
                # Fallback to recent commit history
                cmd = f"git log --pretty=format:'%h|%s|%an|%ad' --date=short --no-merges -n 10"
                output = self.run_command(cmd, cwd=repo_path)
                commits = []
                for line in output.split('\n'):
                    if line.strip():
                        parts = line.split('|')
                        if len(parts) >= 4:
                            commits.append({
                                'hash': parts[0],
                                'subject': parts[1],
                                'author': parts[2],
                                'date': parts[3]
                            })
                return commits[:5]  # Return recent 5 commits
            
        if actual_prev != prev_tag or actual_current != current_tag:
            print(f"    Using tags {actual_prev}..{actual_current} instead of {prev_tag}..{current_tag} for {repo_path.name}")
            
        cmd = f"git log {actual_prev}..{actual_current} --pretty=format:'%h|%s|%an|%ad' --date=short --no-merges"
        output = self.run_command(cmd, cwd=repo_path)
        
        commits = []
        for line in output.split('\n'):
            if line.strip():
                parts = line.split('|')
                if len(parts) >= 4:
                    commits.append({
                        'hash': parts[0],
                        'subject': parts[1],
                        'author': parts[2],
                        'date': parts[3]
                    })
        return commits

    def analyze_commit_categories(self, commits):
        """Categorize commits by type"""
        categories = {
            'features': [],
            'fixes': [],
            'breaking': [],
            'security': [],
            'refactor': [],
            'docs': [],
            'chore': [],
            'other': []
        }

        patterns = {
            'features': r'^(feat|feature|add|implement)[\s\(:]|new\s+|added?\s+',
            'fixes': r'^(fix|bugfix|resolve|patch)[\s\(:]|fixed?\s+|bug\s+',
            'breaking': r'^(break|BREAKING|break\(|BREAKING\s*CHANGE)|breaking\s+',
            'security': r'^(sec|security)[\s\(:]|security|vulnerability|CVE',
            'refactor': r'^(refactor|perf|optimize)[\s\(:]|refactor|performance',
            'docs': r'^(doc|docs)[\s\(:]|documentation|readme|guide',
            'chore': r'^(chore|build|ci|test)[\s\(:]|update.*version|bump|release'
        }

        for commit in commits:
            subject = commit['subject'].lower()
            categorized = False
            
            for category, pattern in patterns.items():
                if re.search(pattern, subject, re.IGNORECASE):
                    categories[category].append(commit)
                    categorized = True
                    break
            
            if not categorized:
                categories['other'].append(commit)

        return categories

    def should_exclude_file(self, file_path, repo_name):
        """Check if a file should be excluded from statistics (auto-generated files)"""
        exclude_patterns = {
            'waldur-homeport': [
                'template.json',  # Auto-generated template file
                'package-lock.json',  # Auto-generated dependency lock
                'yarn.lock',  # Auto-generated dependency lock
                '*.generated.*',  # Any generated files
                'dist/',  # Build output
                'build/',  # Build output
                'tests/',  # Test files don't represent functional changes
                'test.',  # Test files (prefix pattern)
                '.spec.',  # Spec files (test pattern)
                '__tests__/',  # Jest test directory
                '*.test.',  # Test files with .test. pattern
                '*.spec.',  # Spec files with .spec. pattern
            ],
            'waldur-mastermind': [
                'package-lock.json',
                'poetry.lock',  # Auto-generated dependency lock
                'migrations/',  # Database migration files (often auto-generated)
                '*.pyc',  # Compiled Python files
                '__pycache__/',  # Python cache
                'tests/',  # Test files don't represent functional changes
                'test_',  # Test files (prefix pattern)
                '/tests/',  # Test directories anywhere in path
                'docs/admin/configuration-guide.md',  # Auto-generated from print_settings
                'docs/admin/features.md',  # Auto-generated from print_features_docs
                'docs/admin/notifications.md',  # Auto-generated from print_notifications
                'docs/admin/cli-guide.md',  # Auto-generated from print_commands
                'docs/events.md',  # Auto-generated from print_events
                'docs/admin/templates.md',  # Auto-generated from print_templates
                'docs/admin/scheduled.md',  # Auto-generated from print_scheduled_jobs
                'docs/mixins.md',  # Auto-generated from print_mixins
                'docs/handlers.md',  # Auto-generated from print_registered_handlers
                'docs/core_structure.mmd',  # Auto-generated Mermaid diagram
                'docs/core_permissions.mmd',  # Auto-generated Mermaid diagram
                'docs/marketplace_category.mmd',  # Auto-generated Mermaid diagram
                'docs/marketplace_catalog.mmd',  # Auto-generated Mermaid diagram
                'docs/marketplace_provision.mmd',  # Auto-generated Mermaid diagram
            ],
            'py-client': [
                'waldur_client/',  # Auto-generated from OpenAPI
                'docs/',  # Auto-generated docs
                'dist/',  # Build artifacts
            ],
            'js-client': [
                'lib/',  # Auto-generated from OpenAPI  
                'docs/',  # Auto-generated docs
                'dist/',  # Build artifacts
                'package-lock.json',
            ],
            'go-client': [
                'waldur/',  # Auto-generated from OpenAPI
                'docs/',  # Auto-generated docs
            ]
        }
        
        patterns = exclude_patterns.get(repo_name, [])
        file_name = file_path.split('/')[-1]  # Get just filename
        
        for pattern in patterns:
            if pattern.endswith('/'):
                # Directory pattern
                if pattern[:-1] in file_path:
                    return True
            elif '*' in pattern:
                # Wildcard pattern (simple)
                if pattern.replace('*', '') in file_name:
                    return True
            else:
                # Exact match
                if pattern == file_name or pattern in file_path:
                    return True
        
        return False

    def get_file_changes(self, repo_path, prev_tag, current_tag):
        """Get file change statistics excluding auto-generated files"""
        if not self.check_tag_exists(repo_path, prev_tag) or not self.check_tag_exists(repo_path, current_tag):
            return {}
            
        repo_name = repo_path.name
        
        # Get changed files
        files_cmd = f"git diff --name-only {prev_tag}..{current_tag}"
        all_changed_files = self.run_command(files_cmd, cwd=repo_path).split('\n')
        all_changed_files = [f for f in all_changed_files if f.strip()]
        
        # Filter out auto-generated files
        changed_files = [f for f in all_changed_files if not self.should_exclude_file(f, repo_name)]

        # Get line changes excluding auto-generated files
        numstat_cmd = f"git diff --numstat {prev_tag}..{current_tag}"
        numstat = self.run_command(numstat_cmd, cwd=repo_path)
        
        added_lines = 0
        removed_lines = 0
        excluded_files_count = 0
        
        for line in numstat.split('\n'):
            if line.strip():
                parts = line.split('\t')
                if len(parts) >= 3:
                    try:
                        file_path = parts[2]
                        if self.should_exclude_file(file_path, repo_name):
                            excluded_files_count += 1
                            continue
                            
                        added_lines += int(parts[0]) if parts[0] != '-' else 0
                        removed_lines += int(parts[1]) if parts[1] != '-' else 0
                    except ValueError:
                        pass

        return {
            'files_changed': len(changed_files),
            'lines_added': added_lines,
            'lines_removed': removed_lines,
            'changed_files': changed_files[:10],
            'excluded_files': excluded_files_count,
            'total_files_changed': len(all_changed_files)
        }

    def analyze_repository(self, repo_name, repo_path, prev_tag, current_tag):
        """Analyze a single repository between two tags"""
        print(f"Analyzing {repo_name} ({prev_tag}..{current_tag})")
        
        commits = self.get_commits_between_tags(repo_path, prev_tag, current_tag)
        categories = self.analyze_commit_categories(commits)
        file_changes = self.get_file_changes(repo_path, prev_tag, current_tag)
        
        return {
            'repo_name': repo_name,
            'commit_count': len(commits),
            'commits': commits,
            'categories': categories,
            'file_changes': file_changes,
            'has_changes': len(commits) > 0
        }

    def generate_enhanced_changelog(self, current_tag, prev_tag):
        """Generate enhanced changelog by analyzing all repositories"""
        
        # Create temp directory
        self.temp_dir = Path(tempfile.mkdtemp(prefix="waldur_changelog_"))
        print(f"Using temporary directory: {self.temp_dir}")
        
        try:
            all_analyses = {}
            # Separate stats for core vs generated repositories
            core_commits = 0
            core_files = 0
            core_added = 0
            core_removed = 0
            
            # Analyze each repository
            for repo_name, repo_url in self.repositories.items():
                repo_path = self.clone_repo(repo_name, repo_url, self.temp_dir)
                analysis = self.analyze_repository(repo_name, repo_path, prev_tag, current_tag)
                all_analyses[repo_name] = analysis
                
                # Only count core repositories in main statistics
                if analysis['has_changes'] and repo_name in self.core_repositories:
                    core_commits += analysis['commit_count']
                    core_files += analysis['file_changes'].get('files_changed', 0)
                    core_added += analysis['file_changes'].get('lines_added', 0)
                    core_removed += analysis['file_changes'].get('lines_removed', 0)

            # Generate changelog entry
            changelog_parts = []
            
            # Header
            date_str = datetime.now().strftime('%Y-%m-%d')
            changelog_parts.append(f"## {current_tag} - {date_str}")
            changelog_parts.append("")
            
            # Release summary in proper list format
            active_core_repos = len([a for repo, a in all_analyses.items() if a['has_changes'] and repo in self.core_repositories])
            active_sdk_repos = len([a for repo, a in all_analyses.items() if a['has_changes'] and repo in self.generated_repositories])
            
            if core_commits > 0:
                changelog_parts.append("### Release Summary")
                changelog_parts.append("")
                changelog_parts.append(f"- **Release Impact:** {core_commits} commits across {active_core_repos} core repositories")
                if core_files > 0:
                    changelog_parts.append(f"- **Functional Changes:** {core_files} files changed with +{core_added}/-{core_removed} lines")
                if active_sdk_repos > 0:
                    changelog_parts.append(f"- **SDK Updates:** {active_sdk_repos} auto-generated clients updated from OpenAPI schema")
                changelog_parts.append("")
                changelog_parts.append("!!! note \"Statistics Note\"")
                changelog_parts.append("    Excludes tests, auto-generated files, and SDK client code for accurate development metrics.")
                changelog_parts.append("")
            else:
                changelog_parts.append("### Release Summary")
                changelog_parts.append("")
                changelog_parts.append("- **Release Impact:** Minor release with configuration and documentation updates")
                if active_sdk_repos > 0:
                    changelog_parts.append(f"- **SDK Updates:** {active_sdk_repos} auto-generated clients updated")
                changelog_parts.append("")

            # Component status - separate core from generated with improved formatting
            changelog_parts.append("### Core Component Activity")
            changelog_parts.append("")
            for repo_name, analysis in all_analyses.items():
                if repo_name in self.core_repositories:
                    display_name = repo_name.replace('-', ' ').title()
                    if analysis['has_changes']:
                        commit_count = analysis['commit_count']
                        files_count = analysis['file_changes'].get('files_changed', 0)
                        lines_added = analysis['file_changes'].get('lines_added', 0)
                        lines_removed = analysis['file_changes'].get('lines_removed', 0)
                        
                        component_info = f"- **{display_name}**: [{commit_count} commits](https://github.com/waldur/{repo_name}/compare/{prev_tag}...{current_tag})"
                        if files_count > 0:
                            component_info += f" · {files_count} files changed"
                            if lines_added > 0 or lines_removed > 0:
                                component_info += f" (+{lines_added}/-{lines_removed} lines)"
                        
                        changelog_parts.append(component_info)
                    else:
                        changelog_parts.append(f"- **{display_name}**: No changes")
            
            # Show SDK status separately if any were updated
            sdk_updates = [repo for repo, analysis in all_analyses.items() 
                          if repo in self.generated_repositories and analysis['has_changes']]
            if sdk_updates:
                changelog_parts.append("")
                changelog_parts.append("### SDK Updates (Auto-generated)")
                changelog_parts.append("")
                for repo_name in sdk_updates:
                    analysis = all_analyses[repo_name]
                    display_name = repo_name.replace('-', ' ').title().replace('Py ', 'Python ').replace('Js ', 'JavaScript ')
                    commit_count = analysis['commit_count']
                    
                    changelog_parts.append(f"- **{display_name}**: [{commit_count} commits](https://github.com/waldur/{repo_name}/compare/{prev_tag}...{current_tag})")
            
            changelog_parts.append("")

            # Notable changes from core repos (all commits, no categorization)
            all_notable_changes = []
            for repo_name, analysis in all_analyses.items():
                if repo_name in self.core_repositories and analysis['has_changes']:
                    # Get all commits, not just categorized ones
                    for commit in analysis['commits']:
                        all_notable_changes.append((commit, repo_name))
            
            if all_notable_changes:
                changelog_parts.append("### Notable Changes")
                changelog_parts.append("")
                # Sort by date and limit to most recent/important ones
                sorted_changes = sorted(all_notable_changes, key=lambda x: x[0]['date'])[-6:]  # Latest 6 for better readability
                
                for change, repo_name in sorted_changes:
                    clean_subject = self._clean_commit_subject(change['subject'], 'general')
                    commit_hash = change['hash']
                    display_repo = repo_name.replace('-', ' ').title()
                    
                    # Use proper markdown list format
                    changelog_parts.append(f"- **{clean_subject}** ([{commit_hash}](https://github.com/waldur/{repo_name}/commit/{commit_hash}) - {display_repo})")
                
                changelog_parts.append("")

            # Repository-specific highlights
            for repo_name, analysis in all_analyses.items():
                if analysis['has_changes'] and analysis['commit_count'] > 5:  # Only show repos with significant changes
                    changelog_parts.append(f"**{repo_name.replace('-', ' ').title()} Highlights:**")
                    top_commits = analysis['commits'][:3]  # Top 3 commits
                    for commit in top_commits:
                        clean_subject = self._clean_commit_subject(commit['subject'], 'general')
                        changelog_parts.append(f"- {clean_subject}")
                    changelog_parts.append("")

            # Resources
            changelog_parts.append("### Resources")
            changelog_parts.append("")
            changelog_parts.append(f"- [OpenAPI Schema](../API/waldur-openapi-schema-{current_tag}.yaml)")
            changelog_parts.append(f"- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-{current_tag}-diff.md)")
            changelog_parts.append("")
            changelog_parts.append("---")

            return '\n'.join(changelog_parts), all_analyses
            
        finally:
            # Cleanup
            if self.temp_dir and self.temp_dir.exists():
                print(f"Cleaning up {self.temp_dir}")
                shutil.rmtree(self.temp_dir)
    
    def _clean_commit_subject(self, subject, category):
        """Clean commit subjects for better readability with proper capitalization"""
        patterns = {
            'features': r'^(feat|feature|add|implement|new)(\([^)]*\))?[\s:]?\s*',
            'fixes': r'^(fix|bugfix|resolve|patch)(\([^)]*\))?[\s:]?\s*',
            'refactor': r'^(refactor|perf|optimize|improve)(\([^)]*\))?[\s:]?\s*',
            'general': r'^(chore|build|ci|test|docs)(\([^)]*\))?[\s:]?\s*'
        }
        
        # Remove category prefixes
        pattern = patterns.get(category, '')
        if pattern:
            subject = re.sub(pattern, '', subject, flags=re.IGNORECASE).strip()
        
        # Clean up common prefixes and brackets
        subject = re.sub(r'^\[.*?\]\s*', '', subject)  # Remove [TAG] prefixes
        subject = re.sub(r'^\w+-\d+\s*:\s*', '', subject)  # Remove ISSUE-123: prefixes  
        subject = re.sub(r'^\w+-\d+\s+', '', subject)  # Remove ISSUE-123 prefixes
        subject = re.sub(r'^\(.*?\)\s*', '', subject)  # Remove (scope) prefixes
        
        # Clean up and capitalize properly
        subject = subject.strip()
        
        # Handle special cases for proper sentence formatting
        if subject:
            # Capitalize first letter
            subject = subject[0].upper() + subject[1:] if len(subject) > 1 else subject.upper()
            
            # Ensure sentence ends with period if it doesn't already end with punctuation
            if not re.search(r'[.!?]$', subject):
                subject += '.'
        
        return subject

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <current_tag> <previous_tag>")
        print("Example: python script.py 7.9.0 7.8.9")
        sys.exit(1)
        
    current_tag = sys.argv[1]
    prev_tag = sys.argv[2]
    
    print(f"Generating enhanced changelog for {current_tag} (since {prev_tag})")
    print("This will clone multiple repositories - please wait...")
    
    generator = MultiRepoChangelogGenerator()
    
    try:
        enhanced_changelog, analyses = generator.generate_enhanced_changelog(current_tag, prev_tag)
        
        print("=" * 80)
        print("ENHANCED MULTI-REPOSITORY CHANGELOG OUTPUT:")
        print("=" * 80)
        print(enhanced_changelog)
        print("=" * 80)
        
        # Summary statistics
        active_repos = sum(1 for a in analyses.values() if a['has_changes'])
        total_commits = sum(a['commit_count'] for a in analyses.values())
        
        print(f"\nSUMMARY:")
        print(f"Active repositories: {active_repos}/{len(analyses)}")
        print(f"Total commits analyzed: {total_commits}")
        print(f"Changelog length: {len(enhanced_changelog.split(chr(10)))} lines")
        
        # Show repository breakdown
        print(f"\nREPOSITORY BREAKDOWN:")
        for repo_name, analysis in analyses.items():
            status = f"{analysis['commit_count']} commits" if analysis['has_changes'] else "No changes"
            print(f"  {repo_name}: {status}")
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()