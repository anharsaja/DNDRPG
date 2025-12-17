import cv2
import numpy as np
from core import state
from ui.menu import draw_menu, draw_title
from ui.character_select import draw_character_select
from utils.mouse import handle_mouse
from utils.image_loader import load_background
from config.settings import create_canvas, WHITE, GREEN

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

    elif state.mode == "TUTORIAL":
        canvas[:] = menu_bg
        draw_title(canvas, "Tutorial")
        lines = [
            "Welcome to the tutorial!",
            "- Use the mouse to click buttons and select characters.",
            "- Press ESC to return to Menu at any time.",
            "Press any key to continue..."
        ]
        for i, line in enumerate(lines):
            cv2.putText(canvas, line, (50, 200 + i * 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, WHITE, 2)

    elif state.mode == "ENTER_NAME":
        canvas[:] = menu_bg
        draw_title(canvas, "Enter Player Name")
        # Draw input box
        box_w, box_h = 500, 60
        bx = (canvas.shape[1] - box_w) // 2
        by = 220
        cv2.rectangle(canvas, (bx, by), (bx + box_w, by + box_h), WHITE, -1)
        cv2.rectangle(canvas, (bx, by), (bx + box_w, by + box_h), (0,0,0), 2)
        # Render current buffer
        text = state.name_buffer or "Type name..."
        tx = bx + 12
        ty = by + (box_h + 20) // 2
        cv2.putText(canvas, text, (tx, ty), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,0), 2)
        cv2.putText(canvas, "Press Enter to confirm, ESC to cancel", (50, by + box_h + 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, WHITE, 1)

    cv2.imshow("RPG Game", canvas)

    key = cv2.waitKey(1) & 0xFF
    # Handle name entry keys when in ENTER_NAME mode
    if state.mode == "ENTER_NAME":
        if key != 255:
            # Enter/Return
            if key in (13, 10):
                name = state.name_buffer.strip() or "Player"
                from save import load as save_load
                try:
                    save_load.create_new_save(name)
                    state.current_save = name
                    print(f"Created new save for: {name}")
                except Exception as e:
                    print("Failed creating save:", e)
                state.name_buffer = ""
                state.mode = "CHARACTER_SELECT"
            # ESC - cancel
            elif key == 27:
                state.name_buffer = ""
                state.mode = "MENU"
            # Backspace
            elif key == 8:
                state.name_buffer = state.name_buffer[:-1]
            # Regular printable chars
            elif 32 <= key <= 126:
                state.name_buffer += chr(key)

    # If in tutorial mode, any key (except ESC) continues back to menu for now
    if state.mode == "TUTORIAL" and key != 255 and key != 27 and key != 0:
        state.mode = "MENU"
        state.selected_character = None

    if key == 27:
        if state.mode != "MENU":
            state.mode = "MENU"
            state.selected_character = None
        else:
            break

cv2.destroyAllWindows()
