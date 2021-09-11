import sys,os,string
import pygame


class InputBox:
    def __init__(self,surf,left,top,width,height,font):
        self.surf = surf
        self.font = font
        self.rect = pygame.Rect(left,top,width,height)
        self.list = []
        self.active = False
        # 光标
        self.cursor = True
        # 光标闪烁计数器
        self.count = 0
        self.delete = False

    def draw(self):
        # 画框
        pygame.draw.rect(self.surf,(0,0,0),self.rect,1)
        # 投放文字
        text_pic = self.font.render(''.join(self.list),True,(0,0,0))
        self.surf.blit(text_pic,(self.rect.x+5,self.rect.y+10))
        # 光标计数器更新
        self.count += 1
        if self.count == 20:
            self.count = 0 
            self.cursor = not self.cursor
        # 绘制光标
        if self.active and self.cursor:
            text_pic_rect = text_pic.get_rect()
            x = self.rect.x+5+text_pic_rect.width
            pygame.draw.line(self.surf,(0,0,0),\
                (x,self.rect.y+5),(x,self.rect.y+self.rect.height-5),1)
        
        # 删除文字
        if self.delete and self.list:
            self.list.pop()

    def get_text(self,event):
        # 聚焦
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        # 获取用户输入的文字或者把删除状态激活
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.delete = True
                elif    event.unicode in string.ascii_letters or \
                    event.unicode in '0123456789_':
                    self.list.append(event.unicode)
        # 停止删除
        elif event.type == pygame.KEYUP:
            if self.active and event.key == pygame.K_BACKSPACE:
                self.delete = False    

    @property
    def text(self):
        return ''.join(self.list)


        



if __name__ == '__main__':
    # 切换工作目录
    path = os.path.dirname(__file__)
    os.chdir(path)
    # pygame基本设置
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,30)
    
    # 创建两张文字图片
    img1 = font.render('userID',True,(0,0,0))
    img2 = font.render('password',True,(0,0,0))

    # 创建两个文本框
    account = InputBox(screen,270,100,300,40,font)
    password = InputBox(screen,270,200,300,40,font)
    
    
    while True:
        clock.tick(30)
        screen.fill((255,255,255))
        screen.blit(img1,(150,110))
        screen.blit(img2,(150,210))
        account.draw()
        password.draw()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                account.get_text(event)
                password.get_text(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(account.text,password.text)

        pygame.display.update()




