"""The following program is a take on snake in python (no pun intended)
- pygame from pip library
Author: Eric Strong
Date: 04/09/17

"""


import sys
import pygame
import random
import time

#setting up game
value = pygame.init()
if value[1] > 0:
    print 'errors occured in initialization. {0}'.format(value[1])
    sys.exit()

else:
    print 'Game successfully initialized! '


#SCREEN DESIGN
playSurface = pygame.display.set_mode((720,460)) #size of pane for game

# colors for game RGB values
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
black = pygame.Color(0,0,0) #snake color
white = pygame.Color(255,255,255)
yellow = pygame.Color(255,255,0)
brown = pygame.Color(165,42,42)

#Game Variables
fpsController = pygame.time.Clock() #timer for game
snakePos = [100,5] #x and y position of the snake. NOTE: cannot be greater than the set_mode size
snakeBody = [[100,50],[90,50],[80,50]]

#food locations - at random
foodPos = [random.randrange(1,72)*10,random.randrange(1,42)*10] #x and y coordinates at random
food_spawn = True # boolean to indicate if the food has been eaten

#direction function of game
direction = 'RIGHT'
changeTo = direction

def gameOver():
    #displays game over
    myFont = pygame.font.SysFont('monaco',72)
    GOsurf = myFont.render('Game Over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360,15)
    playSurface.blit(GOsurf,GOrect)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()
    sys.exit()


#events for the game























