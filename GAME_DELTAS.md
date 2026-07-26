# GAME DELTAS — where this repository and the games disagree

**Companion to [`CANON.md`](CANON.md).** That document is the settled centre. This one is the honest margin:
every known place where the lore in this repository and the lore shipped in a Nikeverse game do not match, what
each side says, and **which side is right**.

> ### The direction of truth is not always this repository
> This repository calls itself the single source of truth. For cosmology, entities, numbers, language and
> timeline, it is. But for the **regions and their contents**, much of it was transcribed *from* the Discord
> game and then drifted — and the drift is visible in its own records. The clearest case: this repository
> describes Hydra Nike as five arguing heads, while its own `quote_game` for that entry is a verbatim stitch of
> exactly **three** shipped lines. Heads four and five were invented after the transcription.
>
> **The working rule.** Prefer the game where the game side is live engine state, shipped player-facing content,
> or code that actually runs — changing it would regress a running product for no canon gain. Prefer this
> repository where the game side is prose that merely restates lore and got a detail wrong.

**Status of this register.** Every entry below was opened and confirmed against the files on disk. Seven further
claims were investigated and **refuted** — they are listed in §5 so nobody spends a day on them again.

**The games.**

| Short name | Repository | What it is |
|---|---|---|
| **Discord** | `DrCalebL/nikeverse-discord-game` | The live product. 336 story nodes, 8 regions, the seed database, 25 raid bosses. Mostly **upstream** of this repository. |
| **MMO (prior)** | `DrCalebL/nikeverse-mmo-rpg` | The first MMO build. Holds the ratification records and the engine seams. |
| **MMO (current)** | `DrCalebL/Nikeverse-mmo-rpg-from-scratch` | The current MMO build, in three.js. Pre-code; its `GAME_SPEC.md` is inherited from the prior build. |

---

## 1 · The game is right — this repository is the stale side

These are transcription drifts, not design disagreements. Recommended direction: **update this repository.**

### 1.1 Entities

| # | What | This repository says | The game says | Note |
|---|---|---|---|---|
| E1 | **Hydra Nike's heads** | "Five arguing heads… Head 4 is paranoid, Head 5 is calm" | **Three**, everywhere | Decisive: this repo's own `quote_game` is the three shipped head lines stitched with " / ". Also **live code** — `RaidBossConfig.js` defines a trait named `Three Heads` and the raid survive-chokepoint keys off that name. |
| E2 | **Cardano Whale's gender** | *"**Her** form blocks out the void"* | he/him throughout | Self-refuting: the same record's `whyNotRecruited` reads *"No way to communicate with **him**."* |
| E3 | **What Cardano Whale lost** | a lost calf | a **pod — his family**, whose names the void ate | A third version exists in the raid layer: *"Nolem devoured his ocean."* Three accounts, one soul. |
| E4 | **Bertus Maximus's story** | froze himself from guilt over a dimension he destroyed | intercepted alive at the village edge; three centuries of hunting, *"no hall to come home to"* | **A copy-paste.** Bertus and Colossal Nike carry a **byte-identical** `quote_game`, and the shipped game gives that line to Colossal. This record is also self-refuting — its own `corruptionReason` is "Fulfillment — found endless war." ⚠ **See §3.5 before fixing.** |
| E5 | **Harbinger Erik** | "The Eternal Raider" · glory that became emptiness | "The Prisoner in His Own Body" · *"I offered my service for my people's safety. He laughed. Said he'd take my service AND my people."* | A split **inside this repository** — `dimensions/frostfall.json` disagrees with `characters/harbingers/index.json`. The game adjudicates. |
| E6 | **Harbinger Yuki's title** | "The Ice Shadow" (`dimensions/shinden.json`) | "The Devoted Shadow" | Same internal split — `characters/harbingers/index.json` already says "The Devoted Shadow" and matches the game. |
| E7 | **Yuki's premise** | the Nike she loved **died**; grief became rage | the master is **alive** and corrupted; Yuki stays to be near him | Changes the whole character: grief-for-the-dead versus devotion-that-cages. |
| E8 | **Other Harbinger titles** | Slate, Echo and the Abyssal Horror carry titles the shipped game does not use | — | Same class as E5/E6. |
| E9 | **When Ninja Nike fell** | "The Forgetting", 300–500 years after the Prime Era | **fifteen years ago** | The shipped arc depends on it: his clan still remembers him. |
| E10 | **Melon's boss classification** | `raidBoss: true, campaignBoss: false` | a campaign **anchor** boss *and* a raid boss | Self-refuted here too — the same record's `gameEncounter` describes a campaign encounter in Nolem's Maw. |
| E11 | **Melon under pressure** | "Not evil. Not broken. Just… a realist" | breaks: *"I was SCARED, okay?!"* | This repo has the surface; the game has what is underneath it. |

### 1.2 The world

