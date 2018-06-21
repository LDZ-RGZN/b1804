#-*- coding=utf-8 -*-
import pygame

def main():
    #创建游戏窗口
    screen = pygame.display.set_mode((400,500),0,32)   #不明白0是什么意思

    #把本地文件夹的图片,获取到代码中
    background = pygame.image.load('./images/background.png')  #image是文件夹名称
    hero = pygame.image.load('./images/hero1.png')

    #把图片加载到游戏窗口上
    #图片会根据显示顺序而显示
    screen.blit(background,(0,0))
    screen.blit(hero,((400-100)/2,350))

    #刷新显示
    pygame.display.update()
    while True:
        pass

if __name__ == '__main__':
    main()
