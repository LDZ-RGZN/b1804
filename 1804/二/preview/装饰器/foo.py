def foo():
    print ('foo')
foo = lambda x: print(x + 1)
foo (2)
#执行下面的lambda表达式,而不再是原来的foo函数
#因为foo这个名字被重新指向了另外一个匿名函数