| # | What | This repository says | The game says | Note |
|---|---|---|---|---|
| W1 | **The Dimensional Anchors — all six** | Shadow Kunai · Frostfire Axe · Champion's Wraps · General's Sigil · Chrome Interface | `blade_of_shadows` **Blade of Shadows** · `crown_of_berserker` **Crown of the Berserker** · `champions_belt` **Champion's Belt** · `champions_laurel` **Champion's Laurel** · `source_code` **Source Code** | **Live engine state** — these ids are granted on boss defeat and gate region unlocks. Frostfall differs in *form*, not just name (an axe here, a helm there). Shinden's game name also appears in the MMO's generated relic table, so three of four repositories carry it. |
| W2 | **The sixth anchor** | absent — only five are recorded | Void Terminus grants `final_fragment` **Final Fragment** | An enumeration gap, not a conflict. Six anchor flags are hardcoded in the engine. |
| W3 | **Void Terminus's boss** | "Abyssal Horror (Harbinger)" as Act-1 boss | the **Dimension Eater**, "THE DEVOURER OF WORLDS"; the Abyssal Horror is an *elite mini-boss* that gates it | *"Dimension Eater"* returns **zero hits** in this repository. A whole region boss is missing from canon. |
| W4 | **The Abyssal Horror's title** | differs from the shipped title | — | Same class as the Harbinger titles. |
| W5 | **The Act-2 gate** | "Freeing the Act 1 Legendary unlocks deeper content in each dimension" | every one of the seven Act-2 entries additionally requires **`campaign_complete`** | Act 2 is post-campaign endgame, not mid-region content. A structural difference, not a wording one. |
| W6 | **Side-quest rosters** | Grand Arena, Neon City and Void Terminus rosters do not match what shipped | — | Frostfall and Shinden **do** match. |
| W7 | **"The Usurper's Throne"** | Frostfall's boss arena, where Erik holds court | a shipped **side quest** about a kinslayer king; Erik is elsewhere | — |
| W8 | **`quote_game` is unreliable** | asserts a line is spoken in-game | **9 of 27** are present verbatim; 18 are not | Four of the 18 are paraphrases of real lines; one gives Bertus a line the game gives to Colossal. Treat `quote_game` as *authored flavour*, never as a citation. |

---

## 2 · This repository is right — a game should change

| # | What | The game says | This repository says | Note |
|---|---|---|---|---|
| L1 | **Who is in the trap** | *"He's felt this signature before — for 3,000 years, pressed against it in the space-time trap"* — of **OG Nike** | **Nike Prime** is in the trap; OG Nike keeps vigil at the edge of reality | A one-line authoring slip, not a rival cosmology: three other lines in the same file place OG Nike at the edge, and another shipped node says of Nike Prime *"before he sealed himself away for three thousand years."* Low blast radius — the line only renders on the worst Resonance band. Fixable with a preposition. |
| L2 | **The name of the cataclysm** | "the Fracturing" (3 uses, one raid victory template) | **The Shattering / The Great Echo** | An inconsistency *inside* the Discord game — it uses the sanctioned name elsewhere (*"He existed before the Shattering"*). Prose only, no engine dependency. |
| L3 | **What a Retnuhxed is made of** | *"Charles was corrupted. I was **CREATED**. There is no other way for me."* | **partially absorbed beings** — and the First Tongue agrees: `Ret'nux`, *"beings absorbed by Nolem"* | ⚠ **The most consequential entry in this document.** A Retnuhxed that was created from nothing has no soul to release — which breaks the ratified `is_nike` ruling that a slain husk releases a warm soul-mote (`CANON.md` §2.1). The Discord game **contradicts itself**: its own database row for the same creature reads *"Once a legendary Nike, now…"* and agrees with this repository. Fix the story node. |
| L4 | **Level bands, internally** | — | `collectors-journey.json` and `dimensions/*.json` give different bands | This repository disagreeing with itself. Reconcile here. |
| L5 | **`dimensions/index.json` vs its own detail files** | — | Void Terminus and Nolem's Maw rows disagreed with their per-dimension files | ✅ **FIXED** — reconciled, with a CI check so it cannot recur. |

---

## 3 · Open — the owner has not ruled

