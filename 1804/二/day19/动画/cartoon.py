#-*- coding=utf-8 -*-
import time
import pygame

def main():

    #___________
    o = pygame.Rect((180-100)/2-50,80, 50,50)
    t = pygame.Rect((180-100)/2-50,80, 50,50)
    h = pygame.Rect((200-100)/2-50,40, 50,50)
    i = pygame.Rect((510-100)/2-50,20, 50,50)
    #____________

    screen = pygame.display.set_mode((1000,700),0,32)
    background = pygame.image.load('./images/8b318a068702e3ac0f4985cab854e60b.jpg')
    one = pygame.image.load('./bxjg/one.jpg')
    two = pygame.image.load('./bxjg/two.jpg')
    three = pygame.image.load('./bxjg/three.jpg')
    shi = pygame.image.load('./bxjg/shi.jpg')
    clock = pygame.time.Clock()
    a = 0
    while True:
        screen.blit(background,(0,0))
        screen.blit(shi,i)
        screen.blit(one,o)
        screen.blit(two,t)
        screen.blit(three,h)
        h.y -= 2

        #移动
        print (a)
        if a > 5.0:
            print ('b')
            t.y -= 2
            if a > 10.0:
                o.y -= 2
                if a > 15.0:
                    i.y -= 2
        a += 0.02
        pygame.display.update()
        clock.tick(60)
        #游戏退出程序
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ('退出游戏')
                pygame.quit()
                exit()
if __name__ == '__main__':
    main()

