# NIKEVERSE LORE ↔ GAME RECONCILIATION — CHANGELOG

## Date: July 29, 2026 — Nolem's limit is KNOWLEDGE, not permission

**Owner ruling.** The 2026-07-29 *"Nolem can do anything he's evil"* amendment left a piece of ratified content
without a reason to exist. The Dimension Eater — adopted by owner ruling on 2026-07-27 — was justified entirely
by a limit that ruling appeared to remove. `entities/dimension-eater.json` stated it outright: *"Singulars
cannot freely enter most dimensions. The Eater's entire purpose is that it CAN — **that limit is the reason
Nolem needed it at all.**"* Same clause in `singulars/index.json` and in the Eater's severance rationale in
`singulars/nolem.json`.

**The Tier-1 source settles it.** `comic-books/book-01/script.md:910`, Nike Prime explaining how Nolem travels:
*"He can do that because he knows where he is and where his next target is. He then folds space-time, bridging
the two places **because he knows the coordinates of both.**"* And `:911` — the trap works because *"the spatial
coordinates shift multiple times per second."*

**THE RULING: the limit was never permission. It is KNOWLEDGE.** Nolem is not fenced out of anything — he
cannot reach what he cannot **locate**. No door is closed to him; he is hunting. This keeps *"he can do
anything"* fully intact while preserving the constraint the whole endgame rests on, and it explains why the
only thing that has ever held him is a **coordinate scrambler** rather than a wall. The trap stops being a
lucky counter and becomes a direct exploit of his nature.

**The Dimension Eater survives, and its purpose gets stronger.** It needs no coordinates because it does not
*target* a place — it **eats its way** to one. So it reaches what Nolem cannot locate, which is a better reason
for a hunter to have made it than the old one: a scout that finds the unfindable is worth more to him than a
key is to a prisoner. Everything else about the Eater is untouched — still a severed appetite, still
structurally smaller than him by construction, still never steals his thunder.

**Rejected alternative, recorded so it is not re-proposed:** *delegation by appetite* — that he could always go
anywhere and severed the Eater merely to be in ten thousand places at once while he slept. Maximally powerful,
but it requires rewriting the Eater's entire `why` block and discards the comic's tie between how Nolem travels
and how he was imprisoned.

Landed in `singulars/index.json`, `singulars/nolem.json`, `entities/dimension-eater.json`, `GAME_SPEC.md` §3.16
and the regenerated Tesana twin — all three artifacts, same session. Every struck phrasing is retained inside
its amendment note.

## Date: July 29, 2026 — NOTHING IS CONSUMED: Nike Prime is held, not fuelled

**The question.** Why must Nike Prime's manifestation be re-earned each season rather than banked? The owner
proposed: *"Maybe because Nike prime uses up the bond energies and then needs more again to sustain him whole
each time,"* and asked for a multi-agent brainstorm. Four lenses ran — cosmology, narrative, MMO systems, and
an adversarial skeptic briefed to attack rather than build.

**The result was 4/4 against the mechanism and 4/4 FOR the instinct.** Both halves are load-bearing.

**The instinct was right, and it caught a real hole.** "Bonds are structure, not fuel" is a *statement, not a
mechanism* — it says he decoheres and supplies **no cost term at all**, and a posture with no cost is the
high-water mark that LAW 3 already calls a wallpaper generator. There must be a cost and it must recur. The
instinct also has genuine ancestry: `MASTER_LORE_PROPOSAL_FINAL.md:907` says the empathy core was *"to be
**powered by** collective bonds"* — superseded, not imagined.

**But "consume" is the villain's own verb, on the page.** `comic-books/book-01/script.md:915`, Nike Prime
explaining the trap: *"This means he won't be able to **absorb** anyone else, which means he **won't get
stronger**."* Absorb → get stronger → stay whole. A Prime who burns bonds is that sentence with the name
changed. It would also file every bonded Nike as an instrument — beneath even Charles AI in an Absolute Order
that "nothing reorders" — make E10 Singularity rhetorically unwinnable, and invert §1.2's best line: *a
relationship does not go in a vial* would become *does not **stay** in a vial*, and a furnace is not a better
container than a vial.

