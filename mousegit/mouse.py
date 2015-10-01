import pygame
import sys                          # Used to recognize exit commands
from pygame.locals import *
import random


def playmouse():
    pygame.init()                       # Initializes pygame. Can't use any pygame commands without this!
    WIDTH = 1200                         # Initialized to avoid use of Magic Numbers
    HEIGHT = 720
    WHITE = (255,255,255)               # Colors in Pygame are "tuples" of RGB values
    BLACK = (0,0,0)                     # Declare these to make code more readable
    RED = (255,0,0)
    radius = 50                         # Radius of circle/graphic
    FPS = 60                            # Framerate = frames per second. Not used because we wait
    score = 0                           # Cumulative score = number of correct whacks
    missedInARow = -1                    # Number of misses in a row
    Go = True

    fpsClock = pygame.time.Clock()      # Initialilze the game clock
    soundObj = pygame.mixer.Sound("mouse1.wav")     # Initialize the sound object
    myFace = pygame.image.load('head.png')          # Initialize a graphic to move around
    bg = pygame.image.load('bg.jpg')
    cheese = pygame.image.load('cheese.png')
    screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)   # Creates window "Surface"
    pygame.display.set_caption('Mouse! by CamGames ver.1.5')
    fontObj = pygame.font.SysFont("Arial", 48)               # The font and point size for text used

    
    while True:
        # Check to see if any events have occurred
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                mouseX = mouse[0]
                mouseY = mouse[1]
                if (locX - radius < mouseX < locX + radius) and \
                   (locY - radius < mouseY < locY + radius):
                    soundObj.play()
                    missedInARow = 0
                    score += 1
                if resetfunc.collidepoint(mouse):
                    playmouse()

        # Check to see if game is over
        if missedInARow >= 3:
            gameOverText = fontObj.render("Eeek! Game Over!",True,BLACK,WHITE) 
            gameOverTextRect = gameOverText.get_rect()
            gameOverTextRect.centerx = WIDTH/2
            gameOverTextRect.centery = HEIGHT/2 
            Go = False
            pygame.display.update()
                
        # Update the game state
        screen.blit(bg,(0,0))
        resetfunc = screen.blit(cheese,(WIDTH/2,0))
        scoreText = fontObj.render("Score: " + str(score),True,BLACK,WHITE) # set up text
        scoreTextRect = scoreText.get_rect()    # get_rect returns a rectangular shape containing
                                                # the surface, with parameters x, y, width, height
                                                # where x,y indicate upper-left corner
        scoreTextRect.centerx = WIDTH / 5   
        scoreTextRect.centery = 30
        screen.blit(scoreText, scoreTextRect)
        
        missedInARowText = fontObj.render("Missed: " + str(missedInARow),True,BLACK,WHITE) 
        missedInARowTextRect = scoreText.get_rect()   
        missedInARowTextRect.centerx = WIDTH * 4 / 5  # 
        missedInARowTextRect.centery = 30
        screen.blit(missedInARowText, missedInARowTextRect)
     
        locX = random.randrange(WIDTH - 2 * radius) + radius
        locY = random.randrange(HEIGHT - 2 * radius) + radius
        
        # pygame.draw.circle(screen, RED, (locX,locY), radius, 0)
        
        if Go == True:
            screen.blit(myFace,(locX - radius,locY - radius))
            missedInARow += 1       # Assume they're going to miss next round! >:)
        if Go == False:
            screen.blit(gameOverText, gameOverTextRect)
            
        
        # Draw the objects to the Surface
        pygame.display.update()                 # Displays the objects on screen
        pygame.time.wait(1000 - score * 10)      # Wait for a one second time period initially, but that time
                                                # decreases as the game goes on!
        fpsClock.tick(FPS)                      # Advance the game clock, although this is small compared with
                                                # the wait statement above
        
playmouse()  
