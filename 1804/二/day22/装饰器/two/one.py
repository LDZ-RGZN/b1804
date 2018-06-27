def wai(foo):
    def one(*args):
        print ('和是 %d' %sum(args))
        foo(args)
    return one
@wai
def foo(*args):
    print ('===foo===')
    print ('foo 的参数是%s '%args)
foo(1,4,5)

#________________________________________
def Wai(foo):
    def two(*a):
        print ('最多值是%d'%max(a))
        foo(a)
    return two
@Wai
def foo(*a):
    print ('----foo-----')
    print ('%s'%a)
foo(8,8,8)
