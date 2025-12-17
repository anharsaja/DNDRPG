## 📁 Project Structure

```text
rpg_game/
│
├── main.py                 # Entry point (game loop)
│
├── config/
│   ├── __init__.py
│   ├── settings.py         # WIDTH, HEIGHT, colors
│
├── core/
│   ├── __init__.py
│   └── state.py            # game state (mode, selected_character)
│
├── save/
│   ├── load.py
│   ├── ...(player data)
│
├── data/
│   ├── __init__.py
│   └── characters.py       # character data
│
├── ui/
│   ├── __init__.py
│   ├── menu.py             # menu drawing & logic
│   └── character_select.py # character selection UI
│
└── utils/
    ├── __init__.py
    └── mouse.py            # mouse handler
```
