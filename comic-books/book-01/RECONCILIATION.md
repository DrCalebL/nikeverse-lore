# THE RULING REGISTER — Book 1 vs. the corpus

> **STATUS: AUDIT OUTPUT — proposals, not rulings.** Produced 2026-07-29 by a 122-agent sweep of Book 1
> against all four repos (298 claims extracted, 137 findings, 74 refuted under adversarial verification,
> 38 survived). Every `proposedRuling` below is a **recommendation to the owner**, not a decision. Per the
> Tier-0 rule in `../README.md`, only the owner rules. Items already ruled are marked in `claims.json`.
>
> **Two of its own framings were corrected after the fact and are left visible as written:** the audit was
> briefed that "the comic wins and the docs change," which the owner's Tier-0 ruling supersedes; and it
> repeats the brief's wrong path `comics/book-01/` for what is now `comic-books/book-01/`.


**Source:** `/home/user/nikeverse-lore/comic-books/book-01/script.md` (1,059 lines — note the brief's path `comics/book-01/` does not exist).
**Authority:** `comic-books/README.md` — Tier 0 = the owner, Tier 1 = the comic, then everything else. The owner has ruled this session that the comic wins and the docs change; that ruling is broad but it is **not itemised**, and the README's process (`claims.json` → put the collision → log in `CHANGELOG.md` → land all three artifacts in one session) still governs each edit.
**Process defect to fix first:** `comic-books/book-01/claims.json` **does not exist**. The reconciliation pass required by `comic-books/README.md` steps 2–7 has never been run for Book 1. Every ruling below should become a `claims.json` entry before it becomes a diff.

---

## 1. The headline

Book 1 does not overturn the cosmology — it overturns the **last four pages of the Prime Era**, and it exposes one fabricated quotation that has been circulating as verbatim canon in four repositories: Nolem alone goes into the pocket dimension, Nike Prime and Shiro **detach in transit and land elsewhere alive**, Shiro is never wounded and never absorbed into Charles AI, the surviving Nikes are **stranded on Colosseum World** rather than choosing to scatter, and Engineer Nike — who is alive at the end of the book — never says *"Wait, the empathy core isn't—"*. Everything the first-pass audit alleged about the 5,555, the Shattering, simultaneity, Pattern Integrity, Free/Sever, the Sixth Seat and the Shinden mist **failed adversarial verification**: the comic is *silent* on those, and silence is a gap, not a contradiction — which means **the change to the 5,555 is the owner's ruling, not the comic's finding, and must be logged as such** or the corpus will end up citing Book 1 for a claim Book 1 does not make. The single biggest way current canon is wrong is therefore narrower and more fixable than feared: **the docs mis-transcribe the ending of the primary source, and one invented line of dialogue is load-bearing in `GAME_SPEC.md`, the Tesana twin, and the lore JSON.**

---

## 2. FOUNDATIONAL rulings

### F1 — Nike Prime is NOT in the trap. Nolem went in alone; Prime and Shiro detached and landed alive.

**Comic (dialogue — the strongest evidence class), script.md:1033–1035**, Charles AI:
> *"From what I saw after they fell through the portal, Shiro and Nike Prime were able to detach from Nolem. It looked like Nolem was headed where he was supposed to go in the pocket dimension. I'm not sure where the other two landed."*

Corroborated by the closing page — **art direction, script.md:1037–1038**:
> *"DRAW NIKE PRIME AND SHIRO LANDING IN THIS ROOM WITH THE DIGI JOINTZ. NIKE ON HIS KNEES, SHIRO ON HIS FEET"* — and Nike Prime's line at :1039, *"Where the heck am?"*

And the forced, non-elective fall — **art direction, script.md:995**:
> *"DRAW A BEAM COMING OUT OF CHARLES AI AND IT HITTING NOLEM WHILE NOLEM GRABS ONTO NIKE PRO AS THEY FALL INTO A PORTAL THAT SHIRO CREATED"*

**Canon,** `nikeverse-lore/characters/comic-characters.json:105,113`:
> `"status": "Trapped with Nolem"` … `"location": "Inside the trap with Nolem. Still fighting. For thousands of years."`

`nikeverse-lore/characters/collectors-journey.json:136`:
> *"Nike Prime is still inside the trap with Nolem, fighting endlessly for three thousand years."*

`Nikeverse-mmo-rpg-from-scratch/docs/GAME_SPEC.md:223`:
> *"**Nike Prime and Nolem fall into the trap together** (whether intentional or accidental is deliberately unclear)."*

**RULING.** Two separable facts, and they must be worded separately or the fix will overreach:
- **Canon fact (what the reader sees):** Nolem alone continued to the pocket dimension. Nike Prime and Shiro detached in transit and landed together, alive and conscious, in an unnamed room containing *"THE DIGI JOINTZ"*. Nike Prime is on his **knees**, not standing.
- **In-world knowledge (what any character can say):** *"Nike Prime's location has been unknown since the Prime Era."* This is already what Stoner Nike says at :1013 (*"Nike Prime God knows where"*) and Charles AI at :1035.
- **Also settled:** the fall was **forced, not chosen**. Delete the *"deliberately unclear"* hedge and every *"sealed himself away"* / *"walked into the trap"* line.
- **NOT settled by the comic, do not bundle in:** the trap *weakening*, and the *empathy core*. Book 1 ends minutes after the trap springs. Nike Prime's *"he'll be trapped forever"* (:915–916) is a **pre-deployment design prediction spoken by a being released at 99%**, not narration of an outcome — this was tested twice and rejected as a contradiction both times. His 3,000-year fate is a Book-2 question, and a later re-entry is not excluded.

**Files that must change:**

| Repo | File:line |
|---|---|
| lore | `characters/comic-characters.json:105`, `:113` |
| lore | `characters/collectors-journey.json:136` (first sentence only) |
| lore | `timeline/prime-era.json:152`, `:204` |
| lore | `timeline/ages.json:87`, `:97`, `:102`, `:171` |
| lore | `dimensions/nolem-maw.json:18`, `:44`, `:67`; `dimensions/index.json:152`, `:157` |
| lore | `GAME_DELTAS.md:149` (row **L1** — see M1) |
| build | `docs/GAME_SPEC.md:164`, `:223`, `:229`, `:1784` |
| build | `docs/CANON_MAP.md:246` |
| prior build | `docs/TESANA_BUILD_PROMPT.md:119`, `:178`, `:184`, `:1739` — **GENERATED. Regenerate via `tail -n +N`; never hand-edit.** |
| **shipped Discord (player-visible)** | `campaign-data/story_nodes/nolem_maw/act2_003_shadow_approach.json:34` · `act2_004_prophecy_revealed.json:34` · `main_006_campaign_complete.json:30` · `campaign-data/story_nodes/hub/act2_001_return_triumphant.json:26` · `campaign-data/story_nodes/imperial_colosseum/act2_013_truth_revealed.json:41` · `campaign-data/story_nodes/void_terminus/act2_009_elbonzys_boss.json:96` · `campaign-data/regions/nolem_maw.json:451` |

**Blast radius.** Largest in the audit. Nolem's Maw as a destination is premised on Prime being inside it; the Truth Chamber reveal, the endgame raid framing (*"the real Nolem is deeper, locked in eternal combat with Nike Prime"*), and the Discord campaign-complete epilogue all assume it. Elbonzys — an uncorrupted, truth-telling eyewitness NPC — states the wrong version in shipped dialogue. **Mitigant worth reporting up:** `CANON.md` never asserts it — §1.2 (line 29) and §1.3 (line 59) survive untouched — and `timeline/prime-era.json:173–174` (*"No one knows if he's alive, dead, or fighting eternally inside the trap"*) is **already comic-compatible** and should be marked CONFIRMED, not edited. Only the un-hedged assertions collide. **Story upside:** a lost founder to be *found* is a stronger spine than a prisoner to be reinforced, and it makes the Remnant faction's *"they may have already FOUND Nike Prime"* far more interesting.

---

### F2 — Shiro is not wounded, does not sacrifice himself, and never merges with Charles AI. Charles AI leaves Book 1 with **no portal ability**.

**Comic.** Shiro opens portals casually and repeatedly at no cost — script.md:453, :648, :847, :996. He jumps in voluntarily (**art direction, :998**: *"DRAW SHIRO JUMPING IN AFTER THEM AS CHARLES AI PONDERS / CHARLES AI: Not good."*), lands on his feet (:1038) and speaks the book's last line (:1040, *"Shiro: Mow."*). Charles AI is elsewhere and reports the fall second-hand (:1033).

The decisive evidence is **dialogue, script.md:1027–1028**:
> *"Stoner Nike: You said you can reach the world where you came from. Can you reach other realities as well? / Charles AI: They have to have the Charles Chip implanted in them. But Nike Prime should know how to make one."*

and **script.md:1012–1013**: *"With Shiro gonee, our vehicle that can navigate spacetime destroyed in the battle, and Nike Prime God knows where, we might be stuck here for a while."*

**Canon,** `nikeverse-lore/timeline/ages.json:98–99` (Prime Era keyEvents):
> *"Shiro critically wounded, merges with Charles AI"* · *"Charles AI gains portal abilities and cat-like personality"*

`nikeverse-lore/timeline/prime-era.json:155–161`:
> *"Shiro's sacrifice" … "Creating the dimensional anchor points burned through Shiro's life force." … "The merge" … "To save Shiro's consciousness, Charles AI absorbs him." … "result": "Shiro no longer exists as separate entity."*

`Nikeverse-mmo-rpg-from-scratch/docs/GAME_SPEC.md:224`:
> *"**Act 5 — The Sacrifice.** Creating the trap's dimensional anchor points burned out the life force of the being who opened the portals; Charles AI absorbed his patterns to save what could be saved, gaining portal creation, a calming presence, cat-like quirks…"*

**RULING.** The wound, the burnout and the merge are inventions and must go. The **"gained portal creation"** clause is independently false and is the cleanest disproof — at :1027 Charles AI explicitly *cannot* reach realities without a chip on the far end, which is exactly why the party is stranded.

**Keep, on new footing:** the *departure* is real and is mourned in-story (:1008, :1012) — a voluntary leap after Nike Prime into a coordinate-shifting pocket dimension **is** a sacrifice, so the shipped Discord line *"Shiro's sacrifice"* (`imperial_colosseum/act2_006_professor_boss.json:54,92,122`) is comic-compatible and needs **no edit**. Likewise the **IP phase-out is not a transcription error** — `comic-characters.json:66` records that Shiro originates from a separate memecoin IP — so the *name-suppression rule survives*, but it must be re-founded on the IP note instead of on a fabricated death. Charles AI's Echo-Era portal ability then loses its stated origin; the comic leaves the following 3,000 years blank, so that is a gap the owner may fill freely. `campaign-data/story_nodes/hub/hub_004_collectors_purpose.json:69` (*"The portal abilities came later"*) is already the compatible framing and is shipped.

**Files:** lore `timeline/ages.json:98–99`; `timeline/prime-era.json:155–161`; `characters/comic-characters.json:60`, `:65`; `characters/charles-ai.json:12`, `:46–49`; `README.md:181–182`; `prophecies/mysteries.json:175` (**highest priority — the mystery lint currently lists the absorption under `mayAnswer`, so a gate is certifying a false statement**); build `docs/GAME_SPEC.md:224` → regenerate `TESANA_BUILD_PROMPT.md:179`. `MASTER_LORE_PROPOSAL_FINAL.md:340–356` is provenance — leave it as the record of where the beat came from.

**Blast radius.** Charles AI's five named cat-quirks, the Convergence Hub transit diegesis, and `GAME_SPEC.md:224`'s hard rule all sit on this. **Tier-3 safety note:** this is a *fate* correction, not an origin reveal — `CANON.md` §4.1 #6 (*"Where Shiro came from"*) stays frozen, and the comic ratifies it (see C7).

---

### F3 — Engineer Nike's "last words" are fabricated. He is not dying, and the words are not his.

**Comic (dialogue), script.md:873–874:**
> *"Botanist Nike: His size is good, how far away are we from 100% completion? / Engineer: We're at 99% so based on rate of growth, speed of processing of informa- SHIRO NO"*

He speaks again at :885 (*"Nike, you were released a bit before you were 100% complete. How do you feel?"*) and :906, and is alive in the basement at :1010. **`grep -c "empathy" script.md` = 0**, verified against both the extracted script and the PDF content streams.

**Canon,** `nikeverse-lore/characters/comic-characters.json:77`:
> `"lastWords": "Wait, the empathy core isn't—"`

`Nikeverse-mmo-rpg-from-scratch/docs/GAME_SPEC.md:222`, inside §3.5 headed *"The Prime Era — Comic Book 1"*:
> *"He emerges at **99% completion — the empathy core was never integrated** (Engineer Nike's last words: *"Wait, the empathy core isn't—"*)."*

and `GAME_SPEC.md:405`, inside §3.17 *"Canon dialogue — preserve verbatim"*:
> *"- **Engineer Nike** (last words): "Wait, the empathy core isn't—""*

**RULING — split it, and only half moves.**
- **(a) The quotation is fabricated and must be deleted from all four repos.** A line presented as letter-for-letter canon that the Tier-1 source does not contain is the most dangerous class of error in this project. Origin traced: `MASTER_LORE_PROPOSAL_FINAL.md:790–797`, where it was written as a *speculative bullet* under "Mystery #1: The Incomplete Prime → The Conspiracy" and was later promoted to verbatim canon. Correcting a false statement *about the primary source* needs no owner ruling; whether the line survives as an acknowledged non-comic invention does, because `GAME_SPEC.md:402` currently mandates it verbatim.
- **(b) "Empathy core" itself STAYS unless the owner says otherwise.** Tested twice and rejected as a contradiction both times: the comic never names the missing 1% (the Engineer is cut off mid-word answering a *"how far away"* question) and never denies an empathy core. Doc-adds-detail is a **GAP**. The comic's *"I'm feeling several things simultaneously"* (:892) does not collide with the docs either, because the docs claim Prime cannot **BOND**, not that he cannot feel. `CANON.md:73` (§1.4, the Weaver) is untouched.
- **Recommended replacement if the beat is wanted:** the comic supplies a real line in the right mouth at the right beat — **script.md:885**, *"Nike, you were released a bit before you were 100% complete."*

**Minimum safe edit pending the ruling:** rename `comic-characters.json:77`'s `"lastWords"` key (e.g. `"attributedLine"`), annotate that it does not appear in Book 1, and drop the death implication — which already contradicts that same file's `"fate": "Unknown. Possibly joined the Lost Builders"` (:78).

**Files:** `characters/comic-characters.json:77`; `MASTER_LORE_PROPOSAL_FINAL.md:795` (annotate as the invention site, do not delete — it is provenance); `GAME_SPEC.md:222`, `:405` → regenerate `TESANA_BUILD_PROMPT.md:177`, `:360`.

**Blast radius: SMALL, and this is the good news.** The empathy-core reveal chain is footed independently — `CANON.md` §1.4 (RATIFIED), `CANON_MAP.md:58`, `SPINE_LOCK.md:306`, `singulars/index.json:53` — and the **shipped** Discord game stages the whole reveal through an anonymous *"SCHOLAR RECORDING"*, with **zero** occurrences of "Engineer Nike" anywhere in `campaign-data/` or `systems/`. Removing the quote costs the chain nothing.

---

### F4 — The Champions do not scatter in the Prime Era. Book 1 ends with them **stranded**, and the three quoted "Scattering" lines are fabricated.

**Comic (dialogue), script.md:1012–1013 and 1016–1018:**
> *"Stoner Nike: Okay guys, new plan. With Shiro gonee, our vehicle that can navigate spacetime destroyed in the battle, and Nike Prime God knows where, we might be stuck here for a while."*
> *"Gladiator Nike: There is more to this world than what we've accomplished here today. Jobs and housing for each of you. All of us have things we specialize in. Together we'll work to get all of you back where you belong."*

**Canon,** `nikeverse-lore/timeline/prime-era.json:202`:
> `"immediate": "Champions scatter to guard home dimensions"`

`nikeverse-lore/timeline/ages.json:100` (Prime Era keyEvents): *"Champions scatter to guard their home dimensions"*

`Nikeverse-mmo-rpg-from-scratch/docs/GAME_SPEC.md:225`:
> *"**Act 6 — The Scattering.** The Champions wait months for Nike Prime — *"We'll wait for Nike Prime to return"* (Gladiator); *"We can't all stay here. Our dimensions need us."* (Viking) — then scatter… *"We'll meet again when Nike Prime returns."*"*

**RULING — this is a scope error, not a false event.** The Scattering is **CONFIRMED as intent** and **REFUTED as a Prime-Era / Book-1 event**. The comic's immediate aftermath is: stranded on Colosseum World, transit destroyed, Gladiator offering settlement plus a shared project to get everyone home. Crucially, **`timeline/long-silence.json:11–22` already has it right** — The Vigil, 0–50 years, *"Champions wait at the Colosseum for Nike Prime to return. He never does."* → `"endsWhen": "Champions agree to scatter to their home dimensions"`. That entry is CONFIRMED and must **not** be touched. The three quoted lines appear nowhere in `script.md` (verified: 0 hits for *"We'll meet again"*, *"Our dimensions need us"*) and trace to `MASTER_LORE_PROPOSAL_FINAL.md:370,375,378`.

**Files:** `timeline/prime-era.json:6`, `:202`; `timeline/ages.json:100`; `GAME_SPEC.md:225` (move Act 6 out of §3.5, or mark it explicitly *post-Book-1, authored*) and `GAME_SPEC.md:408` (demote the three quotes out of the verbatim-canon list) → regenerate `TESANA_BUILD_PROMPT.md:180`, `:363`.

**Blast radius: moderate and entirely benign.** The eight-region map presupposes each anchor is home 3,000 years later — the comic does not forbid that, it *promises* it (:1016–1018) and defers it. Only causation and the invented dialogue change. **Story upside:** Gladiator genuinely led the Champions in peacetime for years, which is a far stronger root for *"a loyalty with no one left to lead"* than a farewell.

---

## 3. MAJOR rulings

### M1 — `GAME_DELTAS.md` row **L1** must be re-opened; its own ruling is the claim in question.
`GAME_DELTAS.md:149` rules a shipped line wrong because *"**Nike Prime** is in the trap"*, and calls it *"a one-line authoring slip… Low blast radius… Fixable with a preposition."* Under F1 the ruling column is the part that fails. Re-scope the row: not *"OG Nike should be Nike Prime"* but *"the who-is-in-the-trap premise is itself in dispute"* — so the preposition remedy is void. Also **re-tag** `void_terminus/act2_009_elbonzys_boss.json:96` (*"Before he walked into the trap. Before he sealed himself away"*), which the register cites as corroboration and which is now a **second disputed site** (wrong on both volition and outcome). Set status `open`; do not flip the row to *"the trap holds Nolem alone"* — Charles AI's arrival report is hedged (*"It looked like… I'm not sure"*). The **OG Nike** half is a GAP, not a contradiction: the comic never names OG Nike. Mirror in `CANON_MAP.md:246`.

### M2 — `dimensions/index.json`: the Charles-chip origin belongs to **Computer Coder Nike's** chrome world, not Cyberpunk Nike's.
**Comic (art direction), script.md:382:** *"DRAW STONER NIKE AND SHIRO LANDING IN A WORLD FULL OF CHROME. DRAW A COMPUTER NERD NIKE…"* — the chip is discussed there in dialogue (:386, :396). Cyberpunk Nike lands separately at :647 (*"DRAW STONER NIKE AND SHIRO LANDING IN THIS CYBERPUNK REALITY. ON STREET, IN FRONT OF A TALL SKYSCRAPER"*).
**Canon,** `dimensions/index.json:115`: *"Cyberpunk Nike's home dimension… **Also where Charles Interface Chips originated.**"*
**RULING — two narrow edits only.** (1) Delete the chip clause from `:115`; the lore's own `characters/charles-variants/index.json:110–113` already places Charles AI in *"Computer Coder Nike's World"* and is the cheapest evidence that `index.json` is the file in error. (2) `dimensions/index.json:184` asserts `{"comic": "Chrome Reality"}` — the comic contains **no such proper noun** (one hit for "chrome", at :382, and it is *"a world full of chrome"*); drop the false comic attribution. **Do NOT** rename Neon City's Prime-Era name wholesale — "Chrome Reality" is a lore coinage and is defensible once the provenance is stripped, and renaming drags `GAME_SPEC.md:221` + the byte-identical twin into a three-way resync for no canon gain. The Cyberpunk→Neon City mapping is **CONFIRMED**.

### M3 — Delete the sacrifice clause from Boxer Nike's record. He survives Book 1.
**Comic (dialogue), script.md:1007–1008:** *"Stoner Nike: Charles, where's Nike Prime? / Boxer Nike: AND SHIRO? WHERE'S THAT SOFT LITTLE KITTY?!!"* — spoken after Nolem is gone and the Retnuhxed are cleared (:1001).
**Canon,** `dimensions/grand-arena.json:36`: *"In Comic Book 1, he sacrificed himself fighting Nolem directly."*
**RULING.** Delete the clause. His fight with Nolem is a **staged demonstration**, not a death: *"Boxer Niker: WE DIDN'T TEACH YOU HOW TO FIGHT YET! WATCH AND LEARN!"* (:976) → hand-off at :986 (*"YOU KNOW HOW HE FIGHTS NOW! GO GET HIM!"*). Note the correction: **Nolem absorbs Boxer's punches**, not the reverse (*"I barely feel your punches"*, :980) — do not write it up as damage-soaking reconnaissance. Also **not** uniquely immune: Nolem credits Nike Prime with resolve first (:970). This deletion **repairs** an existing internal contradiction with `grand-arena.json:37` (`"corruptionReason": "Boredom"`) and `timeline/legendary-falls.json:90–93` (he falls 500–1500 years *after* the Prime Era), and closes an already-open scrub note at `STORY_BIBLE.md:560`. No owner ruling required — this is a defect fix inside existing canon.

### M4 — Nolem's **civilisational sabotage** phase is unrecorded, and it escalates a collision with RATIFIED `CANON.md` §5.3.
**Comic (dialogue), script.md:559–560,** Charles AI: *"And now the Retnuhxed and Nolem are coming here. They won't be shy about who they hurt this time. **No politics, no games. Just straight up brutality.**"* Each Scholar's world had exactly one pillar of life broken: **birth** (:369, :564), **soil/famine by policy** (:533), **poisoned food supply** (:492) — delivered by a person in authority, Dexter Hun as dictator or poisoner (:554–555).
**Canon,** `singulars/nolem.json:43–48` (isolation / exhaustion / despair / rest) and `GAME_SPEC.md:325` (*"His method, **always in this order**"*). Silent on all of it.
**RULING.** Add the content as **delivery, not a rival method** — break the food supply and you mass-produce exhaustion; break birth and you mass-produce despair; famine isolates the survivors, after which he arrives with the offer of rest. This adds the comic without touching the locked sequence. **Escalate the real item:** `CANON.md:291–297` (§5.3, RATIFIED, owner 2026-07-28) says *"A wound has to come first, and it is not his. That is not a limitation on his method; it is his method."* — and the comic has **Nolem's own avatar manufacturing the wound**. See Q3.
**Confirmed alongside:** `singulars/nolem.json:30–31` (*"Avatar Projection… (Dexter Hun)"*) and `:77–78` (*"Takes different forms in different dimensions"*) match script.md:554–555 exactly; `nolem.json:97` already carries that his method changes across eras. Not new.
**Correction to the record:** the supporting grep claim *"famine returns zero non-comic hits"* is **false** — see `SHINDEN_SPEC.md:116` and `GAME_SPEC.md:1619` (Gashadokuro, a yokai). Do not repeat it in a canon doc.

### M5 — Retnuhxed: an imposed state that **reverts**, colliding with the taxonomy at `CANON.md:183`.
**Comic (art direction), script.md:972 →:1001–1004:** *"DRAW STONER NIKE AND A FEW GUARDS TWEAKING OUT AS IT LOOKS LIKE THEY'RE TURNING INTO RETNUHXED"* … *"DRAW CHARLES AI BACK IN THE ARENA WITH THE RETNUHXED ALL DEFEATED/DEAD AND STONER NIKE AND THE GUARDS BACK TO NORMAL."* — with the first-person memory, **dialogue, :1004**: *"I NEVER WANT TO EXPERIENCE THAT AGAIN!!"*
**Canon,** `CANON.md:183–184`: *"A fallen **Nike** is a **Corrupted Nike**, and a Corrupted Nike who has gone past saving is a **Retnuhxed** — a separate kind of being altogether."*
**RULING — `status: open`, put to the owner; do not edit.** Most of this lens's claims were refuted (the reversal is art direction, the mechanism is inferred from an off-page gap, and `CANON.md` §2.1's husk ruling is expressly bounded). What **survives** is narrow and real: a living, uncorrupted Nike was turned and turned back, which is hard to reconcile with *"a separate kind of being altogether."* Note the lore already carries the comic's version and does not know it — `timeline/prime-era.json:126–127`: *"Temporary corruption / Some soldiers and even Stoner Nike are temporarily corrupted during the battle."* Ask which thing the word names before anyone edits. See Q2.
**Blast radius:** `CANON.md` §2.1 (RATIFIED soul-mote mercy), §3.1 taxonomy, the 292/144 `is_nike` split, `GAME_DELTAS.md` L3 (already **executed** against four shipped sites), and the identical taxonomy sentence in all four `CLAUDE.md` files. High — which is precisely why it goes to the owner and not to a diff.

