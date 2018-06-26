def foo():
    print ('foo')
foo  #表示是函数
foo()  #表示执行foo函数
#______________________

def foo():
    print ('foo')
foo = lambda x: print(x + 1)
foo(2)
