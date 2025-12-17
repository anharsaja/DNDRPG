import cv2
from config.settings import WIDTH, HEIGHT

def load_background(path):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Background not found: {path}")

    img = cv2.resize(img, (WIDTH, HEIGHT))
    return img
