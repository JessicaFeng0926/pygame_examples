import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))


while True:

    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,255,0),(350,100,100,100),border_radius=20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()