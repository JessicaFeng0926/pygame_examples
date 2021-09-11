import sys,os
import pygame


path = os.path.dirname(__file__)
os.chdir(path)

pygame.init()
screen = pygame.display.set_mode((800,600))

pygame.mixer.music.load('滴滴滴滴.mp3')
# 0.0-1.0
pygame.mixer.music.set_volume(0.2)
play_btn = pygame.image.load('播放.png').convert_alpha()
play_btn = pygame.transform.smoothscale(play_btn,(100,100))
stop_btn = pygame.image.load('停止.png').convert_alpha()
stop_btn = pygame.transform.smoothscale(stop_btn,(100,100))

playing = False
img = play_btn
while True:
    screen.fill((255,255,255))
    screen.blit(img,(350,200))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not playing:
                    pygame.mixer.music.play(start=24)
                    playing = True
                    img = stop_btn
                else:
                    pygame.mixer.music.stop()
                    playing = False
                    img = play_btn

    pygame.display.update()

    

