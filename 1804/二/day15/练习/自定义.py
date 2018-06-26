class MyError(Exception):
    def __init__(self):
        self.length = '自定义错误'
        pass

b = MyError()

class Test(object):
    def __init__(self,switch):
        self.switch = switch
    def calc(self,a,b):
        try:
            return a/b
        except Exception as result:
            if self.switch is True:
                print ('捕获开始,已经捕获到了异常,信息如下:')
                print (result)
            else:
                print (b.length)
a = Test(True)
a.calc(11,0)
print ('_________________')
a.switch = False
a.calc(11,0)





'''
def main():
    s = input('please input your name')
    try :
        if len(s) < 3:
            raise MyError(len(s),3)
    except MyError as rest:
        print (rest)
    else:
        print ('no erro')
main()
'''