### M6 — Champions' Prime-Era **assignments** are unrecorded (narrowed).
The docs record *roles* (`legendary-nikes/index.json:23,46,68,89,113` `primeEraRole`) and the battle montage (`prime-era.json:130–131`); what is missing is the PAGE 19 preparation montage (script.md:762–791). Fill **only** these four, into the existing `primeEraRole` sibling — **do not** create a new schema field:
- **Ninja** — set the arena's defences with Gladiator (:640–641); trained the Colosseum troops in shuriken (:771).
- **Cyberpunk** — **upgraded** the Scholars' weapons and trained champions and troops to use them (:674–675, :773–774). *Not* the originator; the Scholars make them.
- **Boxer/Tyson** — ranged punch-energy gloves built by Engineer Nike (:783). Technology, not innate.
- **Gladiator** — commanded the defence (:830); heat-acclimated Viking Nike (:776–778).
**STRIKE "Viking = weather modification."** Unsupported: :707 is Stoner Nike telling Viking to *ask the scientists if it is possible*; the comic never answers. **Move to CONFIRMED:** Ninja's poison/paralysis kit already ships (`nikeverse.db` creature 50 — Smoke Bomb, Phantom Touch 40% paralyze); only *confusion* is absent, which is a balance decision, not a canon correction.

