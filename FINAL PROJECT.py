

import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (113, 70, 255)
GREEN = (120, 213, 132)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
PINK = (255, 138, 201)
BROWN = (108, 44, 1)
ORANGE = (253, 113, 6)
SKY_BLUE = (186, 237, 255)
#skin colours
SKIN1_RED = (255, 204, 153)
SKIN1_YELLOW = (255, 255, 153)
SKIN2 = (255, 212, 124)
SKIN3 = (255, 187, 118)
SKIN4 = (226, 166, 106)
SKIN5 = (153, 76, 0)
SKIN6 = (102, 51, 0)
SKIN7 = (51, 25, 0)

SKIN_COLOURS = [SKIN1_RED, SKIN1_YELLOW, SKIN2, SKIN3, SKIN4, SKIN5, SKIN6, SKIN7]
HAIR_COLOURS = [BLACK, YELLOW, BROWN, ORANGE]

pygame.init()

# Set the width and height of the screen [width, height]
size = (1000, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Coders!!")
    

#A class for the coders!!
class coders():
    def __init__(self, skin_col, interest, hair_type, hair_col, xpos):
        self.skin_col = skin_col
        self.interest = interest
        self.hair_col = hair_col
        self.hair_type = hair_type
        self.xpos = xpos
        self.pants = skin_col

    def draw(self, pos):
        self.pos = pos
        #hair ponytails
        pygame.draw.circle(screen, self.hair_col, (self.xpos - 3, 440), 33)
        pygame.draw.rect(screen, self.hair_col, (self.xpos - 36, 440, 66, 55))
        if self.hair_type == 2:
            pygame.draw.circle(screen, self.hair_col, (self.xpos - 13, 410), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 2, 410), 10)

            pygame.draw.circle(screen, self.hair_col, (self.xpos - 23, 418), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 15, 418), 10)

            
            pygame.draw.circle(screen, self.hair_col, (self.xpos - 33, 428), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 25, 428), 10)

            pygame.draw.circle(screen, self.hair_col, (self.xpos - 13, 410), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 2, 410), 10)

            pygame.draw.circle(screen, self.hair_col, (self.xpos - 23, 418), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 15, 418), 10)

            pygame.draw.circle(screen, self.hair_col, (self.xpos - 36, 440), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos - 36, 455), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos - 36, 470), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos - 36, 485), 10)

            pygame.draw.circle(screen, self.hair_col, (self.xpos + 30, 440), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 30, 455), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 30, 470), 10)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 30, 485), 10)

            pygame.draw.circle(screen, self.hair_col, (self.xpos - 23, 490), 9)
            pygame.draw.circle(screen, self.hair_col, (self.xpos - 14, 490), 9)
            pygame.draw.circle(screen, self.hair_col, (self.xpos - 5, 490), 9)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 4, 490), 9)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 14, 490), 9)
            pygame.draw.circle(screen, self.hair_col, (self.xpos + 23, 490), 9)
        #face
        pygame.draw.circle(screen, self.skin_col, (self.xpos, 450), 30)
        #eyes
        pygame.draw.circle(screen, BLACK, (self.xpos , 440), 5)
        pygame.draw.circle(screen, BLACK, (self.xpos + 15, 440), 4)
        #hair bangs
        pygame.draw.rect(screen, self.hair_col, (self.xpos - 20, 420, 40, 10))    
        #smile
        #pygame.draw.line(screen, RED, (self.xpos + 1, 453), (self.xpos + 16, 453), 3)
        #pygame.draw.circle(screen, RED, (self.xpos + 11, 458), 6)
        #pygame.draw.circle(screen, RED, (self.xpos + 5, 457), 3)
        pygame.draw.arc(screen, RED, (self.xpos, 440, 20, 20), 180/180 * math.pi, 360/180 * math.pi, 1 )


        if self.interest == 1:
            #dress
            pygame.draw.rect(screen, PINK, (self.xpos - 5, 480, 10, 41))
            pygame.draw.polygon(screen, PINK, [(self.xpos - 5, 500), (self.xpos - 5, 520), (self.xpos - 15, 520), (self.xpos - 5, 500)])
            pygame.draw.polygon(screen, PINK, [(self.xpos + 5, 500), (self.xpos + 5, 520), (self.xpos + 15, 520), (self.xpos + 5, 500)])
        elif self.interest == 2:
            pygame.draw.rect(screen, PURPLE, (self.xpos - 8, 480, 16, 30))
            pygame.draw.rect(screen, BLUE, (self.xpos - 8, 510, 16, 10))
            self.pants = BLUE
        elif self.interest == 3:
            pygame.draw.rect(screen, BLACK, (self.xpos - 8, 480, 16, 20))
            pygame.draw.rect(screen, self.skin_col, (self.xpos - 8, 500, 16, 10))
            pygame.draw.rect(screen, BLACK, (self.xpos - 8, 510, 16, 10))
            self.pants = BLACK
        
        if self.pos == 1:
            #legs
            pygame.draw.line(screen, self.pants, (self.xpos - 6, 520), (self.xpos - 6, 550), 5)
            pygame.draw.line(screen, self.pants, (self.xpos + 6, 520), (self.xpos + 2, 550), 5)
            #arms
            pygame.draw.line(screen, self.skin_col, (self.xpos - 7, 478), (self.xpos - 20, 505), 5)
            pygame.draw.line(screen, self.skin_col, (self.xpos + 7, 478), (self.xpos + 10, 505), 5)
        elif self.pos == 2:
            #legs
            pygame.draw.line(screen, self.pants, (self.xpos - 6, 520), (self.xpos - 10, 550), 5)
            pygame.draw.line(screen, self.pants, (self.xpos + 6, 520), (self.xpos + 6, 550), 5)
            #arms
            pygame.draw.line(screen, self.skin_col, (self.xpos - 7, 478), (self.xpos - 10, 505), 5)
            pygame.draw.line(screen, self.skin_col, (self.xpos + 7, 478), (self.xpos + 20, 505), 5)
            
        
        

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#starter girl
skin = random.choice(SKIN_COLOURS)
ha = random.choice(HAIR_COLOURS)
ht = random.randint(1, 2)
inte = random.randint(1, 3)
girl = coders(skin, inte, ht, ha, 500)

#girl coders
girl_coders = [girl]

#variables
walking = 1
walkingcount = 1
earnedscore = False
score = 0


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
    screen.fill(SKY_BLUE)

    # --- Drawing code should go here

    if earnedscore:
        score += 1
        earnedscore = False
        sk = random.choice(SKIN_COLOURS)
        ha2 = random.choice(HAIR_COLOURS)
        ht2 = random.randint(1, 2)
        inte2 = random.randint(1, 3)
        xx = random.randint(100, 450)
        girl_coders.append(coders(sk, inte2, ht2, ha2, xx))
    
    for i in range(len(girl_coders)):
        girl_coders[i].draw(walking)

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