**THE RULING.** He is not fuelled, he is **HELD** — a posture the realm stands in, a chord rather than a
battery. It sounds while the notes are played, stops when they stop, and every string is undamaged afterward.
**The cost is real and it is the Collector's own hands:** six live slots, and those six are what you fight
with, so carrying a form nobody else will carry is a genuine sacrifice. *Your arms ache. Nothing is consumed.*
**It lapses because NOLEM UNMAKES THE SHAPE** — the 2026-07-29 "he makes the wound" amendment cashed out as a
system. Re-forming, never refuelling.

**Re-earning is REUNION, not repetition.** What Nolem tears off is specific and named, so a Collector goes back
for souls they know. Corollary, absolute: every decline event is written as *"he pulled"*, never *"we slipped"*
— a war meter that generates in-fighting is worse than no war meter.

**Sanctioned language:** held · attend · stand · carry · sound · keep the shape · let go. Banned in all
player-facing text: spend · burn · consume · fuel · power · drain · recharge, and the nouns energy · charge ·
battery · reserve. *(This retires the owner's own phrase "bond energies" — an "energy" implies a gauge, and
whoever writes the tooltip will write 4,120 / 5,555, which the odometer ban already forbids.)*

**TWO BUGS FOUND AND FIXED, both verified independently before acting.**

1. **The chapter-win gate eliminated realms mid-season, silently.** `∫1[I≥0.95]dt ≥ 0.8·season` requires 80% of
   the season above 0.95 — on an 8-week season a realm first crossing in week 2 has 6 weeks against a 6.4-week
   requirement and is already mathematically eliminated without being told. Any single dip does the same.
   **Fixed:** manifestation is a continuous read of `I`, never a threshold unlock, so there is nothing to be
   eliminated from; the integral is demoted to a title condition. No season can be over before it ends.
2. **The meter was specced as two incompatible objects.** `GAME_SPEC.md:1984` rules a **census** ("counts souls
   held, not threads held"); `PATTERN_INTEGRITY.md` §3 modelled an **integrator** (a float accumulating
   contributions against decay). A census has no `R_in` and no decay term. **Fixed:** the census is the ruled
   object, and "decay" is Nolem un-holding specific named souls — an event you watch, not a number ticking
   down. Hoarding becomes structurally impossible, since a census cannot be banked.

Landed in `CANON.md` §1.2, `PATTERN_INTEGRITY.md` §0.6 and §3, `GAME_SPEC.md` §7.5, and the regenerated Tesana
twin — all three artifacts, same session.

## Date: July 29, 2026 — THE THREE SCALE LAWS, and the held-vs-cumulative question closed

**Owner ruling, from the design conversation that produced them.** *"5555 different species goal should be a
permanent goal for all new players forever. If Nike prime is completed, we would lose the main motivation"* —
and then, decisively: *"once we hit 9000 players, 5555 will have a high chance of being sustained permanently
perhaps. Removing new player purpose."*

Both objections were correct, and the second one generalises past the specific number: **any fixed
server-wide threshold saturates at scale.** 9,000 players × 6 live slots = 54,000 held slots chasing 5,555
forms — a 10× oversupply that clears any fixed bar permanently and turns the meter into wallpaper. That is
arithmetic, not tuning, and no amount of lore can guarantee it away.

**The three laws, now in `PATTERN_INTEGRITY.md` §0.5, `GAME_SPEC.md`, the Tesana twin and the build repo's
auto-loaded `CLAUDE.md`:**

1. **New-player purpose NEVER depends on realm state.** A player joining in year six needs exactly the same
   reason to play as one who joined at launch. The permanent goal is therefore the **personal Bond Log** —
   5,555 forms, per player, cumulative — and nothing about it may be gated on, accelerated by, or devalued
   by anything the realm has already achieved. The realm meter is the reason to *coordinate*, never the
   reason to *log in*.
