try:
    print ('都是错误')
    open ('1.txt','rb')
    print (name)
    print ('%d'%'error')
    print (True)
except Exception as a:
    print ('程序出现问题%s'%a)
else:
    print ('程序没有任何问题')
finally:
    print ('没错误了')



