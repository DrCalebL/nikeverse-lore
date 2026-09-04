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
#     ⭐ MATCHED CASE-SENSITIVELY, ALONE AMONG THE FOUR — owner ruling. See RETIRED_TITLES below.
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
# Usage: scripts/check-canon-terms.sh [ROOT]
#   No argument  → scans this repo (the script's own parent directory), as before.
#   With a ROOT  → scans that tree with the SAME rules. The retired terms were coined and retired
#                  ACROSS repos, so the check has to be runnable across repos: point it at a sibling
#                  checkout (the Discord game, the MMO build) to prove a retired term did not survive
#                  there. That is also why -w below is load-bearing — see the header note.
#
#   Exit 0 = clean · 1 = a live hit, or a malformed/dead waiver · 2 = the ROOT is unusable.
#
#   TWO IN-BAND WAIVERS (see the block above the search for the full argument):
#     canon-allow: <reason>        on the offending line          (>= 6 chars of reason, mandatory)
#     canon-allow-file: <reason>   in the file's FIRST 25 LINES   (>= 6 chars of reason, mandatory)

set -eu
ROOT="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
STATUS=0

# One term per line. Matched case-insensitively (-i) and on word boundaries (-w).
RETIRED_TERMS="keth'vor
unraveler
sasuke"

# ⭐⭐ THE PROPER-NOUN TITLES — MATCHED CASE-SENSITIVELY (no -i), AND THAT IS AN OWNER RULING.
#
# `Reacher` is a retired TITLE: the character now called the Collector. The lowercase `reacher` is a
# DIFFERENT WORD — the game mechanic *"whoever is currently reaching to soothe a soul"*, rooted in the
# canon "reach" verb. They are homographs, and the case-insensitive list conflated them.
#
# ⚠ MEASURED, and the numbers are the whole argument. Against the MMO build repo this lint reported
# **151 live hits** and was red for months. They decomposed:
#     113  lowercase `reacher`  — the MECHANIC, in the catch subsystem and its tests. Pure false alarm.
#      19  `class Reacher` / `: Reacher` / `new Reacher(` — ALSO the mechanic, in three test FIXTURES.
#      17  the build repo's own runtime ban lists and their tests, which name retired terms to GOVERN
#          them (the same carve-out the EXCLUDED names below exist for).
#       2  genuine title mentions, both governing.
# Splitting the lists takes 151 → 35; the in-band waivers take 35 → 0.
#
# ⛔ DO NOT "SIMPLIFY" THIS BY DROPPING -i FROM THE WHOLE SEARCH. The other three have NO legitimate
# lowercase homograph — verified by grep across all four repos: outside these ban lists, lowercase
# `unraveler` and `sasuke` appear nowhere, and `keth'vor` is lowercase BY SPELLING. Making them
# case-sensitive would let a lowercase revival walk straight through.
#
# ⛔⛔ AND CAPITALISATION DOES NOT, BY ITSELF, SEPARATE A TITLE FROM A MECHANIC — this is the hole, and
# it is named rather than hidden. A class is PascalCase because it is a class, so `class Reacher` is the
# MECHANIC wearing a capital letter. Those three fixture files therefore carry a canon-allow-file:
# marker, and a genuine title use inside one of them would be waived along with the class. That residue
# is bounded on purpose: the build repo's own runtime lints (`client/ui/funnel.ts`, `client/ui/bond.ts`)
# ban the word in every PLAYER-FACING string with their own tests, so what this list still carries for
# `Reacher` is DESIGN PROSE, which is exactly where the retired title actually lives.
#
# ⛔⛔ THE SECOND HOLE, MEASURED AND DELIBERATELY LEFT OPEN: an ALL-CAPS `THE REACHER` is NOT caught.
# Planted in a non-waived doc it exits 0. It is left open because closing it costs more than it buys —
# adding `REACHER` to this list mints **9 fresh false positives** in the build repo, every one of them
# the MECHANIC inside an emphatic all-caps comment (`EVERY REACHER`, `THE REACHER'S FUNNEL STEP`), which
# is that repo's house comment style.
# ⭐ THE GENERAL LESSON, and it is why this is a note rather than a bug: IN THIS CODEBASE NEITHER
# PascalCase NOR ALL-CAPS IS EVIDENCE OF A PROPER NOUN. The first is how a class is spelled, the second
# is how a comment shouts. Only mixed-case `Reacher` in running prose signals the title, and that is
# exactly what this list now matches. The residual risk is carried elsewhere: the build repo's runtime
# audits match case-INSENSITIVELY, so an all-caps title in a PLAYER-FACING string is still caught there.
RETIRED_TITLES="Reacher"

