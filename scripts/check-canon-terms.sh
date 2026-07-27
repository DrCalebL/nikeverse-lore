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
# Usage: scripts/check-canon-terms.sh [ROOT]   (exits 1 on any hit)
#   No argument  → scans this repo (the script's own parent directory), as before.
#   With a ROOT  → scans that tree with the SAME rules. The retired terms were coined and retired
#                  ACROSS repos, so the check has to be runnable across repos: point it at a sibling
#                  checkout (the Discord game, the MMO build) to prove a retired term did not survive
#                  there. That is also why -w below is load-bearing — see the header note.

set -eu
ROOT="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
STATUS=0

# One term per line. Matched case-insensitively (-i) and on word boundaries (-w).
RETIRED_TERMS="keth'vor
unraveler
reacher
sasuke"

# Search all canon content. Four files are excluded because they NAME the retired terms on purpose, in order
# to document the retirement: this script's own header, CHANGELOG.md, CANON.md §3.2 (the retired-names
# section — the canonical statement of what each term was replaced by), and CANON_MAP.md (the cross-repo
# reconciliation table, which has to quote the retired spelling to say what it became). Everything else is
# canon content and must stay clean. If you add another doc that must name a retired term, add it here and
# say why.
for TERM in $RETIRED_TERMS; do
  HITS="$(grep -rnwi --exclude-dir=.git --exclude-dir=scripts \
            --exclude=CHANGELOG.md --exclude=CANON.md --exclude=CANON_MAP.md -- "$TERM" "$ROOT" || true)"
  if [ -n "$HITS" ]; then
    echo "RETIRED canon term '$TERM' found — see scripts/check-canon-terms.sh header for its replacement:"
    echo "$HITS"
    echo
    STATUS=1
  fi
done

[ "$STATUS" -eq 0 ] && echo "ok: no retired canon terms present"
exit "$STATUS"
