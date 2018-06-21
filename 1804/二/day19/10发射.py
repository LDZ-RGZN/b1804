#-*- coding=utf-8 -*-
import pygame
import random
class EnemyPlane(object):
    def __init__(self,img_path,screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.img_path = img_path
        self.plane = pygame.image.load(self.img_path)#飞机图片
        #定义好尺寸
        self.rect = pygame.Rect(self.x,self.y,0,0)
        #列表保存发出的子弹
        self.bullet_list = []
        self.flag = 'right'
    def display(self):
        self.screen.blit(self.plane,self.rect)#飞机图片
        self.move()
        num = random.randint(1,100)
        if num == 10:
            self.fire()
        for i in self.bullet_list:
            if i.judge() == True:
                self.bullet_list.remove(i)
            i.display()#子弹的对象,display()
            i.move()
    def move(self):
        if self.flag == 'right':
            self.rect.x += 2
        else:
            self.rect.x -= 2
        if self.rect.x > 330 - self.rect.width:
            self.flag = 'left'
        elif self.rect.x <= 0:
            self.flag = 'right'
    def fire(self):
        self.bullet_list.append(EnemyBullet('./images/bullet1.png',self.screen,self.rect.x,self.rect.y))

class HeroPlane(object):
    def __init__(self,img_path,screen):
        self.screen = screen
        self.x = (400-100)/2
        self.y = 350
        self.w = 10
        self.h = 12
        self.img_path = img_path
        self.hero_plane = pygame.image.load(self.img_path)#飞机图片
        #定义好尺寸
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        #列表保存发出的子弹
        self.bullet_list = []
    def display(self):
        self.screen.blit(self.hero_plane,self.rect)#飞机图片
        #显示子弹
        for i in self.bullet_list:
            if i.judge() == True:
                self.bullet_list.remove(i)
            i.display()#子弹的对象,display()
            i.move()
    def fire(self):
        self.bullet_list.append(Bullet('./images/bullet.png',self.screen,self.rect.x,self.rect.y))

class Bullet(object):
    '''这是 子弹的抽象类'''
    def __init__(self,img_path,screen,x,y):
        self.screen = screen
        self.x = x + 40
        self.y = y + 30
        self.img_path = img_path
        self.bullet = pygame.image.load(self.img_path)#子弹图片
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y)) #设置子弹
    def move(self):
        self.y -= 2
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

#子弹类
class EnemyBullet(object):
    '''这是 子弹的抽象类'''
    def __init__(self,img_path,screen,x,y):
        self.screen = screen
        self.x = x + 40
        self.y = y + 30
        self.img_path = img_path
        self.bullet = pygame.image.load(self.img_path)#子弹图片
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y)) #设置子弹
    def move(self):
        self.y += 4
    def judge(self):
        if self.y > 500:
            return True
        else:
            return False


def key_control(hero,move_step):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print ('退出游戏')
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hero.fire()
            elif event.key == pygame.K_q:
                for i in range(1,50):
                    hero.fire()
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        hero.rect.x += move_step
    elif keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        hero.rect.x -= move_step
    elif keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        hero.rect.y -= move_step
    elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        hero.rect.y += move_step
    elif keys_pressed[pygame.K_r]:
        hero.fire()




def main():
    #创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)   #不明白0是什么意思

    #把本地文件夹的图片,获取到代码中
    background = pygame.image.load('./images/background.png')  #image是文件夹名称
    hero = HeroPlane('./images/hero1.png',screen)

    enemy = EnemyPlane('./images/enemy1.png',screen)
    #定义好的位置,和尺寸
    clock = pygame.time.Clock() #获得游戏时钟  控制器

    move_step = 10
    while True:

        #把图片加载到游戏窗口上
        #图片会根据显示顺序而显示
        screen.blit(background,(0,0 ))
        hero.display()  #设置飞机的位置 and 大小
        enemy.display()
        key_control(hero,move_step)

        if hero.rect.y <= 0 :
            hero.rect.y = 0
        elif hero.rect.y >= 386:
            hero.rect.y = 386
        if hero.rect.x <= 0:
            hero.rect.x = 0
        elif hero.rect.x >= 300:
            hero.rect.x = 300


        #刷新显示
        pygame.display.update()
        clock.tick(60)  #让游戏时钟,1/60秒运行一次

if __name__ == '__main__':
    main()







