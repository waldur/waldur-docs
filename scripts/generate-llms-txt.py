#!/usr/bin/env python3
"""
Generate llms.txt and llms-full.txt files for LLM-friendly documentation access.

llms.txt: Curated index of documentation with descriptions (smaller, prioritized)
llms-full.txt: Comprehensive documentation content in a single file (larger, complete)

See: https://llmstxt.org/ for specification details.
"""

import argparse
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

# Site configuration
SITE_URL = "https://docs.waldur.com/latest"
SITE_NAME = "Waldur Documentation"
SITE_DESCRIPTION = """Waldur is an open-source hybrid cloud platform for managing multi-cloud environments.
It provides a unified interface for resource orchestration, service catalog management,
and self-service portal functionality. Main components: MasterMind (backend API/orchestrator)
and HomePort (web UI). Licensed under MIT."""

# Priority order for llms-full.txt content generation
# Files are included in this order; sections not listed are included at the end
PRIORITY_SECTIONS = [
    # Getting started - highest priority
    ("docs/index.md", "Introduction"),
    ("docs/about/getting-started.md", "Getting Started"),
    ("docs/about/terminology", "Terminology"),

    # Architecture and deployment
    ("docs/admin-guide/architecture.md", "Architecture"),
    ("docs/admin-guide/hardware-requirements.md", "Hardware Requirements"),
    ("docs/admin-guide/deployment/helm", "Helm Deployment"),
    ("docs/admin-guide/deployment/docker-compose", "Docker Compose Deployment"),
    ("docs/admin-guide/checklist-for-production.md", "Production Checklist"),

    # Configuration
    ("docs/admin-guide/mastermind-configuration", "MasterMind Configuration"),
    ("docs/admin-guide/waldur-roles.md", "Roles"),
    ("docs/admin-guide/billing-and-accounting.md", "Billing"),

    # Identity providers
    ("docs/admin-guide/identities", "Identity Providers"),

    # Cloud providers
    ("docs/admin-guide/providers", "Cloud Providers"),

    # API Integration - high priority for integrators
    ("docs/integrator-guide/APIs/authentication.md", "API Authentication"),
    ("docs/integrator-guide/APIs/permissions.md", "API Permissions"),
    ("docs/integrator-guide/APIs/api.md", "API Overview"),
    ("docs/integrator-guide/api-lifecycle.md", "API Versioning and Change Policy"),
    ("docs/integrator-guide/sdk.md", "Python SDK"),
    ("docs/integrator-guide/APIs/project-api-examples.md", "API Examples"),

    # Developer guide
    ("docs/developer-guide/core-concepts", "Core Concepts"),
    ("docs/developer-guide/guides", "Development Guides"),
    ("docs/developer-guide/ui", "UI Development"),

    # User guide
    ("docs/user-guide", "User Guide"),

    # Integrations
    ("docs/integrations", "Integrations"),

    # About section
    ("docs/about", "About"),
]

# Patterns to exclude from llms-full.txt (too large or auto-generated)
EXCLUDE_PATTERNS = [
    "docs/api-reference/**",                    # Auto-generated API docs (270+ files)
    "**/img/**",                                # Image directories
    "**/*.png",                                 # Images
    "**/*.jpg",                                 # Images
    "**/*.jpeg",                                # Images
    "**/*.gif",                                 # Images
    "**/*.svg",                                 # SVG files
    "**/*.mp4",                                 # Videos
    "**/*.webm",                                # Videos
    "**/.pages",                                # Navigation config
    "**/CHANGELOG.md",                          # Large changelog
]

# Files that should always be included even if in excluded directories
FORCE_INCLUDE = [
    "docs/api-reference/index.md",  # Just the index, not all endpoints
]


