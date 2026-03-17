# LLM-Friendly Documentation (llms.txt)

Waldur documentation supports the [llms.txt standard](https://llmstxt.org/) to provide optimized access for Large Language Models (LLMs) and AI assistants.

## What is llms.txt?

The llms.txt standard provides a structured way for AI systems to understand and navigate documentation. Instead of crawling HTML pages, LLMs can access a curated, text-only version of the documentation that's optimized for their context windows.

## Available Files

### /llms.txt

A curated index of Waldur documentation with descriptions for each section. This file helps AI agents understand the documentation structure and decide which resources to fetch.

**URL:** [https://docs.waldur.com/latest/llms.txt](https://docs.waldur.com/latest/llms.txt)

**Use case:** Quick navigation, understanding documentation structure, deciding which pages to read.

### /llms-full.txt

A comprehensive file containing all documentation content in a single text file. This enables loading the complete documentation context in one request.

**URL:** [https://docs.waldur.com/latest/llms-full.txt](https://docs.waldur.com/latest/llms-full.txt)

**Use case:** Loading complete documentation into AI context, comprehensive searches, full-context assistance.

## Using with AI Assistants

### Claude (Anthropic)

You can reference the llms.txt files directly in conversations:

```
Please read https://docs.waldur.com/latest/llms.txt and help me understand
how to deploy Waldur using Helm.
```

### ChatGPT / GPT-4

With web browsing enabled, GPT can fetch and use the llms.txt files:

```
Fetch https://docs.waldur.com/latest/llms-full.txt and explain how to
configure Keycloak authentication in Waldur.
```

### IDE Integrations (Cursor, Windsurf)

Many AI-powered IDEs support llms.txt natively. Add the Waldur documentation URL to your project's AI context settings.

### MCP (Model Context Protocol)

The [Waldur MCP Server](../integrations/waldur-mcp-server/README.md) provides direct API access that complements the llms.txt files for interactive AI assistance.

## Content Structure

The llms.txt file organizes documentation by topic:

| Section | Description |
|---------|-------------|
| Getting Started | Introduction, quick start, terminology |
| Deployment | Architecture, Helm, Docker Compose |
| Configuration | MasterMind settings, features, billing |
| Identity Providers | Keycloak, LDAP, SAML integration |
| Cloud Providers | OpenStack, Azure, SLURM setup |
| API Integration | Authentication, permissions, SDK |
| Developer Guide | Core concepts, development guides |
| User Guide | End-user documentation |
| Optional | API reference, changelogs (large files) |

## Generation

The llms.txt files are generated using a script that:

1. Reads the curated `docs/llms.txt` index file
2. Generates `llms-full.txt` by concatenating documentation in priority order
3. Cleans content by removing images, videos, and HTML comments
4. Excludes auto-generated API reference files to keep size manageable

### Running Locally

```bash
# Generate llms-full.txt
python scripts/generate-llms-txt.py

# Show statistics only
python scripts/generate-llms-txt.py --stats-only

# Skip llms-full.txt generation
python scripts/generate-llms-txt.py --no-full
```

### Updating llms.txt

The `docs/llms.txt` file is manually curated. When adding significant new documentation:

1. Edit `docs/llms.txt` directly
2. Add new sections or links following the existing format
3. Use descriptive text after the colon for each link
4. Keep the "Optional" section for large or auto-generated content

### File Format

The llms.txt format follows the specification at [llmstxt.org](https://llmstxt.org/):

```markdown
# Project Name

> Brief project description in a blockquote.

## Section Name

- [Link Title](URL): Description of the content
- [Another Link](URL): What this page covers

## Optional

- [Large Reference](URL): Content that can be skipped for shorter contexts
```

## Excluded Content

The following are excluded from `llms-full.txt` to keep the file size reasonable:

- **API Reference** (`/api-reference/`): 270+ auto-generated endpoint files
- **API Changelogs** (`/integrator-guide/APIs/api-changes/`): 50+ version diff files
- **Images and videos**: Binary content not useful for LLMs
- **CHANGELOG.md**: Large file with detailed release history

These resources remain accessible via direct URL or the API reference links in `llms.txt`.

## Token Estimates

| File | Approximate Size | Estimated Tokens |
|------|------------------|------------------|
| llms.txt | ~6 KB | ~1,500 |
| llms-full.txt | ~2.2 MB | ~560,000 |

Token counts vary based on documentation updates. The llms-full.txt file is large and may exceed some LLM context windows. For models with limited context, use the curated llms.txt to identify specific sections to fetch.

## Further Reading

- [llms.txt Specification](https://llmstxt.org/)
- [Waldur MCP Server](../integrations/waldur-mcp-server/README.md) - Model Context Protocol integration
- [API Documentation](../integrator-guide/APIs/api.md) - REST API reference
