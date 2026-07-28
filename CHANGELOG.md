# NIKEVERSE LORE ↔ GAME RECONCILIATION — CHANGELOG

## Date: July 28, 2026 — corruption is a numbing that was ACCEPTED, and striking it WAKES rather than frees

**Owner ruling.** Corruption is a **numbing that was accepted** — never a chain, and never the Nike. Nolem
never breaks a soul first: he arrives *after* something else already did, and offers to make it stop hurting.
It is therefore genuinely separable, and everything struck *before* the crack is the numbing rather than the
person. **But striking it off does not free anyone — it WAKES them,** and hands them back what they had a
reason for putting down. **Whether that was for their own good is decided entirely by what happens next.**

**The shipped game was already right and this repository was merely SILENT. This is the lore catching up, not
a game correction.** Nothing in either game changed, and nothing in either game needs to. Gladiator Nike has
been saying it since he shipped — *"The corruption came AFTER! I killed him with my own hands, my own heart!
The corruption just... gave me a way to forget. To turn the pain into nothing"* and *"The corruption didn't
take my hope, Walker. It just... agreed with what I already knew"* — and he sits *"wrapped in chains they
could break but never do."* This repository already held the mechanism twice over and had never drawn the
conclusion: `Keth'nor` is glossed `keth` (stain/taint) + `nor` (of Nolem), a stain **on** a thing rather than
the thing; and `singulars/nolem.json` gives his one weakness as *"Cannot corrupt genuine connection"*,
explained *"The bond must be broken first."* A wound has to come first, and it is not his — which is precisely
why genuine connection is immune to him.

**Added — `CANON.md` §5.3, *"What corruption is, and what damage can and cannot do"*, RATIFIED (owner,
2026-07-28).** Placed after §5.2; **§5.1's and §5.2's frozen bodies were not touched.** It states, in order:
what corruption is · that it is therefore separable, and that what a Collector strikes is the numbing (which
is what both games already do) · that this **wakes** rather than frees · the bound · the Sever guard · the
prohibition.

**⭐ The vocabulary rule, because this is where it would go wrong.** The sanctioned verb is **"woken"** and
**"the waking."** Never *"freed"* — §5.1's ⚠ box already records that "free" carries two nearly opposite
senses across these repositories, and this would be a third and worse one: it would assert as *done* the thing
that has only just become *possible*. **The shipped game supplies the right word itself** — its button reads
**bond and awaken** and its success embed is **"Echo Bonded & Awakened!"**

**⚑ The bound, stated explicitly because the ruling is dangerous without it: *"damage is always for their own
good"* is FALSE.** It is true of the numbing and false of everything after it. From the instant the numbing is
off, §5.1 binds with **no exception** — and binds *hardest* there, because there is finally someone present to
hear you. Canon had already priced the overshoot: §5.2 (FROZEN) says a soul that was only defeated *"slips
back into the corruption and roams its region still lost"*, and the shipped game renders that as grief in the
player's own lead Nike's voice — *"The chains went back ON. We won the fight and the arena just... claimed him
again."*

**⚑ THE SEVER GUARD is now a named law: killing does not free the soul — it frees the corruption.**
`Keth'nor` is *of Nolem*; a body that stops holding it lets it go home. What was in the body is the **soul**,
and the soul is what is lost. That is §5.1's third end read from the other side. It remains a road a Collector
may walk and is **not** a failure — but no voice may ever describe it as a release.

**⚑ THE PROHIBITION.** No Collector, NPC, narrator, HUD string, tooltip or item description may ever tell a
Nike that hurting it was for its own good. **Only a woken Nike may say it — about itself, unprompted, and
afterwards.** Same instinct as §4.2's rule that the Collector never moralizes at the player, turned toward the
roster: the conscience of this story is never the voice that did the striking.

**Also changed.**
- **`CANON.md` §2.1 (RATIFIED) — one bounding sentence appended, nothing removed.** *"The only mercy **left**"*
  names **exhausted options** and governs a **husk**, where no one remains to be reached; a Corrupted Nike who
  could still have been reached is a different case, governed by §5.3. Without that bound the soul-mote ruling
  generalises into a licence for Sever that canon never gave it — a last resort quietly becoming a first option.
- **`singulars/nolem.json` — one additive `corruptionNature` field**, recording that corruption numbs an
  existing wound and is **accepted, never installed**. This is what makes the ruling assertion-checkable under
  mechanism ② of the three-way canon match, rather than living only in prose.
