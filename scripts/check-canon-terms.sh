#!/usr/bin/env sh
# check-canon-terms.sh — fails if any RETIRED canon term reappears in canon content.
#
# RETIRED TERMS AND WHAT REPLACED THEM
#
#   keth'vor  (2026-06-17) → keth'nor (corruption) + Eth'kara (heart-chain / the First Bond / the Pattern)
#     The term had been glossed two incompatible ways — a corruption-warning in-language, versus a
#     "heart-chain / oldest name for The Pattern" gloss in the English metadata. Both senses already had
#     their own canonical words, so keth'vor is retired and each use points at the word that already
#     means it. See CHANGELOG.md "First Tongue disambiguation".
#
#   Unraveler (2026-06-17) → Harbinger (a fallen Collector HUMAN) / Corrupted Nike (a fallen Nike)
#     The faction is The Harbingers. A fallen Nike beyond saving is a Retnuhxed. Never call a Nike a
#     Harbinger. NOTE the protected carve-out: Nol'meth is glossed "The Unraveling" and is CORRECT —
#     that is why this check is word-boundary matched on "unraveler", not a substring match.
#
#   Reacher    → the Collector       (coined and retired game-side; never appeared in this repo)
#   Sasuke     → Toga                (Ninja Nike's reclaimed personal name; the nameplate stays "Ninja Nike")
#
# If you are introducing a new word of power, add it to languages/first-tongue/dictionary.json — do NOT
# revive a retired term. And never retire an English term whose First-Tongue root is authored:
# Har'ben is glossed "Origin of 'Harbinger'" and Ret'nux "Origin of 'Retnuhxed'", so retiring either
# English word would force re-deriving every phrase and inscription built on its root.
#
# WHY WORD-BOUNDARY MATCHING (-w) IS REQUIRED, NOT OPTIONAL:
#   A bare substring search for "reacher" matches "t-reacher-ous". That false positive is not
#   hypothetical — it fires on real content in the sibling Discord-game repo. Do not "simplify" this
#   back to -F.
#
# Usage: scripts/check-canon-terms.sh   (run from repo root; exits 1 on any hit)

set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
STATUS=0

# One term per line. Matched case-insensitively (-i) and on word boundaries (-w).
RETIRED_TERMS="keth'vor
unraveler
reacher
sasuke"

# Search all canon content. Three files are excluded because they NAME the retired terms on purpose, in order
# to document the retirement: this script's own header, CHANGELOG.md, and CANON.md §3.2 (the retired-names
# section — the canonical statement of what each term was replaced by). Everything else is canon content and
# must stay clean. If you add another doc that must name a retired term, add it here and say why.
for TERM in $RETIRED_TERMS; do
  HITS="$(grep -rnwi --exclude-dir=.git --exclude-dir=scripts \
            --exclude=CHANGELOG.md --exclude=CANON.md -- "$TERM" "$ROOT" || true)"
  if [ -n "$HITS" ]; then
    echo "RETIRED canon term '$TERM' found — see scripts/check-canon-terms.sh header for its replacement:"
    echo "$HITS"
    echo
    STATUS=1
  fi
done

[ "$STATUS" -eq 0 ] && echo "ok: no retired canon terms present"
exit "$STATUS"
