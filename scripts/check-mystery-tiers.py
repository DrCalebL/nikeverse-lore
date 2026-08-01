#!/usr/bin/env python3
"""check-mystery-tiers.py — arms the Tier-3 law: "Tier-3 mysteries stay dark."

The law is CANON.md 4.1 (FROZEN) and GAME_SPEC.md 3.16: six questions are never
answered, "no voice, record, artifact or vision resolves them, and none is ever a
thread that can be followed to its end". Until prophecies/mysteries.json carried a
tier field there was nothing for a machine to check, so the law lived entirely in
human review. This script makes the cheap half mechanical.

TWO HALVES, DELIBERATELY DIFFERENT IN KIND
------------------------------------------
A. STRUCTURAL — exact, no heuristics, no false positives. These can fail a build.
   A1  tierDefinitions exists and defines tiers 1, 2 and 3.
   A2  every prophecies[] / mysteries[] entry declares tier 1|2|3.
   A3  every tier-3 entry declares a non-empty tierSource, neverAnswerTerms and
       mayAnswer; every term (and every mayAnswerTerm) compiles.
   A4  CANON.md 4.1 is parsed from the file itself — not hardcoded here — and each
       of its six questions is claimed by exactly one tier-3 entry via
       "canonQuestion". If 4.1 ever changes, this fails loudly instead of silently
       enforcing a stale list.
   A5  lost-singular stays tier 3 (owner deferral 2026-07-26; GAME_SPEC 3.16,
       UNIVERSE_DEPTH_SPEC C8, singulars/index.json the-weaver.canonNote).
   A6  no content file hangs a quest-marker / codex / completion KEY on a tier-3
       subject. "Never quest-marked" is the one part of the Tier-3 rule that is a
       structural property rather than a matter of prose, so it is checked exactly:
       a JSON key on the line must match the marker vocabulary.
   A7  Shiro is seen, never spoken to — no "speaker": "SHIRO" in content.

B. PROSE TRIPWIRE — heuristic, tuned for PRECISION over recall. Fails a line only
   when ALL of:
        a subject term  AND  a resolution construction  AND  NOT hedged
                        AND  NOT covered by that entry's mayAnswerTerms
   "Theories may be spoken and must all remain unproven" is exactly the hedge
   carve-out: a hedged or interrogative line is canon-legal and passes untouched.
   mayAnswerTerms carve out the settled halves the canon explicitly protects —
   that Cthulhu watches and gives, that Shiro opens the way, that the Void Between
   exists, that the Weaver exists and is scattered. Without those carve-outs the
   lint would block legal canon, and a lint that blocks legal canon gets disabled.

WHAT THIS CANNOT CATCH — say it out loud; do not let anyone believe otherwise:
  * prose that answers without naming the subject ("the shape he came for was never
    arbitrary" answers why-pigs and contains none of its terms);
  * an answer assembled across several lines, several fields, or several files —
    every check here is single-line;
  * implication, allegory, and visual/cinematic answers;
  * an answer phrased in a construction RESOLUTION does not know;
  * an answer wrapped in a fake hedge ("some say Shiro was built by the Aeth'kai",
    where the surrounding scene treats it as fact).
  B is a tripwire, not a proof. The build-blocking gate is still the human content
  review named in GAME_SPEC 3.16; this catches the careless half so that review can
  spend itself on the subtle half.

THIS REPO'S DEFAULT ROOTS ARE AN ALLOWLIST, NEVER THE WHOLE REPO. Design docs,
registers, changelogs and this file's own source MUST name the mysteries in order
to govern them, and they sit at this repo's root beside the content. Scanning
governance is how a lint earns a reputation for crying wolf and gets switched off.
Only player-facing content is scanned, and the register that declares the terms
(prophecies/mysteries.json) is always exempt from B.

A ROOT PASSED ON THE COMMAND LINE IS A DIFFERENT PROMISE. It is the caller saying
"scan this tree", and for the two MMO repos that argument is the repo root — every
top-level directory of both was measured before this was armed, and an explicit
per-repo directory list would leave any NEW top-level directory silently unscanned.
Their governance lines are handled the way governance should be: one visible,
reasoned canon-allow: on the line, not an invisible directory carve-out.

ESCAPE HATCH:  canon-allow: <reason>   on the offending line. The reason is
mandatory (>= 6 characters) so a genuine false positive costs one comment and can
be audited later, and "just disable the lint" is never the cheaper option.

Usage:
    python3 scripts/check-mystery-tiers.py [CONTENT_ROOT ...]
    python3 scripts/check-mystery-tiers.py --stats [CONTENT_ROOT ...]

Exit 0 = clean, 1 = violations, 2 = the register or CANON.md could not be read.
"""