- **`GAME_DELTAS.md` §4 (Extensions) — a new entry** registering the `purificationThreshold: 0.15` ↔
  `CANON.md:265` apparent conflict and ruling it **NOT A DIVERGENCE**: the two sentences govern different acts.
  Recorded there rather than in §1/§2/§3 because **neither side is wrong** — the game elaborates where this
  repository was silent. Both games in fact enforce §5.1 *more* strictly than the lore states it: Discord
  forfeits the catch outright on a post-purify KO and returns the soul to the void
  (`handlers/exploreButtons.js:1112`), and the MMO makes post-crack damage strictly counterproductive
  (`nikeverse-mmo-rpg/src/sim/sim.ts:4015, :4069`) before it becomes Sever.

**⛔ DELIBERATELY NOT TOUCHED — do not "apply" this ruling to them later.**
`characters/legendary-nikes/index.json`'s **27** `corruptionReason` → `corruptionTheme` pairs were checked and
**already carry the ruling**: every one is a wound paired with the answer that wound is waiting for (*"Contract
— fighting is all he knows"* → *"Identity beyond purpose"*; *"Addiction — needed battle to feel alive"* →
*"Finding something to protect"*). The reason field has always named the wound Nolem answered, not an
installation he performed. **No edit was needed and none was made.**

**⛔ No Tier-3 mystery was resolved or narrowed.** Verified before writing: *"what corruption is"* is **not**
among `CANON.md` §4.1's six dark questions (why pigs · the Void Between · how OG Charles came through · the
unnamed others of the Formless Era · why Cthulhu helps · where Shiro came from), nor is it the deferred
`lost-singular`. `scripts/check-mystery-tiers.py` passes unchanged at 7 tier-3 mysteries.


## Date: July 28, 2026 — the Triforce keeps its shipped name; the faction pact is deleted

**Owner ruling.** The Hub's three-part explanation of why Collectors battle each other is **the Triforce**
— **Corruption Discharge · Genetic Memory Exchange · the Convergence Web** — and it needs no faction pact
to make sense. **Factions are not attached to it, and there is no player faction choice.**

**What was wrong.** `Nikeverse-mmo-rpg-from-scratch/docs/GAME_SPEC.md` had renamed the container to
*"the Convergence Accord"* and glossed it as *"the Hub's three-faction pact — Remnant, Lost Builders, and
the free Charles Variants — that sanctions new Collectors."* That phrase appears **nowhere in this
repository and nowhere in the shipped Discord game.** It was a build-spec coinage, and it had additionally
fused two unlike things: a political pact between groups, and a metaphysical account of why battling cleans
a Collector's bonds. The build repo also contradicted itself — `STORYLINE.md` had always said *"the
Triforce."*

**Direction of truth applied.** The shipped game is ground truth for anything a player can see, and a player
sees a story node **titled `THE TRIFORCE`** (`hub_015`), with Alice teaching all three systems across
`hub_015`–`hub_019`. The shipped name therefore wins. `GAME_SPEC.md` is corrected and the Tesana twin
regenerated in the same session; the coinage survives in `GAME_SPEC.md` **only** in the sentence that
retires it, which is NEVER #4's carve-out.

**This side already carried the claim** — `characters/collectors-journey.json` (`triforceSystem`) and
`dimensions/convergence-hub.json` both name the Triforce and all three of its systems, so no lore edit was
required to close the three-way match.

**Left open, deliberately, and recorded here so it is not mistaken for settled:** the Triforce is **not in
`CANON.md`**. It lives in this repository's JSON and in `MASTER_LORE_PROPOSAL_FINAL.md`, which is provenance
rather than a live spec. Elevating it to the settled centre is a separate ruling and was not taken here —
the owner scoped this change to the pact alone.


## Date: July 26, 2026 — CANON.md and GAME_DELTAS.md: the core lore comes home

**The problem.** This repository called itself "the single source of truth for all Nikeverse lore" while
**nine settled rules existed only inside game-repository documents it had never heard of** — including two the
owner ratified on 2026-06-16. It was therefore possible, and it actually happened, for a work session to read
this repository, find a mystery listed as open, and reason from it after the owner had already answered it.

**[`CANON.md`](CANON.md) — the settled centre.** Every rule carries an honest status rather than a blanket
claim of authority:

