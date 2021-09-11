import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)

rect = pygame.Rect(300,200,200,100)

while True:
    screen.fill(white)
    pygame.draw.rect(screen,red+green,rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()