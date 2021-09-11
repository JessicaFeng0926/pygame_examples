import sys,os
import pygame

path = os.path.dirname(__file__)
os.chdir(path)

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
centaur = pygame.image.load('人马.png').convert_alpha()
centaur = pygame.transform.smoothscale(centaur,(200,200))
# mask 遮罩 
c_mask = pygame.mask.from_surface(centaur)
c_rect = centaur.get_rect()
c_rect.x,c_rect.y = 0,200
um = pygame.image.load('um.png').convert_alpha()
um = pygame.transform.smoothscale(um,(130,200))
u_mask = pygame.mask.from_surface(um)
u_rect = um.get_rect()
u_rect.x,u_rect.y = 650,230
font = pygame.font.Font(None,40)
img = font.render('KO!!!',True,'red')

while True:
    clock.tick(30)
    screen.fill('white')
    screen.blit(centaur,(c_rect.x,c_rect.y))
    screen.blit(um,(u_rect.x,u_rect.y))
    # 偏移量，元素，x坐标的差，y坐标的差
    if c_mask.overlap(u_mask,(u_rect.x-c_rect.x,u_rect.y-c_rect.y)):
        screen.blit(img,(300,500))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    c_rect.x += 1
    u_rect.x -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
