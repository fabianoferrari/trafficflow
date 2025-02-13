import pygame, math
pygame.init()

window = pygame.display.set_mode((600,600))
pygame.display.set_caption("car game")

image_url = 'https://raw.githubusercontent.com/fabianoferrari/trafficflow/refs/heads/main/figures/carros/Car64.png'
save_as = 'Car64.png'

import requests 
from PIL import Image 
from io import BytesIO 
 
response = requests.get(image_url)
 
img = pygame.image.load(BytesIO(response.content))


class Car:
    def __init__(self, x, y, height, width):
        self.x = x - width / 2
        self.y = y - height / 2
        self.height = height
        self.width = width        
        self.rect = pygame.Rect(x, y, height, width)
        self.surface = pygame.Surface((height, width)) # 1
        self.surface.blit(img, (0, 0))
        self.vx = 0
        self.vy = 0 # 2
        self.angle = 0

    def draw(self): # 3
        self.rect.topleft = (int(self.x), int(self.y))
        rotated = pygame.transform.rotate(self.surface, self.angle)
        surface_rect = self.surface.get_rect(topleft = self.rect.topleft)
        new_rect = rotated.get_rect(center = surface_rect.center)
        window.blit(rotated, new_rect.topleft)


car1 = Car(300, 300, 73, 73) # 4
clock = pygame.time.Clock()

runninggame = True
while runninggame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runninggame = False
    
    pressed = pygame.key.get_pressed()
    
    car1.vx = 0.0 # 5
    car1.vy = 0.0
    
    if pressed[pygame.K_UP]: car1.vy += 0.5 # 6
    if pressed[pygame.K_DOWN]: car1.vy -= 0.5 # 6

    if pressed[pygame.K_LEFT]: car1.vx -= 0.5 # 7
    if pressed[pygame.K_RIGHT]: car1.vx += 0.5 # 7
    
    car1.x += car1.vx
    car1.y += car1.vy
    
    window.fill((0, 0, 0)) # 9
    car1.draw()
    pygame.display.flip()
    clock.tick(60) # 10

pygame.quit()
