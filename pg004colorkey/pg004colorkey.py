import os,sys
import pygame

path = os.path.dirname(__file__)
os.chdir(path)

pygame.init()

screen = pygame.display.set_mode((800,600))

img = pygame.image.load('柴犬.jpg').convert_alpha()
img = pygame.transform.smoothscale(img,(1200//10,1081//10))
surface = pygame.Surface((800,600))
surface.fill((50,50,50))
surface.set_colorkey((255,0,0))
for i in range(3):
    pygame.draw.circle(surface,(255,0,0),(140+i*250,150),30)


while True:
    screen.fill((255,255,255))
    for i in range(3):
        screen.blit(img,(70+i*250,100))
    
    screen.blit(surface,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()