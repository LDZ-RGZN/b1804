f = open ('定位.txt','w')
f.write('锄禾日当午\n')
f.write('汗滴禾下土\n')
f.write('谁知盘中餐\n')
f.write('粒粒皆辛苦\n')
f.close
#___________________________________
f = open ('定位.txt','r')
a = 1
while a <= 4:
    content = f.readline()
    print ('读取的第%d行内容是:%s'%(a,content))
    position = f.tell()
    print ('当前的游标位置是%d'%position)
    a += 1
#____________________________________
f = open ('定位.txt','rb+')
content = f.read(5)
print ('的一次读取前5个内容%s:'%content)
f.seek(-5,1)
content = f.read(5)
print ('的二次读取前5个内容%s:'%content)
f.close()
#____________________________________
print ('*'*50)
print ('循环遍历')





f = open ('定位.txt','r')
content = f.readlines()
for i in content:
    print (i)











