class LLMSTxtGenerator:
    def __init__(self, docs_path: str = "docs", output_path: str = "docs"):
        self.docs_path = Path(docs_path)
        self.output_path = Path(output_path)
        self.processed_files = set()

    def should_exclude(self, file_path: Path) -> bool:
        """Check if a file should be excluded based on patterns."""
        file_str = str(file_path)

        # Check force include first
        for pattern in FORCE_INCLUDE:
            if file_path.match(pattern) or file_str.endswith(pattern.replace("docs/", "")):
                return False

        # Check exclude patterns
        for pattern in EXCLUDE_PATTERNS:
            if file_path.match(pattern):
                return True
            # Also check string matching for glob patterns
            pattern_regex = pattern.replace("**", ".*").replace("*", "[^/]*")
            if re.match(pattern_regex, file_str):
                return True

        return False

    def clean_content(self, content: str) -> str:
        """Clean markdown content for LLM consumption."""
        # Remove HTML comments
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

        # Remove YAML front matter
        content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

        # Remove image references (keep alt text as description)
        content = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'[Image: \1]', content)

        # Remove video embeds
        content = re.sub(r'<video[^>]*>.*?</video>', '[Video content]', content, flags=re.DOTALL)

        # Remove external document markers
        content = re.sub(r'<!-- EXTERNAL DOCUMENT.*?-->', '', content, flags=re.DOTALL)

        # Normalize multiple blank lines to single
        content = re.sub(r'\n{3,}', '\n\n', content)

        return content.strip()

    def get_file_title(self, file_path: Path, content: str) -> str:
        """Extract title from markdown file."""
        # Try to find H1 header
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()

        # Fall back to filename
        return file_path.stem.replace('-', ' ').replace('_', ' ').title()

    def read_markdown_file(self, file_path: Path) -> Optional[str]:
        """Read and clean a markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except (IOError, UnicodeDecodeError) as e:
            print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)
            return None

    def collect_files_in_order(self) -> list[tuple[Path, str]]:
        """Collect markdown files in priority order."""
        collected = []

        # First, process priority sections in order
        for path_pattern, section_name in PRIORITY_SECTIONS:
            pattern_path = self.docs_path.parent / path_pattern

            if pattern_path.is_file() and pattern_path.suffix == '.md':
                if not self.should_exclude(pattern_path) and pattern_path not in self.processed_files:
                    collected.append((pattern_path, section_name))
                    self.processed_files.add(pattern_path)
            elif pattern_path.is_dir():
                # Collect all markdown files in directory
                for md_file in sorted(pattern_path.rglob('*.md')):
                    if not self.should_exclude(md_file) and md_file not in self.processed_files:
                        collected.append((md_file, section_name))
                        self.processed_files.add(md_file)

        # Then, collect any remaining files not yet processed
        for md_file in sorted(self.docs_path.rglob('*.md')):
            if not self.should_exclude(md_file) and md_file not in self.processed_files:
                collected.append((md_file, "Additional Documentation"))
                self.processed_files.add(md_file)

        return collected

    def generate_llms_full_txt(self) -> str:
        """Generate comprehensive llms-full.txt content."""
        lines = [
            f"# {SITE_NAME}",
            "",
            f"> {SITE_DESCRIPTION.replace(chr(10), ' ')}",
            "",
            f"Generated: {datetime.utcnow().isoformat()}Z",
            f"Source: {SITE_URL}",
            "",
            "---",
            "",
        ]

        files = self.collect_files_in_order()
        current_section = None

        for file_path, section_name in files:
            content = self.read_markdown_file(file_path)
            if content is None:
                continue

            # Add section header if changed
            if section_name != current_section:
                current_section = section_name
                lines.append(f"\n## {section_name}\n")

            # Clean and add content
            cleaned = self.clean_content(content)
            if cleaned:
                # Get relative path for reference
                try:
                    rel_path = file_path.relative_to(self.docs_path.parent)
                except ValueError:
                    rel_path = file_path.name

                title = self.get_file_title(file_path, content)

                lines.append(f"### {title}")
                lines.append(f"<!-- Source: {rel_path} -->")
                lines.append("")
                lines.append(cleaned)
                lines.append("")
                lines.append("---")
                lines.append("")

        return '\n'.join(lines)

    def generate(self, full_txt: bool = True):
        """Generate llms.txt files."""
        # llms.txt is manually curated, just verify it exists
        llms_txt_path = self.output_path / "llms.txt"
        if llms_txt_path.exists():
            print(f"✓ llms.txt exists at {llms_txt_path}")
        else:
            print(f"⚠ llms.txt not found at {llms_txt_path}")
            print("  Please create it manually or copy from the template.")

        # Generate llms-full.txt
        if full_txt:
            print("Generating llms-full.txt...")
            self.processed_files.clear()
            content = self.generate_llms_full_txt()

            output_file = self.output_path / "llms-full.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(content)

            # Calculate stats
            file_count = len(self.processed_files)
            line_count = content.count('\n')
            word_count = len(content.split())
            char_count = len(content)

            # Rough token estimate (1 token ≈ 4 characters for English)
            token_estimate = char_count // 4

            print(f"✓ Generated {output_file}")
            print(f"  Files processed: {file_count}")
            print(f"  Lines: {line_count:,}")
            print(f"  Words: {word_count:,}")
            print(f"  Characters: {char_count:,}")
            print(f"  Estimated tokens: ~{token_estimate:,}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate llms.txt and llms-full.txt for LLM documentation access"
    )
    parser.add_argument(
        '--docs-path',
        default='docs',
        help='Path to documentation directory (default: docs)'
    )
    parser.add_argument(
        '--output-path',
        default='docs',
        help='Path for output files (default: docs)'
    )
    parser.add_argument(
        '--no-full',
        action='store_true',
        help='Skip generating llms-full.txt'
    )
    parser.add_argument(
        '--stats-only',
        action='store_true',
        help='Only show statistics, do not generate files'
    )

    args = parser.parse_args()

    generator = LLMSTxtGenerator(
        docs_path=args.docs_path,
        output_path=args.output_path
    )

    if args.stats_only:
        print("Analyzing documentation structure...")
        files = generator.collect_files_in_order()
        print(f"Total files to include: {len(files)}")

        # Count by section
        sections = {}
        for _, section in files:
            sections[section] = sections.get(section, 0) + 1

        print("\nFiles by section:")
        for section, count in sections.items():
            print(f"  {section}: {count}")
    else:
        generator.generate(full_txt=not args.no_full)


if __name__ == '__main__':
    main()
