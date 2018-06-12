import os
def dk(name):
    f = open(name,'r+')
    con1 = f.read()
    if len(con1) != 0:
        print (con1)
    elif len(con1) == 0:
        f.write('哈哈哈')
        f.close()
        f = open (name,'r')
        print ('0')
        con3 = f.read()
        print (con3)

    f.close()
name = input('请输入您要查询的文件名')
dk(name)