2. **The realm meter is a CONTEST, not a bar.** Its opponent scales with the population. Since the
   2026-07-29 amendment Nolem **makes the wound** and responds; Surge pressure indexes to player count.
   *"Popularity grows the Devourer, never the ease"* is this law.
3. **Any FIXED server-wide bar saturates at scale — never gate anything permanent behind one.**

**The corollary that makes the meter safe to ship:** because Law 1 holds, **it does not matter if the meter
saturates.** A large stable population may well park it high; that is a live-ops knob, not a canon problem.
If nothing permanent was resting on it, saturation costs nothing.

**Held vs cumulative is CLOSED — it is both, on two different objects.** The personal Log is **cumulative**
(your *reach*: which forms you are able to hold; permanent, never decrements). The realm Pattern is **held**
(which forms are live right now; decays, contested). One number, two verbs. **You collect all 5,555 so that
you can hold any of the 5,555** — a Collector with a complete Log can fill an arbitrary gap in the weave;
ten thousand Collectors holding the same form still add exactly **one**. Landed in `CANON.md` §1.2, which
had carried this as an explicit open flag since this morning.

**And the in-world reason the Prime Era's method was insufficient.** Stoner Nike put 5,548 samples *in
vials* — storage. He got the ninety-nine hundredths of a person that **can** be stored and missed the part
that can only be **sustained**. A relationship does not go in a vial. Not a retcon: it is why Book 1's Nike
Prime can think, fight and strategise and cannot connect.

**⛔ Nike Prime is NEVER permanently completed by a realm event, and neither is the Weaver.** A being made of
connection cannot be achieved and banked. This also re-affirms the 2026-07-26 3/3 ruling, whose stated reason
was the owner's exact objection three days early: *"a realm meter may never gate a personal cosmology beat —
that locks out everyone who arrives after the hold."*

**Defect fixed in passing.** `PATTERN_INTEGRITY.md` said the chapter-turn *"immortalizes the top-RCS
contributors"* while `GAME_SPEC.md` said *"**never** a top-RCS list… the people who won it are everyone who
was holding one."* GAME_SPEC is the corrected side. A leaderboard there would also break Law 1 — it makes
the turn a thing that happened to other people.

## Date: July 29, 2026 — NOLEM MAKES THE WOUND; the Discord game is demoted as a lore authority

**Owner ruling.** *"Nolem can do anything he's evil. He can definitely cause wounds. Don't follow discord
game lore. It's the weakest lore of the bunch and I didn't like Nolem in it. He needs to be big, scary and
powerful so it's epic to beat him."*

**§5.3's "the wound is not his" is STRUCK, and so is the immunity it implied.** The section said a wound had
to come first and that it was never Nolem's, concluding that *"genuine connection is immune to him."* Both
clauses are gone. He engineers the despair himself, at whatever scale he likes.

**Two claims were bundled in that section and only ONE is struck.** This is the important part:

| | Status |
|---|---|
| The numbing is **ACCEPTED, never installed** — he offers, the soul takes it | ✅ **STANDS** |
| The wound **is not his** | ⛔ **STRUCK** |

Because the numbing is still *taken* rather than *fitted*, it is still not the person — so separability, the
**waking** verb, `Keth'nor` as a stain *on* a thing, the soul-mote ruling and the entire moral architecture
are **untouched**. Nothing downstream of the accepted-numbing claim moved.

**Connection is now RESISTANCE, not immunity — and it is the scarier reading.** Immunity made safety a rule
and made him small: a monster who literally cannot open a door is a puzzle, not a threat. He can now break
anything given enough force and time; connection makes a soul **expensive**, not unreachable. Bonding becomes
holding a line rather than applying a ward, which is what makes beating him *epic* instead of procedural.

**It also makes him worse on purpose, which is the point.** He must BUILD the despair before he can sell the
cure. Every corrupted Legendary is something he did to them, deliberately, in advance. He is not weather. And
Gladiator Nike's shipped lines get *stronger*: *"The corruption came AFTER"* is still exactly true — what
changes is that the thing which came before need not have been anybody's accident.

