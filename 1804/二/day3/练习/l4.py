f1 = open('唐诗2.txt','w+')
f1.write('盈缩之期\n')
f1.write('不但在天\n')
f1.write('养怡之福\n')
f1.write('可得永年\n')
f1.write('幸甚至哉\n')
f1.write('歌以咏志\n')
#单行读取_________________________________
f1.seek(0,0)
a = 0
while a < 6:
    con =  f1.readline()
    x = con[:len(con)-1]
    print (x )
    position =  f1.tell()
    print ('当前的游标位置是%d'%position)
    a += 1
#重复读取_________________________________
print ('重复读取')
f1.seek(0,0)
#让它重复读取3次
u = 1
while u <= 3:
    con1 = f1.read(5)
    con2 = con1[:len(con1)-1]
    print ('*'*30)
    print ('第%d次读取'%u)
    print (con2)
    f1.seek(0,0)
    u += 1
#遍历循环_________________________________
print ('-'*30)
con3 = f1.read()
f1.seek(0,0)
z = 0
for i in con3:
    con4 = f1.read(1)
    ps4 = f1.tell()
    if con4 == '\n':
        print ('读到了换行标志,当前的游标位置是%d'%ps4)
        print ('*'*30)
    elif con4 != '\n':
        print ('当前读的字是%s,游标位置是%d'%(i,ps4))
    if con4 != '\n':
        z += 1
print ('一共是%d个字'%z)