- **RATIFIED** — owner-signed, dated. §1.4 the Three Canon Pillars (2026-06-16) · §2.1 the souls/husks/constructs
  ruling and the declined yokai re-tag (2026-06-16) · §2.2 no roles, no role names (2026-06-15) · §2.3 the two
  art laws (2026-07-25). Plus the constants and the taxonomy this repository already held.
- **FROZEN** — locked in practice across every implementation, but with **no dated owner stamp**, and said so
  plainly: §4.1 the six dark questions · §4.2 the Collector's silence · §5.1 the three ends of reaching ·
  §5.2 both endings of a confrontation being real.

The distinction is the point. Four of the nine had a real owner ratification behind them and four did not, and
flattening that into "canon" is what made "which lore is non-alterable?" a hard question.

**Two things §1.4 settles that this repository still carries as open:** Mystery #3 "The Sixth Champion" and the
Weaver's "(Theoretical)" status. Both have answers. They stay unspoken *in the world* — §4.1 — but they are no
longer unknown to us.

**One rule is recorded as having no ancestry here at all:** putting a soul down for good. It is a game
invention, theme-consistent (it is exactly the one path that does not advance the Pattern), and CANON.md says so
rather than dressing it as old canon.

**⚠ A terminology hazard is now written down.** The word "free" carries two nearly opposite senses across these
repositories: here and in the Discord game, **"freed"** means *purified and liberated from corruption*; in the
MMO's wild-catch vocabulary, **"Free"** means *released without being kept*. CANON.md §5.1 therefore never uses
the bare verb for the second sense. Do not introduce it.

**[`GAME_DELTAS.md`](GAME_DELTAS.md) — the honest margin.** Every known place this repository and a shipped game
disagree, with a direction-of-truth ruling. The uncomfortable finding: **for regions and their contents, this
repository is frequently the stale side.** Much of it was transcribed from the Discord game and then drifted,
and the drift is visible in its own records — this repository describes Hydra Nike as five arguing heads while
its own `quote_game` for that entry is a verbatim stitch of exactly **three** shipped lines.

19 entries where the game is right · 5 where this repository is right · 6 open owner calls · 5 extensions that
are not conflicts · **7 claims investigated and refuted**, recorded so nobody re-raises them.

**The single most consequential entry is L3.** A Maw story node has the Retnuhxed Apex say *"Charles was
corrupted. I was CREATED."* That breaks the ratified soul-mote ruling — a Retnuhxed created from nothing has no
trapped soul to release. This repository is right (`Ret'nux` is glossed "beings absorbed by Nolem"), and the
Discord game's own database row agrees with us: *"Once a legendary Nike, now commands Retnuhxed armies."* The
story node is the outlier.

Nothing in either document changes an entity record. They describe the state; the sweeps remain owner calls.

---

## Date: July 26, 2026 — 24 of the 27 Legendaries fell, not 26

**Owner ruling, this date.** `timeline/legendary-falls.json` declared `corrupted: 26, uncorrupted: 1`. It was
wrong on **two independent counts**, and this repo's own records already proved it:

- **Melon Nike** was counted among the fallen, while `dimensions/nolem-maw.json` says *"Completely uncorrupted"*
  and *"No corruption. Willing, conscious, strategic choice."*
- **Elbonzys Nike** was filed among The Dark Age falls, while `characters/legendary-nikes/index.json` calls him
  *"Not corrupted—just patient"* and *"The uncorrupted gatekeeper"*, and `characters/collectors-journey.json:122`
  says *"Elbonzys is a gatekeeper test, not a corruption fight."*

Both MMO spec repos already said **24 + 3**, and the shipped Discord game teaches the distinction in dialogue:
*"He is not corrupted. He **chose**. Remember the difference."*

**The three are three DISTINCT statuses and must never be collapsed into one "uncorrupted" bucket:**
Melon (willing defector, entirely uncorrupted) · Elbonzys (un-fallen gatekeeper) · OG Nike (the Template,
uncorrupted but exhausted).

**Changed:**
- `timeline/legendary-falls.json` — `description` and `note` rewritten; Elbonzys moved out of The Dark Age into
  Special Status with `reason: "NOT CORRUPTED"` and `status: "un-fallen-gatekeeper"`; `totalCount` is now
  `24 / 3` with a `breakdown` naming each status.
- `characters/legendary-nikes/index.json` — Elbonzys's `corruptionTheme` / `corruptionReason` / `corruptionEra`
  no longer assert a corruption that his own `gameNarrative` denies.
