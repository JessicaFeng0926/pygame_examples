import pygame
import sys
import os

path = os.path.dirname(__file__)
os.chdir(path)

pygame.init()

screen = pygame.display.set_mode((800,600))
pics = []
for i in range(7):
    pic = pygame.image.load(f'面{i+1}.png').convert_alpha()
    pic = pygame.transform.smoothscale(pic,(200,200))
    pics.append(pic)
pics.append(pics[3])
tree = pygame.image.load('树.png')
tree = pygame.transform.smoothscale(tree,(100,200))

clock = pygame.time.Clock()

y = 500
pnum = 0

while True:
    clock.tick(30)
    screen.fill((255,236,139))
    
    screen.blit(tree,(500,y))
    screen.blit(tree,(100,y+300))
    y -= 2

    screen.blit(pics[pnum//3],(280,200))
    
    pnum += 1
    if pnum > 23:
        pnum = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