import glob
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTER = os.path.join(REPO, "prophecies", "mysteries.json")
CANON = os.path.join(REPO, "CANON.md")

# Player-facing canon content only. Add a directory here when it starts shipping
# to players — never add the repo root, and never add docs/ or CHANGELOG.md.
DEFAULT_ROOTS = [
    os.path.join(REPO, d) for d in (
        "characters", "civilizations", "dimensions", "entities",
        "factions", "languages", "prophecies", "singulars", "timeline",
    )
]

# Files that must name the mysteries in order to govern them. Exempt from the
# prose tripwire (B) and the marker check (A6); the structural checks still read
# the register, they just do not scan it as prose.
GOVERNANCE_FILES = {os.path.realpath(REGISTER)}

# Source extensions are scanned because this check now runs against the two MMO repos, where a
# player-facing line is as likely to be a TypeScript dialogue string as a JSON row: the prior build
# ships ~575 lines of narrative in src/sim/content/narrative/*.ts, and the from-scratch build's sim
# content is TypeScript by construction. A lint that only opens .json and .md cannot see either.
SCAN_EXTS = ("json", "md", "txt", "ts", "tsx", "js", "mjs")

# Never walk vendored or generated trees. Before this, glob("**/*") descended into a 170 MB
# node_modules; scanning a dependency for canon findings can only produce findings nobody here
# can fix.
SKIP_DIRS = ("/.git/", "/node_modules/", "/dist/", "/build/")

# Tier 3 by OWNER DEFERRAL, not by CANON 4.1 — kept separate so the two
# provenances never blur. GAME_SPEC.md 3.16: "DEFERRED BY THE OWNER 2026-07-26 and
# moved to TIER-3". Downgrading this to tier 2 re-opens a question the owner shut.
DEFERRED_TIER3 = {"lost-singular": "owner deferral 2026-07-26 (GAME_SPEC.md 3.16 / "
                                   "UNIVERSE_DEPTH_SPEC.md C8 / singulars/index.json)"}

# A declarative answer. Narrow on purpose: these are the shapes a line takes when
# it RESOLVES something, not when it wonders about it.
RESOLUTION = re.compile(r"""(?ix)
  (?: \b that \s+ (?: is | was ) \s+ (?: why | how | where | what ) \b
    | \b that'?s \s+ (?: why | how | where | what ) \b
    | \b (?: this | here ) \s+ is \s+ (?: why | how | where ) \b
    | \b here'?s \s+ (?: why | how | where | what ) \b
    | \b that \s+ (?: is | was ) \s+ the \s+ (?: answer | reason | truth | origin ) \b
    | \b that'?s \s+ the \s+ (?: answer | reason | truth | origin ) \b
    | \b the \s+ reason \s+ [a-z'\s]{0,30}? \s* (?: is | was ) \b
    | \b (?: was | were ) \s+ (?: consumed | devoured | eaten | absorbed | unmade ) \s+ by \b
    | \b names? \s+ (?: of \s+ [^.!?]{0,45} )? (?: was | were | is | are ) \b
    | \b the \s+ reason \s+ (?: is | was | why | he | she | it | they ) \b
    | \b the \s+ (?: truth | answer ) \s+ (?: is | was ) \b
    | \b (?: now \s+ )? we \s+ know \b
    | \b it \s+ turns \s+ out \b
    | \b the \s+ origin \s+ of \b
    | \b explains? \s+ (?: why | how | it | this | that ) \b
    | \b i \s+ can \s+ tell \s+ you \s+ (?: why | how | where | what ) \b
    | \b (?: he | she | it | they ) \s+ (?: came | comes ) \s+ from \b
    | \b was \s+ (?: created | made | born | forged | sent | built | placed ) \s+
        (?: by | of | from | in | to ) \b
    | \b originated \s+ (?: in | from | as ) \b
    | \b the \s+ answer \s+ (?: to | is ) \b
    # naming and counting. GAME_SPEC 3.16 item 4 forbids all three verbs for
    # the-others: "Never name, count, or show them."
    | \b (?: was | were | is | are ) \s+ (?: called | named | numbered ) \b
    | \b their \s+ names? \s+ (?: was | were | is | are ) \b
    | \b there \s+ (?: was | were ) \s+ (?: exactly \s+ )? \w+ \s+ of \s+ them \b
    # the plainest way to answer a "why" question. Safe only because of
    # PROXIMITY below: measured, an unproximate "because" costs false positives
    # (one long GAME_SPEC line pairs a Shiro cameo with an unrelated
    # "Because you were worth saving"), a proximate one costs none.
    | \b which \s+ is \s+ why \b | \b for \s+ that \s+ reason \b
    # A causal clause is only safe when the pattern carries its OWN context. Bare `because`
    # was removed: measured, it false-positived on ordinary shipped prose ('Shiro appears at
    # the Hub because...'). These two pin it to a crossing/origin verb, so they cannot.
    | \b (?: came | come | comes | crossed | stumbled | fell ) \s+ (?: through | into ) \b
        [^.!?]{0,45} \b (?: because | so \s+ that ) \b
    | \b (?: was | were ) \s+ (?: taken | pulled | drawn | sent ) \s+ (?: through | into | by ) \b )""")