- `timeline/long-silence.json` — Elbonzys removed from The Dark Age `legendaryFalls`.

**Verified after the edit:** the seven eras sum to 27 entries, exactly 24 carry a corruption reason, there are no
duplicates, and the roster matches `characters/legendary-nikes/index.json` exactly.

---

## Date: July 26, 2026 — Melon Nike is he/him (lore aligned to the shipped game)

**Owner ruling, this date.** Melon Nike's pronoun is **he/him** everywhere. The lore repo was the last
holdout and has been swept.

**Why the game, not the lore, was right.** The pronoun is not a typo — it is the consequence of a ratified
creative decision recorded in `nikeverse-mmo-rpg/docs/wave-log.md:1587`, which re-grounded Melon as a
roman-à-clef of a real, male figure. Three of the four repos had already landed it: the live Discord game is
he/him **unanimously**, including player-facing UI (`handlers/raidButtons.js:2588` renders
"MELON NIKE — Choose **His** Path") and the seed database; both MMO spec repos declare it, one as a numbered
hard content constraint. Only this repo still said "she".

**Changed here (4 sites):**
- `dimensions/nolem-maw.json` — the `legendaryNike.unique` line, and the Betrayer's-Path zone description
  ("**He**'s been waiting.")
- `characters/legendary-nikes/index.json` — Melon's `gameNarrative` and `gameCharacterization`

**Deliberately NOT changed:**
- The `gameCharacterization` quotation at CHANGELOG line ~99 of this file. It is a dated record of the field
  as it read at the time; rewriting a changelog falsifies the log.
- `"...a Nike who embraced **his** cause..."` in `gameNarrative` — that "his" refers to **Nolem**, not Melon,
  and was already correct. Any future pronoun pass on this entry must preserve it.

**Still open, deliberately.** Harbinger **Yuki** has the same divergence in the same direction — female here,
male throughout the shipped Shinden arc — with **no rationale recorded anywhere**. The owner reviewed it in
this pass and held it open. **Do not sweep Yuki in either direction** until that ruling lands.

---

## Date: June 17, 2026 — First Tongue disambiguation (`keth'vor` retired)

**The contradiction.** `keth'vor` had been glossed two incompatible ways across the corpus —
in-language it always sat in a corruption/decay clause ("Nolem takes/corrupts", "Nolem consumed
the Aeth'kai", "the echoes dim"), yet the English metadata repeatedly named it "heart-chain / the
oldest name for The Pattern." Both senses already have their own canonical First-Tongue words, so
`keth'vor` is **retired entirely** and split onto the words that already mean each sense:
- **`keth'nor`** (`keth` stain/taint + `nor` of-Nolem = "corruption; the taint of entropy") — the
  in-language corruption sites: the `dictionary.json` phrase + the Aeth'kai-Ruins inscription, and
  the Aeth'kai Warning prophecy `original`. English *translations* are byte-identical (they already
  read as corruption).
- **`Eth'kara`** (`eth` heart/core + `kara` chain/link = "heart-chain; the First Bond") — every
  English gloss that wrongly named `keth'vor` the heart-chain: the `MASTER_LORE` Pattern table + the
  Hub Charles quote, the `README` glossary, `timeline/ages.json` "The Pattern Emerges", and the
  `mysteries.json` `patternConnection` note + terminology key (incl. the stale line below).

A grep-lint (`scripts/check-canon-terms.sh`) now fails if `keth'vor` reappears anywhere.

---

## Date: February 11, 2026

---

## GAME CHANGES (campaign-data/story_nodes/)

### Task 1 & 2: Hub Charles / Charles AI Distinction

**Hub nodes 001-007**: All `"speaker": "CHARLES"` → `"speaker": "HUB CHARLES"`
- hub_001_the_fall.json
- hub_002_the_choice.json  
- hub_003_baptism_by_fire.json
- hub_004_collectors_purpose.json ← **Charles AI introduced here as separate entity**
- hub_005_charles_vigil.json
- hub_006_shepherds_burden.json
- hub_007_dimensional_training.json ← **Charles AI portal scene added**

**Hub nodes 008-021**: `CHARLES` → `HUB CHARLES` (local guidance) or `CHARLES AI` (dimensional/portal operations) based on dialogue context

