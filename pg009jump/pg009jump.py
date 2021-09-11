import pygame
import sys,os

path = os.path.dirname(__file__)
os.chdir(path)
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
man = pygame.image.load('跑.png').convert_alpha()
man = pygame.transform.smoothscale(man,(100,100))



y = 320
diff = 30
jumping = False
while True:
    clock.tick(30)
    screen.fill((255,255,255))
    screen.blit(man,(100,y))
    if jumping:
        y -= diff
        diff -= 2
        if y == 320:
            jumping = False 
            diff = 30
    pygame.draw.line(screen,(0,0,0),(0,400),(800,400),1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                jumping = True
               

    pygame.display.update()