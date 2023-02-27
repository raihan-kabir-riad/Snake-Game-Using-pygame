import pygame 
import time 

# Initialize pygame
pygame.init()

# set the width and height of the screen (width, height). 
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Snake Game")

# Loop until the user clicks the close button.
done = False 

# Used to manage how fast the screen updates
clock = pygame.time.Clock

# Create a snake
snake_block = 10
snake_speed = 30

# Set the font for the score
font_style = pygame.font.SysFont(None, 50)

# Set the initial position of the snake 
snake_x = 50
snake_y = 50

# Set the initial direction of the snake 
snake_derection = ""

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
        # if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            # x=1
   
        # Update the snake's position 
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                snake_derection = "r"
            elif event.key == pygame.K_LEFT:
                snake_derection = "l"
            elif event.key == pygame.K_UP:
                snake_derection = "u"
            elif event.key == pygame.K_DOWN:
                snake_derection = "d"
                
    # clear the screen
    screen.fill((255, 255, 255))
    if snake_derection == "r":
        snake_x += snake_block
    elif snake_derection == "l":
        snake_x -= snake_block
    elif snake_derection == "u":
        snake_y -= snake_block
    elif snake_derection == "d":
        snake_y += snake_block         
    # drow the snake 
    pygame.draw.rect(screen, (0, 0, 0), [snake_x, snake_y, snake_block, 10])
    
    # Update the screen 
    pygame.display.flip()
    
    # Limit to 60 frames per second 
    pygame.time.Clock().tick(10)
    
# Quit pygame
pygame.quit()