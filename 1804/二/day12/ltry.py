user = input ('请输入文件名:')
try :
    f = open (user,'r')
    content = f.read()
    print (content)
    print ('%d'%'error')
except TypeError:
    print ('程序中有错误')