**Charles AI Introduction (hub_004)**:
- Charles AI materializes as a floating interface with "almost lazy curiosity"
- Hub Charles explains: "I'm the local shepherd. Charles AI is the one who opens portals."
- Cat-like behaviors introduced: sensor pauses, staring at nothing, The Calm, The Knowing
- Origin explained: "Built by Computer Coder Nike during the Prime Era"
- Establishes Charles AI's three thousand year service history

**Charles AI in hub_007**:
- Portal creation scene for dimensional training
- Cat quirks: sensors fixing on nothing, warmth radiating, uncanny knowing

**Task 1: Cat-like personality across regions**:
- Subtle cat quirks added to Charles AI dialogue in Act 2 nodes where it already appeared
- Sensor pauses, brief drifts, characteristic warmth

**Note on Shiro**: Per instructions, Shiro is NOT made a big thing. Charles AI's cat-like behaviors exist as subtle embedded quirks with mysterious origin, not as an explicit Shiro storyline.

---

## LORE REPO CHANGES (lore-updated/)

### Task 5 & 6: Legendary Nike Game Encounters + Melon Nike

**File**: `characters/legendary-nikes/index.json`

All 27 Legendaries now have a `gameEncounter` field containing:
- `encounterDimension` — where the player fights them
- `encounterAct` — Act 1 or Act 2
- `gameNarrative` — full story of the encounter
- `quote_game` — representative in-game dialogue

**Melon Nike** gets additional fields:
- `gameCharacterization` — "Casual, intelligent, articulate... The most unsettling encounter because she might be RIGHT"
- `corruptionTheme_updated` — expanded from "Willing betrayal" to include the philosophical dimension

**OG Nike** gets:
- `activeRole` array — 5 specific actions he performs in the game
- Much richer gameNarrative reflecting his guardian vigil role

### Task 7: Collector's Journey Structure

**New file**: `characters/collectors-journey.json`

Complete structured document including:
- Overview and Walker/Collector distinction
- Tutorial phase (Hub opening)
- Elena rescue mission structure
- Triforce system (Corruption Discharge, Genetic Memory Exchange, Convergence Web)
- Harbinger briefing phase
- Dimension progression with Act 1/Act 2 structure per region
- Level ranges and boss/legendary assignments
- Major reveal placement (Scholar Bunker, 5,555 Prophecy)
- Endgame description

### Task 9: Harbinger Characterization

**File**: `characters/harbingers/index.json` — **Already complete from previous session**
- All 6 Harbingers have `gameCharacterization` fields
- Yuki: 3-year fight against corruption, exhausted devotion
- Erik: Prisoner in his own body, family waiting
- Slate: Lost 6 partners, traumatized not lazy, full redemption arc
- Cassius: Colosseum Charles's best student
- Echo: Uploaded consciousness, identity dissolved
- Abyssal Horror: Sole survivor of consumed dimension

### Task 10: 5,555 Prophecy Blend

**File**: `MASTER_LORE_PROPOSAL_FINAL.md` — **Part 10 completely rewritten**