# Search all canon content. Five files are excluded by NAME because they name the retired terms on
# purpose, in order to document the retirement: CHANGELOG.md, CANON.md §3.2 (the retired-names section —
# the canonical statement of what each term was replaced by), CANON_MAP.md (the cross-repo reconciliation
# table, which has to quote the retired spelling to say what it became), CLAUDE.md (NEVER #3 states the
# retirement rule and must quote the terms to state it), and docs/progress-log.md (the wave that retired
# them).
#
# This script and its two siblings are excluded as FILES, not by excluding scripts/ as a DIRECTORY.
# In THIS repo scripts/ holds nothing but the three lints, so the two spellings looked equivalent.
# They are not: pointed at nikeverse-mmo-rpg, --exclude-dir=scripts silently blinded 27 real tooling
# files, while the sibling build repo's equivalent tools/ stayed scanned — the same flag giving
# different coverage per repo. node_modules/, dist/ and build/ are excluded for the opposite reason:
# a dependency that happens to vendor one of these words would red an innocent build with a finding
# nobody in this project can fix.
#
# TWO IN-BAND WAIVERS, because this check now runs against repos whose canon docs must NAME a retired
# term to GOVERN it, and a per-repo exclusion LIST is the artefact that historically failed to travel
# when the corpus moved repos. In-band travels with the file, and — load-bearing — a waiver written
# below the GAME_SPEC.md fence propagates into its regenerated TESANA_BUILD_PROMPT.md twin for free.
#
#   canon-allow: <reason>        on the offending line          (>= 6 chars of reason, mandatory)
#   canon-allow-file: <reason>   in the file's FIRST 25 LINES   (>= 6 chars of reason, mandatory)
#
# A reason must contain no apostrophe and no double quote (the sibling python lint's reason capture is
# [^"']* and would truncate), and must not itself contain a retired term.
#
# A canon-allow-file: marker on a file with ZERO hits is a FAILURE, not a courtesy. Dead exclusions are
# exactly how an allowlist rots into theatre; this makes the list prune itself.

[ -d "$ROOT" ] || { echo "check-canon-terms: ROOT '$ROOT' is not a directory"; exit 2; }

# A lint that scans nothing prints ok and gates nothing. Refuse to be that lint. -prune rather than a
# -not -path filter, or this descends into a 170 MB node_modules just to discard it.
SCANNABLE="$(find "$ROOT" \
    \( -name .git -o -name node_modules -o -name dist -o -name build \) -prune -o \
    -type f -print 2>/dev/null | wc -l | tr -d ' ')"
if [ "$SCANNABLE" -eq 0 ]; then
  echo "check-canon-terms: ROOT '$ROOT' contains no scannable files."
  echo "A lint that scans nothing reports green. Fix the path; never let this pass."
  exit 2
fi

EXCL="--exclude-dir=.git --exclude-dir=node_modules --exclude-dir=dist --exclude-dir=build
--exclude=check-canon-terms.sh --exclude=check-fallen-taxonomy.py --exclude=check-mystery-tiers.py
--exclude=CHANGELOG.md --exclude=CANON.md --exclude=CANON_MAP.md
--exclude=CLAUDE.md --exclude=progress-log.md"

# A reason is >= 6 characters AFTER the comment closer is removed. Measuring the raw tail instead is
# the obvious shortcut and it is wrong: in "<!-- canon-allow: ab -->" the closer contributes four
# characters, so a regex that just counts what follows the marker waives a line for the word "ab".
# Markup is not an explanation. Lowercased first so the marker matches case-insensitively, which is
# safe because only the LENGTH of the reason is measured here, never its content.
reason_ok() {                                   # $1 = line, $2 = marker (lowercase)
  _r="$(printf '%s' "$1" | tr 'A-Z' 'a-z' \
        | sed -n "s/.*$2[[:space:]]*//p" \
        | sed -e 's/-->.*$//' -e 's,\*/.*$,,' -e 's/[[:space:]]*$//' \
        | head -1)"
  [ "${#_r}" -ge 6 ]
}

