def test1():
    print ('---in test1 func---')
test1() #调用函数
ret = test1 #引用函数
print ('test1 id = %s'%id(test1))
print ('ret id = %s'%id(ret))
ret()  #通过引用调用函数