### M7 — Book 1 ends with **five unpaid obligations** that no document registers.
All dialogue: (1) **Nutritionist Nike joined on a condition** — *"as long as I receive help from you all afterwards to fix my world, I will do it happily"* (:502–503), accepted singular by Stoner Nike, *"It'd be my genuine pleasure"* (:504). His world is still poisoned by Dexter Hun (:492), a guise of Nolem (:554). (2) **Cyberpunk Nike was promised a fight with Nike Prime** — *"After you help us defeat Nolem and the Retnuhxed, I'll make sure of it!"* (:669–670) — now structurally unpayable. (3) **Ninja Nike was promised Shiro** — *"Can I keep him later." / "Kind of up to him but sure."* (:644–645) — broken on the page by the ending. (4) **Viking Nike was promised more cats** (:700–703). (5) **Computer Coder Nike asked for more entities like his Charles AI** (:413). Gladiator's closing pledge (:1016–1018) substitutes an *adjacent* obligation — passage home — not the promised repair.
**RULING.** Record all five as the Long Silence's authored starting conditions. This is the Vigil's real emotional content, and it is better than *"they waited."* Additive; `status: open`.

### M8 — The cross-reality **intelligence drain** is a cosmological law the corpus does not have.
**Comic (dialogue), script.md:214–216:** *"YES! EVERYONE IN DIFFERENT UNIVERSES STARTS OFF WITH THE SAME GENETICS AND HAS THE SAME BRAIN. BUTTT EACH TIME ONE OF THAT PERSON DIES, A FRACTION OF THEIR INTELLIGENCE DIES WITH THEM!"* — with corollaries: IQ loss with age (:216–220) and Alzheimer's (:224). It is the forensic signature that starts the plot: *"CTHULHU RECOGNIZED THAT SQUILYA WAS DUMBER THAN SHE SHOULD BE! SO HE LOOKED THROUGH OTHER UNIVERSES…"* (:225–228).
**RULING — three corrections to how this is filed.** (a) It is **not a Nolem ability** — it is a general law of death across variants, any cause; do **not** put it in `singulars/nolem.json`. Correct home is a cosmology entry, with at most a cross-reference on Nolem's `targetSpecies` recording the detection signature. (b) `status: open` — the owner's ruling this session does not reach it. (c) **Do NOT frame it against `CANON.md` §1.2.1** — that section is RATIFIED, already founded on one-thing-in-many-bodies, and it explicitly forbids *"explain[ing] how one soul can be reached by many… in mechanics."* If ratified, this must stay about **intelligence**, never souls, threads or the Pattern.
**Separately CONFIRMED:** Cthulhu's gift of intelligence (:208) is already carried at `singulars/cthulhu.json:14–16`.

