"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Define some colors
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


pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500 # all caps variable means no change

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE
import random

color_list = [WHITE, RED, BLUE, BLACK, GREY, HONEYDEW, CYAN, CHARTREUSE, TAN]
color1 = random.choice(color_list)
x = 350
y = 250
apples1 = random.randint(-10,10)
apples2 = random.randint(-10,10)

dx = apples1
dy = apples2

size1 = random.randint(20, 80)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    for event in pygame.event.get(): #returns list of events in game 
        if event.type == pygame.QUIT:
        	done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
        	mouse_pos = pygame.mouse.get_pos()
        	x, y = mouse_pos
    x += dx #updates x coordinates to glide
    y += dy
    if y<0 or y>SCREEN_HEIGHT - 40:
    	dy *= -1
    if x<0 or x>SCREEN_WIDTH - 40:
    	dx *= -1
    color1 = random.choice(color_list)
    
    



    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)
    pygame.draw.circle(screen, color1, (x,y), size1, 0)


    # --- Drawing code should go here



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
