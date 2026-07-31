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
0. **THE OWNER'S RULING IS THE FINAL TRUTH — Tier 0, above everything, including the comics.**
   *"My say is the final truth. And it will be my vision."* The comics (`comic-books/`) are the highest
   **source** in the project and outrank every doc, every JSON file and both games — but they are
   **evidence, not the verdict.** A comic/canon collision is a **question put to the owner**: quote both
   sides, state the blast radius, recommend, then wait. Never rewrite ratified canon on a comic's
   authority alone — and never treat an unruled comic detail as canon either.
1. **`nikeverse-discord-game` is the FACTUAL RECORD of what shipped — NOT a lore authority.**
   **⛔ SCOPED, owner 2026-07-29:** *"Don't follow discord game lore. It's the weakest lore of the bunch."*
   - **Still authoritative for WHAT EXISTS:** rosters, creature/move/trait data, flags, gates, region
     contents, level bands, mechanics. It is a running product; go to the data before you trust a document
     about what is in the game. Every `GAME_DELTAS` ruling made on that basis stands.
   - **NOT authoritative for COSMOLOGY, CHARACTERISATION, or tone** — above all **Nolem**, whom the owner
     explicitly dislikes as written there. For those, `comic-books/` (Tier 1) and ratified `CANON.md`
     outrank it, and a weak shipped line is a thing to *outgrow*, not to propagate.
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
   the thing that explains the rule; deleting it leaves the rule unexplained. **The same carve-out now
   covers *spare* / *extra*** (banned as nouns for a soul, §1.2.2): the governing docs quote the owner's
   own *"store all extras in the Sanctuary"* verbatim, so a future lint on those words must exclude them
   exactly as it excludes the retired terms.
5. **Never resolve a Tier-3 mystery.** `CANON.md` §4.1 is FROZEN at six dark questions (+ `lost-singular`
   by owner deferral). `scripts/check-mystery-tiers.py` enforces it. **A Tier-3 entry with no
   `neverAnswerTerms` is an UNENFORCEABLE entry** — never add one without them.
6. **Never introduce a new word of power without adding it to** `languages/first-tongue/dictionary.json`.
7. **Never render a second life as a copy.** **ONE SOUL, MANY LIVES** (owner 2026-07-30, `CANON.md` §1.2.2):
   repeat bonding is unlimited and permanent, and a fragment is not divided by living more than one life. Only
   the **form** is counted (Log, Pattern); the **life** is counted by nothing. So: no stacks, no "×3", no
   *spare*/*extra*, per-life names and natures always — and **never explain the topology in-world** (§1.2.1's
   ban binds this too). *A census is not a rescue.*
8. **Never treat SHIRO as a precedent, and never state a count of FRAGMENTS.** Two owner rulings, 2026-07-30.
   **Shiro** is out-of-world provenance — *"a crypto token that I didn't want to promote in my lore"* — phased
   out, his function carried by Charles AI. He is **not a Nike, did not evolve, and is never an example of
   transformation or growth**; Book 1's *"unevolved cat"* is a quadruped pet and must never touch the bipedal
   law (`CANON.md` §3.1). **THE SETTLING** (§1.2.3): evolution keeps the transformation, each shape gets its
   own slot, **a fragment may wake into more than one form**, and *"a unique individual and a unique kind"* is
   **not a bijection** — a form is a SOMEONE, always; whether two forms are the same someone is a question the
   game never asks. **THE BOND IS THE WITNESS, NEVER THE CAUSE** — the shipped chains include a CORRUPTION ARC,
   so a causal reading blames the player for a devil. A settling is **neutral**, and it **blooms**.
9. **⛔ NO LEGENDARY'S STORY IS RATIFIED — owner ruling 2026-07-31.** *"All legendary's stories aren't
   ratified — especially those without a clear link to the real world."* `corruptionTheme`, `corruptionReason`,
   `gameNarrative`, `quote_game` and every encounter shape in `characters/legendary-nikes/index.json` are
   **drafts the build may reshape to fit mechanics**, and the audit runs **last**, after the mechanics settle.
   **Freest: the ones with no real person behind the name.** Ask first on real-person names and on the three
   with a documented origin (**Melon** → the crypto trader, `CANON.md` §6 · **Nolem** = MELON reversed ·
   **Retnuhxed** = DEXHUNTER reversed). **Structural load is a separate axis** — re-home a load-bearing line
   before rewriting whoever carries it. ⚠ **`"Unknown"` IS A REAL ANSWER, NOT A GAP TO FILL:** 4 of 27 are
   marked Unknown (Professor, Corey Hort, Guthix, Jedi) and the build repo authored Jedi a theme, a Lie and a
   full non-combat encounter over the top of his, then cited it back as canon. Full ruling and the tiering:
   `Nikeverse-mmo-rpg-from-scratch/docs/KNOWN_ISSUES.md` Q19.
10. **Never blur the fallen-side taxonomy.** **Corrupted Nike = REVERSIBLE · Retnuhxed = past REACHING (never
    soul-destroyed — §2.1's warm soul-mote still releases) · Harbinger = a fallen COLLECTOR HUMAN, never a Nike and
    never "corrupted" (`factions/index.json`: *"Not corrupted—converted"*).** `scripts/check-fallen-taxonomy.py`
    enforces it by proximity, and governing documents are excluded for the same reason as the retired-terms lint.
    Reserve *"too far gone"* / *"so far gone"* for **Retnuhxed only** — it is now the definitional phrase.

## ✅ Verify — all five before calling a change done

```sh
sh scripts/check-canon-terms.sh                 # retired terms
python3 scripts/check-fallen-taxonomy.py        # Corrupted vs Retnuhxed vs Harbinger
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

**`comic-books/`** — **Tier-1 source material** (`book-01/` = *Nike the Pig: Book 1*, PDF + verbatim
`script.md`). Its README carries the Tier-0 authority rule and the dialogue/art-direction/author-note
evidence split — **read it before citing a comic line** ·
`CANON.md` — the settled centre (§4.1 = the FROZEN dark questions) · **`THE_5555.md`** — the canon
*history* of the number (six readings in ten months, what is still open; **HISTORY, not canon —
`CANON.md` §1.2 rules**) · `GAME_DELTAS.md` — the divergence
register (this repo vs a shipped game, with a ruling each) · `CHANGELOG.md` — resolutions ·
`CONTRIBUTING.md` — the source-authority tiers · `MASTER_LORE_PROPOSAL_FINAL.md` — the founding
synthesis (**provenance, not a live spec** — superseded wherever `CANON.md` speaks)
**Not auto-loaded — grep these, don't load them:** `docs/progress-log.md` (append-per-wave; grep by wave
number for "why is this like this") · `docs/KNOWN_ISSUES.md` (open defects and accepted deferrals)
