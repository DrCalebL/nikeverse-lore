# Contributing to Nikeverse Lore

Thank you for your interest in expanding the Nikeverse!

## 📋 Guidelines

### Suggesting Lore Additions
1. Open an Issue with tag `lore-proposal`
2. Describe your addition and how it connects to existing canon
3. Wait for approval before submitting PR

### Fixing Errors
1. Fork the repository
2. Make corrections
3. Submit PR with clear explanation

### Canon Hierarchy

| Tier | Source | Authority |
|------|--------|-----------|
| **0** | **The owner's ruling** | **Final. Supersedes every tier below, including the comics.** |
| 1 | Comic books, main campaign | Primary source material — the strongest evidence, **not the verdict** |
| 2 | Raid lore, side quests | Secondary canon |
| 3 | Community contributions | Requires approval |

**Tier 1 is evidence, not a verdict.** The comics are the highest-authority *source* in the project and
they outrank every design doc, every JSON file, and the shipped games — but the owner outranks them.
Where a comic and current canon disagree, that is a **question put to the owner**, never a resolved
ruling: quote both sides, state the blast radius, recommend, and wait. Do not rewrite ratified canon on
a comic's authority alone. Equally, a comic detail the owner has not ruled on is **not thereby canon** —
it is evidence awaiting a ruling. See `comic-books/README.md`.

### Style Guide

- Present tense for current-era content
- Past tense for historical events
- Maintain mystery — not everything needs explaining
- **Connection > Isolation** — this is the core theme

### JSON Files

- Follow existing schemas in `/schemas/`
- Use camelCase for keys
- Include `id`, `name`, and `description` at minimum
- Test that JSON is valid before submitting

## 🚫 Don't

- Contradict established canon without discussion
- Add content that doesn't fit the tone
- Submit low-effort additions

## ✅ Do

- Reference existing lore when adding new content
- Think about how additions affect the larger story
- Be creative within the established framework

## Questions?

Open an Issue with tag `question`.