### M9 — Nolem's **combat profile** exists nowhere.
On-page (all art direction / dialogue, script.md:926–991): a **cosmic sniper gun**, damaged by a stadium-wide electrical discharge (:931–933); **immune to Ninja's poison** while the same poison works on Retnuhxed (:943); barely feels Boxer's punches (:980); **successfully slowed** by Cyberpunk's weapon (:946); Gladiator's and Viking's weapons **lodge in him** and he clears them by releasing energy from within (:951–953); ordinary troops fail to subdue him (:938–939); **Nike Prime physically pushes him back** (:991). `singulars/nolem.json:11` has no corporeal profile at all, and `RaidBossConfig.js:1533–1567` is explicitly a projection. Record it, or a future Nolem encounter will be invented from nothing. Additive.

### M10 — The trap is anchored to a **naturally occurring magnetic anomaly**.
**Comic (dialogue), script.md:959–960:** *"Nike Prime: Computer, figure out the location of the nearest naturally occurring magnetic anomaly. Shiro, you know what to do."* This is Hennifer's own discipline (:89) and the basis of BETTY — the science that opened the doors is the science that shuts one. It also explains why Charles AI had to reposition outside the stadium and Nike Prime was *"FORCED to bring the fight there"* (:963). `dimensions/nolem-maw.json:71–74` records the pocket and its shifting coordinates but no anchor. Additive; consequence for future writing: **a trap of this kind cannot be sprung just anywhere.**

