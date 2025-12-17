import cv2
import numpy as np

# =====================
# Canvas
# =====================
WIDTH, HEIGHT = 1000, 800
canvas = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

# =====================
# Warna
# =====================
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (70, 70, 70)
GREEN = (0, 255, 0)
YELLOW = (0, 255, 255)
RED = (0, 0, 255)

# =====================
# Game State
# =====================
mode = "MENU"
selected_character = None

# =====================
# MENU BUTTONS
# =====================
menu_buttons = ["New Adventure", "Exit"]

BUTTON_W = int(WIDTH * 0.3)
BUTTON_H = 70
SPACING = 30

menu_buttons_rect = []
start_y = HEIGHT // 2 - 100
start_x = (WIDTH - BUTTON_W) // 2

for i, label in enumerate(menu_buttons):
    y = start_y + i * (BUTTON_H + SPACING)
    menu_buttons_rect.append((start_x, y, BUTTON_W, BUTTON_H, label))


# =====================
# CHARACTERS
# =====================
characters = [
    {"name": "Warrior", "hp": 120, "atk": 15, "def": 10},
    {"name": "Mage", "hp": 80, "atk": 25, "def": 5},
    {"name": "Rogue", "hp": 100, "atk": 18, "def": 8},
]

CHAR_W = 220
CHAR_H = 300
CHAR_SPACING = 50

char_cards = []
total_w = len(characters) * CHAR_W + (len(characters) - 1) * CHAR_SPACING
start_x = (WIDTH - total_w) // 2
y = HEIGHT // 2 - 100

for i, char in enumerate(characters):
    x = start_x + i * (CHAR_W + CHAR_SPACING)
    char_cards.append((x, y, CHAR_W, CHAR_H, char))


# =====================
# DRAW FUNCTIONS
# =====================
def draw_title(text):
    size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.4, 3)[0]
    x = (WIDTH - size[0]) // 2
    cv2.putText(canvas, text, (x, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.4, GREEN, 3)


def draw_menu():
    for x, y, w, h, label in menu_buttons_rect:
        cv2.rectangle(canvas, (x, y), (x + w, y + h), GRAY, -1)
        cv2.rectangle(canvas, (x, y), (x + w, y + h), WHITE, 2)

        t = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
        tx = x + (w - t[0]) // 2
        ty = y + (h + t[1]) // 2
        cv2.putText(canvas, label, (tx, ty),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, WHITE, 2)


def draw_characters():
    global selected_character

    for x, y, w, h, char in char_cards:
        color = YELLOW if selected_character == char["name"] else GRAY

        cv2.rectangle(canvas, (x, y), (x + w, y + h), color, -1)
        cv2.rectangle(canvas, (x, y), (x + w, y + h), WHITE, 2)

        cv2.putText(canvas, char["name"],
                    (x + 20, y + 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, WHITE, 2)

        cv2.putText(canvas, f"HP  : {char['hp']}", (x + 20, y + 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, WHITE, 2)
        cv2.putText(canvas, f"ATK : {char['atk']}", (x + 20, y + 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, WHITE, 2)
        cv2.putText(canvas, f"DEF : {char['def']}", (x + 20, y + 200),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, WHITE, 2)


# =====================
# MOUSE EVENTS
# =====================
def mouse_event(event, x, y, flags, param):
    global mode, selected_character

    if event == cv2.EVENT_LBUTTONDOWN:

        # MENU
        if mode == "MENU":
            for bx, by, bw, bh, label in menu_buttons_rect:
                if bx <= x <= bx + bw and by <= y <= by + bh:
                    if label == "New Adventure":
                        mode = "CHARACTER_SELECT"
                    elif label == "Exit":
                        exit()

        # CHARACTER SELECT
        elif mode == "CHARACTER_SELECT":
            for bx, by, bw, bh, char in char_cards:
                if bx <= x <= bx + bw and by <= y <= by + bh:
                    selected_character = char["name"]
                    print("Character selected:", selected_character)


# =====================
# MAIN LOOP
# =====================
cv2.namedWindow("RPG Game")
cv2.setMouseCallback("RPG Game", mouse_event)

while True:
    canvas[:] = BLACK

    if mode == "MENU":
        draw_title("RPG DnD")
        draw_menu()

    elif mode == "CHARACTER_SELECT":
        draw_title("Select Your Character")
        draw_characters()

        if selected_character:
            cv2.putText(canvas,
                        f"Selected: {selected_character}",
                        (WIDTH // 2 - 140, HEIGHT - 120),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        GREEN,
                        2)

            cv2.putText(canvas,
                        "Press ENTER to start",
                        (WIDTH // 2 - 150, HEIGHT - 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        WHITE,
                        1)
            cv2.putText(canvas,
                        "< ESC to back",
                        (WIDTH // 2 - 150, HEIGHT - 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        WHITE,
                        1)

    cv2.imshow("RPG Game", canvas)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC
        if mode != "MENU":
            mode = "MENU"
            selected_character = None
        else:
            break

cv2.destroyAllWindows()
