import cv2
from config.settings import WIDTH, HEIGHT, GRAY, WHITE, GREEN

BUTTON_W = int(WIDTH * 0.3)
BUTTON_H = 70
SPACING = 30

menu_buttons = ["New Adventure", "Load Game", "Exit"]
menu_buttons_rect = []

start_y = HEIGHT // 2 - 100
start_x = (WIDTH - BUTTON_W) // 2

for i, label in enumerate(menu_buttons):
    y = start_y + i * (BUTTON_H + SPACING)
    menu_buttons_rect.append((start_x, y, BUTTON_W, BUTTON_H, label))


def draw_title(canvas, text):
    size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.4, 3)[0]
    x = (WIDTH - size[0]) // 2
    cv2.putText(canvas, text, (x, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.4, GREEN, 3)


def draw_menu(canvas):
    for x, y, w, h, label in menu_buttons_rect:
        cv2.rectangle(canvas, (x, y), (x + w, y + h), GRAY, -1)
        cv2.rectangle(canvas, (x, y), (x + w, y + h), WHITE, 2)

        t = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
        tx = x + (w - t[0]) // 2
        ty = y + (h + t[1]) // 2
        cv2.putText(canvas, label, (tx, ty), cv2.FONT_HERSHEY_SIMPLEX, 0.8, WHITE, 2)
