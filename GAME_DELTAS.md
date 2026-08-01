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
| E1 ✅ **FIXED** | **Hydra Nike's heads** | "Five arguing heads… Head 4 is paranoid, Head 5 is calm" | **Three**, everywhere | Decisive: this repo's own `quote_game` is the three shipped head lines stitched with " / ". Also **live code** — `RaidBossConfig.js` defines a trait named `Three Heads` and the raid survive-chokepoint keys off that name. |
| E2 ✅ **FIXED** | **Cardano Whale's gender** | *"**Her** form blocks out the void"* | he/him throughout | Self-refuting: the same record's `whyNotRecruited` reads *"No way to communicate with **him**."* |
| E3 ✅ **FIXED** | **What Cardano Whale lost** | a lost calf | a **pod — his family**, whose names the void ate | A third version exists in the raid layer: *"Nolem devoured his ocean."* Three accounts, one soul. |
| E4 ✅ **FIXED** | **Bertus Maximus's story** | froze himself from guilt over a dimension he destroyed | intercepted alive at the village edge; three centuries of hunting, *"no hall to come home to"* | **A copy-paste.** Bertus and Colossal Nike carry a **byte-identical** `quote_game`, and the shipped game gives that line to Colossal. This record is also self-refuting — its own `corruptionReason` is "Fulfillment — found endless war." *(The old pointer here read "see §3.5" — no such section exists; it meant row O5, now resolved.)* |
| E5 ✅ **FIXED** | **Harbinger Erik** | "The Eternal Raider" · glory that became emptiness | "The Prisoner in His Own Body" | **Internal split, closed on the game's evidence.** `frostfall/main_004_harbinger_erik.json` is *titled* `THE PRISONER IN HIS OWN BODY` and carries the bargain verbatim in `battle.preBattle`. "The Eternal Raider" was a premise the game never shipped, and it was already self-refuting here: Erik's own record gives his vulnerability as *"His family. The bonds he never stopped feeling"* while the dimension file said he *"found nothing worth keeping."* Both sites now agree, casing included. |
| E6 ✅ **FIXED** | **Harbinger Yuki's title** | "The Ice Shadow" (`dimensions/shinden.json`) | "The Devoted Shadow" | **Internal split, closed — and the game speaks the lore title out loud.** In `shinden_008_shadow_temple.json` Yuki says *"That Yuki died the night she accepted Nolem's gift. I am what remains — **the Devoted Shadow**."* "Ice Shadow" returns **zero hits** in the shipped game. The dead-love premise (E7) went with it: her master is **corrupted, not dead**, and she stayed to be near him. |
| E7 | **Yuki's premise** | the Nike she loved **died**; grief became rage | the master is **alive** and corrupted; Yuki stays to be near him | Changes the whole character: grief-for-the-dead versus devotion-that-cages. |
| E8 | **Other Harbinger titles** | Slate, Echo and the Abyssal Horror carry titles the shipped game does not use | — | Same class as E5/E6. |
| E9 ✅ **FIXED** | **When Ninja Nike fell** | "The Forgetting", 300–500 years after the Prime Era | **fifteen years ago** | The shipped arc depends on it: his clan still remembers him. |
| E10 ✅ **FIXED** | **Melon's boss classification** | `raidBoss: true, campaignBoss: false` | a campaign **anchor** boss *and* a raid boss | Self-refuted here too — the same record's `gameEncounter` describes a campaign encounter in Nolem's Maw. |
| E11 ✅ **FIXED** | **Melon under pressure** | "Not evil. Not broken. Just… a realist" | breaks: *"I was SCARED, okay?!"* | This repo has the surface; the game has what is underneath it. |

> #### ✅ E1, E2, E3, E9, E10, E11 executed — with one correction to this register itself
> **E10's word "anchor" was wrong.** Melon is a campaign boss, but he is **not** a region anchor:
> `act2_002_melon_boss.json` carries **no `isAnchorBoss` and no `grantAnchor`**, and the Discord repo's own
> `CLAUDE.md` names the five anchors, none of them Melon. He is one of the 21 Act-2 sub-bosses (with a
> `catchOpportunity`) *and* a raid boss (`RaidBossConfig` `MELON`). Lore now reads `campaignBoss: true` with a
> note recording exactly that, rather than promoting him to an anchor he never was.
>
> **E9 was self-refuting inside one record.** Ninja Nike's `corruptionEra` said *"The Forgetting (300–500
> years after Prime Era)"* while his own `gameNarrative`, four lines below, said the mist had covered the realm
> *"for fifteen years."* Only his date moved — **"The Forgetting" is a shared era** used by three other
> Legendaries and by `timeline/long-silence.json` and `timeline/ages.json`, and sweeping the phrase would have
> moved four falls to fix one.
>
> **E3 had a second site the register did not list:** `dimensions/void-terminus.json` carried the same
> "lost calf" line as the Legendary record. Both are now the pod.
>
> **E1's fix is larger than a numeral.** The five-head reading carried per-head personalities for heads 4 and 5
> that had to be deleted, not renumbered, and the shipped backstory tells a different story than lore did:
> they were one Nike until a dimensional collision, Charles balanced them, and Nolem corrupted only the
> *weakest* head, which corrupted the others. Lore said Nolem "offered silence to all five."

