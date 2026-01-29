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
    │  • Nike Prime created & traps Nolem
    │  • Shiro merges with Charles AI
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
    │  • Free the Champions, save the multiverse
```

---

## 📁 REPOSITORY STRUCTURE

```
nikeverse-lore/
│
├── MASTER_LORE_PROPOSAL_FINAL.md    # ⭐ START HERE - Complete canon
├── LORE_BIBLE.md                     # Previous version (reference)
├── README.md                         # This file
├── CONTRIBUTING.md                   # How to contribute
│
├── timeline/
│   ├── ages.json                     # All cosmic ages
│   ├── prime-era.json                # Comic Book 1 events
│   ├── long-silence.json             # Expansion space for future comics
│   └── legendary-falls.json          # When each Legendary was corrupted
│
├── characters/
│   ├── legendary-nikes/
│   │   └── index.json                # All 27 Legendary Nikes
│   ├── charles-ai.json               # Charles AI (post-Shiro merge)
│   ├── charles-variants/
│   │   └── index.json                # Hub Charles, Ronin Charles, etc.
│   ├── comic-characters.json         # Stoner Nike, Pico, Hennifer, etc.
│   └── harbingers/
│       └── index.json                # Corrupted servants of Nolem
│
├── dimensions/
│   ├── index.json                    # All 8 dimensions with comic connections
│   ├── shinden.json                  # Feudal Japan
│   └── frostfall.json                # Viking Tundra
│
├── singulars/
│   ├── index.json                    # Cosmic entities overview
│   ├── nolem.json                    # The Devourer
│   └── cthulhu.json                  # The Whisperer
│
├── factions/
│   └── index.json                    # Remnant, Unravelers, Lost Builders
│
├── mysteries/
│   └── conspiracies.json             # The Five Great Mysteries
│
├── civilizations/
│   └── aethkai.json                  # The lost precursor civilization
│
├── languages/
│   └── first-tongue/
│       └── dictionary.json           # Ancient language
│
├── prophecies/
│   └── mysteries.json                # Unsolved mysteries
│
└── schemas/
    └── dimension.schema.json         # JSON validation schema
```

---

## 🔑 KEY NUMBERS

| Count | What |
|-------|------|
| **5,555** | Total Nikes created in The Shattering |
| **27** | Legendary Nikes (special fragments with more of OG Nike's essence) |
| **5** | Champions gathered in Comic Book 1 |
| **8** | Dimensions in the Discord Game |
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
McJared Nike, Olecram Nike, Melon Nike

### Multiverse (1)
Peter Porker Nike

### Template (1)
OG Nike (not corrupted, but exhausted)

---

## 📚 MEDIA CONNECTIONS

| Media | Era | Content |
|-------|-----|---------|
| **Comic Book 1** | Prime Era | The First War Against Nolem |
| **Comic Books 2-???** | The Long Silence | EXPANSION SPACE |
| **Discord Game** | Echo Era | Free the Legendary Nikes |

---

## ⚠️ IMPORTANT NOTES

### Shiro Status
Shiro merged with Charles AI at the end of Comic Book 1. He no longer exists as a separate entity. Charles AI now has portal abilities and cat-like personality quirks.

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
```

---

## 📝 CONTRIBUTING

See `CONTRIBUTING.md` for guidelines on proposing lore changes.

---

*"Nike Prime isn't one soul carrying 5,555. Nike Prime is 5,555 souls carrying each other."*
