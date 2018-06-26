class MyName(Exception):
    '''自定义异常类'''
    def __init__(self):
        self.error = '填写错误'

class Test(object):
    def __init__(self,switch):
        self.switch = switch  #开关

    def calc(self,a,b):
        try:
            return a/b
        except Exception as result:
            if self.switch is True:
                print ('捕获开启,已经捕获到了异常,信息如下:',result)
            else:
                #重写抛出这个异常,此时就不会被这个异常处理给捕获到了,从而触发默认的异常处理
                my = MyName()
                raise my.error

a = Test(True)
a.calc(11,0)
print ('------华丽的分割线------')
a.switch = False
a.calc(11,0)
