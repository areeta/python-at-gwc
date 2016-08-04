import random

apples = random.randint(-10,10)

print(apples)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
HONEYDEW = (240, 255, 240)
CYAN = (0 ,255, 255)
CHARTREUSE = (127, 255, 0)
TAN = (210, 180, 140)

color = [WHITE, BLACK, RED, BLUE, GREY, HONEYDEW, CYAN]
color_length = len(color)
random_color = random.randint(0, color_length -1)

print(random_color)