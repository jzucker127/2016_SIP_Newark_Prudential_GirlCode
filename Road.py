import pygame
import random
import math
import sys
import time

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
        pygame.draw.polygon (screen, GREEN, ([self.x1, self.y1-100], [self.x3, self.y1-100],[self.x2, self.y1-230]))
        pygame.draw.polygon (screen, GREEN, ([self.x1, self.y1-200], [self.x3, self.y1-200], [self.x2, self.y1-330]))

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
        self.trees.append ( Tree ( 1000, 1100, 1200, 410, 280))
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


pygame.font.init()
font = pygame.font.SysFont("vgafix.fon", 25)
message1 = font.render ("Hey", 1, WHITE)
screen.blit(message1, (570, 340))



keypressedfor = 1
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
    screen.fill(BLACK)
    screen.fill(SKY_BLUE)
    # --- Drawing code should go here
    
    
    if keypressedfor == 1:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 50)
        message1 = font.render ("NAME OF APP", 1, WHITE)
        screen.blit(message1, (350, 250))
    elif keypressedfor == 2:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 25)
        message2 = font.render ("-Women make up half of the total U.S.", 1, WHITE)
        screen.blit (message2, (100, 50))
        message22 = font.render("college-educated workforce but only 29% of", 1, WHITE)
        screen.blit (message22, (100, 100))
        message23 = font.render ("the science and engineering workforce.", 1, WHITE)
        screen.blit (message23, (100, 150))
        message24 = font.render ("-Female scientists and engineers are,", 1, WHITE)
        screen.blit (message24, (100, 200))
        message25 = font.render("concentrated in different occupations than are men", 1, WHITE)
        screen.blit (message25, (100, 250))
        message26 = font.render ("with relatively high shares of women in ", 1, WHITE)
        screen.blit (message26, (100, 300))
        message27 = font.render ("the social sciences (62%) and biological,", 1, WHITE)
        screen.blit (message27, (100,350))
        message28 = font.render ("agricultural and environmental life sciences,",1, WHITE)
        screen.blit (message28, (100, 400))
        message29 = font.render ("(48%) and relatively low shares in engineering", 1, WHITE)
        screen.blit (message29, (100, 450))
        message30 = font.render ("(15%) and computer and mathematical sciences (25%).",1, WHITE)
        screen.blit (message30, (100, 500))
    elif keypressedfor == 3:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 30)
        message31 = font.render ("Explain the goal of the game.", 1, WHITE)
        screen.blit (message31, (100, 75))
    elif keypressedfor == 4:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 30)
        message4 = font.render ("Syntax Errors Are: A character or string ", 1, WHITE)
        screen.blit (message4, (75, 50))
        message42 = font.render("incorrectly placed in a command or instruction ", 1, WHITE)
        screen.blit(message42, (75, 125))
        message43 = font.render("that causes a failure in execution of code", 1, WHITE)
        screen.blit (message43, (75, 200))
    elif keypressedfor == 5:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 30)
        message5 = font.render ("Don't worry though!", 1, WHITE)
        screen.blit (message5, (75, 50))
        message52 = font.render("Every coder experiences syntax errors!", 1, WHITE)
        screen.blit (message52, (75, 125))
        message53 = font.render("Don't be discouraged!!!", 1, WHITE)
        screen.blit (message53, (75, 200))
        message54 = font.render("The only wrong descision is to give up!", 1, WHITE)
        screen.blit (message54, (75, 275))
    elif keypressedfor == 6:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 30)
        message6 = font.render ("INTRODUCTION TO JAVASCRIPT!!!", 1, WHITE)
        screen.blit (message6, (250, 50))
        message62 = font.render ("Here are some examples of syntax errors:", 1, WHITE)
        screen.blit (message62, (50, 125))
        message63 = font.render ("';' are like the '.'s in computer languages like", 1, WHITE)
        screen.blit (message63, (50, 200))
        message64 = font.render ("JavaScript! Think of '{}'s (after functions) as ", 1, WHITE)
        screen.blit (message64, (50, 275))
        message65 = font.render ("paragraphs.  They let the computers know that", 1, WHITE)
        screen.blit (message65, (50, 350))
        message66 = font.render ("these command belong within/to the function!", 1, WHITE)
        screen.blit (message66, (50, 425))
    elif keypressedfor == 7:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 30)
        message7 = font.render ("INTRODUCTION TO JAVASCRIPT!!! PART 2", 1, WHITE)
        screen.blit (message7, (200,50))
        message72 = font.render ("A single line comment is added when a user", 1, WHITE)
        screen.blit (message72, (25, 125))
        message73 = font.render ("inserts '//' before their comments", 1, WHITE)
        screen.blit (message73, (25, 200))
        message74 = font.render ("A multi-line comment begins with, '/*' and ends with,", 1, WHITE)
        screen.blit (message74, (25, 275))
        message75 = font.render ("'*/', after the comment has been finished/completed.", 1, WHITE)
        screen.blit (message75, (25, 350))
        pause_time = 200
    elif keypressedfor == 8:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 25)
        message8 = font.render ("DEBUGGING", 1, WHITE)
        screen.blit (message8, (480, 45))
        message82 = font.render ("-Debugging is a crucial aspect of mastering", 1, WHITE)
        screen.blit (message82, (35, 125))
        message83 = font.render ("computer science/Javascript!", 1, WHITE)
        screen.blit (message83, (35, 200))
        message84 = font.render ("-Everyone makes mistakes!  The important thing", 1, WHITE)
        screen.blit (message84, (35, 275))
        message85 = font.render ("is that you learn from them!!", 1, WHITE)
        screen.blit (message84, (35, 350))
        pause_time = 200
    elif keypressedfor == 9:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 30)
        message9 = font.render ("I", 1, WHITE)
        screen.blit (message9, (500, 300))
        pause_time = 200
    elif keypressedfor == 10:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 35)
        message10 = font.render ("INTRODUCTION TO PYTHON!!!", 1, WHITE)
        screen.blit (message10, (500, 300))
        pause_time = 200
    elif keypressedfor == 11:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 15)
        message11 = font.render ("INTRODUCTION TO PYTHON!!!", 1, WHITE)
        screen.blit (message11, (500, 300))
        pause_time = 200
    elif keypressedfor == 12:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 25)
        message12 = font.render ("BEGIN THE GAME!!", 1, WHITE)
        screen.blit (message12, (379, 50))
        message122 = font.render ("You're now ready to take on the virtual world", 1, WHITE)
        screen.blit (message122, (50, 100))
        message123 = font.render ("and become a hero!  You must show women can do", 1, WHITE)
        screen.blit (message123, (50, 150))
        message124 = font.render ("anything!", 1, WHITE)
        screen.blit (message124, (50, 200))
        pause_time = 200
    elif keypressedfor == 13:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 25)
        message13 = font.render ("DIRECTIONS!!!", 1, WHITE)
        screen.blit (message13, (500, 300))
        pause_time = 200
    elif keypressedfor == 14:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 25)
        message14 = font.render ("INTRODUCTION TO PYTHON!!!", 1, WHITE)
        screen.blit (message14, (500, 300))
        pause_time = 200
    elif keypressedfor == 15:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 30)
        message15 = font.render ("INTRODUCTION TO PYTHON!!!", 1, WHITE)
        screen.blit (message15, (500, 300))
        pause_time = 200
    elif keypressedfor == 16:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 35)
        message16 = font.render ("INTRODUCTION TO PYTHON!!!", 1, WHITE)
        screen.blit (message16, (500, 300))
        pause_time = 200
    elif keypressedfor == 17:
        screen.fill(BLACK)
        pygame.font.init()
        font = pygame.font.SysFont("OCR A Extended", 40)
        message17 = font.render ("INTRODUCTION TO PYTHON!!!", 1, WHITE)
        screen.blit (message17, (500, 300))
        pause_time = 200
        
    if event.type == pygame.KEYDOWN:
        print(keypressedfor)
        if event.key == pygame.K_RIGHT and keypressedfor == 1:
            pause_time = 200
            keypressedfor = 2
        elif event.key == pygame.K_RIGHT and keypressedfor == 2:
            pause_time = 200
            keypressedfor = 3
        elif event.key == pygame.K_RIGHT and keypressedfor == 3:
            pause_time = 200
            keypressedfor = 4
        elif event.key == pygame.K_RIGHT and keypressedfor == 4:
            pause_time = 200
            keypressedfor = 5
        elif event.key == pygame.K_RIGHT and keypressedfor == 5:
            pause_time = 200
            keypressedfor = 6
        elif event.key == pygame.K_RIGHT and keypressedfor == 6:
            pause_time = 200
            keypressedfor = 7
        elif event.key == pygame.K_RIGHT and keypressedfor == 7:
            pause_time = 200
            keypressedfor = 8
        elif event.key == pygame.K_RIGHT and keypressedfor == 8:
            pause_time = 200
            keypressedfor = 9
        elif event.key == pygame.K_RIGHT and keypressedfor == 9:
            pause_time = 200
            keypressedfor = 10
        elif event.key == pygame.K_RIGHT and keypressedfor == 10:
            pause_time = 200
            keypressedfor = 11
        elif event.key == pygame.K_RIGHT and keypressedfor == 11:
            pause_time = 200
            keypressedfor = 12
        elif event.key == pygame.K_RIGHT and keypressedfor == 12:
            pause_time = 200
            keypressedfor = 13
        elif event.key == pygame.K_RIGHT and keypressedfor == 13:
            pause_time = 200
            keypressedfor = 14
        elif event.key == pygame.K_RIGHT and keypressedfor == 14:
            pause_time = 200
            keypressedfor = 15
        elif event.key == pygame.K_RIGHT and keypressedfor == 15:
            pause_time = 200
            keypressedfor = 16
        elif event.key == pygame.K_RIGHT and keypressedfor == 16:
            pause_time = 200
            keypressedfor = 17
        elif event.key == pygame.K_RIGHT and keypressedfor == 17:
            pause_time = 200
            keypressedfor = 18
        elif event.key == pygame.K_RIGHT and keypressedfor == 18:
            pause_time = 200
            keypressedfor = 19 
        pygame.time.delay(300)
            
        


    #Road
    #pygame.draw.rect(screen, BLACK, [0, 450, 1000, 150])
    #pygame.draw.polygon(screen, GREEN, [116, 170], [166, 235], [216, 170])
    
    #Yellow Dashes
    #x_coor = 0
    
    #for i in range(0, 10):
        #pygame.draw.rect(screen, YELLOW, (x_coor, y_coor, 20, 10))
        #x_coor = x_coor + 100
    
    #Trees
    #if exp != 60:
        #exp = exp +1
    #else:
        #tree.add_trees()
        #exp = 0
        
    #tree.draw_trees()
    #tree.move_trees()
    
 
            

    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
