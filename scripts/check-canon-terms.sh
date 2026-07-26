#!/usr/bin/env sh
# check-canon-terms.sh — fails if any RETIRED First-Tongue term reappears in canon content.
#
# retired: keth'vor  (2026-06-17) — split into keth'nor (corruption) + Eth'kara (heart-chain).
#   The term had been glossed two incompatible ways (a corruption-warning in-language vs a
#   "heart-chain / oldest name for The Pattern" gloss in the English metadata). Both senses already
#   have their own canonical words, so keth'vor is retired and each use points at the word that
#   already means it. See CHANGELOG.md "First Tongue disambiguation". If you are introducing a new
#   word of power, add it to languages/first-tongue/dictionary.json — do NOT revive keth'vor.
#
# Usage: scripts/check-canon-terms.sh   (run from repo root; exits 1 on any hit)

set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RETIRED="keth'vor"
STATUS=0

# Search all canon content. Exclude .git, this scripts dir, and CHANGELOG.md — the linter header
# and the changelog entry both NAME the retired term on purpose (to document the retirement).
HITS="$(grep -rn --exclude-dir=.git --exclude-dir=scripts --exclude=CHANGELOG.md -F "$RETIRED" "$ROOT" || true)"
if [ -n "$HITS" ]; then
  echo "RETIRED canon term '$RETIRED' found — see scripts/check-canon-terms.sh header for the split:"
  echo "$HITS"
  STATUS=1
fi

[ "$STATUS" -eq 0 ] && echo "ok: no retired canon terms present"
exit "$STATUS"