---

## 4. MINOR / gaps

| # | Item | Comic (line) | Doc state | Disposition |
|---|---|---|---|---|
| m1 | **C.H.A.R.L.E.S. expansion** — *"Core Harmonized Array for Real-time Linguistic Exchange Signaling"* | :44 (dialogue) | `charles-ai.json:4–7` carries the bare styling; `GAME_SPEC.md:262` + Tesana twin too | Add to `charles-variants/index.json` `otherDimensions[]` as **Stoner Nike's household room/telephone system** — NOT to `charles-ai.json`. Three-artifact change. |
| m2 | **Hennifer ONDO** — surname, female chicken, geophysicist, magnetic anomalies, covert government work, Pico's ex | :84, :89, :122, :154, :243 (dialogue) | `comic-characters.json:42–56` has "Hennifer", role mis-stated as portal tech | Add. **Correct the substance:** BETTY moves things by *alignment* (:261), needs *quantum inertial dampeners* for biologicals (:271), and **cannot open a return portal** (:272). Every portal in Book 1 is Shiro's. |
| m3 | **Ben** of the Charles Security Company; the abbreviation **CSC** | :462–467 (dialogue) | CSC **already recorded** (`comic-characters.json:125`, `GAME_SPEC.md:260`); Ben and "CSC" are not | Add Ben. Correct `GAME_SPEC.md:260`'s *"referenced, never met"* — Ben is met and has four lines. |
| m4 | **Charm** — a hen, Pico's receptionist, three speaking lines | :54–59 (dialogue) | `GAME_SPEC.md:298` closes the Prime-Era support cast at three names | Add. Closed lists are how a name is permanently lost. |
| m5 | **Vulture Pareto** | :117 (dialogue) | absent | Record as a named background figure. **Do not** elevate to "a worldbuilding law" — it is one gag line. |
| m6 | **the space penguins** / the bipedals / Cthulhu's home universe | :20–21 (art direction), :204–205 (dialogue) | `singulars/cthulhu.json` quotes the same panel's dialogue but not its cast | Add the neighbourhood; art-direction tier for the penguins. |
| m7 | **THE DIGI JOINTZ** | :1037 (**art direction only**) | absent everywhere | Record as an unexplained proper noun and Book 1's hook into Book 2. **Do NOT** add a `dimensionMapping` row — the room is unnamed and the table is keyed by the eight *game* dimensions. |
| m8 | **Four gag Nike variants** — Water World, ladies man, gigolo, the unevolved cave boar; plus an unnamed skittish Nike | :589, :596, :599, :603, :608 (dialogue) | absent | Add as a `dnaDonorVariants` list **inside existing blocks** — not a new fork. **Do NOT touch `CANON.md` §2.3.** "Unevolved" cannot mean quadruped: it is applied at :758 to *Shiro*, who opens portals. |
| m9 | **Ninja Nike joined for Shiro, not "destiny"** | :632–636 (dialogue) | `timeline/prime-era.json:41–45` `"whyJoined": "Destiny calling"` — while `legendary-nikes/index.json:52` **already quotes the Shiro line** | Internal split, not a comic collision. Fix the timeline file to match its sibling. |
| m10 | **Nike Tyson's raid backstory credits Charles with recruiting him** | Stoner Nike recruits every champion in person (:746–749) | `RaidBossConfig.js:295` *"Charles recruited him as a protector"* | One clause, shipped player-facing. *"as a protector"* is **correct** (:314–315). Only the recruiter is wrong. |
| m11 | **Boxer Nike's `whyJoined` is his battle cry** | pitch at :748–749 (*"CAN I LIVE STREAM IT?!"*); *"I LOVE THIS GAME!!"* is a mid-battle line at :838 | `prime-era.json:52–56` | One field. The livestream detail is the character. *(not adversarially verified)* |
| m12 | **Stoner Nike's two canon quotes are not in the comic** | 0 hits for *"cosmic octopus"*, *"We need warriors"* | `comic-characters.json:22–23` | Replace with real lines. He is stoned but technically fluent — cites the Pareto principle, reads a Faraday cage. *(not adversarially verified)* |
| m13 | **"the Abyss"** as the Retnuhxed's origin | :826 — Gladiator's **war speech** | absent | Flag; do **not** canonise. Rhetorical register. Ask, don't assume. |
| m14 | **"pocket dimension"** (:1034) and **"DIMENSIONAL CONVERGENCE"** (:794) | dialogue | lore says "The Trap"; no event term | Add both. **Guard:** the Discord repo's non-canon `campaign_scripts/` carries a rival *"THE CONVERGENCE PROTOCOL"* under a superseded banner — adopting the comic's word must not be mistaken for reviving that draft. |
| m15 | **"sub-picosecond" is an author-note-only figure** | :1047–1049, the **unmarked author-note block** | already a Charles AI ability in `charles-ai.json:29,63`, `GAME_SPEC.md:262`, Tesana twin | Correct. This is a worked example of an author note already treated as in-world fact — the exact failure the evidence-tier rule exists to prevent. |
| m16 | **Author notes (:1041–1058)** pair each broken pillar to its counter-invention: birth→Engineer, famine→Botanist, nutrition→Nutritionist, data/energy→Coder, all marked "done" | author-note | absent | Adopt as **flavour/structure**, never as in-world text. It makes the four Scholars a designed set, which is what the Scholar Bunker needs. Never elevate *"REXH THING"/"RHEX THING"* to a term. |
| m17 | **Stoner Nike's home reality has no place on the dimension map** | :44, :52–58, :84, :117, :157, :290 | `dimensions/index.json:160–203` maps five comic realities, omits it | Either add it, or state that the eight are the *Echo Era's surviving* dimensions and not a census of Book 1. Also absent: Engineer's, Nutritionist's, Botanist's, Shiro's quadruped-cat world, and the *"strange reality"* where physics fails (:262–265). |
| m18 | **"Charles Arena" is a stadium, not a reality name** | :712 (art direction) | `dimensions/index.json:76,179` treats it as the reality | Cosmetic correction while the table is open. |

---

