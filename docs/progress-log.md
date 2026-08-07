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

## Wave 13 — the bonding phase

Third design wave in the build repo (`CIRCLE_DESIGN.md` Part III) collapsed the two-phase catch into one
"bonding phase" under five owner rulings. **Nothing in it changes a lore claim** — the assertion sweep found
no divergence to close on this side.

Checked and clear:
- **The Bond Struggle is dissolved** into the bonding phase, and `GAME_DELTAS.md:258` already rules the
  Struggle, Composure and Resonance to be net-new game systems with **zero occurrences in this repo** and
  free to tune. Only the *simultaneity* of the 5,555 (`CANON.md` §1.2) is canon, and it is untouched.
- **Souls-held vs threads-held** (Wave 12) is unaffected by the merge.
- **`Eth'kara`'s usage note** (Wave 12) still governs: the thread is player-facing, "chain" stays banned in
  the living language, the term keeps its First Tongue register.
- **No retired term entered the new canon text.** Verified by the lint.

Durable rule reaffirmed rather than added: **a game-mechanic change that touches no lore claim still gets the
assertion sweep** — the sweep's output being "nothing to do" is a result, not a skipped step.

## Wave 14 — the Triforce ruling; nothing to change on this side

Owner ruling in the build repo restored **the Triforce** as the name of the Hub's three-part explanation of
why Collectors battle each other, deleting a build-spec coinage (*"the Convergence Accord"*, a
"three-faction pact") that existed in neither this repository nor the shipped game. **Factions are not
attached to the Triforce and there is no player faction choice.**

**The assertion sweep found nothing to fix here** — `characters/collectors-journey.json` (`triforceSystem`)
and `dimensions/convergence-hub.json` already name the Triforce and all three systems, matching the shipped
`hub_015`–`hub_019` nodes. Recorded in `CHANGELOG.md` as a resolution; the sweep returning "nothing to do"
is a result, not a skipped step (Wave 13's rule).

**Left open on purpose, and written down so it is not mistaken for settled:** the Triforce is **not in
`CANON.md`**. It lives in this repo's JSON and in `MASTER_LORE_PROPOSAL_FINAL.md` — provenance, not a live
spec. Elevating it to the settled centre is a separate ruling; the owner scoped this change to the pact.

---

## Wave 15 — 2026-07-29 · Comic Book 1 lands; ten owner rulings; two audits

**What arrived.** The owner uploaded *Nike the Pig: Book 1* — the Tier-1 primary source, which for ten months
had existed in no repository. Every prior reading of the 5,555 was therefore derived from a secondhand
paraphrase of a document nobody working on it could open. Landed at `comic-books/book-01/` as PDF + verbatim
uncorrected `script.md`, with a 122-agent cross-repo audit (`RECONCILIATION.md`) and a per-claim register
(`claims.json`).

**Ten owner rulings**, all logged in `CHANGELOG.md`: Tier 0 (owner above comic) · 5,555 = distinct **forms** ·
the arithmetic closing by subtraction at 5,548 · Nolem **makes the wound** · the Discord game demoted as a
*lore* authority (scoped) · the Long Silence stays open · the Three Scale Laws · the Bond Log is
**completable** · **nothing is consumed** · Nolem's limit is **knowledge, not permission**.

**Defects found and fixed along the way:** a **fabricated quotation** ("Wait, the empathy core isn't—") that
was load-bearing in four repos and originated as a speculative bullet in a draft; the published 5,555
derivation that summed to **5,559**; Boxer Nike's non-existent sacrifice; two Pattern Integrity bugs (a
chapter-win gate that eliminated realms mid-season *silently*, and a meter specced as two incompatible
objects); and an incomplete Yuki pronoun sweep that misgendered her mid-sentence.

**⚠ THE LESSON, and it cost a whole second pass.** Two independent Opus audits named the same failure:
**an amendment appended to one clause while the sibling clause carrying the same claim was left standing** —
same file, sometimes the same sentence. Six of the eight highest findings were that one pattern.

> **THE GUARD: after any strike, grep the STRUCK PHRASE ITSELF across all four repos before committing —
> not just the file you opened.** Every one of those findings would have surfaced on the first grep.

Second lesson: **a refutation is not self-verifying.** The first brainstorm wave "refuted on five independent
grounds" that `NOLEM` reverses to `MELON`. It does. Check anything mechanically checkable yourself.

---

## 2026-07-30 · ONE SOUL, MANY LIVES — repeat bonding becomes canon (`CANON.md` §1.2.2)

**The ask.** *"Bonding in my game works the same way as catching a pokemon. I want players to bond/catch and
store all extras in the sanctuary. Now make a lore that makes this work. Meaning even if 5555 is complete, we
can continue to bond with as many repeat species as we want."*

