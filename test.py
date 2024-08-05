import pygame
from Dino import Dino #import the class Dinosaur from the file ’dinosaur’

pygame.init() #this ‘starts up’ pygame

#initialize game
size = width,height = 640, 480#creates tuple called size with width 400  and height 230
gameDisplay= pygame.display.set_mode(size) #creates screen
xPos = 0
yPos = 0
GROUND_HEIGHT = height-100

# create Dinosaur
dinosaur = Dino(GROUND_HEIGHT)

#create lastframe variable
lastFrame = pygame.time.get_ticks() #get ticks returns current time in milliseconds

#define game colours
white = 255,255,255
black = 0,0,0

while True: #gameLoop it draws the frames of the game
    t = pygame.time.get_ticks() #Get current time
    deltaTime = (t-lastFrame)/1000.0 #Find difference in time and then convert it to seconds
    lastFrame = t #set lastFrame as the current time for next frame.

    for event in pygame.event.get(): #Check for events
        if event.type == pygame.QUIT:
            pygame.quit() #quits
            quit()
        if event.type == pygame.KEYDOWN: #If user uses the keyboard
            if event.key == pygame.K_SPACE: #If that key is space
                dinosaur.jump() #Make dinosaur jump


    gameDisplay.fill(black)

    dinosaur.update(deltaTime)
    dinosaur.draw(gameDisplay)

    pygame.draw.rect(gameDisplay,white, [0,GROUND_HEIGHT, width, height-GROUND_HEIGHT])
    pygame.display.update() #updates the screen
