import cv2
from core import state
from ui.menu import menu_buttons_rect
from ui.character_select import char_cards
from utils.player_factory import create_player

def handle_mouse(event, x, y):
    if event != cv2.EVENT_LBUTTONDOWN:
        return

    # MENU
    if state.mode == "MENU":
        for bx, by, bw, bh, label in menu_buttons_rect:
            if bx <= x <= bx + bw and by <= y <= by + bh:
                if label == "New Adventure":
                    # Switch to on-screen name entry mode
                    state.name_buffer = ""
                    state.mode = "ENTER_NAME"
                elif label == "Exit":
                    exit()
                elif label == "Load Game":
                    exit()

    # CHARACTER SELECT
    elif state.mode == "CHARACTER_SELECT":
        for bx, by, bw, bh, char in char_cards:
            if bx <= x <= bx + bw and by <= y <= by + bh:
                state.selected_character = char["name"]
                state.player = create_player(char["name"])
                print("Player created:", state.player.name)
                # If there is an active save, update it with the chosen character
                if state.current_save:
                    from save import load as save_load
                    try:
                        save_load.update_save(state.current_save, {"character": char["name"]})
                        print(f"Updated save '{state.current_save}' with character {char['name']}")
                    except Exception as e:
                        print("Failed updating save:", e)
                # After choosing character, go to tutorial
                state.mode = "TUTORIAL"
