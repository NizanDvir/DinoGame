import pygame

color = 0,255,0
class Obstacle:
    def __init__(self, x, size, GroundHeight):
        self.x = x
        self.size = size
        self.GroundHeight = GroundHeight
    def draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, color, [self.x, self.GroundHeight-self.size, 50, self.size])
    def update(self, deltaTime, velocity):
        self.x -= velocity*deltaTime
    def checkOver(self):
        if self.x<0:
            return True
        else:
            return False