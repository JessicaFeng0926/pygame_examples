import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
rect1 = pygame.Rect(0,100,100,50)
rect2 = pygame.Rect(700,100,100,50)

font = pygame.font.Font(None,40)
img = font.render('Bang!',True,(255,0,0))

while True:
    clock.tick(30)
    screen.fill((255,255,255))
    pygame.draw.rect(screen,'red',rect1)
    pygame.draw.rect(screen,'green',rect2)
    rect1.x += 1
    rect2.x -= 1
    if rect1.colliderect(rect2):
        screen.blit(img,(350,200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()