**The move that made it safe: this is DERIVED, not invented.** §1.2.1 already ratifies that a soul reached by
many Collectors *is not divided by it, because distance and number are nothing to the Pattern.* That same
sentence covers a soul living in more than one place at once. So the answer is the ratified axiom applied to a
second axis — **a fragment is not divided by living more than one life** — rather than a new axiom bolted on.
Nothing had to be struck to make room for it. When a request looks like it needs new cosmology, check whether
the existing cosmology already covers it on a different axis; here it did, and the version that had to be
invented from scratch (many individuals per kind) would have contradicted §1.2's ratified referent outright.

**What landed.** `CANON.md` §1.2.2 (two objects — the **fragment**, counted; the **life**, counted by nothing);
`CHANGELOG.md`; `GAME_DELTAS.md` **L11**; `THE_5555.md` phases 7–8 + header; `claims.json` `cb1-5555-referent-species`
extended; `CLAUDE.md` NEVER #7 (fallen-taxonomy renumbered #7→#8, and its stale cross-reference in `CHANGELOG.md:64`
fixed in the same pass). Sibling artifacts in the other two repos landed the same session, per the three-way rule.

**Three things the ruling bought that were not asked for:**
1. **The Circle Draws are re-founded.** Open since 2026-07-29, when the form referent struck the sentence they
   stood on. They needed a drawn soul to be *a distinct person*; *a distinct **life*** supplies it exactly.
2. **`THE_5555.md`'s own prediction closed.** Its species-question section said adopting the species reading
   *"would cost one ratified sentence… which is load-bearing for Circle Draws and would need a successor."*
   The cost was paid on 07-29 and the successor landed on 07-30 — a one-day gap, now recorded rather than
   forgotten. Both readings survive: *one soul in 5,555 bodies* AND *all 5,555 Nike types*.
3. **A found divergence that is really a confirmation** (L11). The shipped Discord game already runs the exact
   sanctioned shape — unbounded `player_creatures` + a 6-slot `party` — and calls the overflow **"storage"**
   (`commands/party.js:260,1050,1492`). The mechanic agrees; only the noun diverges. Going to the data turned
   "is this risky?" into "this already ships."

**The guard was applied and it caught two.** After striking *"legal (tunable — ship it on)"* I grepped the
struck phrase itself across all four repos, per the standing rule. Two live siblings surfaced that a
file-by-file pass would have missed: two Emo Nike notes in `GAME_SPEC.md` (~1651, ~2418), and — the one that
mattered — `claims.json`'s ruling record, which is *not prose* and would never have turned up in a prose sweep.

**One derived precision, unasked-for and load-bearing.** The freed-soul respawn rule said the spawn point
*"re-populates with a NEW soul."* Under §1.2.2 "new" means a new **life**, never "a form you have not seen" —
so a spawn point must never exclude an already-reached form. Left ambiguous, a builder implements per-form
exclusion and the game quietly tells the player a soul is used up, which is the copy-reading in mechanical
form. Fixed at `GAME_SPEC.md` §4.5.8, `CIRCLE_DESIGN.md` §5.3, `KNOWN_ISSUES.md` Q7 and the build `CLAUDE.md`.

**Vocabulary:** *spare* and *extra* (as nouns for a soul) join the banned list. **A life is never a commodity** —
NOTHING IS CONSUMED binds here unchanged, and bulk trade of repeats must never be enabled.

### QC pass — the register entry I wrote was the worst thing in the wave

**`GAME_DELTAS` L11 first read: *"The MECHANIC AGREES — this is a wording divergence only… the shipped game
is the existence-proof that this works at product scale, which is why the ruling is low-risk."* That is
FALSE, and it was the ruling's own risk argument.** The store *shape* agrees, but the shipped game's actual
product answer to repeat accumulation is a **disposal flow that converts souls into currency**:

- `deployCommands.js:88` — *"Browse & **release duplicates** (send to Truffle Pastures)"*
- `handlers/exploreButtons.js:116` — *"💡 **Too many Nikes?** Release **extras** to Truffle Pastures"*
- `commands/species.js:293,450` — *"🌾 **Truffle Harvest:** +N Nexus Coins"*

*"Too many Nikes?"* is the exact sentence §1.2.2 exists to forbid, and Nexus-Coins-per-soul is the going
rate it bans. **It is a design divergence, not a wording one**, and the shipped precedent de-risks nothing.

**The signal worth keeping is better than the claim I replaced.** The MMO independently grew the same shape
— `GAME_SPEC.md` §7.5's Return-home faucet pays Resonance + Bond-Echoes, and unlimited repeats just removed
its only structural bound. **Two builds arrived at soul-for-currency on their own.** That is faucet
pressure, not coincidence: an unbounded collection generates a disposal verb, and a disposal verb wants a
payout. It needs a stated rule, which is now `KNOWN_ISSUES.md` Q9 ②.