# The subject and the resolution must be NEAR EACH OTHER, not merely on the same
# line. Content lines here run to 2,000+ characters; without this a subject in
# clause one and a declarative in clause twelve read as an answer. Measured over
# ~75k lines of real content: 80 costs zero true positives and removes a whole
# class of false ones.
PROXIMITY = 80

# Wonder is a feature. A hedged or interrogative line is canon-legal and passes.
HEDGE = re.compile(r"""(?ix)
  \b(?: some \s+ say | they \s+ say | it \s+ is \s+ said | it's \s+ said
      | perhaps | maybe | might | may \s+ have | could \s+ have | would \s+ have
      | rumou?r | theor (?: y | ies | ise | ize | ised | ized | etical )
      | legend \s+ (?: says | has \s+ it ) | claims? | claimed
      | believ (?: e | es | ed ) | supposedly | allegedly | apparently
      | seems? | seemed | appears? \s+ to
      | no \s? (?: one | body ) \s+ knows | who \s+ knows | none \s+ know
      | never \s+ (?: knew | learned | learnt | found \s+ out | said | answered )
      | unknown | unproven | unknowable | unanswered | unexplained
      # NOTE: 'unnamed' is deliberately NOT a hedge. It is part of a tier-3 subject's own
      # canonical name ('the unnamed others of the Formless Era'), so hedging on it made that
      # entire mystery unenforceable — every line about it self-suppressed. Do not re-add it.
      | not \s+ (?: known | proven | recorded ) | no \s+ record
      | i \s+ (?: don'?t | do \s+ not | cannot | can'?t ) \s+ (?: know | say | tell )
      | we \s+ (?: don'?t | do \s+ not ) \s+ know
      | could \s+ not \s+ say | cannot \s+ say | will \s+ not \s+ pretend
      | sheds \s+ no \s+ light | says \s+ nothing )\b""")

# A question is legal. Allow the trailing JSON/markdown punctuation a line carries.
QUESTION = re.compile(r"""\?["'”]?\s*[,\]\}]*\s*$""")

# Mandatory-reason escape hatch. PER LINE ONLY, deliberately: the sibling retired-terms lint also
# offers a whole-FILE waiver, because whole files there (an owner-frozen build record, an append-only
# wave log) legitimately name a retired term on every page. Nothing needs that here — the two known
# findings across both MMO repos are a single line each, and one of them is the generated twin of the
# other. An escape hatch nobody exercises is worse than none: it rots untested and is then reached for
# under deadline. Add one when a real file needs it, not before.
ALLOW = re.compile(r"canon-allow:\s*(\S[^\"']*)", re.I)

# "Never quest-marked": the structural half of the Tier-3 rule. Matched against
# JSON KEY NAMES only, never against free prose — that is what keeps A6 exact.
MARKER_STEM = re.compile(r"(?i)^(?:quest|objective|codex|collectible|completion|"
                         r"achievement|journal|marker|tracker|unlock|reveal|"
                         r"resolution|answer)[a-z0-9]*$")
