import sys,os
import pygame

path = os.path.dirname(__file__)
os.chdir(path)

pygame.init()

screen = pygame.display.set_mode((500,403))

img = pygame.image.load('fhcq.jpg')
surface = pygame.Surface((500,403),pygame.SRCALPHA)
pygame.draw.circle(surface,(255,105,180,100),(500//2,403//2),403//2)


while True:
    screen.blit(img,(0,0))
    screen.blit(surface,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()

