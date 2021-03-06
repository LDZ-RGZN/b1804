#-*- coding=utf-8 -*-
import pygame
import random
#英雄类___________________________________________________
class HeroPlane(object):
    def __init__(self,img_path,screen):
        self.screen = screen
        self.x = (400-100)/2
        self.y = 550
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
            i.display()#子弹的对象,display()
            i.move()

    def fire(self):
        self.bullet_list.append(Bullet('./images/bullet.png',self.screen,self.rect.x,self.rect.y))
        self.bullet_list.append(Bullet('./images/bullet.png',self.screen,self.rect.x-40,self.rect.y))
        self.bullet_list.append(Bullet('./images/bullet.png',self.screen,self.rect.x+40,self.rect.y))

#敌人机类______________________________________________________
class Enemy(object):
    def __init__(self,screen):
        self.screen = screen
        self.x = (400-100)/2
        self.y = 50
        #英雄
        self.image = pygame.image.load('./images/enemy0.png')
        #定义英雄的初始位置
        self.rect= pygame.Rect(self.x,self.y,102,126)
        #列表保存发出的子弹
        self.enemy_list = []
        self.enemy_remove = []
        self.direction = 'right' #保持敌机默认方向
    def display(self):
        self.screen.blit(self.image,self.rect) #把敌机添加到屏幕上
        if len(self.enemy_list) > 0:
            for l in self.enemy_list:
                l.display()
                l.move()
                if l.judge():
                    self.enemy_remove.append(l)
            if len(self.enemy_remove) > 0:
                for i in self.enemy_remove:
                    self.enemy_list.remove(i)
                del self.enemy_remove[:]
    def move(self):
        if self.direction == 'right':
            self.rect.x += 5
        elif self.direction == 'left':
            self.rect.x -= 5
        if self.rect.x > 400-self.rect.width:
            self.direction = 'left'
        elif self.rect.x < 0 :
            self.direction = 'right'

    def fire(self):
        self.enemy_list.append(EnemyBullet(self.screen,self.rect.x,self.rect.y))

#英雄子弹类_______________________________________________________
class Bullet(object):
    '''这是 子弹的抽象类'''
    def __init__(self,img_path,screen,x,y):
        self.screen = screen
        self.x = x + 40
        self.y = y - 10
        self.img_path = img_path
        self.bullet = pygame.image.load(self.img_path)#子弹图片
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y)) #设置子弹
    def move(self):
        self.y -= 2
#敌机子弹类_______________________________________________________
class EnemyBullet(object):
    '''敌人子弹抽象类'''
    def __init__(self,screen,x,y):
        self.screen = screen
        self.x = x+25
        self.y = y+25
        #子弹
        self.image = pygame.image.load('./images/bullet1.png')
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y += 4
    def judge(self): #不明白这里建这个方法的意义
        if self.y > 600:
            return True
        else:
            return False

#_____________________________________________________________________


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
    screen = pygame.display.set_mode((400,700),0,32)   #不明白0是什么意思

    #把本地文件夹的图片,获取到代码中
    background = pygame.image.load('./images/background.png')  #image是文件夹名称

    hero = HeroPlane('./images/hero1.png',screen)


    #定义好的位置,和尺寸
    clock = pygame.time.Clock() #获得游戏时钟  控制器

    enemy = Enemy(screen)
    enemy1 = Enemy(screen)

    move_step = 10
    y = 0
    while True:

        ra = random.randint(0,8)
        #把图片加载到游戏窗口上
        #图片会根据显示顺序而显示
        screen.blit(background,(0,0 ))
        hero.display()  #设置飞机的位置 and 大小
        enemy.display()
        enemy1.display()
        enemy.move()
        if y >= 2.0:
            enemy1.move()
        if ra == 1 :
            enemy.fire()
            enemy1.fire()
        if hero.rect.y <= 0 :
            hero.rect.y = 0
        elif hero.rect.y >=590:
            hero.rect.y =590
        if hero.rect.x <= 0:
            hero.rect.x = 0
        elif hero.rect.x >=310:
            hero.rect.x = 310
        y += 0.01

        clock.tick(60)  #让游戏时钟,1/60秒运行一次


        #刷新显示
        key_control(hero,move_step)
        pygame.display.update()

if __name__ == '__main__':
    main()







