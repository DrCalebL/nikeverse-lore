#!/usr/bin/env python3
"""check-fallen-taxonomy.py — guards the fallen-side taxonomy on the axis that had no lint.

THE RULING (owner, 2026-07-29): "follow my current game's definitions — corrupted nikes are
reversible, retnuhxed is too far gone."  THE THRESHOLD BETWEEN THE TERMS IS REVERSIBILITY.

    Corrupted Nike  a fallen Nike who CAN be brought back. Purify / bond / wake works.
    Retnuhxed       past REACHING — not soul-destroyed. CANON.md §2.1: a slain husk still
                    releases a warm soul-mote; the soul is in there and cannot be called back,
                    so death is the only door left. Never "consumed", never "nothing left inside".
    Harbinger       a fallen COLLECTOR (human) who followed Nolem. Never a Nike, and never
                    "corrupted" — factions/index.json: "Not corrupted—converted."

WHY THIS EXISTS. Two independent Opus audits on 2026-07-29 swept 286 live occurrences of these
terms across four repos — the first time this axis had ever been checked — and found six editable
violations. Every one was the same failure: an amendment applied to one clause while the sibling
clause carrying the same claim was left standing, sometimes in the same file. The sharpest was
singulars/nolem.json asserting Nolem "turns living, uncorrupted allies into Retnuhxed" — i.e. a
Retnuhxed made and then recovered — written the SAME DAY as the ruling that forbids it.

    All six would have been caught mechanically. That is what this script is for.

DESIGN NOTES, so this does not get disabled the first time it is noisy:
  * Proximity-based, not substring. A term only trips when a contradicting verb/phrase sits within
    PROXIMITY characters of it, which is what makes it precise enough to keep armed.
  * Governing documents are EXCLUDED by the same logic as check-canon-terms.sh: a file that names a
    forbidden pairing in order to FORBID it must be allowed to say it. Deleting the record leaves
    the rule unexplained.
  * Shipped Discord content is GRANDFATHERED (owner ruling: the game is the factual record and is
    not swept). Violations there belong in GAME_DELTAS, not in a diff.
  * Villain speech is legitimate: a Nolem-aligned character claiming a Nike is beyond saving is
    dramatic irony the game disproves. Lines that are quoted claims get flagged as WARN, not FAIL.

Exit 0 = clean. Exit 1 = at least one FAIL.
"""
import os
import re
import sys

# Target root: default = this lore repo (self-check). An optional argv[1] points the SAME
# taxonomy guard at another repo (a game repo A/B) so it can be armed in that repo's CI,
# exactly as check-canon-terms.sh and check-mystery-tiers.py already accept a target root.
_LORE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else _LORE_ROOT
LORE_SELF = (ROOT == _LORE_ROOT)
PROXIMITY = 160  # chars either side of the term

# Files that discuss the rule itself, or record its history, and must be free to name violations.
EXCLUDED = {
    "CANON.md", "CHANGELOG.md", "GAME_DELTAS.md", "CANON_MAP.md",
    "MASTER_LORE_PROPOSAL_FINAL.md", "THE_5555.md", "CONTRIBUTING.md", "CLAUDE.md",
    "RECONCILIATION.md", "claims.json", "script.md", "README.md",
    # Append-only meta / history that names violations in order to record them — present in
    # the game repos too; the same governing carve-out as the retired-terms lint.
    "KNOWN_ISSUES.md", "progress-log.md", "wave-log.md", "TESANA_BUILD_LOG.md",
}
# In the LORE repo, docs/ is meta (progress-log, KNOWN_ISSUES) and is excluded wholesale.
# In a GAME repo the canon prose LIVES in docs/, so it must be scanned there; its meta files
# are excluded by name via EXCLUDED above instead.
EXCLUDED_DIRS = {".git", "node_modules", "scripts", "schemas"}
if LORE_SELF:
    EXCLUDED_DIRS = EXCLUDED_DIRS | {"docs"}

# An occurrence is exempt if the surrounding window says it is being corrected or recorded.
EXEMPT_MARKERS = re.compile(
    r"STRUCK|AMENDED|CORRECTED|RE-CONFIRMED|SUPERSEDED|GRANDFATHERED|formerly|Formerly|"
    r"never write|NEVER write|do not|Do NOT|reworded|struck|deliberately|"
    # In-band governing markers. `fallen-allow` is this lint's own marker; `canon-allow` is
    # the retired-terms lint's marker, honored here too because a line already waived as a
    # governing use of a retired term is, by construction, a governing line that may name a
    # forbidden pairing to forbid it. Reason text after the marker is free-form.
    r"fallen-allow|canon-allow|"
    # Definitional / boundary passages: text that states what a Retnuhxed IS, in order to rule
    # what something ELSE is not, must be free to state it. entities/dimension-eater.json's
    # `notARetnuhxed` block is the model case — it defines the term precisely so the Eater
    # cannot be mis-filed as one.
    r"notARetnuhxed|mis-fil|never a Nike, never a person|is a fallen NIKE",
)

