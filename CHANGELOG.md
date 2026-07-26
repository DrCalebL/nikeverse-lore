# NIKEVERSE LORE ↔ GAME RECONCILIATION — CHANGELOG

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
