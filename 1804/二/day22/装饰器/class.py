'''
class Test():
    def __call__(self):
        print ('call mel')
t = Test()
t() #call me
'''
#类装饰器demo

class Test(object):
    def __init__(self,func):
        print ('___初始化___')
        print ('func name is %s'%func.__name__)
        self.__func = func
    def __call__(self):
        print ('--装饰器中的功能--')
        self.__func()
@Test
def test():
    print ('---test---')
test()
#showpy() #如果把这句话注释,重新运行程序,依然会看到''___初始化___''









