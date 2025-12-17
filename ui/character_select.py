import cv2
from config.settings import WIDTH, HEIGHT, GRAY, WHITE, YELLOW, GREEN, RED
from data.characters import characters
from utils.ui_panel import draw_panel
from config.ui_layout import CHAR_AREA_Y, CHAR_AREA_H
from config.ui_layout import PLAYER_INFO_Y, PLAYER_INFO_H

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


def draw_character_select(canvas, selected_character):
    draw_panel(canvas, 40, CHAR_AREA_Y, WIDTH - 80, CHAR_AREA_H)

    for x, y, w, h, char in char_cards:
        color = RED if selected_character == char["name"] else GRAY

        cv2.rectangle(canvas, (x, y), (x + w, y + h), color, -1)
        cv2.rectangle(canvas, (x, y), (x + w, y + h), WHITE, 2)

        cv2.putText(
            canvas,
            char["name"],
            (x + 20, y + 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            WHITE,
            2,
        )

        cv2.putText(
            canvas,
            f"HP  : {char['hp']}",
            (x + 20, y + 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            WHITE,
            2,
        )
        cv2.putText(
            canvas,
            f"ATK : {char['atk']}",
            (x + 20, y + 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            WHITE,
            2,
        )
        cv2.putText(
            canvas,
            f"DEF : {char['def']}",
            (x + 20, y + 200),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            WHITE,
            2,
        )

    if selected_character:
        cv2.putText(
            canvas,
            f"Selected: {selected_character}",
            (WIDTH // 2 - 140, HEIGHT - 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            GREEN,
            2,
        )

def draw_player_preview(canvas, player):
    if not player:
        return

    panel_x = 50
    panel_w = WIDTH - 100

    draw_panel(canvas, panel_x, PLAYER_INFO_Y, panel_w, PLAYER_INFO_H)

    y = PLAYER_INFO_Y + 40
    x = panel_x + 30

    cv2.putText(canvas, "PLAYER INFO", (x, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.putText(canvas, f"Name : {player.name}", (x, y + 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)
    cv2.putText(canvas, f"HP   : {player.hp}/{player.max_hp}", (x, y + 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)
    cv2.putText(canvas, f"ATK  : {player.atk}", (x + 300, y + 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)
    cv2.putText(canvas, f"DEF  : {player.defense}", (x + 300, y + 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)