#!/usr/bin/env python3
import os
import re
import sys
import subprocess
import argparse
import datetime
from pathlib import Path

# Paths relative to repository root
CHANGELOG_PATH = Path("docs/about/CHANGELOG.md")
PUBLICCODE_PATH = Path("publiccode.yml")


def run_cmd(cmd, check=True):
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error executing command: {' '.join(cmd)}")
        print(f"Stdout:\n{result.stdout}")
        print(f"Stderr:\n{result.stderr}")
        sys.exit(result.returncode)
    return result


def get_previous_tag(changelog_content: str) -> str:
    # Find all headings: ## <version>
    # Ignore any version with -rc
    matches = re.findall(r"^##\s+([^\s]+)", changelog_content, re.MULTILINE)
    for match in matches:
        if "-rc" not in match:
            return match
    return "0.0.0"


def clean_rc_entries(changelog_content: str, base_version: str) -> str:
    lines = changelog_content.splitlines()
    cleaned_lines = []
    skip = False
    pat = re.compile(rf"^## {re.escape(base_version)}-rc\.[0-9]+")

    for line in lines:
        if pat.match(line):
            skip = True
            continue
        if skip:
            if line == "---":
                skip = False
                continue
            if line.startswith("## "):
                skip = False
                # Do NOT continue here because we want to print this line if it's not skipped!
        if not skip:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


def rotate_changelog(changelog_content: str, max_entries: int = 20) -> str:
    lines = changelog_content.splitlines()
    heading_count = 0
    cutoff_idx = len(lines)
    for idx, line in enumerate(lines):
        if line.startswith("## "):
            heading_count += 1
            if heading_count == max_entries + 1:
                cutoff_idx = idx
                break
    return "\n".join(lines[:cutoff_idx])


def main():
    parser = argparse.ArgumentParser(description="Consolidate release changelog")
    parser.add_argument(
        "--version", help="Version to release (defaults to CI_COMMIT_TAG)"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Do not commit or push changes"
    )
    args = parser.parse_args()

    version = args.version or os.environ.get("CI_COMMIT_TAG")
    if not version:
        print("Error: Version must be provided via --version or CI_COMMIT_TAG env var.")
        sys.exit(1)

    is_rc = "-rc." in version

    # Configure Git
    if not args.dry_run:
        gitlab_token = os.environ.get("GITLAB_TOKEN")
        ci_server_host = os.environ.get("CI_SERVER_HOST")
        ci_project_path = os.environ.get("CI_PROJECT_PATH")
        gitlab_user_name = os.environ.get("GITLAB_USER_NAME", "GitLab CI")
        gitlab_user_email = os.environ.get("GITLAB_USER_EMAIL", "ci@waldur.com")

        run_cmd(["git", "config", "--global", "user.name", gitlab_user_name])
        run_cmd(["git", "config", "--global", "user.email", gitlab_user_email])

        if gitlab_token and ci_server_host and ci_project_path:
            origin_url = f"https://gitlab-ci-token:{gitlab_token}@{ci_server_host}/{ci_project_path}.git"
            run_cmd(["git", "remote", "set-url", "origin", origin_url])

        run_cmd(["git", "fetch", "origin", "master"])
        run_cmd(["git", "branch", "-D", "master"], check=False)
        run_cmd(["git", "checkout", "--track", "origin/master"])
        run_cmd(["git", "pull"])

    if not CHANGELOG_PATH.exists():
        print(f"Error: {CHANGELOG_PATH} not found.")
        sys.exit(1)

    with open(CHANGELOG_PATH, "r", encoding="utf-8") as f:
        changelog_content = f.read()

    # Check if entry already exists
    if re.search(rf"^## {re.escape(version)}", changelog_content, re.MULTILINE):
        print(f"Changelog entry for {version} already exists — skipping.")
        sys.exit(0)

    prev_tag = get_previous_tag(changelog_content)
    print(f"Generating consolidated changelog for {version} (since {prev_tag})")

    # Generate new entry
    gen_cmd = [
        "python3",
        "scripts/generate_enhanced_changelog_multi_repo.py",
        version,
        prev_tag,
    ]
    gen_result = run_cmd(gen_cmd)

    # Extract only lines from ## to --- (excluding --- itself)
    gen_lines = gen_result.stdout.splitlines()
    new_entry_lines = []
    started = False
    for line in gen_lines:
        if line.startswith("## "):
            started = True
        if started:
            if line == "---":
                break
            new_entry_lines.append(line)

    new_entry = "\n".join(new_entry_lines)
    print(f"Generated changelog entry:\n{new_entry}")

    # Remove any existing RC entries for the same base version
    base_version = version.split("-rc.")[0] if is_rc else version
    changelog_content = clean_rc_entries(changelog_content, base_version)

    # Rotate old entries (keep max 20)
    entries_part = changelog_content
    header_match = re.match(r"^(# Changelog\s*)", changelog_content)
    if header_match:
        entries_part = changelog_content[header_match.end() :]

    entries_part = rotate_changelog(entries_part, 19)

    # Reconstruct final changelog
    final_changelog = f"# Changelog\n\n{new_entry}\n\n{entries_part}"

    # Clean up empty lines or double newlines
    final_changelog = re.sub(r"\n{3,}", "\n\n", final_changelog)

    # Save changelog
    with open(CHANGELOG_PATH, "w", encoding="utf-8") as f:
        f.write(final_changelog)

    # Update publiccode.yml if not RC
    if not is_rc and PUBLICCODE_PATH.exists():
        with open(PUBLICCODE_PATH, "r", encoding="utf-8") as f:
            pub_content = f.read()

        pub_content = re.sub(
            r"^softwareVersion:.*",
            f"softwareVersion: {version}",
            pub_content,
            flags=re.MULTILINE,
        )
        today = datetime.date.today().isoformat()
        pub_content = re.sub(
            r"^releaseDate:.*", f"releaseDate: {today}", pub_content, flags=re.MULTILINE
        )

        with open(PUBLICCODE_PATH, "w", encoding="utf-8") as f:
            f.write(pub_content)

        if not args.dry_run:
            run_cmd(["git", "add", str(PUBLICCODE_PATH)])

    # Commit and push
    if not args.dry_run:
        run_cmd(["git", "add", str(CHANGELOG_PATH)])
        diff_res = run_cmd(["git", "diff", "--cached", "--quiet"], check=False)
        if diff_res.returncode != 0:  # meaning there are changes
            run_cmd(["git", "--no-pager", "diff", "--cached", "--stat"])
            run_cmd(
                [
                    "git",
                    "commit",
                    "-m",
                    f"Release {version}: update changelog and publiccode.yml",
                ]
            )
            run_cmd(["git", "pull", "--rebase", "origin", "master"])
            run_cmd(["git", "push", "-o", "ci.skip", "origin", "master"])
        else:
            print("No changes to commit.")


if __name__ == "__main__":
    main()
