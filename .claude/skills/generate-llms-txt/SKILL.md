---
name: generate-llms-txt
description: Generate llms.txt and llms-full.txt files for LLM-friendly documentation access.
disable-model-invocation: true
---

# LLM Documentation Generation

Generate llms.txt files following the [llmstxt.org](https://llmstxt.org/) standard.

## Files

| File | Purpose | Size |
|------|---------|------|
| `docs/llms.txt` | Curated navigation index (manual) | ~6 KB |
| `docs/llms-full.txt` | Complete documentation (generated) | ~2.2 MB |

## Commands

```bash
# Generate llms-full.txt
python3 scripts/generate-llms-txt.py

# Show statistics only
python3 scripts/generate-llms-txt.py --stats-only

# Skip full file generation
python3 scripts/generate-llms-txt.py --no-full
```

## Updating llms.txt

The `docs/llms.txt` file is manually curated. When adding major new documentation:

1. Edit `docs/llms.txt` directly
2. Add new sections or links following the format:
   ```markdown
   ## Section Name

   - [Link Title](https://docs.waldur.com/path/): Description of content
   ```
3. Keep the "Optional" section for large/auto-generated content

## What's Excluded from llms-full.txt

- `docs/api-reference/**` - 270+ auto-generated API files
- `docs/integrator-guide/APIs/api-changes/**` - 50+ version diff files
- Images, videos, and binary files
- CHANGELOG.md (large release history)

## CI/CD Integration

The llms-full.txt generation runs automatically:
- In merge request tests
- During deployment builds
- Outputs statistics for monitoring

## Documentation

See `docs/about/llms-txt.md` for user-facing documentation about using llms.txt with AI assistants.
