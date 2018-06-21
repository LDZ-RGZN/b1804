#-*- coding=utf-8 -*-
import pygame

def main():
    #创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)   #不明白0是什么意思

    #把本地文件夹的图片,获取到代码中
    background = pygame.image.load('./images/background.png')  #image是文件夹名称
    hero = pygame.image.load('./images/hero1.png')

    #定义好的位置,和尺寸
    rect = pygame.Rect((400-100)/2,350, 100,124)
    clock = pygame.time.Clock() #获得游戏时钟  控制器

    while True:
        #把图片加载到游戏窗口上
        #图片会根据显示顺序而显示
        screen.blit(background,(0,0))
        screen.blit(hero,rect)  #设置飞机的位置 and 大小

        #移动
        rect.y += 1
        rect.x += 1
        if rect.x > 400:
            rect.x = 0
            rect.y = 0

        #游戏事件的监听
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ('退出游戏')
                pygame.quit()
                exit() #退出程序

        #刷新显示
        pygame.display.update()
        clock.tick(60)  #让游戏时钟,1/60秒运行一次

if __name__ == '__main__':
    main()







