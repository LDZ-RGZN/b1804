class Test(object):
    def __init__(self,swich):
        self.switch = swich
    def calc(self,a,b):
        try:
            return a/b
        except Exception as result:
            if self.switch == True:
                print ('捕获开启,已经捕获到了异常,信息如下:')
                print (result)

            else:
                #重新抛出这个异常,此时就不会被这个一层处理给捕获到,从而触发默认的异常处理
                raise #向上一层传递

a = Test(True)
a.calc(11,0)

