# Comics — Tier 1, Primary canon

`CONTRIBUTING.md` puts comic books at the **top** of the canon hierarchy — above the shipped Discord
game, above `CANON.md`, above every design doc in every repo. Until now that tier had **no body**: the
comic was cited only through `MASTER_LORE_PROPOSAL_FINAL.md`'s secondhand paraphrase, which is itself
labelled *"provenance, not a live spec."* This directory is where the primary source lands.

## The split — artifact vs. assertions

**Page scans do not go in this repo.** This repo is 2.8 MB of pure text and its whole value is being
greppable and instant; none of the verify gates can read an image. Put the artwork in
`DrCalebL/nikeverse-assets` (already the binary home) and reference it by raw URL from the transcript.

| What | Where | Why |
|---|---|---|
| Page scans, PDF, cover art | **`nikeverse-assets`** `comics/book-01/` | binary, large, already the asset repo's job |
| Transcript (text of every panel) | **here** — `comics/book-NN/transcript.md` | greppable; what a canon question is actually answered from |
| Extracted claims (structured) | **here** — `comics/book-NN/claims.json` | machine-checkable against `CANON.md` and the lints |
| Page-image URLs | **here** — in the transcript's page headers | keeps the two repos joined without duplicating bytes |

A scan nobody transcribed is not canon anyone can use. **The transcript is the canonical artifact in this
repo; the scan is its evidence.**

## Layout

```
comics/
  README.md          ← this file
  book-01/
    transcript.md    ← page-by-page, panel-by-panel; the readable primary source
    claims.json      ← every falsifiable assertion, with a page/panel citation
```

## `transcript.md` format

One `##` heading per page, one bullet per panel. Keep art description and dialogue distinct — a canon
question is usually settled by one or the other, and merging them loses which.

```md
## Page 4
![page 4](https://raw.githubusercontent.com/DrCalebL/nikeverse-assets/main/comics/book-01/p004.png)

- **Panel 1** — *Art:* Stoner Nike at a workbench, vials racked behind him.
  **Stoner Nike:** "Five thousand five hundred and forty-eight. One for each variant."
- **Panel 2** — *Art:* close on the rack; the count is legible on the label.
  *(no dialogue)*
```

Transcribe **verbatim**, including anything that contradicts current canon. A comic that disagrees with
`CANON.md` is not an error to be smoothed — it is a Tier-1 source overruling a Tier-2 one, and the
disagreement gets a `GAME_DELTAS.md` row and a `CHANGELOG.md` resolution.

## `claims.json` format

Every assertion that could be checked, cited to a panel. This is what makes the comic *enforceable*
rather than merely archived.

```json
{
  "source": "Comic Book 1",
  "tier": 1,
  "claims": [
    {
      "id": "cb1-vial-count",
      "claim": "Stoner Nike requests 5,548 vials for DNA collection.",
      "page": 4,
      "panel": 1,
      "topic": ["the-5555", "prime-era"],
      "status": "open"
    }
  ]
}
```

`status`: `open` (not yet reconciled) · `agrees` (matches current canon) · `overrules` (Tier 1 beats
what canon says — needs a CHANGELOG entry) · `superseded` (owner has explicitly retconned it).

## After a book lands — the reconciliation pass

1. Transcribe → `transcript.md`; extract → `claims.json` with every `status: "open"`.
2. Check each claim against `CANON.md`, the JSON data, and the shipped Discord game.
3. Every disagreement gets a `GAME_DELTAS.md` row and a `CHANGELOG.md` resolution.
4. Re-run the gates (`check-canon-terms.sh`, `check-mystery-tiers.py`, the JSON parse).
5. **Anything the comic settles that the game spec assumes must propagate to all three artifacts in the
   same session** — the three-way rule in `CLAUDE.md` applies to comic-sourced rulings like any other.

## Known question waiting on Book 1

**The 5,555's arithmetic does not close.** `MASTER_LORE_PROPOSAL_FINAL.md:927-928` paraphrases the comic
as 5,548 vials + 4 Scientist Nikes + 5 Champions + Stoner Nike + Nike Prime — which sums to **5,559**,
not 5,555. Either the paraphrase is wrong or the number was retrofitted. The comic settles it, and
`THE_5555.md` Phase −1 gets corrected from the primary source once it does.

Also open, and comic-settleable: whether the 5,548 are **variants/species** or **individuals** — the
paraphrase says *"DNA from 5,548 Nike **variants**"*, which reads as species, and that bears directly on
the live species-vs-individuals ruling.
