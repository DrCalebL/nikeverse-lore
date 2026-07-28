# Nikeverse Lore Bible — CLAUDE.md

Notes for AI assistants working in this repo. **Auto-loaded every session — keep it lean.**
**DURABLE FACTS ONLY.** No commit SHAs, no dates, no status narration, no findings lists. Four
destinations, and putting a thing in the wrong one is how this file bloats: a **rule** goes here · a
**resolution** to a canon question goes in `CHANGELOG.md` · a **cross-repo divergence** goes in
`GAME_DELTAS.md` · **per-wave history** goes in `docs/progress-log.md` and **open defects** in
`docs/KNOWN_ISSUES.md` — both append-only and **NOT auto-loaded**, grep them.
Edit this file only when a *rule* changes.

## What this is

The canon bible for the Nikeverse: cosmology, entities, timeline, language, prophecies and mysteries, as
**structured JSON** plus `CANON.md` (the settled centre) and `GAME_DELTAS.md` (the honest margin — every
known place this repo and a shipped game disagree, and which side is right).

**This repo is NOT a runtime dependency of any game.** Nothing fetches it. It is the reference the games
are checked against.

## 🔗 THE THREE-WAY CANON MATCH — owner rule, 2026-07-28

**These three must always tell the SAME STORY. A ruling that lands in one and not the others is not landed.**

| # | Artifact | Repo |
|---|---|---|
| 1 | `docs/GAME_SPEC.md` — the game design | `Nikeverse-mmo-rpg-from-scratch` (**the build**) |
| 2 | `docs/TESANA_BUILD_PROMPT.md` — the tesana.ai build spec | `nikeverse-mmo-rpg` (the prior build) |
| 3 | the lore bible (JSON + `CANON.md`) | `nikeverse-lore` |

**Two mechanisms, because the media genuinely differ — this is not a loophole, it is what makes the rule
enforceable instead of aspirational.**

1. **① ↔ ② is BYTE-IDENTICAL below the fence, and is machine-checked.**
   ```sh
   SPEC=../Nikeverse-mmo-rpg-from-scratch/docs/GAME_SPEC.md
   N=$(grep -n '^# NIKEVERSE — THE TESANA.AI BUILD PROMPT' "$SPEC" | head -1 | cut -d: -f1)
   diff <(tail -n +"$N" "$SPEC") ../nikeverse-mmo-rpg/docs/TESANA_BUILD_PROMPT.md && echo identical
   ```
   **NEVER edit `TESANA_BUILD_PROMPT.md` directly.** Edit `GAME_SPEC.md`, then regenerate the twin with
   `tail -n +N` and re-run the diff. The offset is DERIVED, never pinned — the fence grows.
2. **① ↔ ③ is ASSERTION-CHECKED, not byte-identical.** One side is JSON facts, the other is design prose;
   they can never be the same bytes. What must match is every *claim*: names, numbers, counts, gates,
   titles, motivations, taxonomy, retired terms. `nikeverse-lore/GAME_DELTAS.md` is the register of known
   divergences and `Nikeverse-mmo-rpg-from-scratch/docs/CANON_MAP.md` is the cross-repo ruling doc — **open them before resolving any
   disagreement.**

**THE WORKFLOW RULE — this is the part that actually prevents the drift:**

> **A canon change is not DONE until all three carry it, in the SAME session.** Never land one and defer
> the rest. That deferral *is* the divergence: one owner ruling becoming separate commits in separate
> repositories landing on separate days is the exact mechanism that produced the whole `GAME_DELTAS`
> register, and it cost five and a half weeks once already.

**Direction of truth when they disagree** (do not guess — this order is load-bearing):
1. **`nikeverse-discord-game` is the SHIPPED GROUND TRUTH for anything a player can see.** It has beaten
   the design documents on essentially every contested point. Go to the data before you trust a document.
2. **`Nikeverse-mmo-rpg-from-scratch/docs/CANON_MAP.md`** for anything already locked.
3. For cosmology, entities, numbers, language and timeline → the **lore** is upstream.
4. For regions and their contents → much of the lore was transcribed *from* the Discord game and then
   drifted, so prefer the game.

---

## 🛑 NEVER

1. **Never push to `main`; never open a PR unless asked.** Branch = `claude/<name>` from the session brief.
2. **Never put the model identifier** in commits, code, or docs.
3. **Never revive a retired term.** `keth'vor` → **`Eth'kara`** (the Pattern) vs **`Keth'nor`**
   (corruption) · "Reacher" → **the Collector** · "Sasuke" → **`Tōga`** · "Unraveler" RETIRED.
   `scripts/check-canon-terms.sh` is word-boundary matched and **`-w` is required, not optional** — a bare
   substring search for "reacher" matches "t-reacher-ous", a real false positive in the sibling repo.
   **The carve-out is deliberate:** `Nol'meth` is glossed "The Unraveling" and is CORRECT.
4. **Never sweep a retired term out of a file that names it in order to GOVERN it.** `CANON.md`,
   `CHANGELOG.md` and `CANON_MAP.md` are excluded for exactly this reason. A term's retirement record is
   the thing that explains the rule; deleting it leaves the rule unexplained.
5. **Never resolve a Tier-3 mystery.** `CANON.md` §4.1 is FROZEN at six dark questions (+ `lost-singular`
   by owner deferral). `scripts/check-mystery-tiers.py` enforces it. **A Tier-3 entry with no
   `neverAnswerTerms` is an UNENFORCEABLE entry** — never add one without them.
6. **Never introduce a new word of power without adding it to** `languages/first-tongue/dictionary.json`.

## ✅ Verify — all four before calling a change done

```sh
sh scripts/check-canon-terms.sh                 # retired terms
python3 scripts/check-mystery-tiers.py          # Tier-3 stays dark
python3 -c "import json,glob;[json.load(open(f)) for f in glob.glob('**/*.json',recursive=True)];print('ok')"
# and the CI jobs in .github/workflows/canon.yml: dimensions-agree, level-bands, legendary-arithmetic
```

## Gotchas

- **`better-sqlite3` is NOT installed in web sessions** — read the Discord game's
  `data-seed/nikeverse.db` with `python3`'s `sqlite3`. Ground truth: **436 creatures (292 Nikes + 144
  hostiles), 658 moves, 138 traits, 117 relics, 25 raid bosses.**
- **Free-order level bands are CO-BANDED and must overlap** — Frostfall ⇄ Grand Arena 31–55, Neon ⇄ Void
  71–95, each split into an anchor tier and a Deep tier. Non-overlapping bands made whichever sibling you
  played second a wall. `level-bands` CI enforces it; do not "tidy" them back apart.
- **The Deep tier ("Act 2") opens PER-REGION** on that region's own anchor falling — never on campaign
  completion. The three anchorless regions read their own completion flag instead.
- **The story corpus is NOT here.** It lives in `Nikeverse-mmo-rpg-from-scratch/docs/story/`.

## Doc map

`CANON.md` — the settled centre (§4.1 = the FROZEN dark questions) · `GAME_DELTAS.md` — the divergence
register (this repo vs a shipped game, with a ruling each) · `CHANGELOG.md` — resolutions ·
`CONTRIBUTING.md` — the source-authority tiers · `MASTER_LORE_PROPOSAL_FINAL.md` — the founding
synthesis (**provenance, not a live spec** — superseded wherever `CANON.md` speaks)
**Not auto-loaded — grep these, don't load them:** `docs/progress-log.md` (append-per-wave; grep by wave
number for "why is this like this") · `docs/KNOWN_ISSUES.md` (open defects and accepted deferrals)
