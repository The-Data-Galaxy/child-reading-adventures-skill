#!/usr/bin/env bash
set -euo pipefail

MODE="${1:---all}"
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

fail() { printf 'repository gate: %s\n' "$1" >&2; exit 1; }

for required in README.md LICENSE INSTALL.md RELEASE_NOTES.md MANIFEST.md design-child-reading-adventures/SKILL.md; do
  [[ -f "$required" ]] || fail "missing required file: $required"
done

head -n 30 design-child-reading-adventures/SKILL.md | grep -Eq '^name:[[:space:]]*design-child-reading-adventures' || fail "invalid Skill name"
head -n 30 design-child-reading-adventures/SKILL.md | grep -Eq '^description:[[:space:]]*[^[:space:]]' || fail "missing Skill description"

if [[ "$MODE" == "--staged" ]]; then
  file_command=(git diff --cached --name-only --diff-filter=ACMR)
else
  file_command=(git ls-files)
fi

while IFS= read -r path; do
  [[ -z "$path" ]] && continue
  case "$path" in
    *.DS_Store|.DS_Store|*.pem|*.key|*.p12|*.pfx|*.jks|*.keystore|.env|.env.*)
      fail "forbidden sensitive filename: $path" ;;
  esac
done < <("${file_command[@]}")

secret_pattern='AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{36,255}|sk-[A-Za-z0-9_-]{20,}|-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----'
if [[ "$MODE" == "--staged" ]]; then
  if git diff --cached --no-ext-diff -U0 | grep '^+' | grep -Eq "$secret_pattern"; then fail "credential-like content detected"; fi
elif git grep -I -q -E "$secret_pattern" -- .; then
  fail "credential-like content detected"
fi

if [[ -f CHECKSUMS.txt ]]; then
  if command -v sha256sum >/dev/null 2>&1; then sha256sum -c CHECKSUMS.txt >/dev/null || fail "checksum failed";
  else shasum -a 256 -c CHECKSUMS.txt >/dev/null || fail "checksum failed"; fi
fi

printf 'repository gate: passed (%s)\n' "$MODE"