# 0 = this file carries a well-formed whole-file waiver in its first 25 lines.
file_marker_ok() {                              # $1 = file
  _m="$(head -25 "$1" 2>/dev/null | grep -iE 'canon-allow-file:' | head -1)"
  [ -n "$_m" ] || return 1
  reason_ok "$_m" 'canon-allow-file:'
}

RAW="$(mktemp)"; KEPT="$(mktemp)"; WAIVED="$(mktemp)"; SHORT="$(mktemp)"
HITFILES="$(mktemp)"; MARKERS="$(mktemp)"
trap 'rm -f "$RAW" "$KEPT" "$WAIVED" "$SHORT" "$HITFILES" "$MARKERS"' EXIT
: > "$RAW"; : > "$KEPT"; : > "$WAIVED"; : > "$SHORT"

# shellcheck disable=SC2086
for TERM in $RETIRED_TERMS; do
  grep -rnwi $EXCL -- "$TERM" "$ROOT" >> "$RAW" 2>/dev/null || true
done
# The titles: same -w, same exclusions, same waivers — everything except the -i. Both loops append to
# the SAME $RAW, so the waiver machinery, the short-reason bucket and the dead-marker sweep below cover
# the titles without knowing they exist.
# shellcheck disable=SC2086
for TITLE in $RETIRED_TITLES; do
  grep -rnw $EXCL -- "$TITLE" "$ROOT" >> "$RAW" 2>/dev/null || true
done
cut -d: -f1 "$RAW" | sort -u > "$HITFILES"

# Redirected, never piped: `while ... done < file` runs in THIS shell, so the STATUS it sets survives.
# The same loop fed by a pipe runs in a subshell and every assignment is discarded on exit — a lint
# that reports its findings and then exits 0.
while IFS= read -r HIT; do
  [ -n "$HIT" ] || continue
  F="${HIT%%:*}"; REST="${HIT#*:}"; TEXT="${REST#*:}"
  if printf '%s' "$TEXT" | grep -qiE 'canon-allow:'; then
    if reason_ok "$TEXT" 'canon-allow:'; then
      continue
    fi
    # Its own bucket, not KEPT: KEPT is sorted to dedupe lines two terms both matched, and a sort
    # would tear a multi-line explanation away from the finding it explains.
    printf '%s\n' "$HIT" >> "$SHORT"
    continue
  fi
  if file_marker_ok "$F"; then
    printf '%s\n' "$F" >> "$WAIVED"; continue
  fi
  printf '%s\n' "$HIT" >> "$KEPT"
done < "$RAW"

if [ -s "$KEPT" ]; then
  echo "RETIRED canon term(s) found — see this script's header for each replacement."
  echo "If the line names a retired term in order to GOVERN it, append  canon-allow: <reason>"
  echo "If the WHOLE FILE does, put  canon-allow-file: <reason>  in its first 25 lines."
  sort -u "$KEPT"
  echo
  STATUS=1
fi

if [ -s "$SHORT" ]; then
  echo "canon-allow: present, but the reason is under 6 characters — and surrounding markup"
  echo "does not count toward it. An unexplained waiver is a disabled lint. Say why, in words:"
  sort -u "$SHORT"
  echo
  STATUS=1
fi

# Dead-marker sweep: a whole-file waiver that waives nothing is a disabled lint with a comment on it.
# shellcheck disable=SC2086
grep -rlE 'canon-allow-file:' $EXCL "$ROOT" > "$MARKERS" 2>/dev/null || true
while IFS= read -r M; do
  [ -n "$M" ] || continue
  if ! file_marker_ok "$M"; then
    echo "MALFORMED or MISPLACED canon-allow-file: marker in $M"
    echo "  It must sit in the first 25 lines and carry >= 6 characters of reason."
    STATUS=1
    continue
  fi
  if ! grep -qxF "$M" "$HITFILES"; then
    echo "DEAD canon-allow-file: marker in $M — the file has no retired-term hit."
    echo "  Remove the marker. A waiver nobody needs is how an allowlist becomes theatre."
    STATUS=1
  fi
done < "$MARKERS"

[ "$STATUS" -eq 0 ] && echo "ok: no retired canon terms present ($SCANNABLE files under $ROOT, $(sort -u "$WAIVED" | wc -l | tr -d ' ') file waiver(s))"
exit "$STATUS"
