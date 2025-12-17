import cv2
import numpy as np
from core import state
from ui.menu import draw_menu, draw_title
from ui.character_select import draw_character_select
from utils.mouse import handle_mouse
from utils.image_loader import load_background
from config.settings import create_canvas

# ===== Init =====
canvas = create_canvas()

menu_bg = load_background("assets/backgrounds/bg.jpg")
char_bg = load_background("assets/backgrounds/bg1.jpg")

def mouse_event(event, x, y, flags, param):
    handle_mouse(event, x, y)

cv2.namedWindow("RPG Game", cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback("RPG Game", mouse_event)

while True:

    if state.mode == "MENU":
        canvas[:] = menu_bg
        draw_title(canvas, "RPG DnD")
        draw_menu(canvas)

    elif state.mode == "CHARACTER_SELECT":
        canvas[:] = char_bg
        draw_title(canvas, "Select Your Character")
        draw_character_select(canvas, state.selected_character)

    cv2.imshow("RPG Game", canvas)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        if state.mode != "MENU":
            state.mode = "MENU"
            state.selected_character = None
        else:
            break

cv2.destroyAllWindows()
