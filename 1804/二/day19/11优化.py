#-*- coding=utf-8 -*-
import pygame
import random
from defo import *
#英雄类_____________________________________________________________
class HeroPlane(BasePlane):
    def __init__(self,img_path,screen):
        BasePlane.__init__(self,img_path,screen,(400-100)/2,350)

    def fire(self):
        self.bullet_list.append(Hero_Bullet('./images/bullet.png',self.screen,self.rect.x,self.rect.y))

#敌人类______________________________________________________
class EnemyPlane(BasePlane):
    def __init__(self,img_path,screen):
        BasePlane.__init__(self,img_path,screen,0,0)
        self.flag = 'right'
        self.ky = False
    def move(self):
        if self.flag == 'right':
            self.rect.x += 2
            if self.ky == True:
                self.rect.y += 10
                self.ky = False
        else:
            self.rect.x -= 2
            if self.ky == True:
                self.rect.y += 1
                self.ky = False
        if self.rect.x > 330 - self.rect.width:
            self.flag = 'left'
            self.ky = True

        elif self.rect.x <= 0:
            self.flag = 'right'
        if self.rect.x == 0:
            self.ky = True
        elif self.rect.x == 320:
            self.ky = True
    def fire(self):
        self.bullet_list.append(Enemy_Bullet('./images/bullet1.png',self.screen,self.rect.x,self.rect.y))
#爆炸类_____________________________________________________________
class Bose_Plane(Plane):
    def __init__(self,img_path,screen):
        Plane.__init__(self,img_path,screen,10,10)
    #def move(self):

    def fire(self):
        self.bulet_list.append(Bose_Bullet('./images/'))

#英雄子弹类_____________________________________________________________
class Hero_Bullet(Bullet):
    def __init__(self,img_path,screen,x,y):
        Bullet.__init__(self,img_path,screen,x,y)
    def move(self):
        self.y -= 4
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

#敌人子弹类_______________________________________________________
class Enemy_Bullet(Bullet):
    '''这是 子弹的抽象类'''
    def __init__(self,img_path,screen,x,y):
        Bullet.__init__(self,img_path,screen,x,y)
    def move(self):
        self.y += 4
    def judge(self):
        if self.y > 500:
            return True
        else:
            return False
#调用函数________________________________________________________
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
        enemy.move()
        enemy.display()
        if random.randint(1,60) == 5:
            enemy.fire()

        key_control(hero,move_step)
        for i in enemy.bullet_list:
            if hero.rect.y+124 >= i.y >= hero.rect.y and hero.rect.x+100 >= i.x >= hero.rect.x:
                hero.bomb()
        for i in hero.bullet_list:
            if enemy.rect.y+89 >= i.y >= enemy.rect.y and enemy.rect.x+69 >= i.x >= enemy.rect.x:
                enemy.Two()

        hero.rect.y = frame(hero.rect.y)
        hero.rect.x = frameo(hero.rect.x)

        #刷新显示
        pygame.display.update()
        clock.tick(60)  #让游戏时钟,1/60秒运行一次

if __name__ == '__main__':
    main()







