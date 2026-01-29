# 🐷 Nikeverse Lore

> *"I don't know what you are, but you're not dying today. Not while I'm here."*  
> — OG Charles Hoskinson, The First Bond

The official lore repository for the **Nikeverse** — a multiverse of 5,555 Nikes across infinite dimensions, bound together by the power of connection.

---

## 📖 About Nikeverse

Nikeverse is an expansive multimedia universe featuring:

- 🎮 **Nikeverse Discord MMORPG** — Creature collection and campaign game
- 📚 **Nike the Pig Comics** — Graphic novel series
- ⚔️ **Legendary Siege Raids** — Multiplayer events with deep lore
- 🌐 **Expanded Universe** — Future games, stories, and content

**Core Theme**: *Connection defeats isolation. Bonds are stronger than entropy.*

---

## 🗂️ Repository Structure

```
nikeverse-lore/
├── README.md                    # This file
├── LORE_BIBLE.md               # Complete lore overview
├── CONTRIBUTING.md             # Contribution guidelines
│
├── timeline/                   # Historical eras & events
│   ├── ages.json              # The six cosmic ages
│   └── events.json            # Major historical events
│
├── singulars/                  # Cosmic entities
│   ├── index.json             # All singulars
│   ├── cthulhu.json
│   └── nolem.json
│
├── civilizations/              # Peoples & cultures
│   └── aethkai.json           # Lost precursor civilization
│
├── dimensions/                 # Playable regions
│   ├── index.json             # All dimensions summary
│   ├── convergence-hub.json
│   ├── shinden.json
│   ├── frostfall.json
│   ├── grand-arena.json
│   ├── imperial-colosseum.json
│   ├── neon-city.json
│   ├── void-terminus.json
│   └── nolem-maw.json
│
├── characters/                 # Major characters
│   ├── charles-variants/      # All Charles echoes
│   ├── legendary-nikes/       # Freeable legendary Nikes
│   ├── harbingers/            # Corrupted Nike bosses
│   └── villains/              # Antagonists
│
├── creatures/                  # Nike variants & enemies
│   ├── nike-categories.json   # Champion, Scholar, Oddity, etc.
│   └── retnuhxed.json         # Shadow army
│
├── artifacts/                  # Important items
│   └── dimensional-anchors.json
│
├── languages/                  # Constructed languages
│   └── first-tongue/
│       ├── dictionary.json    # Word definitions
│       └── phrases.json       # Common phrases
│
├── prophecies/                 # Prophecies & mysteries
│   ├── aethkai-prophecy.json
│   └── mysteries.json
│
├── mythology/                  # Regional legends & folklore
│   ├── shinden/
│   ├── frostfall/
│   ├── grand-arena/
│   ├── imperial-colosseum/
│   ├── neon-city/
│   └── void-terminus/
│
└── schemas/                    # JSON schemas for validation
    └── dimension.schema.json
```

---

## 🚀 Quick Start

### For Readers
Start with the [Lore Bible](LORE_BIBLE.md) for a complete overview.

### For Developers
All data is available as JSON. Fetch directly from GitHub raw:

```javascript
// Example: Fetch dimension data
const res = await fetch(
  'https://raw.githubusercontent.com/YOUR_USERNAME/nikeverse-lore/main/dimensions/shinden.json'
);
const shinden = await res.json();
console.log(shinden.name);          // "Shinden"
console.log(shinden.theme);         // "Feudal Japan"
console.log(shinden.charles.name);  // "Ronin Charles"
```

---

## 🌟 Core Concepts

| Concept | Description |
|---------|-------------|
| **The First Bond** | OG Charles + OG Nike's cosmic connection that started everything |
| **The Shattering** | When reality fractured and the First Bond echoed into 5,555 Nikes |
| **Charles Constant** | Cosmic law: wherever Nikes exist, a Charles exists to help them |
| **Nike Prime** | All 5,555 Nikes as one — "5,555 souls carrying each other" |
| **Nolem** | The Singular of Entropy — corrupts through isolation |
| **Singulars** | Cosmic beings that exist once across all realities |
| **Harbingers** | Corrupted Nikes who serve Nolem |
| **Retnuhxed** | Nolem's shadow army |
| **First Tongue** | Ancient language from before the Shattering |

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📜 License

© Nikeverse. All rights reserved.

---

*"Every Nike carries a fragment of the First Bond. Every Charles carries its echo. Together, we are stronger than entropy itself."*