**The lesson, and it is a new one.** The wave's guard is *"after any strike, grep the struck phrase across
all four repos."* I ran it and it worked. But L11 was not a struck phrase — it was **a new claim I made
about another repo without checking that repo's code**, in the middle of a session whose whole discipline is
*go to the data before you trust a document*. I applied that rule to the docs and exempted my own summary of
them. **A claim about a shipped product is a grep, not an inference — including when you are the one making
it, and especially when it is the sentence that makes your own ruling look safe.**

**Two overclaims of mine were also struck in the same pass** (see the build repo's log for the full set):
the "anti-grind by arithmetic" inference, which is simply unsound — quality re-rolls drive grind, not
counters — and "Free costs nothing on a repeat", which is backwards: on a repeat **Free out-pays Bond**,
on the moral band. Both had already been copied into more than one ratified document by the time they were
caught, which is the same propagation speed that made the sibling-clause pattern expensive in the first place.

### The three-mind brainstorm (part 2) — what the lore side gained

Full wave record is in `Nikeverse-mmo-rpg-from-scratch/docs/progress-log.md`. The lore-specific gains:

**`CANON.md` §1.2 — the eight-cap.** *"One form per universe"* read as **occupancy** caps repeat bonding at
eight bodies per form across the eight dimensions, which makes the owner's requirement unshippable. Ruled
**provenance**: each of the 5,555 *originates* in one world; where it has since come to rest is unbounded.
Settled on Tier-1 evidence the ruling had never cited — *"thousands of other realities"* (`script.md:207`).
**The phrase was written in the same session that ratified the thing above it, which is exactly why it read
as settled.**

**`CANON.md` §1.2.2 — the ground was already in our own dictionary, and nobody had looked.** `Shat'ael` is
glossed *"The Echoing; the great fragmentation… **also called the Great Echo**"*, and §1.2.1 already ratifies
that the First Bond ***echoed* rather than broke**. So the Great Echo never stopped going out — and that
fixes a register defect in the landed text: ***life* is a SERIAL noun.** You have one at a time, so "living
twelve lives" reads as sequential reincarnation while the requirement is *simultaneous*; forty echoes of one
shout all sound at once and nobody imagines the shout was divided. **The lesson: when a ruling's wording feels
slightly wrong, grep the First Tongue before writing new prose.** The corpus had the word for ten months.

**`languages/first-tongue/dictionary.json` — `Ael'tur`** (*ael* soul + *tur* body), the moral mirror of
**`Dex'tur`** (*dex* "to wear" — Nolem's avatar): a `Dex'tur` is a body **worn as an instrument**, an
`Ael'tur` is a body that **is somebody**, so the language now carries NOTHING IS CONSUMED by itself. Plus the
inscription **`Shat'ael meth`** — *"The Echoing is endless."* ⚠ **The echo is the GROUND, never the
player-facing noun:** *Bond-Echoes* is a currency, and a soul sharing a noun with money is the NOTHING IS
CONSUMED failure in one word. Design docs may say echo; the game says *"a life."*

**A JSON formatting near-miss worth recording.** The first attempt added `Ael'tur` by `json.load` →
`json.dumps`, which produced **47 insertions and 9 deletions** — the round-trip exploded every compact array
in the file and stripped its blank lines. Reverted and done as a surgical text insert instead: **15
insertions, 0 deletions.** *Never round-trip a hand-formatted JSON file to add one entry;* the diff is the
review surface, and a 56-line diff for a 15-line change is a diff nobody reads properly.

**And a formatting break I made in `CANON.md` and caught on read-back:** the provenance blockquote absorbed
the tail of the paragraph it was inserted into, leaving *"Two wild Nikes of the same"* inside the quote and
*"form remain legal to bond…"* outside it. **Read the rendered region back after any mid-paragraph insert** —
an assert on the replaced string proves the edit applied, never that the result parses as intended prose.

## 2026-07-30 (part 3) · THE SETTLING — evolution keeps the transformation

**Two owner rulings**: *"I want to keep the transformation"* and *"Sonic gets his own slot."* Landed as
`CANON.md` §1.2.3 with `Thael'tur` and `THE_5555.md` Phase 9. **The bill came to one sentence** — *no
document, UI or line of dialogue ever states a count of fragments* — because nothing was ever denominated
in fragments.

**⭐ THE LESSON OF THE WHOLE DAY, and it cost four blockers to learn: I OVER-PRICED EVERY BILL, AND THE
OVER-PRICING NEARLY PRE-EMPTED AN OWNER RULING.** Of the four costs I quoted for keeping the transformation,
**three were wrong**: *repeats become mandatory* (false — a wild Oinkachu is a different **form**, so a first
meeting), *the win condition becomes unreachable* (false, and the previous ruling is what saves it), and *the
census precisification must be rewritten* (I called it unnecessary — see below). I also relayed the vial
argument as **decisive** when it is suggestive: Stoner Nike ordered 5,548 vials *before meeting anyone*, so it
is a planning figure. **Presenting a soft argument as forced is how a lead pre-empts the owner**, and the
owner's actual ruling went the other way.

**The sharpest single error, and it is a new failure mode worth naming.** I wrote *"the census precisification
must be rewritten — **unnecessary**, forms-held serves its anti-inflation purpose identically"* — which is
**true, and is exactly why the word had to change and I then did not change it.** Under §1.2.3 souls are
strictly fewer than 5,555, so *"all 5,555 **souls** held at once"* is unsatisfiable by construction and the
victory condition was arithmetically unreachable for as long as the word stood. **Declaring a rewrite
unnecessary is not the same as checking whether a word is still true.** One word, five documents.

**THE MID-PARAGRAPH INSERT, THREE TIMES IN ONE DAY.** §1.2's provenance blockquote swallowed the paragraph
tail; `PATTERN_INTEGRITY.md` §0's insert orphaned another; and worst, **the `### 1.2.3` heading landed
mid-§1.2 and silently re-labelled ~140 lines** — THE BOND LOG IS COMPLETABLE, **NOTHING IS CONSUMED**, the
sanctioned-language lint — leaving the file ordered 1.2 → 1.2.3 → 1.2.1 → 1.2.2 and three external documents
citing NOTHING IS CONSUMED at a section that no longer contained it. I recorded a lesson after the first one
and it was too weak.

> **THE GUARD, restated so it actually binds: anchor an insert on the WHOLE paragraph including its tail,
> never on a prefix — and after inserting a HEADING, print the section list and check the ORDER.** "Read the
> region back" is not a procedure; printing `grep -n '^### '` is.

**Two more of mine, both caught by reviewers:** I edited `CANON_MAP.md` without checking whether an agent had
already written the same rulings and produced a duplicate block with colliding numbers — the *never two agents
on one file* rule, broken by the lead. And a builder correctly **rejected my stated mechanism** for the
evolution-exclusive rule: I claimed the only way to log Oinkachu becomes a repeat, which does not follow,
because if a settling moves no counter then evolving never logs it **at all** — the real defect is an
unfillable slot.

**What the wave got right.** The keystone was **forced by the shipped data, not chosen**: the chains are
biographies and several are dark (*CORRUPTION ARC: Glowing → Angel → Devil*), so a bond-gated causal reading
tells the player their love made a devil. **THE BOND IS THE WITNESS, NEVER THE CAUSE** is §5.3's *resistance,
never immunity* applied to a second axis, and it makes a settling **neutral**. And the corpus supplied its own
answer twice — `Shat'ael` for the echo, and §2.3's *"has no settled form yet"* for the settling. **When a
ruling's wording feels wrong, grep the First Tongue and the ratified sections before writing new prose.**

## 2026-08-02 · Corruption is a DEPTH — the §5.3 wild-catch extension

**Owner ruling (Tier 0):** every wild carries some corruption; damaging a wild removes it (a low-HP wild soothes
faster); and a wild fights back during the encounter (the Nolem-hold resisting the cleanse). Owner chose the
two-phase shape.

**Lore side is an EXTENSION of §5.3, not a reversal.** §5.3 already says *"what a Collector strikes is the
numbing"* and already blesses the shipped *"Reduce its HP below 15% to break the corruption."* Added `CANON.md`
§5.3 **EXTENDED**: the numbing is a **continuum** — a thin ambient film on every wild → the thick engineered
wall on a Legendary — with **HP as its proxy**; damaging a wild to strip its film and beating a Legendary to its
crack are **one mechanism on a corruption-depth spectrum**. The film **resists its own removal** (*"connection
is RESISTANCE"* from the corruption's side), so a wild is hostile before it is reached — **what attacks is the
corruption, never the soul**, and the hostility ends the instant the reach begins. The bound is unchanged (the
film is the numbing; the soul beneath the line is §5.1; the moral line is the soothe, not the HP bar).

**No divergence created.** `GAME_DELTAS.md:282` already reconciled the shipped `purificationThreshold` as *not* a
divergence — cited as precedent, unedited. No retired term, no Tier-3 touch, no fallen-taxonomy change; all five
lints green. `CHANGELOG` entry added. Three-way in sync (build `GAME_SPEC.md` §4.5.1/§4.6 + twin diffed
identical; `Nikeverse-mmo-rpg-from-scratch/docs/KNOWN_ISSUES.md` Q26 carries the mechanics + owner-owed numbers).
