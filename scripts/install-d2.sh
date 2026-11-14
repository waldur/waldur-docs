#!/bin/sh
# Install the pinned D2 binary that mkdocs-d2-plugin renders diagrams with.
# Used by the CI jobs that build the site (Linux runners, as root).
#
# The release tarball is downloaded straight from GitHub releases and checked
# against a pinned sha256. d2lang.com/install.sh is not used: it looks the
# release up through api.github.com, which allows 60 anonymous requests an hour
# per IP. Every runner shares one egress IP, so in a busy hour the installer got
# HTTP 403 three times and failed the job (exit 22). Release downloads are not
# subject to that API limit.
#
# To bump: change D2_VERSION and replace both checksums with the sha256 of the
# new d2-<version>-linux-{amd64,arm64}.tar.gz assets.
set -eu

D2_VERSION=v0.7.1

case "$(uname -m)" in
  x86_64 | amd64)
    arch=amd64
    sha256=eb172adf59f38d1e5a70ab177591356754ffaf9bebb84e0ca8b767dfb421dad7
    ;;
  aarch64 | arm64)
    arch=arm64
    sha256=ce3a0b985a8f91335a826c254b3a88736fd81afcdd08b58f6c749d2add6864b0
    ;;
  *)
    echo "install-d2: unsupported architecture $(uname -m)" >&2
    exit 1
    ;;
esac

name="d2-${D2_VERSION}-linux-${arch}"
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

curl -fsSL --retry 3 -o "$tmp/$name.tar.gz" \
  "https://github.com/d2lang/d2/releases/download/${D2_VERSION}/${name}.tar.gz"
echo "$sha256  $tmp/$name.tar.gz" | sha256sum -c -
tar -xzf "$tmp/$name.tar.gz" -C "$tmp"
install -m 0755 "$tmp/d2-${D2_VERSION}/bin/d2" /usr/local/bin/d2
d2 --version
