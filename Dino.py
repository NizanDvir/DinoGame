import pygame

DINOHEIGHT = 40
DINOWIDTH = 20
DINOCOLOR = "Black"

class Dino:
    def __init__(self, surfaceHeight):
        self.x = 60
        self.y = 0
        self.yvelocity = 0
        self.height = DINOHEIGHT
        self.width = DINOWIDTH
        self.color = DINOCOLOR
        self.surfaceHeight = surfaceHeight
    
    def jump(self):
        #only allow jump if dino is on the ground (y==0)
        if self.y == 0:
            self.yvelocity = 300
    def update(self, deltaTime):
        self.y += self.yvelocity * deltaTime
        self.yvelocity += -500 * deltaTime #gravity
        if self.y < 0:
            self.y = 0
            self.yvelocity = 0

    def draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, self.color, [self.x, self.surfaceHeight-self.y-self.height, self.width, self.height])