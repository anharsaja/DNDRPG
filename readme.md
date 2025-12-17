rpg_game/
│
├── main.py                 # Entry point (game loop)
│
├── config/
│   ├── __init__.py
│   ├── settings.py         # WIDTH, HEIGHT, warna
│
├── core/
│   ├── __init__.py
│   ├── state.py            # game state (mode, selected_character)
│
├── data/
│   ├── __init__.py
│   ├── characters.py       # data karakter
│
├── ui/
│   ├── __init__.py
│   ├── menu.py             # menu drawing & logic
│   ├── character_select.py # character selection UI
│
└── utils/
    ├── __init__.py
    └── mouse.py            # mouse handler