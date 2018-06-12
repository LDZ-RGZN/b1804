f1 = open ('唐诗.txt','w')
f1.write('神龟虽寿\n')
f1.write('犹有竟时\n')
f1.write('腾蛇乘雾\n')
f1.write('终为土灰\n')
f1.close()

f2 = open ('唐诗.txt','r')
a = 0
z = ''
while a < 4:
    x = f2.readline()
    y = x[:len(x)-1]
    z += (y + '*_*\n')
    print (y + '*_*')
    a += 1

f3 = open ('唐诗.txt','a')
f3.write('|\n')
f3.write(z)
f2.close
f3.close