**Nolem now has a power profile, assembled from Comic Book 1** (`singulars/nolem.json` → `power`). The record
previously had no corporeal portrait at all, so any future encounter would have been invented from nothing.
On the page: a Singular, one across all realities, eons old; at full strength he devours entire realities;
killing him fails outright; he has massacred one being across thousands of realities; he wears avatars to
break a world's birth, soil and food; he corrupts living allies mid-battle on sight; he is immune to the
poison that drops Retnuhxed, shrugs off the champion boxer, clears embedded weapons by releasing energy from
inside himself, and is pushed back — but not beaten — by a being grown from the DNA of thousands of Nikes.
**And all of that is him WEAKENED.** Writing rule recorded: never write him as weather, luck or an ambient
force; when in doubt make him bigger, and let the *cost of beating him* be what is expensive, never his reach.

**The Discord game is demoted — SCOPED, deliberately.** The direction-of-truth rule in all three `CLAUDE.md`
files called it *"the SHIPPED GROUND TRUTH for anything a player can see… it has beaten the design documents
on essentially every contested point."* It is now split:

- **Still authoritative for WHAT EXISTS** — rosters, creature/move/trait data, flags, gates, region contents,
  level bands, mechanics. It is a running product. **Every `GAME_DELTAS` ruling made on that basis stands**,
  including the anchor roster, the 292/144 split and the co-banded levels.
- **NOT authoritative for cosmology, characterisation or tone** — above all Nolem. For those, `comic-books/`
  and ratified `CANON.md` outrank it, and a weak shipped line is a thing to **outgrow**, not to propagate.

The scoping is a judgement call and is flagged as one: demoting the factual record too would invalidate a
large amount of correctly-settled work that has nothing to do with the quality of the writing.

## Date: July 29, 2026 — Comic Book 1 lands; the 5,555 is a SPECIES count and the arithmetic closes

**The primary source finally exists in a repository.** `comic-books/book-01/` now carries *Nike the Pig:
Book 1* — the owner's own comic, Tier 1 — as the delivered PDF plus a verbatim, uncorrected extraction.
For ten months every reading of the 5,555 was derived from a secondhand paraphrase of a document nobody
working on it could open. The full 122-agent audit against all four repos is `RECONCILIATION.md`; the
per-claim register is `claims.json`.

**Owner ruling — Tier 0 is established above Tier 1.** *"I know comic contradicts canon in many ways. And
it's also not the final tier 1 truth. My say is the final truth. And it will be my vision."* The comic is
the highest-authority **source** in the project — above every design doc, every JSON file and both games —
and the owner is above the comic. A comic/canon collision is a **question put to the owner**, never an
automatic rewrite; and an unruled comic detail is **not thereby canon** either. Landed in
`CONTRIBUTING.md`, `comic-books/README.md` and `CLAUDE.md`'s direction-of-truth list.

**Owner ruling — the 5,555 counts distinct Nike FORMS.** One form per universe, so each of the 5,555 is at
once a unique individual *and* a unique kind; the species and individuals readings were never actually
rivals. Bonding a duplicate form stays **legal** but does not advance the 5,555. This **restores** the
original vision — `LORE_BIBLE.md` §9, *"all 5,555 Nike types"*, deleted 2026-02-11 in a bare commit with no
rationale, no CHANGELOG entry and no register row — and it **supersedes** `THE_5555.md`'s former assertion
that *"the 5,555 cannot be a species count."* Landed in `CANON.md` §1.2 and `GAME_SPEC.md` §4.1 + the twin.

**Owner ruling — the arithmetic closes by subtraction.** `5,555 − 1 (Stoner Nike himself, who collects from
"all of the Other Nike's") − 6 already accounted for in the order = 5,548 vials`, the comic's one stated
figure (`script.md:339`). **The six are Engineer, Computer Coder, Botanist, Nutritionist, Gladiator and
Boxer.** The wording is *"already accounted for in the order"*, not *"already swabbed"*: the order is placed
before any recruitment, and the spit vials handed to champions on-page are fungible stock from the same box.

