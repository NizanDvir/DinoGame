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
    
game_over = False
#game loop
while not game_over:
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
        if dinosaur.collides_with(obs):
            game_over = True
    
    lastObstacle -= VELOCITY*deltaTime

    pygame.draw.rect(gameDisplay, "black", [0,GROUND_HEIGHT,width,height-GROUND_HEIGHT])
    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {SCORE}", True, (0, 0, 0))
    gameDisplay.blit(score_text, (10, 10))

    pygame.display.update()
    
# Game over screen
font = pygame.font.Font(None, 72)
game_over_text = font.render("Game Over", True, (255, 0, 0))
gameDisplay.blit(game_over_text, (width//2 - game_over_text.get_width()//2, height//2 - game_over_text.get_height()//2))
pygame.display.update()

# Wait for a moment before quitting
pygame.time.wait(2000)

pygame.quit()
quit()