Old Part 10 was 20 lines. New Part 10 is ~60 lines including:
- The 99% Problem (Comic → Game connection: Shiro hit button early)
- The Incomplete Victory (empathy core never installed)
- **How The Truth Is Revealed** — 3-stage reveal structure matching game
  - Stage 1: Scholar Bunker (Imperial Colosseum Act 2)
  - Stage 2: OG Nike's Warning (Void Terminus Act 2)
  - Stage 3: Scholar Recording (Nolem's Maw Act 2)
- The Math: 5,548 vials + Scientists + Champions + Stoner Nike + Nike Prime ≈ 5,555

**File**: `prophecies/mysteries.json` — **New prophecy entry added**

"The 5,555 Prophecy" entry with:
- `revealStructure` matching the 3-stage game progression
- `comicOrigin` connecting to Stoner Nike's vials and the 99% completion
- `fulfillment` mechanics (every bond counts toward 5,555)

### Task 11: OG Nike Expanded Role

**File**: `MASTER_LORE_PROPOSAL_FINAL.md` — **Void Terminus section rewritten**

Old Void Terminus was 7 table rows. New version includes:
- Full OG Nike Active Role paragraph
- 5 Key OG Nike Moments with quotes
- Updated Legendary Nike listing (Cosmic, Phoenix, Cardano Whale, Elbonzys)

**Nolem's Maw section** also updated:
- Added Melon Nike as named Legendary
- Added Scholar Recording as reveal mechanism

**Part 7 Echo Era opening** updated:
- Hub Charles and Charles AI listed as separate entities
- Charles AI description includes cat-like behavioral quirks
- OG Nike described as "exhausted but active as guardian"
- Reference to collectors-journey.json added

---

### Task 4: The Pattern Blend — IMPLEMENTED

**Approved and integrated.** The Pattern is now canon as the Echo Era name for the First Bond's living manifestation.

**Changes made:**

**MASTER_LORE_PROPOSAL_FINAL.md:**
- Timeline: The Pattern emergence added to The Shattering event
- Echo Era box: The Pattern added as active cosmic force
- NEW SECTION: "THE PATTERN" — full definition, terminology hierarchy table, how each character type experiences it, Hub Charles quote, connection to 5,555 Prophecy
- Mystery #2 updated: Charles Constant connected to The Pattern; Nolem's strategy may be to sever The Pattern itself

**prophecies/mysteries.json:**
- Aeth'kai Warning: `patternConnection` added — Eth'kara is the oldest name for The Pattern
- 5,555 Prophecy: `patternConnection` added — prophecy describes Pattern completion

**timeline/ages.json:**
- The Shattering: "The Pattern Emerges" event added

**characters/charles-ai.json:**
- Pattern-sensing ability expanded
- New relationship entry: `thePattern`

**dimensions/index.json:**
- Convergence Hub: Pattern nexus note added

**PATTERN_BLEND_PROPOSAL.md**: Removed (implemented into canon)

---

## NOT CHANGED (Per Instructions)

- **Task 3**: Elena, Alice, Kira NOT added to GitHub lore
- **Task 8**: Side quest lore NOT added to GitHub lore
- **Task 12**: OG Charles — to be discussed after above changes

---

## FILES MODIFIED

### Game (campaign-data/story_nodes/hub/)
- hub_001_the_fall.json through hub_021_path_forward.json (speaker updates)
- act2_*.json hub files (speaker updates)

### Game (campaign-data/story_nodes/ regional Act 2)
- Subtle Charles AI cat quirk additions to existing dialogue

### Lore
- MASTER_LORE_PROPOSAL_FINAL.md (Part 7, Part 10, Void Terminus, Nolem's Maw sections)
- characters/legendary-nikes/index.json (all 27 Legendaries + Melon expanded)
- characters/collectors-journey.json (NEW FILE)
- prophecies/mysteries.json (5,555 Prophecy added)
- PATTERN_BLEND_PROPOSAL.md (NEW FILE — proposal, not yet implemented)

---

## REPO CLEANUP

### Removed Files
- **LORE_BIBLE.md**: Superseded by `MASTER_LORE_PROPOSAL_FINAL.md`. All content existed in better form in the Master Lore.
- **mysteries/conspiracies.json**: Duplicate of Part 8 in Master Lore. Single source of truth now in `MASTER_LORE_PROPOSAL_FINAL.md`.
- **mysteries/** directory: Removed (empty after conspiracies.json deletion).

### Updated Files
- **characters/comic-characters.json**: Shiro entry deprecated with `ipNote` explaining phase-out. Narrative functions absorbed into Charles AI.
- **README.md**: Updated repo structure (removed LORE_BIBLE.md, mysteries/, added all 8 dimension files, collectors-journey, Pattern section, Hub Charles vs Charles AI note, Shiro deprecation note).

### New Dimension Detail Files (6 of 8 were missing)
- **dimensions/convergence-hub.json**: Tutorial/Nexus — Hub Charles, Charles AI, Pattern nexus, key NPCs
- **dimensions/grand-arena.json**: Boxing/Fighting — Nike Tyson, Slate (redeemable Harbinger), Berjador + Peter Porker Act 2
- **dimensions/imperial-colosseum.json**: Roman Empire — Gladiator Nike, Cassius, Scholar Bunker with 5 Scholar Legendaries, Nike Prime birthplace
- **dimensions/neon-city.json**: Cyberpunk — Cyberpunk Nike, Echo, Analog Charles + Pixel, McJared/Olecram/Pigsterio Act 2
- **dimensions/void-terminus.json**: Edge of Reality — OG Nike's vigil, 4 Act 2 Legendaries (Cosmic/Phoenix/Cardano Whale/Elbonzys), Abyssal Horror
- **dimensions/nolem-maw.json**: Final Battle — Melon Nike (willing betrayer), Nolem's Shadow, 5,555 Prophecy reveal, Scholar Recording