# "question" is not a quest marker; every mystery entry has one by design.
NOT_MARKER = re.compile(r"(?i)^questions?$")
JSON_KEY = re.compile(r'"([A-Za-z0-9_\-]{1,48})"\s*:')


def is_marker_key(key):
    """True for questMarker, codexEntry, boss_completion, objectiveId, ...

    Split on '_' as well as testing whole, so snake_case and camelCase both land.
    """
    for part in [key] + re.split(r"[_\-]+", key):
        if NOT_MARKER.match(part):
            continue
        if MARKER_STEM.match(part):
            return True
    return False



SPEAKER_SHIRO = re.compile(r"""(?i)["']speaker["']\s*:\s*["']\s*shiro\s*["']""")


class Fail(Exception):
    pass


# --------------------------------------------------------------------------- io

def read_json(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError) as exc:
        raise Fail("cannot read %s: %s" % (os.path.relpath(path, REPO), exc))


def canon_frozen_questions(path):
    """Parse the six questions out of CANON.md 4.1 rather than hardcoding them.

    Hardcoding is the failure mode this whole script exists to prevent: a frozen
    list copied into a checker drifts silently the day the source moves.
    """
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as exc:
        raise Fail("cannot read CANON.md: %s" % exc)
    m = re.search(r"^###\s*4\.1\b.*$", text, re.M)
    if not m:
        raise Fail("CANON.md has no '### 4.1' section — the frozen list moved; "
                   "fix this parser rather than hardcoding the questions")
    body = text[m.end():]
    nxt = re.search(r"^###\s", body, re.M)
    if nxt:
        body = body[:nxt.start()]
    out = []
    for line in body.splitlines():
        item = re.match(r"\s*(\d+)\.\s+\*\*(.+?)\*\*", line)
        if item:
            out.append(item.group(2).strip())
    return out


# ------------------------------------------------------------------- structural

def compile_terms(terms, where, errs):
    """A term is a literal phrase, or a regex when prefixed 're:'."""
    pats = []
    for raw in terms:
        if not isinstance(raw, str) or not raw.strip():
            errs.append("%s: term %r is not a non-empty string" % (where, raw))
            continue
        if raw.startswith("re:"):
            src = raw[3:]
            try:
                pats.append(re.compile(src, re.I))
            except re.error as exc:
                errs.append("%s: term %r does not compile: %s" % (where, raw, exc))
        else:
            pats.append(re.compile(r"\b" + re.escape(raw) + r"\b", re.I))
    return pats


