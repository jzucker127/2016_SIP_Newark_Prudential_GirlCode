
import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
PINK = (255, 138, 201)
#skin colours
SKIN1_RED = (255, 204, 153)
SKIN1_YELLOW = (255, 255, 153)
SKIN2 = (255, 212, 124)
SKIN3 = (255, 187, 118)
SKIN4 = (226, 166, 106)
SKIN5 = (153, 76, 0)
SKIN6 = (102, 51, 0)
SKIN7 = (51, 25, 0)

SKIN_COLOURS = {SKIN1_RED, SKIN1_YELLOW, SKIN2, SKIN3, SKIN4, SKIN5, SKIN6, SKIN7}

pygame.init()

# Set the width and height of the screen [width, height]
size = (1000, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Coders!!")

#A class for the coders!!
class coders():
    def __init__(self, skin_col, interest, hair_col, xpos):
        self.skin_col = skin_col
        self.interest = interest
        self.hair_col = hair_col
        self.xpos = xpos

    def draw(self, pos):
        self.pos = pos
        pygame.draw.circle(screen, self.skin_col, (self.xpos, 450), 30)
        pygame.draw.circle(screen, BLACK, (self.xpos - 10, 440), 5)
        pygame.draw.circle(screen, BLACK, (self.xpos + 10, 440), 5)
        pygame.draw.line(screen, self.hair_col,(self.xpos, 420),(self.xpos, 435), 2)
        pygame.draw.line(screen, self.hair_col,(self.xpos, 420),(self.xpos + 12, 433), 3)
        pygame.draw.line(screen, self.hair_col,(self.xpos, 420),(self.xpos - 12, 433), 3)
        pygame.draw.line(screen, self.hair_col,(self.xpos, 420),(self.xpos + 23, 431), 2)
        pygame.draw.line(screen, self.hair_col,(self.xpos, 420),(self.xpos - 23, 431), 2)
        pygame.draw.arc(screen, RED, (self.xpos - 15, 440, 30, 30), 180/180 * math.pi, 360/180 * math.pi, 3 )
        pygame.draw.line(screen, self.hair_col,(self.xpos - 30, 450),(self.xpos - 30, 480), 2)
        pygame.draw.line(screen, self.hair_col,(self.xpos + 30, 450),(self.xpos + 30, 480), 2)
        pygame.draw.line(screen, self.hair_col,(self.xpos - 30, 450),(self.xpos - 38, 478), 2)
        pygame.draw.line(screen, self.hair_col,(self.xpos + 30, 450),(self.xpos + 38, 478), 2)
        pygame.draw.line(screen, self.hair_col,(self.xpos - 30, 450),(self.xpos - 22, 478), 2)
        pygame.draw.line(screen, self.hair_col,(self.xpos + 30, 450),(self.xpos + 22, 478), 2)

        pygame.draw.line(screen, self.skin_col, (self.xpos - 5, 480), (self.xpos - 20, 500), 5)
        pygame.draw.line(screen, self.skin_col, (self.xpos + 5, 480), (self.xpos + 20, 500), 5)

        if self.interest == 1:
            pygame.draw.rect(screen, PINK, (self.xpos - 5, 480, 10, 41))
            pygame.draw.polygon(screen, PINK, [(self.xpos - 5, 500), (self.xpos - 5, 520), (self.xpos - 15, 520), (self.xpos - 5, 500)])
            pygame.draw.polygon(screen, PINK, [(self.xpos + 5, 500), (self.xpos + 5, 520), (self.xpos + 15, 520), (self.xpos + 5, 500)])
        
        if self.pos == 1:
            pygame.draw.line(screen, self.skin_col, (self.xpos - 6, 520), (self.xpos - 6, 560), 5)
            pygame.draw.line(screen, self.skin_col, (self.xpos + 6, 520), (self.xpos + 10, 550), 5)
        elif self.pos == 2:
            pygame.draw.line(screen, self.skin_col, (self.xpos - 6, 520), (self.xpos - 2, 550), 5)
            pygame.draw.line(screen, self.skin_col, (self.xpos + 6, 520), (self.xpos + 6, 560), 5)
            
        
        

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#our list
girl = coders(SKIN2, 1, BLACK, 500)

#variables
walking = 1
walkingcount = 1


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
    screen.fill(WHITE)

    # --- Drawing code should go here
        
    girl.draw(walking)

    if walkingcount % 10 == 0:
        if walking == 1:
            walking = 2
        elif walking == 2:
            walking = 1


    walkingcount += 1


    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
