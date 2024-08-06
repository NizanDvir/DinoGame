import pygame
from Dino import Dino
import random
from Obstacle import Obstacle

pygame.init()

size = width, height = 640, 480
gameDisplay = pygame.display.set_mode(size) # Create the window
# xPos = 0
# yPos = 0
GROUND_HEIGHT = height-200

dinosaur = Dino(GROUND_HEIGHT)

lastFrame = pygame.time.get_ticks() #get ticks returns current time in milliseconds

MINGAP = 200
VELOCITY = 300
MAXGAP = 600
Obstacles = []
num_of_obstacles = 4
lastObstacle = width
SCORE = 0
obstacleSize = 50
for i in range(4):
    lastObstacle += MINGAP+(MAXGAP-MINGAP)*random.random()
    Obstacles.append(Obstacle(lastObstacle, obstacleSize, GROUND_HEIGHT))
    

#game loop
while True:
    t = pygame.time.get_ticks() #Get current time
    deltaTime = (t-lastFrame)/1000.0 #Find difference in time and then convert it to seconds
    lastFrame = t #set lastFrame as the current time for next frame.
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: #If that key is space
                dinosaur.jump() #Make dinosaur jump
            if event.key == pygame.K_DOWN:
                dinosaur.duck()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                dinosaur.unduck()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    gameDisplay.fill("White")

    dinosaur.update(deltaTime)
    dinosaur.draw(gameDisplay)

    for obs in Obstacles:
        obs.update(deltaTime, VELOCITY)
        obs.draw(gameDisplay)
        if obs.checkOver():
            Obstacles.remove(obs)
            lastObstacle += MINGAP+(MAXGAP-MINGAP)*random.random()
            Obstacles.append(Obstacle(lastObstacle, obstacleSize, GROUND_HEIGHT))
            SCORE += 1
    
    lastObstacle -= VELOCITY*deltaTime


    pygame.draw.rect(gameDisplay, "black", [0,GROUND_HEIGHT,width,height-GROUND_HEIGHT])
    # pygame.draw.rect(gameDisplay, "black", [xPos,yPos,40,50]) #make xPos the value of pygame 
    # xPos += 1 #increment by 1
    # yPos += 1 #increment by 1
    pygame.display.update() # Update the window