### 1.2 The world

| # | What | This repository says | The game says | Note |
|---|---|---|---|---|
| W1 ✅ **FIXED** | **The Dimensional Anchors — all six** | Shadow Kunai · Frostfire Axe · Champion's Wraps · General's Sigil · Chrome Interface | `blade_of_shadows` **Blade of Shadows** · `crown_of_berserker` **Crown of the Berserker** · `champions_belt` **Champion's Belt** · `champions_laurel` **Champion's Laurel** · `source_code` **Source Code** | **Live engine state** — these ids are granted on boss defeat and gate region unlocks. Frostfall differs in *form*, not just name (an axe here, a helm there). Shinden's game name also appears in the MMO's generated relic table, so three of four repositories carry it. |
| W2 ✅ **FIXED** | **The sixth anchor** | absent — only five are recorded | Void Terminus grants `final_fragment` **Final Fragment** | An enumeration gap, not a conflict. Six anchor flags are hardcoded in the engine. |
| W3 ✅ **FIXED** | **Void Terminus's boss** | "Abyssal Horror (Harbinger)" as Act-1 boss | the **Dimension Eater**, "THE DEVOURER OF WORLDS" | **The gap was real; the CONFLICT never existed.** ADOPTED by owner ruling 2026-07-27 and authored into canon at `entities/dimension-eater.json`. The shipped node carries `isRegionBoss: false` **and** `isAnchorBoss: false` — it was never Void Terminus's region boss, so *"no region anchor — the bottom of the world is not a boss"* (W1/W2) was never in tension with it. It is a **narrative-only gate** on the road to OG Nike, with no purify path. |
| W4 | **The Abyssal Horror's title** | differs from the shipped title | — | Same class as the Harbinger titles. |
| W5 | **The Act-2 gate** | "Freeing the Act 1 Legendary unlocks deeper content in each dimension" | every one of the seven Act-2 entries additionally requires **`campaign_complete`** | ⚑ **REVERSED 2026-07-27 — the LORE was right and the shipped gate is an engine artifact.** Deep tier ("Act 2") opens **PER-REGION**, on that region's own anchor falling. The `campaign_complete` gate is not canon: it lives in **engine code** (`StoryNodeLoader.js:149,158,258` — `n.act === 2 && !flags.campaign_complete`), not in the 63 nodes, and the shipped DATA contradicts it — the seven Deep-tier entries carry a monotone **minimumLevel staircase 22·38·50·62·78·90·98**, interleaved with the region bands. Shinden's Deep tier gates at **level 22**, inside Shinden's own 11–30 band; a genuinely post-campaign tier would flatten all seven to campaign-exit level. The MMO port must **DELETE that predicate**, not inherit it. **The shipped Discord game KEEPS its global gate — owner decision 2026-07-27, leave that story alone.** This is a CLOSED, accepted, permanent divergence between the two products, not an open defect: the Discord game has players mid-campaign and flipping the gate would change what 20+ nodes do for every existing save. Do not re-open it, and do not "fix" `StoryNodeLoader.js`. |
| W6 ✅ **FIXED** | **Side-quest rosters** | Grand Arena, Neon City and Imperial rosters did not match what shipped | — | **The row was right about two regions, wrong about the third, and silent about a fourth.** Grand Arena spent a slot on *"Slate's Redemption"*, which is a **main** node (`grand_arena_004_slate_battle`, `type: "main"`), and dropped the shipped `corner` chain → **"The Corner Doctor"**. Neon City was missing the `defense` chain → **"The Hesitating Guardian"** (the shipped node's own title). Imperial listed *"The Scholar's Legacy"*, which has **no shipped side chain at all** (the scholars are the Act-2 bunker arc), while the `storm` chain was unrepresented → **"Jupiter's Judgment"**. **Void Terminus is REFUTED — see §5.** Frostfall and Shinden do match, as the row said. |
| W7 ✅ **FIXED** | **"The Usurper's Throne"** | Frostfall's boss arena, where Erik holds court | a shipped **side quest** about a kinslayer king; Erik is elsewhere | **One file used one name for two different things.** The `sideQuests` use was correct; the `locations` use was wrong on all three fields. Erik never holds court — he is at `mountain_pass` (`exploration`); the boss arena is `eternal_battlefield` (Viking Nike); the Usurper content is `warlords_hall`, a `secret` zone. Replaced with those three real locations, and the `locations` entry "The Ghost Fleet" renamed to its shipped name **Frozen Harbor** so the file stops colliding a location with a side quest. **An unrecorded TWIN was found and fixed in Shinden:** `midnight_gardens` ships as `type: "story"`, and the boss arena is `dojo_arena`. |
| W8 | **`quote_game` is unreliable** | asserts a line is spoken in-game | **10 of 27** are present verbatim; 17 are not | Four are paraphrases of real lines. *(The Bertus/Colossal duplicate that used to sit here is fixed — E4.)* Treat `quote_game` as *authored flavour*, never as a citation. |

> #### ✅ W3, W6, W7 executed — one adoption, one over-claim, one file naming two things
> **W3 — the gap was real, the conflict was invented by this register.** *"Dimension Eater"* genuinely
> returned zero hits: a being with ten thousand consumed dimensions behind it, named in six shipped nodes and
> a DB row, was invisible to the bible. But the row framed it as a **region-boss conflict**, and it never was
> one — the shipped node carries `isRegionBoss: false` **and** `isAnchorBoss: false`. Adopted by owner ruling
> and authored at `entities/dimension-eater.json`, in a new `entities/` directory for the narrative-only,
> never-purifiable class (it could not live in `dimensions/` — the `dimensions-agree` CI job counts files
> against index rows, so a new file there fails the build). It is filed as **Nolem's instrument, never a third
> Singular**, and reachable from `singulars/nolem.json` `agents[]` so the subordination is structural rather
> than asserted in prose.
>
> **W6 over-claimed by one region and under-claimed by another.** Void Terminus is 4/4 and moves to §5. Imperial
> was wrong and the row never said so. The recurring shape: *the roster was checked against the region's story,
> not against the shipped chain list.*
>
> **W7 was one file using one name for two different things** — "The Usurper's Throne" as both a side quest
> (correct) and a boss arena (wrong on all three fields). Its twin in Shinden had never been recorded at all.
>
> #### ✅ E5 + E6 executed — and the two halves of the Harbinger ruling must not be confused
> The 2026-07-26 ruling says Harbinger lore **need not align BETWEEN products** — there are hundreds of them and
> Collectors fall daily; only **Vane** (the First Harbinger) and **Slate** (the first redeemed) are canon-bearing
> across builds. That half is **dissolved and must not be re-opened.** E5 and E6 were the *other* thing: splits
> **inside this repository**, one character with two mutually exclusive titles and origins across two files. The
> ruling permits divergence between games, never within one file set. A `dimensions-agree` CI check now asserts
> the harbinger title in `dimensions/<d>.json` equals the one in `characters/harbingers/index.json` — the exact
> check that would have caught both.
>
> #### ⚑ Five rows opened while closing the above — verify before acting on any of them
> 1. **The Dimension Eater is typed two ways.** DB row `creatures` id 155 says **Shadow/Cosmic**, ability
>    **"Reality Hunger"**; the story node says **Void/Cosmic Horror**, traits **Reality Consumption ·
>    Dimensional Collapse · Nolem's Hunger**. The lore record carries both under `type` and `dbType` rather than
>    picking a winner.
> 2. **`void_terminus_defeated` exists only in the MMO spec.** The Discord game runs
>    `og_nike_blessing_received` → `void_terminus_complete`. An enumeration difference, not a conflict.
> 3. **`GAME_SPEC.md` §3.15's "Five Great Mysteries"** (Incomplete Prime · Charles Divergence · Sixth Champion ·
>    Dexter Pattern · OG Absence) is a **second, disjoint mystery set** with no home in this repository at all.
>    Harmless to the Tier-3 lint, which keys only on Tier 3 — but it is a real gap.
> 4. **`CANON.md` §4.1 is FROZEN at "six questions" while SEVEN subjects are now dark** — `lost-singular` joined
>    by owner deferral 2026-07-26. Recommend a **note** under §4.1; do **not** renumber a frozen section.
> 5. **O1's premise was wrong** — restated above on measured pronoun counts.