def structural(doc, errs):
    """Returns {id: {'never': [pat], 'may': [pat], 'says': [str]}} for tier 3."""
    defs = doc.get("tierDefinitions")
    if not isinstance(defs, dict):                                          # A1
        errs.append("prophecies/mysteries.json: no top-level tierDefinitions block "
                    "— transcribe UNIVERSE_DEPTH_SPEC.md T1")
        declared = set()
    else:
        declared = {t.get("tier") for t in defs.get("tiers", [])
                    if isinstance(t, dict)}
        missing = {1, 2, 3} - declared
        if missing:
            errs.append("prophecies/mysteries.json: tierDefinitions does not define "
                        "tier(s) %s" % ", ".join(str(t) for t in sorted(missing)))

    entries = ([("prophecies", e) for e in doc.get("prophecies", [])] +
               [("mysteries", e) for e in doc.get("mysteries", [])])
    if not entries:
        errs.append("prophecies/mysteries.json: no prophecies[] or mysteries[] entries")

    tier3, claimed = {}, {}
    for arr, entry in entries:
        eid = entry.get("id", "<no id>")
        where = "prophecies/mysteries.json: %s[%s]" % (arr, eid)
        tier = entry.get("tier")
        if tier not in (1, 2, 3):                                           # A2
            errs.append("%s declares tier=%r, expected 1, 2 or 3 — every entry must "
                        "be tiered or the law only covers what someone remembered"
                        % (where, tier))
            continue
        if tier != 3:
            if entry.get("neverAnswerTerms"):
                errs.append("%s is tier %d but declares neverAnswerTerms — those are "
                            "tier-3 machinery; either the tier or the terms is wrong"
                            % (where, tier))
            if entry.get("canonQuestion"):
                errs.append("%s is tier %d but claims a CANON 4.1 question (%r); 4.1 "
                            "questions are permanently unknowable and must be tier 3"
                            % (where, tier, entry["canonQuestion"]))
            continue

        never = entry.get("neverAnswerTerms") or []
        if not never:                                                       # A3
            errs.append("%s is tier 3 with no neverAnswerTerms[] — an unkeyed tier-3 "
                        "entry is an unenforceable one" % where)
        if not (entry.get("tierSource") or "").strip():
            errs.append("%s is tier 3 with no tierSource — cite CANON.md 4.1 or "
                        "GAME_SPEC.md 3.16 so the rating can be audited" % where)
        if not entry.get("mayAnswer"):
            errs.append("%s is tier 3 with no mayAnswer[] — say what content IS still "
                        "allowed to state, or this lint over-blocks legal canon and "
                        "gets switched off" % where)
        tier3[eid] = {
            "never": compile_terms(never, where + ".neverAnswerTerms", errs),
            "may": compile_terms(entry.get("mayAnswerTerms") or [],
                                 where + ".mayAnswerTerms", errs),
            "says": [s for s in (entry.get("mayAnswer") or []) if isinstance(s, str)],
        }
        cq = entry.get("canonQuestion")
        if cq:
            claimed.setdefault(cq, []).append(eid)

    frozen = canon_frozen_questions(CANON)                                  # A4
    if len(frozen) != 6:
        errs.append("CANON.md 4.1 is FROZEN at six questions but %d parsed — either "
                    "the frozen section changed (which needs an owner ruling) or this "
                    "parser broke. Parsed: %s" % (len(frozen), frozen))
    for question in frozen:
        owners = claimed.get(question, [])
        if not owners:
            errs.append("CANON.md 4.1 (FROZEN) keeps %r dark, but no tier-3 entry in "
                        "prophecies/mysteries.json claims it via \"canonQuestion\" — "
                        "the lint would silently enforce only part of the law" % question)
        elif len(owners) > 1:
            errs.append("CANON.md 4.1 question %r is claimed by %d entries (%s); it "
                        "must be claimed by exactly one" % (question, len(owners),
                                                            ", ".join(owners)))
    for question, owners in claimed.items():
        if question not in frozen:
            errs.append("%s claims canonQuestion %r, which is not one of the six in "
                        "CANON.md 4.1 — fix the quotation or drop the field"
                        % (", ".join(owners), question))

    for eid, why in DEFERRED_TIER3.items():                                 # A5
        if eid not in tier3:
            errs.append("'%s' is tier 3 by %s, but is not tier 3 here" % (eid, why))
    return tier3


# ---------------------------------------------------------------------- content

def gather(roots):
    files, missing = [], []
    for root in roots:
        if os.path.isfile(root):
            files.append(root)
        elif os.path.isdir(root):
            files += [p for p in glob.glob(os.path.join(root, "**", "*"), recursive=True)
                      if os.path.isfile(p)
                      and p.rsplit(".", 1)[-1].lower() in SCAN_EXTS
                      and not any(s in p.replace(os.sep, "/") + "/" for s in SKIP_DIRS)]
        else:
            missing.append(root)
    if missing:
        # A typo'd root used to print a note to stderr and let the run go green. A gate pointed at
        # nothing is worse than no gate: the badge keeps saying the canon is checked.
        raise Fail("content root(s) do not exist: %s" % ", ".join(missing))
    return sorted(set(os.path.abspath(p) for p in files))


def show(path):
    """Shortest readable label. REPO first (this repo's own content), then the working directory,
    which is what makes a finding in a SIBLING repo print as docs/STORYLINE.md rather than as an
    unreadable /home/runner/work/... absolute path."""
    for base in (REPO, os.getcwd()):
        rel = os.path.relpath(path, base)
        if not rel.startswith(".."):
            return rel
    return path