## 5. CONFIRMED — what was right all along

These are the load-bearing beams that **survive the primary source untouched**. Report them loudly: the campaign spine, the region cast, the villain's nature, the win-shape and the ensemble structure all hold.

| # | What is ratified | Comic evidence | Where it lives |
|---|---|---|---|
| **C1** | **The five Champions ARE the five shipped anchor bosses — 5-for-5.** Gladiator→Imperial Colosseum, Ninja→Shinden, Viking→Frostfall, Boxer/Tyson→Grand Arena, Cyberpunk→Neon City. The most comic-faithful structure in the project; treat as settled. | :312–314 (art direction + dialogue), :709, montage :830–840 | `legendary-nikes/index.json:625–631`, `prime-era.json:36–70`, `GAME_SPEC.md:221`, all five shipped Discord anchors |
| | *Two documented bridges, recorded so they are not re-derived:* **(i)** the comic's explicit enumeration is FOUR — *"THE LAST OF THE CHAMPIONS WILL BE VIKING NIKE!"* (:314) — reopened by Charles AI's *"along with more champions to fight"* (:579) and closed by the five-panel montage; **(ii)** *"Tyson"* occurs **zero** times, so `legendary-nikes/index.json:632` is the only tether. **Never delete it in a tidy-up.** | | |
| **C2** | **Nolem is bound, never killed — and the comic supplies the reasoning canon asserted flatly.** *"HE COULD BUT NOLEM IS ESSENTIALLY IMMORTAL! KILL HIM AND HE JUST COMES BACK LIKE HE DID THIS TIME! BUTT!!! IF YOU CAN KEEP HIM FROM DOING WHAT HE'S DOING LONG ENOUGH, WE CAN FIGURE OUT A WAY TO TRAP HIM, IN HIS CURRENT WEAK FORM, HE'LL NEVER BE A UNIVERSAL THREAT!"* | :190–195 (dialogue), enacted :901–916, :1033–1035 | `SPINE_LOCK.md:215`, `GAME_SPEC.md:1782`, `CANON.md:35`, `mysteries.json:14`, shipped `main_006_campaign_complete.json:30`, `act2_009_elbonzys_boss.json:17` |
| | ⚠ **Do not "fix" the parenthetical.** A future agent will be tempted to edit *"(entropy can't die)"* to match *"HE COULD"*. Leave it — the comic's own gloss two words later is *"ESSENTIALLY IMMORTAL"*. | | |
| **C3** | **Nolem is a Singular: one across all realities, eons old, cannot be permanently destroyed.** *"there are beings LIKE CTHULHU!! Where only one of them exist across all realities"* / *"HE'S EONS OLD JUST LIKE CTHULHU!"* | :168–171, :185 (dialogue) | `singulars/index.json:2`, `:4`, `:5` |
| | *Scope limit:* the comic says **"EONS OLD"** — it does **not** support `index.json:8` *"Predate the concept of time itself"* (GAP), and it cuts **against** `index.json:7` *"Cannot freely enter most dimensions directly"* (see Q6). | | |
| **C4** | **The Charles Constant, stated almost verbatim.** *"The relationship between Charles and Nike differs in each reality. But in each one, we're somehow helped by him in one way or another."* — set up by *"This is the 3rd universe I've been to, and they all have Charles related stuff in it."* (:405) | :406–407 (dialogue) | `charles-variants/index.json:2`, `:117`; `GAME_SPEC.md:185` |
| | *Attach the citation to `charles-variants/index.json`, not `CANON.md` — `CANON.md:25` only names the Constant in the Absolute Order; there is no definition sentence there to cite.* Instantiated on-page nine ways: President Charles (:157), Dr. Charles (:371), Professor Charles (:496–499), the CHARLES room system (:44), the complete Charles AI (:395), the interface chip (:386), the CSC (:462), Charles dollars (:290), Charles Arena (:712–713, art direction). | | |
| **C5** | **Nike Prime released at 99%, and the growth chamber left empty.** *"Botanist Nike: …how far away are we from 100% completion? / Engineer: We're at 99%…"* + *"DRAW CHARLES AI AND THE REST OF THE NIKE'S IN THE BASMENT WHERE THEY HAVE NIKW PRIMES NOW EMPTY CHAMBER"* | :873–874, :885 (dialogue); :1010–1011 (art direction) | `CANON.md:59–60` (*"ninety-nine hundredths"*), `GAME_SPEC.md:152`, `:1754`, `prime-era.json:108`, `mysteries.json:152` |
| | ⚠ **Two proposed "refinements" were tested and STRUCK.** (i) `prime-era.json:108` *"due to the Retnuhxed attack"* is **causally correct** (:811, :858–859) and complementary to `mysteries.json:152`'s *"when Shiro pressed the button early"*; both stay. (ii) `CAMPAIGN_AND_COMPANIONS.md:324`'s *"Nike Prime's chassis at 99%"* is **not** contradicted — it is scoped to the Bunker 3,000 years later. **No edits.** | | |
| **C6** | **The four Scholars and their four contributions — clean 4-for-4**, incl. the CHARLES Fluid and the fetal-chamber origin. | :564–577 (dialogue) | `comic-characters.json:70–98`, `legendary-nikes/index.json:632–641`, `GAME_SPEC.md:221`, `:298` |
| | *One clause overreaches:* `:95` *"Created Charles AI."* — the comic says only *"my complete Charles AI"* (:395). Ownership stated; authorship not. *Free enrichments:* Perfluorooctyl Bromide (:565) and *"I bonded the FT proteins to activate the nucleus of the meristem cells"* (:538) — both **GAPS**, not matches. *Vocabulary note:* "Scholar" occurs **zero** times; the comic says "the scientists". Same idea, different word — CONFIRMED, not a collision. | | |
| **C7** | **Why Nolem hunts the Nikes stays dark — ratified by the source's own refusal.** *"Pico: Why? / Stoner Nike: NO IDEA, BUT HE'S ALREADY DONE THIS TO AT LEAST ONE OTHER CREATURE"* — from the character with the most information in the book, who has spoken to a Singular directly. | :198–199 (dialogue) | `CANON.md:203` §4.1 #1; `mysteries.json:15` |
| | Same for §4.1 #5 (*why Cthulhu helps* — the act is shown at :26–28, the reason never) and #6 (*where Shiro came from* — asked and unanswered three times: :278–279, :635, :699). **All three stay frozen; `check-mystery-tiers.py` stays armed and correct.** | | |
| **C8** | **Dexter Hun is Nolem's worn avatar — the JSON and the First Tongue got this exactly right.** *"Sometimes he showed up as Dexter Hun. Sometimes as something else."* + *"Ever have to fight a Dexter Hun?" / "I've killed countless."* | :554–555, :622–623 (dialogue) | `singulars/nolem.json:30–32`, `:77–79`; `dictionary.json:126–132` (`Dex'tur` = *dex* to wear + *tur* body); `GAME_SPEC.md:354` |
| **C9** | **Corruption is never the Nike, and it is separable.** Stoner Nike wore the state and remembers being inside it — *"I NEVER WANT TO EXPERIENCE THAT AGAIN!!"* | :1004 (dialogue); :1001–1003 (art direction) | `CANON.md:291–294` (separability half **only**) |
| | ⚠ **Rationale rewritten:** this is *compatible with*, not *proof of*, the `Keth'nor` etymology — the comic uses no First-Tongue word and calls the mechanism *"MIND TRICKS"* (:981). And the **Sever Guard reinforcement is struck**: the reverted characters were never severed, and the comic treats killing Retnuhxed as costless victory (:824–826, :1001–1003). | | |
| **C10** | **The trap's name and geometry, verbatim.** *"a way to trap Nolem in a space-time distortion field"* … *"a pocket of warped space, a place where the spatial coordinates shift multiple times per second"* | :901–912 (dialogue) | `GAME_SPEC.md:223`, `prime-era.json:144–150`, `nolem-maw.json:73`, shipped `main_006_campaign_complete.json:30` |
| **C11** | **Boxer Nike = Nike Tyson.** The venue is literally CHARLES ARENA; *"Fiery Fists of Furociousness"* survives verbatim; the boredom motive is comic-native (*"I'M TIRED OF FIGHTING THESE BUMS!"*). | :712 (art direction), :731, :736 (dialogue) | `legendary-nikes/index.json:84–98`, `grand-arena.json:35` |
| **C12** | **5,548 vials · the basement beneath the Colosseum · gestation in months · Charles AI as a tool on loan.** *"5548 vials"* · *"DRAW ALL OF THE NIKES IN SOME BIG BASEMENT THAT'S BENEATH THE COLOSSEUM"* · *"grow a full grown Nike … in just a few months"* | :339, :546, :577 | `GAME_SPEC.md:151`, `:222`; `CANON.md:26–27`; `prime-era.json:5,92,100`; shipped `act2_001_bunker_opens.json:20` |
| **C13** | **Retired terms — the source revives none.** `scripts/check-canon-terms.sh` returns **zero hits across the whole script** for all four retired terms it guards (run it yourself rather than spelling them here — this file is not on the governing-document exclusion list, and naming them would trip the gate). The comic says *"Ninja Nike"* throughout, independently ratifying §3.2's ruling that his name in the world stays Ninja Nike. | `sh scripts/check-canon-terms.sh`, whole file | `CANON.md:191–194`; `check-canon-terms.sh` |
| **C14** | **The battle montage roles, 5-for-5, in order.** | :830–840 (art direction) | `prime-era.json:~175`; `GAME_SPEC.md:270–281` *(not adversarially verified)* |

