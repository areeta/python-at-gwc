"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
light_blue = (176,224,230)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


# Your SnowFlake class
class snowflake():

	def __init__(self, radius, position):  #init creates snowflakes
		self.position = position # the position is the list of xy = current position of snowflake 
		self.radius = radius
		
		
	def draw(self):
		pygame.draw.circle(screen, WHITE, self.position, 3)
		
	def fall(self, speed):
		self.speed = speed
		self.position[1] += speed #self.postion(y) + speed (3)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Speed
speed = 3

# Snow List
snow_list = []

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(light_blue)
 
    # --- Drawing code should go here
    # Begin Snow
    x_random = random.randint(0, 700)
    
    snow_list.append(snowflake(10, [x_random,0])) #computer knows youre making snowflake object 
    for flake in snow_list:
    	flake.draw()
    	flake.fall(speed)

    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