def scan(roots, tier3, errs):
    stats = {"files": 0, "lines": 0, "allowed": 0, "subject_hits": 0}
    for path in gather(roots):
        governance = os.path.realpath(path) in GOVERNANCE_FILES
        try:
            with open(path, encoding="utf-8") as fh:
                lines = fh.read().splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        stats["files"] += 1
        stats["lines"] += len(lines)
        rel = show(path)
        for n, line in enumerate(lines, 1):
            allow = ALLOW.search(line)
            if allow:
                if len(allow.group(1).strip()) < 6:
                    errs.append("%s:%d: canon-allow needs a real reason (>= 6 chars) "
                                "— an unexplained waiver is a disabled lint" % (rel, n))
                stats["allowed"] += 1
                continue
            if governance:
                continue
            if SPEAKER_SHIRO.search(line):                                   # A7
                errs.append("%s:%d: Shiro is seen, never spoken to (CANON.md 4.1; "
                            "GAME_SPEC.md 3.16 item 6) — no \"speaker\": \"SHIRO\""
                            % (rel, n))
            keys = [k for k in JSON_KEY.findall(line) if is_marker_key(k)]
            # shiro_origin_found / shiro-origin are the same subject as "Shiro".
            keyline = re.sub(r"[_\-]+", " ", line) if keys else line
            for eid, spec in sorted(tier3.items()):
                if keys:                                                     # A6
                    hit = next((p.pattern for p in spec["never"]
                                if p.search(keyline)), None)
                    if hit:
                        stats["subject_hits"] += 1
                        errs.append(
                            "%s:%d: tier-3 '%s' is hung on a quest-marker/codex key "
                            "(%s) — tier 3 is never quest-marked, atmospheric only\n"
                            "      %s" % (rel, n, eid, ", ".join(keys),
                                          line.strip()[:160]))
                        continue
                subj = next((m for m in (p.search(line) for p in spec["never"]) if m),
                            None)
                if not subj:
                    continue
                stats["subject_hits"] += 1
                if any(p.search(line) for p in spec["may"]):
                    continue
                if HEDGE.search(line) or QUESTION.search(line.rstrip()):
                    continue
                res = next((m for m in RESOLUTION.finditer(line)               # B
                            if abs(m.start() - subj.start()) <= PROXIMITY), None)
                if res:
                    says = "\n".join("        may say: " + s for s in spec["says"])
                    errs.append(
                        "%s:%d: tier-3 '%s' looks ANSWERED — subject %r and a "
                        "declarative %r sit %d characters apart, and the line is not "
                        "hedged.\n      %s\n%s\n      if this is canon-legal, append  "
                        "canon-allow: <reason>"
                        % (rel, n, eid, subj.group(0)[:60], res.group(0)[:40],
                           abs(res.start() - subj.start()), line.strip()[:160], says))
    return stats


# ------------------------------------------------------------------------- main

def main(argv):
    show_stats = "--stats" in argv
    roots = [a for a in argv if not a.startswith("--")] or DEFAULT_ROOTS
    errs = []
    try:
        doc = read_json(REGISTER)
        tier3 = structural(doc, errs)
        stats = scan(roots, tier3, errs) if tier3 else {"files": 0, "lines": 0,
                                                        "allowed": 0, "subject_hits": 0}
    except Fail as exc:
        print("TIER-3 MYSTERY LAW CANNOT BE CHECKED: %s" % exc)
        return 2
    if tier3 and stats["files"] == 0:
        print("TIER-3 MYSTERY LAW CANNOT BE CHECKED: 0 files scanned under %s"
              % ", ".join(roots))
        print("  A lint that scans nothing reports green. Fix the roots; never let this pass.")
        return 2
    if errs:
        print("TIER-3 MYSTERY LAW VIOLATED — CANON.md 4.1 (FROZEN) / GAME_SPEC.md 3.16:")
        for e in errs:
            print("  " + e)
        print("\n  %d finding(s). Tier 3 is never answered, never quest-marked, "
              "atmospheric only." % len(errs))
        return 1
    print("ok: %d tier-3 mysteries stay dark across %d content files (%d lines, "
          "%d subject mentions, %d canon-allow waivers)"
          % (len(tier3), stats["files"], stats["lines"], stats["subject_hits"],
             stats["allowed"]))
    if show_stats:
        for eid in sorted(tier3):
            print("   - %s: %d never-terms, %d may-terms"
                  % (eid, len(tier3[eid]["never"]), len(tier3[eid]["may"])))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
