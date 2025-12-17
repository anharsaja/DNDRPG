import cv2

def draw_panel(canvas, x, y, w, h, alpha=0.6):
    overlay = canvas.copy()
    cv2.rectangle(overlay, (x, y), (x + w, y + h), (0, 0, 0), -1)
    cv2.addWeighted(overlay, alpha, canvas, 1 - alpha, 0, canvas)