# (label, term regex, contradiction regex, severity)
RULES = [
    ("R1  a Retnuhxed described as recoverable",
     r"\bRetnuhxed\b",
     r"\b(purif\w+|redeem\w*|be saved|can be saved|bring \w+ back|brought back|come back|"
     r"woken|awaken\w*|bond(ed|able)?\s+(it|him|her|them)|soothe\w*|reversib\w+)\b",
     "FAIL"),

    ("R2  a Retnuhxed described as soul-destroyed (breaks §2.1's soul-mote)",
     r"\bRetnuhxed\b",
     r"(souls?\s+consumed|nothing left inside|no soul|soulless|already a tombstone|"
     r"soul (is )?(gone|destroyed|eaten))",
     "FAIL"),

    ("R3  a Corrupted Nike described as beyond saving (collapses the line from the other side)",
     r"\bCorrupted (Nike|Legendary)\b",
     r"\b(too far gone|so far gone|beyond saving|past saving|cannot be saved|unsavable|"
     r"never be reached|irreversib\w+)\b",
     "FAIL"),

    ("R4  a human called corrupted (Harbingers are FALLEN / converted, never corrupted)",
     r"\b[Cc]orrupted\s+(Collector|Walker|human|Harbinger)s?\b",
     r".",
     "FAIL"),

    ("R5  a Nike called a Harbinger (wrong axis entirely)",
     r"\bHarbinger\b",
     r"\b(a|the) (fallen |corrupted )?Nike\b(?!.{0,40}\bnever\b)",
     "WARN"),

    ("R6  'Retnuhxed' used as a process rather than a kind of being",
     r"\b(being|becoming|turned into|turn into|made into) (a )?Retnuhxed\b",
     r".",
     "WARN"),
]


def walk():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS and not d.startswith(".")]
        for fn in filenames:
            if not fn.endswith((".json", ".md")):
                continue
            if fn in EXCLUDED:
                continue
            yield os.path.join(dirpath, fn)


def main():
    fails, warns = [], []
    scanned = occurrences = 0

    for path in walk():
        scanned += 1
        try:
            text = open(path, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        rel = os.path.relpath(path, ROOT)

        for label, term_re, contra_re, severity in RULES:
            for m in re.finditer(term_re, text):
                occurrences += 1
                lo = max(0, m.start() - PROXIMITY)
                hi = min(len(text), m.end() + PROXIMITY)
                window = text[lo:hi]
                # Exempt if a marker sits in the proximity window OR anywhere on the flagged
                # LINE — so a per-line governing marker works even when the line is longer
                # than the proximity window (common for the game repos' dense spec lines).
                line_start = text.rfind("\n", 0, m.start()) + 1
                line_end = text.find("\n", m.end())
                full_line = text[line_start:(line_end if line_end != -1 else len(text))]
                if EXEMPT_MARKERS.search(window) or EXEMPT_MARKERS.search(full_line):
                    continue
                hit = re.search(contra_re, window)
                if not hit:
                    continue
                line = text.count("\n", 0, m.start()) + 1
                snippet = " ".join(window.split())[:150]
                entry = f"  {rel}:{line}\n      {label}\n      …{snippet}…"
                (fails if severity == "FAIL" else warns).append(entry)

    if warns:
        print(f"\n⚠ {len(warns)} WARNING(S) — review, not necessarily wrong "
              f"(villain speech and quoted claims are legitimate):\n")
        for w in warns:
            print(w + "\n")

    if fails:
        print(f"\n❌ {len(fails)} TAXONOMY VIOLATION(S):\n")
        for f in fails:
            print(f + "\n")
        print("THE RULE: Corrupted = reversible · Retnuhxed = past REACHING (not soul-destroyed) ·")
        print("Harbingers are FALLEN humans, never 'corrupted', and never Nikes.")
        print("If a line names a violation in order to FORBID it, add a marker "
              "(STRUCK / AMENDED / CORRECTED / never write) or add the file to EXCLUDED.\n")
        return 1

    # Zero-scan assertion: a lint that scans nothing reports green and hides everything.
    # Guards against a wrong root or an over-broad exclusion silently disarming the check.
    if scanned == 0:
        print(f"❌ ZERO FILES SCANNED under {ROOT} — refusing to report green. "
              f"Check the target root and EXCLUDED_DIRS (a lint that scans nothing hides everything).")
        return 1

    print(f"ok: fallen-side taxonomy clean — {scanned} files scanned, "
          f"{occurrences} term occurrences checked, {len(warns)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
