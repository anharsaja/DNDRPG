import numpy as np

WIDTH, HEIGHT = 1000, 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (70, 70, 70)
GREEN = (0, 255, 0)
YELLOW = (0, 255, 255)
RED = (0, 0, 255)

def create_canvas():
    return np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
