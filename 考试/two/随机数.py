#coding=utf-8
import random
pc = random.randint(1,100)
i = 0
while True:
    i += 1
    you = int (input ('输入你猜的数字1~100:'))
    if you > pc :
        print ('数字太大了')
    elif you < pc :
        print ('数字太小了')
    else :
        print ('您猜对了')
        break
print ('一共猜了%d次.'%i)