| # | What | Why it is open |
|---|---|---|
| O1 | **Harbinger Yuki's gender** | Female here, male throughout the shipped Shinden arc, with **no rationale recorded anywhere** — unlike Melon, whose he/him has a written reason. Reviewed and deliberately held open (2026-07-26). **Do not sweep in either direction.** |
| O2 | **Is Melon corrupted at all?** | This repository and the Maw node say entirely uncorrupted. The raid layer says *"neither fully corrupted nor truly free — the shadow clings to him."* A game-internal split as much as a lore one. |
| O3 | **Per-region level bands** | This repository's bands are a clean non-overlapping partition; the game's overlap by design ("you can start here"). Both defensible. The enforced gates are per-node minimums, so the region bands are display text. |
| O4 | **Neon City's Charles** | "Analog Charles" here; the shipped node uses "Neon Charles" throughout while titling him "The Analog Rebel". Possibly two names for one character on purpose. |
| O5 | **Fixing Bertus (E4)** | Correcting it **invalidates a landed design document**: the prior MMO's `LEGENDARY_MOTIVATIONS.md` records "OLD motivation: guilt over a dimension he broke" and builds a whole new wound on that premise. The premise was a copy-paste error. Raise before fixing. |
| O6 | **The anchor count shown to players** | Two shipped surfaces disagree: one progress bar renders **/7**, the map footer renders **/6**. Engine truth is six; the /7 comes from a flag list containing a phantom entry no node ever sets. A game bug, recorded here because it is player-visible. |

---

## 4 · Extensions — the games elaborate where this repository is silent

**These are not conflicts.** Silence is not contradiction. Listed so they are not mistaken for drift.

- **The 4,892 timelines.** Nolem has consumed everything in 4,892 documented timelines. Ten occurrences across six live story files, including a stated objective. Nothing here contradicts it. **Recommended for adoption** — if adopted, note that a shipped line derives *"in 4,891 of them, you fail"*, so the two figures must stay in lockstep.
- **"The Seven-Tongued Deceiver."** Nolem's epithet in the Maw, with a seven-mouths boss mechanic behind it.
- **The Harbinger / Retnuhxed intelligence axis.** Retnuhxed are mindless; Harbingers are intelligent and *chose*. Consistent with the taxonomy here, and sharper than it.
- **Resonance, Composure, the Bond Struggle, Pattern Integrity, and putting a soul down for good.** All net-new game systems. This repository has zero occurrences of any of them as named states. Tune freely — only the *simultaneity* of the 5,555 (`CANON.md` §1.2) is canon.
- **The Legendary rarity tier.** The database has 38 creatures at `is_nike=1, rarity='Legendary'`; this repository names 27. **Not a contradiction** — a rarity tier and a narrative roster are different things, and the database proves it: all 27 canon Legendaries are batch `C` with `ABCD###` ids, the 11 extras are batch `B`. The extras are wild-catchable and have no lore entry, which is a content gap rather than a canon conflict.

---

## 5 · Refuted — do not raise these again

Each was investigated and did not survive.

| Claim | Why it fails |
|---|---|
| "The Imperial Colosseum side-quest roster is a direct inversion (Sane/Mad Emperor)" | No inversion. The shipped quest *is* a mad-seeming emperor who is secretly sane. This repo's title names the twist; the game's title names the surface. |
| "Nolem is 'pure evil' in the game but 'neither good nor evil' here" | Not a conflict. "Neither good nor evil" is explicitly his **original** state; "current" is "actively malevolent". The game line is present-tense and in-character. |
| "The Retnuhxed definition is broader in the games" | Could not be confirmed. The MMO phrasing is consistent with this repository's. |
| "`quote_game` is fiction — only 1 of 13 findable" | Overstated. **9 of 27** are present verbatim, 8 with the correct speaker. The field is *unreliable*, not fabricated. (The real defect is §1.2 W8.) |
| "The raid config disagrees with lore on corruption themes ~21/22" | Agreement is **higher** than claimed — reasons match 22/22 once the config's snake_case is read as the leading token of this repository's reason string. |
| "The database has 38 Legendaries but lore says 27" | A rarity tier versus a narrative roster. See §4. |
| "27 Legendaries here but only 22 raid bosses" | Explains itself: the 5 absent are exactly the 5 wild-spawn batch-C Legendaries. |

---

## 6 · How to keep this from growing

The root cause is not disagreement, it is **latency**. One owner ruling becomes separate commits in separate
repositories landing on separate days — and the 2026-06-17 taxonomy ruling landed in the game repository that
day and here **five and a half weeks later**, during which this repository actively published the opposite rule
and two work sessions reasoned from it.

1. **One ruling is one cross-repository unit.** No half lands until every half lands.
2. **Every ruling gets a dated `CHANGELOG.md` entry here**, quoting the owner.
3. **`scripts/check-canon-terms.sh` runs in CI**, over all four retired terms, on word boundaries.
4. **Stamp new canon `RATIFIED <date>` or `FROZEN`** — see `CANON.md`'s status column.
5. **When a game and this repository disagree, add a row here rather than silently editing one side.**

---

*Verified against `nikeverse-lore`, `nikeverse-discord-game`, `nikeverse-mmo-rpg` and `Nikeverse-mmo-rpg-from-scratch`
on 2026-07-26. A fuller cross-repository map, including the locks and their durability, lives at
`Nikeverse-mmo-rpg-from-scratch:docs/CANON_MAP.md`.*