**Things that were feared and are NOT true — record these so nobody re-raises them:**
- The **Sixth Seat** provenance panic is dead. The claim that *"Five Champions was never a designed number"* was **refuted**: canon already says five, the comic shows five, and they are the same five including Boxer. No 28-file rewrite.
- The **Shinden mist** collision is dead. *"Purple smog"* at :612 is **art direction** and does not reach ratified canon; it is a GAP, not a contradiction. `SHINDEN_SPEC.md`, the `world_shinden_mist_level` mechanic and the freeing cinematic are untouched.
- **`NOLEM` reversed is `MELON`** was fabricated and refuted on five independent grounds. Do not log it. ⚠ **THIS REFUTATION WAS ITSELF WRONG — corrected 2026-07-29.** `NOLEM` reversed *is* `MELON`, and `RETNUHXED` reversed *is* `DEXHUNTER`; both verify mechanically, and the owner has confirmed the real-world origin. The audit refuted a trivially checkable string reversal. Kept as the record of the error: **a refutation is not self-verifying.** The reversals are out-of-world provenance only — never in-world, never a puzzle (`CANON.md` §3.2).
- The **`Ret'nux` / `Dex'tur` "false etymology"** charge is refuted — the comic makes no etymological claim, so it cannot contradict one.
- **`pigment shard`**, **Squilya-as-individual**, **"bipedals"**, **Shiro's Shinden origin**, and **the First Tongue's post-comic status** were all refuted as collisions.

---

## 6. Open questions for the owner

Each is a genuine judgment call the comic does not settle. Recommendation given for each.

**Q1 — Shiro: the IP firewall vs. the primary source.**
The phase-out is a **rights** decision (`comic-characters.json:66`), not a story invention — but it currently launders itself through an in-world death the comic contradicts, and that death is the stated origin of Charles AI's portal powers, i.e. the game's entire transit system.
→ **(a)** Keep the name-suppression rule, delete the fabricated death/merge, and leave Charles AI's portal ability **unexplained** — fully consistent with §4.1 keeping Shiro's origin dark, and it costs nothing mechanically. **(b)** Keep the merge as a knowing, owner-ratified departure from Tier 1, logged in `GAME_DELTAS.md`.
→ **Recommend (a).** It is the smaller edit and the only one consistent with `CANON.md` §4.1 as currently frozen. Note `GAME_SPEC.md:130` simultaneously lists "Shiro" as a canon spelling and forbids naming him — fix that either way.

**Q2 — What does the word "Retnuhxed" name?**
→ **(a)** Two things sharing a name: Nolem's Abyss-spawned army *and* a reversible imposed state — cleanest, preserves both the shipped 26-creature `is_nike=0` roster and the soul-mote ruling. **(b)** Amend `CANON.md` §2.1/§3.1 so *"past saving"* is a **late stage** rather than the word's definition.
→ **Recommend (a).** (b) reopens a RATIFIED pillar and turns *"the only mercy left to give it"* from a bound into a licence — the exact failure §2.1's 2026-07-28 amendment was written to prevent.

**Q3 — §5.3: does Nolem manufacture the wound?**
`CANON.md:291–297` (RATIFIED): *"A wound has to come first, and it is not his."* The comic has Nolem's own avatar engineering infertility, famine and poisoned food.
→ **(a)** The comic operates one level up: Nolem manufactures the **civilisational** wound but still cannot touch an intact **individual** connection — §5.3 holds at the level it was written about. **(b)** §5.3's absolute clause is wrong and must be scoped.
→ **Recommend (a).** It costs one clarifying sentence and preserves the LOCKED thesis, the absorption-immunity chokepoint (`TODO(S2-absorption)`), and every Legendary motivation built on it.

**Q4 — The empathy core.**
The comic never names the missing 1% and never denies it; the fabricated quote is the only thing that ever tied it to Book 1.
→ **(a)** Keep it, explicitly re-founded as a **post-comic Scholar-Bunker reconstruction** — which is already how the shipped Discord game stages it (anonymous SCHOLAR RECORDING, zero "Engineer Nike" in `campaign-data/`). **(b)** Retire the term.
→ **Recommend (a).** (b) is 119 references across 41 files including shipped runtime (`nikeverse-mmo-rpg/src/ui/loreCards.ts:61–66`, with a test pinning the string) and all five Resonance-band endings — an enormous cost paid for an *absence*. Delete the quote (F3) regardless.

**Q5 — Nike Prime's 3,000-year state.**
Book 1 covers none of the gap.
→ **(a)** **Lost** — location unknown since the Prime Era; the Maw holds Nolem. **(b)** **Lost, then re-entered** — a later retcon in the Long Silence puts him back inside, preserving *"still inside, still fighting"* and the weakening-trap urgency.
→ **Recommend (a)** for the canon fact and leave (b) available: `long-silence.json:5` explicitly calls the era *"expansion space for future comics."* Under (a) the weakening trap needs a new cause; under (b) nothing downstream moves.

**Q6 — Nolem's mobility limit.**
`singulars/index.json:7` (*"Cannot freely enter most dimensions directly"*) is the **stated reason** Nolem severed the Dimension Eater (`nolem.json:86`, `dimension-eater.json:29`). The comic has him folding space-time at will between known coordinates (:906–912) and arriving in person (:918) — while Cthulhu also describes him working through *"shadow entities"* (:26).
→ **(a)** Rewrite the limit as **coordinate knowledge, not permission** — deny him coordinates and you deny him movement, which is exactly what the win condition exploits. **(b)** Leave it; the comic cuts both ways.
→ **Recommend (a)**, but note it forces a new motive for the Dimension Eater's severance. `status: open`, separate claim.

