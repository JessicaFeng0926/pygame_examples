import sys,os
import pygame

path = os.path.dirname(__file__)
os.chdir(path)

pygame.init()

screen = pygame.display.set_mode((800,600))

img = pygame.image.load('俺也一样.gif')

surfs = [pygame.Surface((200,151),pygame.SRCALPHA) for _ in range(4)]

white = pygame.Color(255,255,255)

red_colors = [pygame.Color(255,0,0,i*80) for i in range(4)]

for i in range(4):
    surfs[i].fill(red_colors[i])


while True:
    screen.fill(white)
    for row in range(2):
        for col in range(2):
            screen.blit(img,(100+col*400,100+row*200))
            screen.blit(surfs[row*2+col],(100+col*400,100+row*200))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()

