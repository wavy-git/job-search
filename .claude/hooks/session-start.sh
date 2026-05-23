#!/bin/bash
# SessionStart hook: project inclusion tests + discipline rules dynamically from files.
# Single source of truth = the files themselves. This script reads them at runtime.

cd "$(dirname "$0")/../.."

echo "=== Job Search System ==="
echo ""
echo "Read CLAUDE.md first. It indexes everything and routes to the right skill."
echo ""

echo "=== CLAUDE.md Index ==="
awk '/^## Index/,/^---$/' CLAUDE.md
echo ""

echo "=== Inclusion tests (17 stable files, projected from source) ==="
for file in \
  me/background.md \
  me/voice.md \
  me/constraints.md \
  me/resume.md \
  me/linkedin.md \
  skills/profiling/profiling.md \
  skills/sourcing/sourcing.md \
  skills/screening/screening.md \
  skills/tailoring/tailoring.md \
  skills/outreach/outreach.md \
  skills/interviewing/interviewing.md \
  skills/maintenance/maintenance.md \
  skills/composing/composing.md \
  CLAUDE.md \
  design.md \
  discipline.md \
  pending.md; do

  if [ -f "$file" ]; then
    echo "--- $file ---"
    awk '/^## Inclusion test/,/^---$/' "$file"
    echo ""
  fi
done

echo "=== Discipline rules (names only — read discipline.md for full text) ==="
grep -E "^## Rule [0-9]+" discipline.md
echo ""

echo "=== Git status ==="
git status --short 2>/dev/null | head -10
