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

        self.is_ducking = False
        self.normal_height = DINOHEIGHT
        self.duck_height = DINOHEIGHT // 2
        self.duck_gravity = -1500  # Increased gravity while ducking
        self.normal_gravity = -750  # Normal gravity
    
    def jump(self):
        #only allow jump if dino is on the ground (y==0)
        if self.y == 0 and not self.is_ducking:
            self.yvelocity = 400
    def duck(self):
        if not self.is_ducking:
            self.is_ducking = True
            self.height = self.duck_height
            
    def unduck(self):
        if self.is_ducking:
            self.is_ducking = False
            self.height = self.normal_height
        
        
    def update(self, deltaTime):
        self.y += self.yvelocity * deltaTime
        gravity = self.duck_gravity if self.is_ducking else self.normal_gravity
        self.yvelocity += gravity * deltaTime 
        if self.y < 0:
            self.y = 0
            self.yvelocity = 0

    def draw(self, gameDisplay):
        pygame.draw.rect(gameDisplay, self.color, [self.x, self.surfaceHeight-self.y-self.height, self.width, self.height])
    def collides_with(self, obstacle):
        dino_rect = pygame.Rect(self.x, self.surfaceHeight-self.y-self.height, self.width, self.height)
        obstacle_rect = pygame.Rect(obstacle.x, obstacle.GroundHeight - obstacle.size, obstacle.size, obstacle.size)
        return dino_rect.colliderect(obstacle_rect)