**The old derivation was wrong and is struck.** `MASTER_LORE_PROPOSAL_FINAL.md:928` — *"5,548 + the 4
Scientist Nikes, the 5 Champions, Stoner Nike himself, and Nike Prime"* — sums to **5,559**. It was the
corpus's only published justification for the number and it never closed. Annotated in place as provenance;
never cite it. **Book 1 never states 5,555** (`grep` = 0): cite the comic for 5,548 and the owner for 5,555.

**A fabricated quotation was found load-bearing in four repositories and is STRUCK.** Engineer Nike's
*"Wait, the empathy core isn't—"* does **not** appear in Book 1 (`grep -c -i "empathy"` = 0), and Engineer
Nike is **alive** at the end of the book, so he has no last words. It originated as a speculative bullet
under *"The Conspiracy"* at `MASTER_LORE_PROPOSAL_FINAL.md:795` and was later promoted into `GAME_SPEC.md`'s
*"Canon dialogue — preserve verbatim"* list and stored as `lastWords` in the lore JSON. Replaced everywhere
with the real line at `script.md:885`: *"Nike, you were released a bit before you were 100% complete."*
Correcting a false statement **about** the primary source needed no owner ruling. **The empathy-core CONCEPT
is not struck** — that is a separate open question (`claims.json` → `cb1-empathy-core-concept`).

**Boxer Nike does not die in Book 1.** The sacrifice clause is deleted from `dimensions/grand-arena.json:36`.
His fight with Nolem is a staged demonstration for the newly-released Nike Prime (*"WE DIDN'T TEACH YOU HOW
TO FIGHT YET! WATCH AND LEARN!"*, `:976`), he hands off at `:986`, and he speaks after the battle (`:1008`).
A defect fix inside existing canon: the clause already contradicted its own file's `corruptionReason`
(*"Boredom"*) and `timeline/legendary-falls.json:90-93`, where he falls 500–1500 years later.

**What the comic RATIFIED, and this is most of it.** The five Champions are the five shipped anchor bosses,
5-for-5. Nolem bound and never killed — with the *reasoning* the docs had only asserted. Nike Prime at 99%
with the chamber left empty. The four Scholars, 4-for-4. Dexter Hun as Nolem's worn avatar, matching the
First Tongue's `Dex'tur` (*dex* to wear + *tur* body) exactly. And three Tier-3 mysteries stay frozen,
ratified by the source's own refusal to answer them.

**Refuted, so nobody re-raises them:** the comic does **not** invert the Shattering (it never mentions OG
Nike and never denies it — a gap, not a contradiction, and its *"SAME GENETICS"* line at `:214` is evidence
*for* one-soul-many-bodies); `NOLEM` reversed is **not** `MELON` ⚠ **THIS REFUTATION WAS ITSELF WRONG — corrected 2026-07-29.** `NOLEM` reversed *is* `MELON`, and `RETNUHXED` reversed *is* `DEXHUNTER`; both verify mechanically, and the owner has confirmed the real-world origin. The audit refuted a trivially checkable string reversal. Kept as the record of the error: **a refutation is not self-verifying.** The reversals are out-of-world provenance only — never in-world, never a puzzle (`CANON.md` §3.2).; the Sixth Seat provenance panic is dead;
the Shinden mist collision is dead. 74 of 137 findings died under adversarial verification.

**STILL OPEN — put to the owner, not edited.** Nike Prime may not be in the trap at all (`script.md:1033` —
Nolem goes alone; Prime and Shiro detach and land alive), which contradicts ~25 sites including shipped
Discord dialogue. Whether *"Retnuhxed"* names a reversible state as well as a kind. Whether Nolem
manufactures the wound (`CANON.md` §5.3). The Shiro/Charles-AI merge. The Scattering's era. And the
**mechanism** question the species ruling deliberately does *not* settle: Book 1's win is a cumulative
collection, `CANON.md` §1.2's is a simultaneous hold. Until ruled, the held-threshold reading stands and no
document may cite Book 1 for a cumulative game-side win condition.

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
