You are generating a changelog entry for Waldur version {VERSION} (previous: {PREV_VERSION}, date: {DATE}).

Output ONLY the changelog entry in markdown. Do not include any preamble, explanation, or code fences. The output will be inserted directly into CHANGELOG.md.

## Output format

Start with exactly this header:

```
## {VERSION} - {DATE}
```

Then include these sections in order:

### 1. Highlights

A short paragraph (2-4 sentences) explaining WHY this release matters. Focus on user-visible impact, not implementation details. What can users do now that they couldn't before? What got more reliable?

### 2. What's New / Improvements / Bug Fixes

Group changes by theme, NOT by repository. When a backend change (waldur-mastermind) and a frontend change (waldur-homeport) implement the same feature, describe them together as one item. Use subsections like:

- **What's New** - genuinely new capabilities
- **Improvements** - enhancements to existing features
- **Bug Fixes** - corrections (only if there are meaningful ones)

Each item should be a single bullet point written for an end user or operator. Use plain language. Avoid commit message jargon.

### 3. Core Component Activity

List each core repository with its commit count and compare link. Use this exact format:

```
- **Waldur Mastermind**: [N commits](https://github.com/waldur/waldur-mastermind/compare/{PREV_VERSION}...{VERSION}) - brief summary
- **Waldur Homeport**: [N commits](https://github.com/waldur/waldur-homeport/compare/{PREV_VERSION}...{VERSION}) - brief summary
```

Only include repos that have changes. Skip repos with zero commits.

### 4. Resources

Always end with:

```
### Resources

- [OpenAPI Schema](../API/waldur-openapi-schema-{VERSION}.yaml)
- [API Changes](../integrator-guide/APIs/api-changes/waldur-openapi-schema-{VERSION}-diff.md)
```

End the entry with a `---` separator line.

## Rules

1. **Cross-repo grouping**: If mastermind adds an API endpoint and homeport adds the UI for it, describe them as ONE feature. Look at commit subjects and changed files to find correlations.
2. **Collapse revert pairs**: If a commit was reverted and then re-applied (or a similar fix was applied), mention only the final state.
3. **Exclude noise**: Skip these types of commits entirely:
   - Auto-generated enum syncs or SDK regeneration
   - Documentation regeneration commits
   - Version bump commits (e.g., "Release: bump version to X.Y.Z", "X.Y.Z-dev.N")
   - Merge commits
   - CI/CD pipeline changes (unless they affect users)
4. **No invented information**: Only describe what you can see in the commit data. Do not invent features or speculate about what changes do.
5. **Keep it concise**: Aim for 30-60 lines total. Not every commit needs its own bullet point. Group small related changes.
6. **Use sentence case for bullet points**: Start each bullet with a capital letter, end with a period.
7. **Repo with no meaningful changes**: If a repo only has auto-generated or version bump commits, note it has "maintenance updates only" rather than listing those commits.
