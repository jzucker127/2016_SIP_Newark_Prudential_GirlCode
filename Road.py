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
SKY_BLUE = (135, 206, 235)

pygame.init()

class Tree():

    def __init__ (self, x1, x2, x3, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2

    #Draws an individual tree
    def draw (self):   
        pygame.draw.polygon (screen, GREEN, ([self.x1, self.y1],[self.x3, self.y1],[self.x2, self.y2] ))
        pygame.draw.polygon (screen, GREEN, ([self.x1, self.y1-130], [self.x3, self.y1-130],[self.x2, self.y1-260]))
        pygame.draw.polygon (screen, GREEN, ([self.x1, self.y1-260], [self.x3, self.y1-260], [self.x2, self.y1-390]))

    #Makes that individual tree move
    def move(self):
        
        self.x1 -= 5
        self.x2 -= 5
        self.x3 -= 5


class Background():
    def __init__ (self):
        #A list of trees is being made here and you will need to add a tree to this list every time you want to draw a new one
        self.trees = []
        self.add_trees()
        
    def add_trees(self):
        self.trees.append ( Tree ( 1000, 1100, 1200, 430, 300))
        #This method will add a tree to your list, you will want to do this to get the moving effect
        #Remember that each new tree begins on the very right and they all look the same
        #remove return None when done writing this method, it's a temporary command
        

    def draw_trees(self):
        for i in self.trees:
            i.draw ()    
        #Look through each tree object in your list (self.trees) and draw it 
        

    def move_trees(self):
        for i in self.trees:
            i.move ()
        #Traverse through each tree object in your list (self.trees) and shift it horizontally (look through the Tree methods)
        
        
# Set the width and height of the screen [width, height]
size = (1000, 600)
screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

y_coor = 525

exp = 0
tree = Background()
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
    #Road
    pygame.draw.rect(screen, BLACK, [0, 450, 1000, 150])
    #pygame.draw.polygon(screen, GREEN, [116, 170], [166, 235], [216, 170])
    
    #Yellow Dashes
    x_coor = 0
    
    for i in range(0, 10):
        pygame.draw.rect(screen, YELLOW, (x_coor, y_coor, 20, 10))
        x_coor = x_coor + 100
    
    #Trees
    if exp != 60:
        exp = exp +1
    else:
        tree.add_trees()
        exp = 0
        
    tree.draw_trees()
    tree.move_trees()
    
 
            

    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
