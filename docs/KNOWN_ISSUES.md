# Lore bible — known issues & accepted deferrals

**NOT auto-loaded.** Open defects and deliberate deferrals, each with a file (and line where it helps).
Two neighbours, and the boundary matters:

- **`GAME_DELTAS.md`** — cross-repo *disagreements* (this repo vs a shipped game), each with a ruling on
  which side is right. That register is the honest margin and stays where it is.
- **This file** — defects and deferrals *internal to this repo*: gaps, unenforceable gates, things a lint
  cannot see, and decisions deliberately left open.

Close an entry by deleting it and, if it produced a rule, putting the rule in `CLAUDE.md`.

---

## Open

### 1. `lost-singular` is Tier-3 by owner deferral, not by ruling
`prophecies/mysteries.json` · `CANON.md` §4.1

The six frozen dark questions are ratified. `lost-singular` sits with them because the owner deferred the
call, not because it was ruled Tier-3. If it is ever ruled Tier-2 it needs `neverAnswerTerms` removed and
the lint's expected-count updated in the same commit, or `check-mystery-tiers.py` will start failing on
legal prose.

### 2. The mystery lint cannot see paraphrase
`scripts/check-mystery-tiers.py`

It matches `neverAnswerTerms` — a *lexical* gate. A doc that answers a Tier-3 question in fresh wording
that shares no term with the entry passes clean. Measured 7/7 recall against the corpora as they stand
today, which is a statement about today's prose, not a guarantee. Treat a green run as "no known
resolution", never as "no resolution".

### 3. No lint covers the `_freed` softlock law
`CLAUDE.md` NEVER · Wave 4

The law (gate on `<anchor>_defeated`, never `_freed`) is enforced by review only. The Discord game is
where it would actually bite, and this repo has no visibility into that repo's JSON. Grep-checked by hand
each time it comes up.

### 4. The three-way match has no CI job on the ①↔③ leg
`CLAUDE.md` "THE THREE-WAY CANON MATCH"

The ①↔② leg is machine-checked (byte-identical below the fence). The ①↔③ leg is assertion-checked by a
human reading both sides, because one side is JSON facts and the other is design prose. The existing CI
gates (`dimensions-agree`, `level-bands`, `legendary-arithmetic`) cover three specific claims; everything
else on that leg is unenforced. Widening it means one CI job per claim — worth doing for any claim that
has drifted twice.

## Accepted deferrals

### A. The Discord game's global Act-2 gate
Register row W5 · owner call

The shipped game gates Act 2 globally; the lore describes a per-region gate. **Permanent and accepted** —
neither side changes. Do not "fix" this; do not re-open it.

### B. `MASTER_LORE_PROPOSAL_FINAL.md` is a founding synthesis, not a live spec
994 lines, and the largest single file here. It is the historical proposal the bible was built from. It
is superseded in every place `CANON.md` speaks, and it is kept for provenance. Do not cite it against
`CANON.md`.