> #### ✅ W1 + W2 executed — and they carried a third defect the register had not recorded
> All six lore anchors now match live engine state 6-for-6, by `id` **and** display name, and each lore entry
> now carries the engine `id` so the pairing is checkable rather than inferred.
>
> **The third defect:** every lore anchor read `"obtainedFrom": "<Boss> after freeing him"`. The engine grants
> them on **defeat** — `grantedOnBossDefeat: true`, and `grantAnchor` sits in the `completion` block as a
> *sibling* of `setFlagsOnCatch`/`setFlagsOnKO`, so it fires on either outcome. "After freeing him" is exactly
> the `_freed` gating that `CANON.md` §5.2 and both game repos' `CLAUDE.md` forbid, because it softlocks the
> supported KO path. All five now say the anchor is granted on defeat, both resolutions counting.
>
> **Void Terminus is legitimately different and this is not a contradiction.** `final_fragment` is
> `grantedOnBossDefeat: false, grantedByNPC: "OG Nike"` — a gift, not a drop. That is what lets
> `dimensions/index.json`'s *"No region anchor Legendary — deliberate. The bottom of the world is not a boss."*
> and `Nikeverse-mmo-rpg-from-scratch/docs/story/SPINE_LOCK.md` §8's *"Void Terminus 'no region anchor' is correct"* both
> stand while the region still completes the set of six. The new lore entry says so explicitly, so nobody
> "fixes" it into a boss drop later.

---

## 2 · This repository is right — a game should change

