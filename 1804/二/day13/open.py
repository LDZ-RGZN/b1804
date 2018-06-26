class yest(object):
    def __init__(self):
        self.switch = 'open'  #初始化开关 实例属性
    def div (self,a,b):
        try:
            return a/b
        except Exception as result:
            if self.switch is 'open':
                #对异常进行处理
                print ('出现了异常:%s'%result)
            else:
                raise #不处理异常,直接抛出到
t = yest()
t.switch = 'open'
print (t.div(2,0))


class Test(object):
    def __init__(self,switch):
        self.switch = switch
    def ty(self,a,b):
        try:
            print(a/b)
        except Exception as result:
            if self.switch is 'open':
                print ('出现了异常:%s'%result)
            else:
                raise

t = Test(object)
t.switch = 'open'
t.ty(2,0)






















