# Comic books — Tier 1 source material

## ⭐ THE AUTHORITY RULE — read this before citing anything here

**The owner's ruling is the final truth. The comic is the highest-authority *source*, not the verdict.**

Owner, verbatim:

> *"I know comic contradicts canon in many ways. And it's also not the final tier 1 truth. My say is the
> final truth. And it will be my vision."*

So the comic **outranks every design doc, every JSON file, and the shipped games** — and the owner
outranks the comic. When the comic and canon disagree, that is a **question put to the owner**, not a
resolved ruling. Never rewrite ratified canon on the comic's authority alone, and never present a
comic-derived reading as settled. Bring the collision, quote both sides, recommend — then wait.

This cuts both ways, and the second direction is the one that gets forgotten: a comic detail the owner
has **not** ruled on is not thereby canon either. It is evidence awaiting a ruling.

| Tier | Source | Authority |
|---|---|---|
| **0** | **The owner's ruling** | **Final. Supersedes everything below, including the comics.** |
| 1 | Comic books (this directory) | Primary source material — the strongest evidence, not the verdict |
| 2 | Raid lore, side quests | Secondary |
| 3 | Community contributions | Requires approval |

## What lives here

| What | Where | Why |
|---|---|---|
| The script / lettered PDF | **here** — `comic-books/book-NN/` | small and text-bearing; belongs with the canon it governs |
| Extracted text layer | **here** — `comic-books/book-NN/script.md` | greppable; what a canon question is actually answered from |
| Extracted claims | **here** — `comic-books/book-NN/claims.json` | machine-checkable against `CANON.md` and the lints |
| **Full-res page art, scans, covers** | **`nikeverse-assets`** `comics/book-NN/` | large binaries; this repo is 2.8 MB of pure text and its value is being instant to grep |

A scan nobody transcribed answers no canon question — **none of this repo's verify gates can read an
image.** The extracted text is the working artifact; the PDF is its evidence. Reference page art from
`nikeverse-assets` by raw URL rather than duplicating bytes.

## Layout

```
comic-books/
  README.md          ← this file
  book-01/
    NIKE_THE_PIG_COMIC_BOOK_1.pdf   ← the source as delivered
    script.md                        ← extracted text, verbatim and uncorrected
    claims.json                      ← every falsifiable assertion, cited to a line
```

## `script.md` — the extraction rule

Committed **verbatim and uncorrected.** Typos, inconsistent speaker tags (`Stoner Niko`, `Nike Pro`,
`Boxer Niker`), and malformed art direction all stay. This is the file other documents are checked
against; a silent correction here is an unlogged edit to the highest-authority source in the project.

Book 1 is a **script**, not a lettered page transcript, so it carries its own `PAGE n` / `PANEL n`
labels inline. Those drift from PDF pagination — the `===== PAGE n =====` markers are PDF pages, and
script PAGE 2 begins partway down PDF page 1. **Cite both** when it matters: "PDF p.9 / script PAGE 7".

Three kinds of text live in a script and they are **not equal evidence** — always say which you are
citing:

1. **Dialogue** — strongest. A character stating something in-story.
2. **Art direction** (the ALL-CAPS `DRAW …` lines) — strong for what exists on the page, weaker for
   why. It describes a picture, not a claim.
3. **Author notes** — Book 1 ends with loose planning notes (from *"QUANTUM PHYSICS TELLS US…"*
   onward), several marked `done`. These are **intent, not story**, and several are build checklists.
   Never cite one as in-world fact.

## `claims.json` format

```json
{
  "source": "Nike the Pig: Book 1",
  "tier": 1,
  "claims": [
    {
      "id": "cb1-vial-count",
      "claim": "Stoner Nike requests 5,548 vials to collect the DNA of all the other Nikes.",
      "quote": "I'm going to need 5548 vials though so I can collect the DNA of all of the Other Nike's.",
      "scriptLine": 339,
      "scriptPage": "PDF p.10 / PAGE 7",
      "evidenceKind": "dialogue",
      "topic": ["the-5555", "nike-prime"],
      "status": "open"
    }
  ]
}
```

`evidenceKind`: `dialogue` · `art-direction` · `author-note` — per the rule above.

`status`:
- `open` — collision found, **awaiting the owner's ruling**
- `ruled-comic` — owner ruled the comic stands; canon changes to match
- `ruled-canon` — owner ruled the existing canon stands; the comic is superseded on this point
- `ruled-new` — owner ruled a third thing that is neither
- `agrees` — no collision; the comic ratifies existing canon

**Nothing moves out of `open` without an owner ruling logged in `CHANGELOG.md`.**

## After a book lands — the reconciliation pass

1. Commit the source **verbatim, in isolation**, before any interpretation.
2. Extract `claims.json`, every entry `status: "open"`.
3. Audit each claim against `CANON.md`, the JSON data, the build spec, and the shipped Discord game.
4. **Put the collisions to the owner** — quote both sides, state the blast radius, recommend. Do not
   edit ratified canon before the ruling.
5. Log each ruling in `CHANGELOG.md`; register any surviving cross-repo divergence in `GAME_DELTAS.md`.
6. Re-run the gates (`check-canon-terms.sh`, `check-mystery-tiers.py`, the JSON parse).
7. A ruling that touches the game must land in **all three artifacts in the same session** — the
   three-way rule in `CLAUDE.md` applies to comic-sourced rulings like any other.