**Q7 — "Summoned" or "grown"?**
The owner's own word was *summoned*; the comic grows Nike Prime in a rebuilt fetal chamber over months (:373, :577), first seen as *"A SMALL PIGLET INSIDE"* (:765), released by a button (:870). *"Summon"* is also the vocabulary of the explicitly non-canon `campaign_scripts/` "Convergence Protocol" draft — the project's largest documented contamination hazard.
→ **(a)** GROWN, per *"as per my comic book 1."* **(b)** Recalled/summoned as an existing being.
→ **Recommend (a).** Every live artifact already says grown; no doc anywhere says summoned. One sentence settles it and prevents a future writer importing the banned cosmology.

**Q8 — The intelligence drain: adopt or not?** (M8) → **Recommend adopt, as a cosmology entry, kept strictly about intelligence.**

**Q9 — The arithmetic.** See §7 — the owner must pick a bridge.

---

## 7. The arithmetic — does the comic reach 5,555?

**No. Plainly: the comic never states 5,555. `grep -c "5555\|5,555" script.md` = 0.** The only collection number in Book 1 is **5,548**, and it counts **vials**.

**The one stated figure — dialogue, script.md:339:**
> *"Stoner Nike: I'm going to need 5548 vials though so I can collect the DNA of all of the Other Nike's. / Hennifer: That's a lot."*

**Step 1 — what 5,548 counts.** Vials, for *"all of the Other Nike's"* — i.e. every Nike except the speaker, and every Nike he can still reach. Note also that **"5,548 Nike *variants*" is a lore coinage quoted back as if it were the comic's word** (`THE_5555.md:33,90,273`; `MASTER_LORE_PROPOSAL_FINAL.md:310`; `comic-characters.json:106`; `ages.json:93`; `prime-era.json:100`; `GAME_SPEC.md:222` + twin). The comic's nouns are *"the Other Nike's"* and, defining them, Pico at :131 — *"You're talking multiple versions of yourself, each of them in their own universe?"* The number is right everywhere; the attribution is not.

**Step 2 — the living population at the moment of the request.**
> 5,548 others + Stoner Nike himself = **5,549 living Nikes**

**Step 3 — the published derivation, and why it fails.** `MASTER_LORE_PROPOSAL_FINAL.md:928`:
> *"Add the 4 Scientist Nikes, the 5 Champions, Stoner Nike himself, and Nike Prime—the number was always approaching 5,555."*
>
> 5,548 + 4 + 5 + 1 + 1 = **5,559**. Overshoots by **4**.

This is already flagged at `THE_5555.md:35` and has never been resolved. *(The further "double-count" charge — that the Champions and Scholars take vials from the same 5,548 stock, so adding them counts nine Nikes twice — was tested and **rejected** as not what the comic shows. Do not rely on it.)*

**Step 4 — Closure A (drop the four Scholars).**
> 5,548 others + Stoner Nike (1) + the 5 Champions + Nike Prime (1) = **5,555** ✅
>
> Requires: the four Scholars are *inside* the 5,548, and the Champions and Nike Prime are *outside* it. **Internally shaky** — the Champions are each handed a spit vial from that same stock (:645, :675, :709), which argues they are inside it too. And under the owner's species ruling, Nike Prime is the *product* of the collection, not a member of it.

**Step 5 — Closure B (the shrinking census).** Grounded in a comic line — **dialogue, script.md:128–130**:
> *"I MEAN ME AND EVERY OTHER UNIVERSE THAT HAS ME IN IT! **WHICH IS NOT ALL OF THEM ANYMORE! THE ONES THAT ARE LEFT!**"*
>
> 5,555 original complement − **6 already killed by Nolem** = 5,549 alive = Stoner Nike + 5,548 others ✅
>
> Requires: one unstated fact (six Nikes dead before the request). Everyone else — Scholars, Champions — sits inside the 5,548, and Nike Prime is correctly outside the count entirely. **Arithmetically exact and internally consistent.**

**Step 6 — Closure C (chronological, needs no gymnastics).** :339 precedes *every* recruitment in the book; Stoner Nike asked for the vials **before he knew who he would recruit**.
> 5,555 − 5,548 = **7** = Stoner Nike + the 5 Champions + Nike Prime ✅
>
> Arithmetically identical to Closure A, but framed as *"5,555 is the owner-set total; 5,548 is an in-story snapshot taken before recruitment"* rather than as a derivation the comic performs.

**What must be said on the record, whichever is chosen:**
1. **5,548 is CONFIRMED** and correctly carried everywhere. It is the comic's only number and it stays a locked constant.
2. **5,555 does not come from the comic.** It comes from the owner. `THE_5555.md:172` currently states outright that *"5,555 cannot be a species count"*, and `CANON.md` §1.2 is RATIFIED on souls-held-simultaneously — **the owner's ruling this session supersedes both, and that supersession is not yet logged anywhere.** Log it in `CHANGELOG.md` and state the referent in `CANON.md` §1.2 and `THE_5555.md` explicitly.
3. **Delete the `MASTER_LORE:928` derivation.** It is the sole published justification for the number in the whole corpus and it is arithmetically wrong. Removing it leaves 5,555 resting on the owner's ruling alone — which is correct, and should be said out loud rather than left as folklore.
4. **The comic does not establish that the collection ever completed.** The last status line is Botanist Nike's *"Just a few more to go!"* (:610) — before four more champions are recruited — and Charles AI's brief is *"We just need the one who brought us all here to get the DNA of the rest of them"* (:578). So the **completion gate is the owner's, not the comic's.** No future writer may cite `script.md` for it.
5. **Recommendation: Closure B for the fiction, Closure C for the bookkeeping.** B gives the number a dramatizable meaning (six Nikes are already dead, and the count is a *shrinking census*, which is what :128–130 actually asserts) and it is the only closure that is both exact and internally consistent. C is what the docs should *say* so nobody claims the comic performed the arithmetic. Either way, the `THE_5555.md` Bond-Log off-by-one (5,553 vs 5,554) and the three mutually exclusive occupants of the 5,555th slot (`GAME_SPEC.md:1942` "you" vs `MASTER_LORE:928` / `mysteries.json:151` "Nike Prime") should be resolved in the same pass — and under a species ruling the **human** Collector cannot be a member of the count at all.

---

### Immediate, zero-controversy actions

1. Create `comic-books/book-01/claims.json`; enter every ruling above at `status: "open"` with `evidenceKind` (`dialogue` / `art-direction` / `author-note`) and `scriptLine`.
2. Delete the fabricated quote (**F3a**) — it is a false statement *about the primary source* and needs no ruling.
3. Delete the Boxer Nike sacrifice clause (**M3**) — a defect fix inside existing canon, already flagged for scrubbing.
4. Fix `prophecies/mysteries.json:175` (**F2**) — a gate is currently certifying a contradicted statement as sayable.
5. Log the owner's 5,555 ruling and its supersession of `CANON.md` §1.2 and `THE_5555.md:172` in `CHANGELOG.md`.
6. Re-run `check-canon-terms.sh`, `check-mystery-tiers.py`, and the JSON parse. **Never hand-edit `TESANA_BUILD_PROMPT.md`** — regenerate it from `GAME_SPEC.md` via the derived `tail -n +N` offset in the same session.