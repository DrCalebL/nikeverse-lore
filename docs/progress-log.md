# Lore bible — progress log

**APPEND-ONLY. NOT auto-loaded — grep it by wave number.** This file exists so `CLAUDE.md` can stay
lean: everything here is *history*, not a rule. If a wave produced a durable **rule**, that rule belongs
in `CLAUDE.md` and this entry just says so. If it produced a **resolution** to a canon question, that
belongs in `CHANGELOG.md`. If it left something **open**, that belongs in `docs/KNOWN_ISSUES.md` or
`GAME_DELTAS.md`.

One entry per wave. Newest at the bottom. Keep entries short — what changed, why, and where the rule
landed. No commit SHAs (they churn under rebase), no "✅ done" narration, no findings lists.

---

## Wave 1 — the divergence register is built

Established `GAME_DELTAS.md` as the honest margin: every known place this repo and a shipped game
disagree, with a ruling on which side is right. Established the source-authority tiers in
`CONTRIBUTING.md`.

**Durable rule that came out of it →** `CLAUDE.md` "Direction of truth": the Discord game is the
shipped ground truth for anything a player can see. It has beaten the design documents on essentially
every contested point.

## Wave 2 — retired terms, and the lint that enforces them

`keth'vor` → `Eth'kara` / `Keth'nor` · "Reacher" → the Collector · "Sasuke" → `Tōga` · "Unraveler"
retired. `scripts/check-canon-terms.sh` armed.

**Two rules came out of it, both in `CLAUDE.md`:** the lint must be word-boundary matched (`-w` is
required — a bare substring search for "reacher" matches "t-reacher-ous", a real false positive in the
sibling repo); and `Nol'meth` glossed "The Unraveling" is a deliberate carve-out, not a miss.

## Wave 3 — the Harbinger/Corrupted-Nike taxonomy

A fallen Collector *human* is a **Harbinger**; a fallen **Nike** is a **Corrupted Nike** (→ a
**Retnuhxed** if beyond saving). Two Harbingers must align, not one — Vane and Slate.

## Wave 4 — the `_freed` softlock law

Two gates corrected. Downstream content gates on `<anchor>_defeated`, **never** on `_freed` — gating on
`_freed` softlocks the KO path, which is a supported outcome, not a failure state.

## Wave 5 — the Deep tier, and an accepted permanent divergence

Aligned the Deep tier to the game's in-region, post-anchor gate: the Deep tier opens **per region** on
that region's own anchor falling, never on campaign completion; the three anchorless regions read their
own completion flag instead.

**Owner call, recorded as closed:** the shipped Discord game keeps its *global* Act-2 gate. This is a
permanent, accepted divergence — the lore describes the intended design, the game ships what it ships,
and neither is going to be changed to match the other. Register row W5.

## Wave 6 — co-banding (L4), and four register rows closed

Free-order level bands are **co-banded and must overlap** — Frostfall ⇄ Grand Arena 31–55, Neon ⇄ Void
71–95, each split into an anchor tier and a Deep tier. Non-overlapping bands made whichever sibling you
played second a wall. Closed W6, W7, E5, E6.

**Rule →** `CLAUDE.md` Gotchas, plus a `level-bands` CI gate so it cannot be "tidied" back apart.

## Wave 7 — the Dimension Eater enters canon

W3 resolved in the Discord game's favour: the Dimension Eater is adopted rather than written out, as a
severed organ of Nolem. Authored lore, not a stub.

## Wave 8 — the mysteries are tiered and the Tier-3 lint is armed

`prophecies/mysteries.json` gains `tierDefinitions` and a tier on every entry. Two frozen questions that
had gone missing were restored (`the-others`, `cthulhu-motive`). `scripts/check-mystery-tiers.py`
enforces that Tier-3 stays dark. Three CI gates added: `dimensions-agree`, `level-bands`,
`legendary-arithmetic`.

**The expensive lesson, and it is now a rule in `CLAUDE.md`:** the lint first shipped at **3/7 recall**,
then — after widening — fired on **7/7 legal canon prose**. Root causes were bare subject terms
(`shiro`, `void between`) and a bare `because`; worse, the hedge pattern matched **"unnamed"**, which is
part of a Tier-3 subject's own canonical name, making that mystery unenforceable *by construction*.
Final measured: 7/7 recall, 0 false positives across four corpora (355 shipped files).
**A gate that passes without checking anything is worse than no gate.**

## Wave 9 — the story corpus leaves this repo

All 19 story/canon docs moved to `Nikeverse-mmo-rpg-from-scratch/docs/` and `…/docs/story/`. This repo
keeps the *bible* (cosmology, entities, timeline, language, prophecies); the *corpus* (spine, arcs,
region specs, campaign) lives with the build.

**Rule →** never fork a second live copy of a ratified spine. Two live copies is the exact latency
defect that produced this whole divergence register.

## Wave 10 — the three-way canon match rule

Owner rule: `GAME_SPEC.md` (the build), `TESANA_BUILD_PROMPT.md` (the tesana.ai spec) and this lore
bible must always tell the same story, enforced by two different mechanisms because the media differ.
`CLAUDE.md` created for this repo (it had never had one) and the rule added to all three repos'
`CLAUDE.md`.

**The rule that actually prevents the drift →** a canon change is not DONE until all three carry it, in
the **same session**.

## Wave 11 — context-bloat pass

This file and `docs/KNOWN_ISSUES.md` created, matching the sibling repos' pattern: `CLAUDE.md` holds
durable rules only and is auto-loaded; per-wave history and open defects live here and are **not**.

## Wave 12 — the Circle, and the reach phase

Two owner-directed design waves in the build repo (`Nikeverse-mmo-rpg-from-scratch/docs/CIRCLE_DESIGN.md`)
produced canon claims this repo must carry. Applied here in the same session, per the three-way rule.

**What landed on this side:**

- **`CANON.md` §1.2 precisified:** the 5,555 counts **souls held**, never **threads held**. The section said
  "5,555 bonds exist at the same moment", which stopped being the same count the moment one soul could be
  reached by many Collectors at once. A soul reached by ten is **one** re-anchored, not ten — forced, because
  otherwise a realm could read "the Pattern is whole" while five thousand souls were still dark, and a meter
  that lies about wholeness is the False Box.
- **`CANON.md` §1.2.1 added:** one soul, many threads. The Pattern counts connections, not creatures. A Nike
  is never copied. Never explain the topology.
- **`dictionary.json`: `Eth'kara` gains a usage note.** `kara` is chain-as-*linkage* — a chain of hands, a
  chain of custody — never chain-as-restraint. The term and its "heart-chain" gloss stay in the First Tongue
  register; the bare English "chain" is banned player-facing, where it collides with the never-a-leash art
  law. **The owner's phrase "bond chain" was already canon; only the English was wrong.**
- **`scripts/check-canon-terms.sh`: two more exclusions.** `CLAUDE.md` and `docs/progress-log.md` name retired
  terms *in order to govern them*, which is NEVER #4's carve-out. Both files are new this session and both
  tripped the lint on their first run — the fix is the exclusion, never deleting the governing text.