| # | What | The game says | This repository says | Note |
|---|---|---|---|---|
| L1 ⚠️ **RE-OPENED** | **Who is in the trap** | *"He's felt this signature before — for 3,000 years, pressed against it in the space-time trap"* — of **OG Nike**; and, elsewhere, of Nike Prime *"before he walked into the trap. Before he sealed himself away"* | **At the moment of the fall: NOLEM ALONE** — Nike Prime and Shiro detached in transit. **Thereafter: whereabouts UNKNOWN by ruling** (the 3,000 years are open expansion space; the repo's own files say "location unknown since the Prime Era", not "landed alive elsewhere" as a standing fact) | ⚠ **This row's own ruling was the part that failed.** It previously said *"Nike Prime is in the trap… fixable with a preposition"* — but Comic Book 1, now in-repo, contradicts the premise both sides shared: *"Shiro and Nike Prime were able to **detach** from Nolem. It looked like **Nolem** was headed where he was supposed to go in the pocket dimension. I'm not sure where the other two landed."* (`comic-books/book-01/script.md:1033`), then they land alive and conscious (`:1037-1040`). The preposition remedy is **void**. The fall is also **forced, not chosen** (`:995`), so *"walked into"* and *"sealed himself away"* are wrong on volition as well as outcome — making `void_terminus/act2_009_elbonzys_boss.json:96` a **second disputed site**, spoken by an uncorrupted truth-telling NPC. **The OG Nike half is a GAP, not a contradiction** — Book 1 never names OG Nike (grep = 0). The lore and build spec are corrected; **the shipped game is deliberately NOT edited**. Do not flip this row to a new certainty either: Charles AI's report is hedged (*"It looked like… I'm not sure"*), and the owner has ruled the following 3,000 years are open expansion space, so a later re-entry is permitted but not canon. **Status: open.** |
| L11 🆕 | **The overflow store is called "storage"** | The shipped Discord game already runs **exactly the sanctioned shape** — an unbounded `player_creatures` table plus a 6-slot `party` — and calls the overflow **"storage"** in player-facing text: `commands/party.js:260` (*"Storage Only"*), `:1050` (*"This Nike will be moved to storage"*), `:1492` (*"Removed Nikes go back to storage"*) | **ONE SOUL, MANY LIVES** (`CANON.md` §1.2.2): the Sanctuary is *a place with residents, never a container with contents*; **"storage" and "box" are banned** and the retrieval verb is *visit* | ⚠ **CORRECTED 2026-07-30, same day — the first version of this row said *"the mechanic agrees; this is a wording divergence only"* and that is FALSE.** The store shape does agree, but the shipped game's actual product answer to repeat accumulation is a **disposal flow that converts souls into currency**: `deployCommands.js:88` (*"Browse & **release duplicates** (send to Truffle Pastures)"*), `handlers/exploreButtons.js:116` + `systems/battle/BattleHandler.js:58,82` (*"💡 **Too many Nikes?** Release **extras** to Truffle Pastures"*), `commands/species.js:293,450` (*"🌾 **Truffle Harvest:** +N Nexus Coins"*). *"Too many Nikes?"* is the exact sentence `CANON.md` §1.2.2 exists to forbid, and Nexus-Coins-per-soul is the going rate it bans. **This is a DESIGN divergence, not a wording one**, and the ruling is therefore *not* de-risked by the shipped precedent. **GRANDFATHERED** — do not edit the shipped game. **The signal worth keeping:** the MMO independently grew the same shape (`GAME_SPEC.md:1938`'s Return-home faucet pays Resonance + Bond-Echoes), so two builds arrived at soul-for-currency on their own. That is faucet pressure, not coincidence, and it needs a stated rule rather than an assumption. Storage-noun sites also include `commands/inspect.js:237`, `commands/items.js:442,1091,1165,1183,1339`, `commands/movelist.js:111,210`. |
| L9 🆕 | **A Retnuhxed told it can come back** | `nolem_maw/miniboss_void.json:99` — YOUR LEAD NIKE, to the Retnuhxed Void: *"You can be something again. **Nothing isn't permanent.**"* (+ `:94` intact memory, `:124` it is changed by the encounter, `:135` reward *"A piece of nothing that learned to be something"*) | **Retnuhxed is past reaching** (owner, 2026-07-29) | The most explicit "a Retnuhxed can come back" line in any repo, spoken by the player's own Nike in the final approach to Nolem. **GRANDFATHERED — narrative only**, no mechanical breach (`is_nike=0`, no `catchOpportunity`). Do not edit the shipped game. New MMO writing must not repeat it. |
| L3-b 🆕 | **A full redemption arc played on a Retnuhxed** | `nolem_maw/miniboss_apex.json:52, 61, 109, 130` — *"You don't have to serve Nolem"* · *"Nature can change. We've proven that."* · APEX: *"Freedom… I will... consider this."* | same | **Same node as L3, different clause.** L3 fixed the *origin* clause (`:56` is now the corpus's cleanest statement of the ruling — *"Corruption implies something still underneath, waiting. **Do not look for that in me.**"*) and left the *redemption* clauses standing, which contradict it four lines later. **GRANDFATHERED.** |
| L3-c 🆕 | **The fifth L3 site — in the TUTORIAL, and unregistered** | `hub/hub_003_baptism_by_fire.json:51` — CHARLES: *"You FREED it. Retnuhxed are already dead—**souls consumed**, bodies puppeted…"* (sibling `hub_002:25` *"**nothing left inside** but hunger"*) | `CANON.md` §2.1: a slain husk *"releases a **warm soul-mote** — the trapped soul finally let go"* | ⚠ **Highest-value new row.** L3's own fix note says it was *"four sites not one"* — **all four were in `miniboss_apex.json`. This is the fifth**, it is the player's FIRST Retnuhxed, and *"souls consumed"* directly negates the soul-mote ruling. Also trips the SEVER GUARD (*no voice may describe it as a release*) and §5.1's bare-"freed" warning. **GRANDFATHERED**, but new writing must use *"the soul is still in there and cannot be called back"* — the model at `OPENING_ARC.md:208`. |
| L10 🆕 | **OG Nike called corrupted** | `systems/raids/RaidBossConfig.js:2502` — *"Now OG Nike staggers through dimensions, **half-corrupted**, fighting himself."* | `CANON.md:133` **RATIFIED**: *"OG Nike is the Template, **uncorrupted** but exhausted."* | One of the three explicitly-uncorrupted Legendaries, called corrupted in a shipped raid backstory. **GRANDFATHERED.** Note `RaidBossConfig.js:8` (*"LEGENDARY NIKES: Corrupted but SAVEABLE"*) is otherwise the best statement of the ruling in the shipped product. |
| L6 🆕 | **What the 5,555 counts** | *"5,555 individuals, each with their own story"* (`void_terminus/main_006_quiet_moment.json:57`) | **distinct Nike FORMS** (owner ruling, 2026-07-29) | Registered, **not** actioned. The shipped line predates the ruling and reads fine in isolation — a form *is* an individual under the one-form-per-universe reading, so this is a soft divergence, not a contradiction. **Do not edit the shipped game for it.** |
| L7 🆕 | **Nolem's characterisation** | the shipped portrayal the owner explicitly dislikes (*"the weakest lore of the bunch… I didn't like Nolem in it"*) | **Nolem MAKES THE WOUND**; big, scary, powerful; a full `power` profile assembled from Book 1 | Ruling: the Discord game is the **factual record of what shipped**, not a lore or characterisation authority. Shipped content is **grandfathered and NOT swept**; new writing follows the comic and `CANON.md`. |
| L8 🆕 | **The vocabulary lint vs shipped dialogue** | *"The flickering **core** needs **fuel** only genuine warmth can provide"* (`nolem_maw/main_006_campaign_complete.json:49`) and ~7 more bond+*burn/drain/energy* pairings | **NOTHING IS CONSUMED** — Nike Prime is held, not fuelled | The lint binds **new MMO strings only**; shipped Discord content is **grandfathered**. Registered so the divergence is known rather than silently violated. |
| L2 | **The name of the cataclysm** | "the Fracturing" (3 uses, one raid victory template) | **The Shattering / The Great Echo** | An inconsistency *inside* the Discord game — it uses the sanctioned name elsewhere (*"He existed before the Shattering"*). Prose only, no engine dependency. |
| L3 ✅ **FIXED** | **What a Retnuhxed is made of** | *"Charles was corrupted. I was **CREATED**. There is no other way for me."* | **partially absorbed beings** — and the First Tongue agrees: `Ret'nux`, *"beings absorbed by Nolem"* | ⚠ **The most consequential entry in this document.** A Retnuhxed that was created from nothing has no soul to release — which breaks the ratified `is_nike` ruling that a slain husk releases a warm soul-mote (`CANON.md` §2.1). The Discord game **contradicts itself**: its own database row for the same creature reads *"Once a legendary Nike, now…"* and agrees with this repository. Fix the story node. |
| L4 ✅ **FIXED** | **Level bands, internally** | — | `collectors-journey.json` and `dimensions/*.json` gave different bands | **This was never an open design question — it was a PROPAGATION failure, and that distinction is the lesson.** `Nikeverse-mmo-rpg-from-scratch/docs/story/SPINE_LOCK.md` has carried *"✅ FREE-ORDER LEVEL BANDS — 3/3 consensus 2026-07-26. **Each pair SHARES one band**"* since the owner ratified it; it simply never reached the lore repo or `GAME_SPEC.md`, which still carried an open ⚠ describing the very problem the ruling had solved. Applied, not re-litigated: **Frostfall ⇄ Grand Arena = 31–55** (anchor 31–45 · Deep 46–55), **Neon ⇄ Void = 71–95** (anchor 71–83 · Deep 84–95). `collectors-journey.json` had all seven ranges wrong — directionally right to overlap, numerically wrong. All seven shipped Act-2 `minimumLevel` values still sit inside their region's band, so **no Discord content changed** — but note **4 of 7 differ from the new Deep-tier floor** (Frostfall 38 vs 46 · Grand Arena 50 vs 46 · Neon 78 vs 84 · Void 90 vs 84). That is expected, not a defect: the MMO's co-banded pairs need *symmetric* floors (46/46, 84/84) or the second sibling walls, while the Discord game is hard-ordered and keeps its asymmetric values. Recorded so nobody "fixes" one product to match the other. A `level-bands` CI job now enforces it. |
| L5 | **`dimensions/index.json` vs its own detail files** | — | Void Terminus and Nolem's Maw rows disagreed with their per-dimension files | ✅ **FIXED** — reconciled, with a CI check so it cannot recur. |

> #### ✅ L3 executed — in the game, as ruled, and it was four sites not one
> `campaign-data/story_nodes/nolem_maw/miniboss_apex.json`. The created-from-nothing premise ran through the
> node description, the chamber narration (*"Nolem refined his creations… his masterwork"*), the line itself,
> and the parting warning (*"I was created by him"*). All four now rest on hollowing. The Apex keeps his
> despair and his refusal — he **was** someone and declines to go looking — so nothing was redeemed to fix a
> cosmology. One detail this register had slightly off: the `Ret'nux` support is in the dictionary entry's
> **`notes`** field (*"Describes beings absorbed by Nolem"*), not its `meaning` (*"Shadow servant; entropy's
> hand"*). The claim stands; the citation is now precise.

> #### ⚑ Found while fixing L3 — a scope question, NOT a defect. Do not "fix" this.
> `CANON.md` §4.2 (**FROZEN**) says the Collector never speaks, with *"Carry me."* the single reserved line.
> The Discord game uses **`"speaker": "COLLECTOR"` 663 times** across its story nodes, including in this very
> node. That is the shipped product's established convention, and §4.2's provenance (`CANON.md` §6) is the
> **MMO** spec — `Nikeverse-mmo-rpg-from-scratch/docs/GAME_SPEC.md:113, :395, :429` — not the Discord game.
> **Open question for the owner: does §4.2 bind the Discord game at all, or is it an MMO-only design law?**
> Recorded here so a future session that reads `CANON.md` and then greps the Discord repo does not open 663
> "violations" and start rewriting shipped dialogue.

> #### ✅ E4 + O5 executed — and the copy-paste had a twin
> Bertus's `gameEncounter` was rebuilt from the shipped Frostfall nodes and his `quote_game` is now his own wound
> line; the duplicate string is gone (1 occurrence left, Colossal's, correct). **A second, independent
> Bertus↔Colossal swap turned up next door:** `CANON.md`'s illustrator note attributed *"majestic lion, greatest
> beast king"* — Bertus's description — to **Colossal**, whose own is *"Mountains tremble at its approach."* Two
> swaps between the same pair is a pattern, not an accident. Fixed.
> **Also caught in passing, and it is the softlock law again:** Viking's record read *"**Freeing** Viking Nike
> begins the thaw."* The engine gates `act2_001_the_thaw` on `viking_nike_**defeated**`. Same defect class as W1.
> Corrected to name defeat, with "either resolution counts" made explicit.
> **⚑ `campaignBoss` — RE-ANALYSED 2026-07-26.** *(The Act-2-is-post-campaign premise below is itself SUPERSEDED 2026-07-27 — see W5. The `campaignBoss` conclusion still stands, because that field means "an Act-1 boss fight", which is unaffected by when the Deep tier opens.)*
> It was recorded here as "a 21-record inconsistency" implying 20 records should flip to `true`. The shipped data
> says the opposite. **Act 2 is post-campaign endgame** — every Act-2 chain entry is gated on `campaign_complete`
> (8 entry nodes carry it; the 55 downstream nodes chain off them). So an Act-2 boss is *not* a campaign boss, and
> the 20 `false` records are CORRECT.
> **Exactly one record is doubtful: Melon.** He is `campaignBoss:true` but his chain entry
> (`nolem_maw/act2_001_betrayer_path`) requires `campaign_complete` — post-campaign by the same test. E10 promoted
> him on the criterion "an Act-2 sub-boss with a `catchOpportunity`", which **20 other records also satisfy while
> reading `false`.**
> **Also corrected:** this register and Melon's own `campaignBossNote` both claimed his node has "no
> `isAnchorBoss`". **False** — it sets `isAnchorBoss:true`, which is the engine's CATCHABILITY gate, not a
> region-anchor marker. What he lacks is `grantAnchor`.
> **The six `grantAnchor` holders (the real anchors):** Viking · Nike Tyson · Gladiator · Cyberpunk · Ninja ·
> **OG Nike** (`void_terminus/main_005_og_nike.json` → `final_fragment`). Note OG Nike grants an anchor without
> being a boss fight, and correctly reads `campaignBoss:false` — which is itself evidence the field means
> *boss fight in Act 1*, not *anchor*.
> **Recommended ruling:** `campaignBoss` = "a boss fight in the main campaign (Act 1)". Revert Melon to `false`.
> One record changes, not twenty. Owner call — do not sweep before it.

> #### ⛔ HARBINGER ENTRIES DISSOLVED — owner ruling 2026-07-26. Do not work E7, E8 or W4.
> **Harbingers are a POPULATION, not a cast.** Hundreds of them; Collectors fall every day; in the MMO a Hollow
> player *becomes* one. Six are named and authored; the rest need no lore. **Therefore Harbinger lore does NOT
> need to align across games** — different products may give them different names, titles and premises, and that
> is not a defect. See `CANON.md` §3.1.
> - **E7 (Yuki's premise — dead-love vs living-caged-master) — DISSOLVED.** Each game picks its own. The MMO's
>   Shinden spec simply states the MMO's version; it need not match the Discord game.
>   **⚑ 2026-07-27 — this repository's OWN copy still changed, and that is not E7 being worked.** The owner
>   ruled separately that Yuki is a girl and her backstory is **devoted-student, never dead-love**. Fixing E6
>   rewrote `dimensions/shinden.json`'s harbinger block anyway, and leaving a dead-love premise there while
>   `characters/harbingers/index.json` said devoted-student would have re-created the exact internal split E6
>   exists to close. Cross-game divergence on Yuki remains permitted; this repo just has to agree with itself.
> - **E8 (Slate / Echo / Abyssal Horror titles the game doesn't use) — DISSOLVED.** Cross-game title drift is now
>   explicitly permitted.
> - **W4 (the Abyssal Horror's title differs) — DISSOLVED.** Same class.
> - **E5 and E6 SURVIVE, rescoped to internal coherence only.** Both are splits *inside this repository*
>   (`dimensions/*.json` vs `characters/harbingers/index.json`). One repo giving one character two titles is an
>   ordinary error and still gets fixed — the ruling permits divergence *between games*, not *within a file set*.
> - **O1 (Yuki's pronouns) is UNAFFECTED** and still open. It is a respect question, not a lore-alignment one.
>
> **NET-NEW and canon-bearing: THE FIRST HARBINGER.** The first Collector ever to fall and worship Nolem —
> likely strongest, and the leader. This one DOES need to align everywhere. He does not exist yet.
> ⚠ **Naming collision to resolve first:** "First Harbinger" already means *"first Harbinger **redeemed**
> in-game"* (Slate) in `characters/harbingers/index.json` and `dimensions/grand-arena.json`.

> #### ✅ E1 CLOSED HARDER — the Hydra has THREE heads, in the ART too (owner, 2026-07-26)
> The prior reconciliation everywhere was *"trait named `Three Heads`, visual is 5 heads."* **The owner has ruled
> the image is three as well.** So there is no split to maintain: three heads, destruction · caution · sleep, in
> the art and in the trait name alike. The two extra heads (*"paranoia, calm"*) were never canon.
> **Corroborated by the shipped voice**, which has exactly three speakers: *"FINALLY FREE! I say we DESTROY
> everything!" / "Wait. We should assess—" / "I just want to go back to sleep."* The design doc reads them the
> same way — a **parliament**, a council that argued its way to a decision, silenced into one agreeing voice.
> Swept from both spec twins (6 sites). The trait name `Three Heads` stays — it is live code the raid
> survive-chokepoint keys off by string.

---

## 3 · Open — the owner has not ruled

| # | What | Why it is open |
|---|---|---|
| O1 ✅ **RULED — Yuki is FEMALE, she/her (owner, 2026-07-26)** | **Harbinger Yuki's gender** | **The premise was measurably wrong and is now corrected.** Not "male throughout the shipped Shinden arc" — in `shinden_008_shadow_temple.json` the pronouns run **13 female to 5 male** — and **not all five are strays**: *"drawing **his** blade"* is RONIN CHARLES and *"the master **he** still loves"* is Ninja Nike, both correct third-party references. The actual Yuki-misgendering is **two to three pronouns**, sitting *inside the same sentences as the female ones* (*"**She** was the first to accept Nolem's whispers after **her** master fell… **He** guards the Temple…"*). So the shipped game's dominant voice already matches the owner ruling, and what exists is a **pronoun bug inside one shipped node**, not a lore-vs-game divergence. The lore file was already right. **Do not sweep the Discord repo** — that story is owner-frozen (see W5); the strays are recorded here, not fixed. |
| **O7** ⚠ **OPENED 2026-08-01 — the highest-stakes row in this register** | **The 5,555 simultaneous hold is this bible's stated VICTORY, and the MMO has ruled it permanently unreachable** | `CANON.md:31-33` — *"whole only when all 5,555 **forms are held at the same time**… **The simultaneity IS the victory**."* Against the build's owner ruling of **2026-07-31** (*"defended, but i want the score to never be able to sustainably hold 5555"*), implemented as the load servo's **`X_target ≥ 1` — he ALWAYS keeps one** — which makes **5,554/5,555 a hard ceiling at every population forever.** So the condition this bible calls *the victory* is now **unsatisfiable by construction**, and **nothing in this repository has been told.** ⚠ **This is probably not a contradiction to be "fixed" but a ruling to be RECORDED**: the same owner ruling re-pointed the realm's job from *win* to **DEFEND** (*"hold the weave and go get back whoever he takes"*), moved the permanent goal to the **personal Bond Log**, and gave the *won* object a different form — a season held all the way through gets **NAMED**. Read that way, simultaneity survives as the **mythic** frame while ceasing to be a live game state. **But this bible states it flatly, as the victory, with no such bound** — so a reader here believes a win condition the build has ruled out. **Owner call: does §1.2's simultaneity keep its status as *the* victory (and the servo floor is wrong), or does it take a bound (and this bible needs the amendment)?** Do not resolve either way without the owner: §1.2 is RATIFIED and the floor is *derived, not tuned*. |
| O2 | **Is Melon corrupted at all?** | This repository and the Maw node say entirely uncorrupted. The raid layer says *"neither fully corrupted nor truly free — the shadow clings to him."* A game-internal split as much as a lore one. |
| O3 ✅ **CLOSED by L4** | **Per-region level bands** | **The premise no longer holds.** This row said this repository's bands are "a clean non-overlapping partition" — after L4 they deliberately OVERLAP: Frostfall and Grand Arena both 31–55, Neon and Void both 71–95, per the owner-ratified co-banding in `SPINE_LOCK.md`, and a `level-bands` CI job now *enforces* the overlap. The row also sat under "the owner has not ruled" when the owner had ruled, on 2026-07-26. The residual observation survives and is still true: the enforced gates are per-node minimums, so region bands are pacing guidance rather than hard walls. |
| O4 | **Neon City's Charles** | "Analog Charles" here; the shipped node uses "Neon Charles" throughout while titling him "The Analog Rebel". Possibly two names for one character on purpose. |
| O5 ✅ **RULED — fix both (owner, 2026-07-26)** | **Fixing Bertus (E4)** | Correcting it **invalidates a landed design document**: the prior MMO's `LEGENDARY_MOTIVATIONS.md` records "OLD motivation: guilt over a dimension he broke" and builds a whole new wound on that premise. The premise was a copy-paste error. **Owner ruled Option B: correct the lore AND rewrite the design row.** Both landed; the `ABSOLVE` freeing-key was re-keyed to `OFFER-THE-HALL` because a fulfillment premise leaves nothing to absolve. |
| O6 | **The anchor count shown to players** | Two shipped surfaces disagree: one progress bar renders **/7**, the map footer renders **/6**. Engine truth is six; the /7 comes from a flag list containing a phantom entry no node ever sets. A game bug, recorded here because it is player-visible. |

---

## 4 · Extensions — the games elaborate where this repository is silent

**These are not conflicts.** Silence is not contradiction. Listed so they are not mistaken for drift.

- **The 4,892 timelines.** Nolem has consumed everything in 4,892 documented timelines. Ten occurrences across six live story files, including a stated objective. Nothing here contradicts it. **Recommended for adoption** — if adopted, note that a shipped line derives *"in 4,891 of them, you fail"*, so the two figures must stay in lockstep.
- **"The Seven-Tongued Deceiver."** Nolem's epithet in the Maw, with a seven-mouths boss mechanic behind it.
- **The Harbinger / Retnuhxed intelligence axis.** Retnuhxed are mindless; Harbingers are intelligent and *chose*. Consistent with the taxonomy here, and sharper than it.
- **Resonance, Composure, the Bond Struggle, Pattern Integrity, and putting a soul down for good.** All net-new game systems. This repository has zero occurrences of any of them as named states. Tune freely — only the *simultaneity* of the 5,555 (`CANON.md` §1.2) is canon.
- **The Legendary rarity tier.** The database has 38 creatures at `is_nike=1, rarity='Legendary'`; this repository names 27. **Not a contradiction** — a rarity tier and a narrative roster are different things, and the database proves it: all 27 canon Legendaries are batch `C` with `ABCD###` ids, the 11 extras are batch `B`. The extras are wild-catchable and have no lore entry, which is a content gap rather than a canon conflict.
- **`purificationThreshold: 0.15` — the 15% purify gate. NOT A DIVERGENCE, and this row exists so nobody opens it as one.** `BattleHandler.js:201` and `BattleEngine.js:91` both set `this.purificationThreshold = options.purificationThreshold || 0.15`: beat a corrupted Nike below 15% HP and *"💜✨ **The corruption shatters!**"* (`BattleEngine.js:858`). Set beside `CANON.md:265` — *"A soul opens only to calm and closes against injury"* — that reads as a flat contradiction: the game appears to require exactly the injury the lore forbids. **It is not one. The two sentences govern different acts** (`CANON.md` §5.3, RATIFIED 2026-07-28). Corruption is a **numbing that was accepted**, not the Nike, so the damage phase is aimed at the numbing — the shipped strings say so in as many words: *"Reduce its HP below 15% **to break the corruption** and enable catching!"* (`BattleHandler.js:1406`) and the button label `💜 Purify (HP<15%)` (`BattleEngine.js:878`). **The reach — the act §5.1 actually governs — begins where the numbing ends.** From that instant **both games enforce §5.1 *more* strictly than the lore states it**: Discord **forfeits the catch outright** on a post-purify KO and returns the soul to the void (*"💀 If it **faints**, it escapes back to the void and continues roaming"*, `handlers/exploreButtons.js:1112`; *"fades back into the mist, the corruption still clinging to it… It will continue to roam this region"*, `:1572` — which is `CANON.md:284` rendered as a shipped outcome), and the MMO makes post-crack damage strictly counterproductive: pre-crack the soul is not yet `isNike` so soothe/bond cannot even be attempted, post-crack a hit on a soothed Nike recoils its bond meter and a hit on the Collector mid-Struggle auto-misses the pulse into a graded break (`nikeverse-mmo-rpg/src/sim/sim.ts:4015, :4069`), and striking on regardless *is* Sever, routed to the death chokepoint. **⚑ Always state the bound when citing this row: *"damage is always for their own good"* is FALSE** — true of the numbing, false of everything after it. **⚠ And the vocabulary: the act is a WAKING, never a *freeing*.** The shipped verb is already the right one (*"bond and awaken"*, `handlers/exploreButtons.js:1108`; *"💜✨ Echo Bonded & Awakened!"*, `:1560`); "freed" would be a third sense of a word `CANON.md` §5.1 already warns carries two.

---

## 5 · Refuted — do not raise these again

Each was investigated and did not survive.

| Claim | Why it fails |
|---|---|
| "Void Terminus's side-quest roster does not match what shipped" (part of W6) | It matches **4/4**. `hope`→"The Ember's Last Light" (the NPC *is* THE EMBER) · `mirror`→"Shadow-Self Confrontation" · `walker`→"The Previous Failed Walker" · `survivor`→"Consumed Dimension Survivor". Only the array **order** differs, and order is not canon. |
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
