# NIKEVERSE LORE REPOSITORY

The single source of truth for all Nikeverse lore, connecting Comic Book 1 to the Discord Game and beyond.

## 📖 QUICK START

**New to the lore?** Start with `MASTER_LORE_PROPOSAL_FINAL.md` - it contains the complete canon overview.

**Looking for specific data?** Browse the JSON files below.

---

## 🌌 TIMELINE OVERVIEW

```
PRIME ERA (Comic Book 1)
    │
    │  • Cthulhu warns Stoner Nike
    │  • Five Champions gathered
    │  • Nike Prime created at 99% — missing empathy core
    │  • Nike Prime traps Nolem, vanishes into the trap
    │  • The Pattern pulses through every fragment
    │
    ▼
THE LONG SILENCE (Comic Books 2-???)
    │
    │  • 3,000 years of expansion space
    │  • 27 Legendary Nikes fall to corruption
    │  • History becomes legend becomes nothing
    │
    ▼
ECHO ERA (Discord Game)
    │
    │  • All Legendaries corrupted
    │  • A new Collector rises
    │  • Free the Champions, gather 5,555 bonds
    │  • Complete Nike Prime's missing empathy core
```

---

## 📁 REPOSITORY STRUCTURE

```
nikeverse-lore/
│
├── MASTER_LORE_PROPOSAL_FINAL.md    # ⭐ START HERE - Complete canon
├── README.md                         # This file
├── CONTRIBUTING.md                   # How to contribute
├── CHANGELOG.md                      # Change history
│
├── timeline/
│   ├── ages.json                     # All cosmic ages
│   ├── prime-era.json                # Comic Book 1 events
│   ├── long-silence.json             # Expansion space for future comics
│   └── legendary-falls.json          # When each Legendary was corrupted
│
├── characters/
│   ├── legendary-nikes/
│   │   └── index.json                # All 27 Legendary Nikes + game encounters
│   ├── charles-ai.json               # Charles AI (portal abilities, cat quirks)
│   ├── charles-variants/
│   │   └── index.json                # Hub Charles, Ronin Charles, etc.
│   ├── comic-characters.json         # Stoner Nike, Pico, Hennifer, etc.
│   ├── collectors-journey.json       # Game campaign structure & progression
│   └── harbingers/
│       └── index.json                # Nolem's corrupted lieutenants
│
├── dimensions/
│   ├── index.json                    # All 8 dimensions (summary)
│   ├── convergence-hub.json          # Tutorial / Nexus
│   ├── shinden.json                  # Feudal Japan
│   ├── frostfall.json                # Viking Tundra
│   ├── grand-arena.json              # Boxing / Fighting
│   ├── imperial-colosseum.json       # Roman Empire (Nike Prime's birthplace)
│   ├── neon-city.json                # Cyberpunk
│   ├── void-terminus.json            # Edge of Reality (OG Nike's vigil)
│   └── nolem-maw.json               # Final Battle
│
├── singulars/
│   ├── index.json                    # Cosmic entities overview
│   ├── nolem.json                    # The Devourer
│   └── cthulhu.json                  # The Whisperer
│
├── factions/
│   └── index.json                    # Remnant, Harbingers, Lost Builders
│
├── prophecies/
│   └── mysteries.json                # Prophecies & the 5,555 Prophecy
│
├── civilizations/
│   └── aethkai.json                  # The lost precursor civilization
│
├── languages/
│   └── first-tongue/
│       └── dictionary.json           # Ancient Aeth'kai language
│
└── schemas/
    └── dimension.schema.json         # JSON validation schema
```

---

## 🔑 KEY NUMBERS

| Count | What |
|-------|------|
| **5,555** | Total Nike souls — bonds needed to complete Nike Prime |
| **27** | Legendary Nikes (special fragments with more of OG Nike's essence) |
| **5** | Champions gathered in Comic Book 1 |
| **8** | Dimensions in the Discord Game |
| **6** | Harbingers — Nolem's fallen-Collector lieutenants (the player-kind) |
| **~3,000** | Years of The Long Silence (expansion space) |

---

## 🐷 THE 27 LEGENDARY NIKES

### Champions (7)
Gladiator Nike, Ninja Nike, Viking Nike, Nike Tyson Nike, Cyberpunk Nike, Berjador Nike, Bertus Maximus Nike

### Scholars (5)
Dr Caleb Nike, Professor Nike, Satoshi Nike, Corey Hort Nike, Guthix Nike

### Mystics (3)
Nel Nike, Pigsterio Nike, Jedi Nike

### Beasts (5)
Hydra Nike, Wolf Mode Nike, Colossal Nike, Elbonzys Nike, Cardano Whale Nike

### Cosmic (2)
Cosmic Nike, Phoenix Nike

### Oddities (3)
McJared Nike, Olecram Nike, Melon Nike (The Betrayer — willingly chose Nolem)

### Multiverse (1)
Peter Porker Nike

### Template (1)
OG Nike (not corrupted — active guardian at Void Terminus)

---

## 🌐 THE PATTERN

The living web of connections between all 5,555 Nike fragments and all Charles Variants. Different names across history:

| Term | Who Uses It |
|------|-------------|
| **Eth'kara** (heart-chain) | Aeth'kai prophecy (ancient) |
| **The First Bond** | Scholars, OG Nike (origin event) |
| **The Charles Constant** | Theorists (the law) |
| **The Pattern** | Collectors, Charles Variants (lived experience) |

---

## 📚 MEDIA CONNECTIONS

| Media | Era | Content |
|-------|-----|---------|
| **Comic Book 1** | Prime Era | The First War Against Nolem |
| **Comic Books 2-???** | The Long Silence | EXPANSION SPACE |
| **Discord Game** | Echo Era | Free the Legendary Nikes, gather 5,555 bonds |

---

## ⚠️ IMPORTANT NOTES

### Hub Charles vs Charles AI
**Hub Charles** is the local Shepherd at the Convergence Hub — a person. **Charles AI** is a separate floating interface built by Computer Coder Nike — a tool with portal abilities and subtle cat-like behavioral quirks (calming presence, mysterious pauses, uncanny intuition). They are distinct entities.

### Shiro Status
Shiro is being phased out of Nikeverse IP. His narrative functions have been absorbed into Charles AI as subtle behavioral quirks with deliberately mysterious origin. New content should not reference Shiro directly.

### Nike Tyson = Boxer Nike
Nike Tyson in the game IS Boxer Nike from the comic. The name evolved over millennia as legend became myth.

### Hierarchy
```
OG CHARLES HOSKINSON ─── The Legend (untouchable)
        │
CHARLES VARIANTS ─────── The Echoes (NPCs)
        │
CHARLES AI ───────────── The Tool (helpful, NOT a legend)
```

---

## 🎮 API USAGE

```javascript
const LORE_BASE = 'https://raw.githubusercontent.com/DrCalebL/nikeverse-lore/main';

// Get all Legendary Nikes
const legendaries = await fetch(`${LORE_BASE}/characters/legendary-nikes/index.json`).then(r => r.json());

// Get dimension data
const dimensions = await fetch(`${LORE_BASE}/dimensions/index.json`).then(r => r.json());

// Get timeline
const ages = await fetch(`${LORE_BASE}/timeline/ages.json`).then(r => r.json());

// Get Collector's Journey structure
const journey = await fetch(`${LORE_BASE}/characters/collectors-journey.json`).then(r => r.json());
```

---

## 📝 CONTRIBUTING

See `CONTRIBUTING.md` for guidelines on proposing lore changes.

---

*"Nike Prime isn't one soul carrying 5,555. Nike Prime is 5,555 souls carrying each other."*
