class counter(object):
    __instance = None
    '''先设置出加减乘除的方法'''
    def __init__(self,one,two):
        self.one = one
        self.two = two
    def plue(self):    #加
        h = self.one + self.two
        return h
    def minus(self):    #减
        h = self.one - self.two
        return h
    def multiply(self):    #乘
        h = self.one * self.two
        return h
    def divide(self):    #除
        h = self.one / self.two
        return h

    def __new__(cls,*k):     #满足单例模式的题意
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
#______________________________________________

def j(one,two,symbol):
    if symbol is '+':
        jsq = counter(one,two)
        jsq.plue()
        print (jsq.plue())
    elif symbol is '-':
        jsq = counter(one,two)
        jsq.minus()
        print (jsq.minus())
    elif symbol is '*':
        jsq = counter(one,two)
        jsq.multiply()
        print (jsq.multiply())
    elif symbol is '/':
        jsq = counter(one,two)
        jsq.divide()
        print (jsq.divide())
def s():
    one = 0
    while True:
        one = int (input('请输入数字:'))
        symbol = input('请输入符号:')
        two = int (input('请输入数字:'))
        symbol1 = input('请输入符号:')
        if symbol1 is '=':
            j(one,two,symbol)
            one = 0
        elif symbol1 != '=':
            j(one,two,symbol)
            symbol = symbol1

#______________________________
try:
    s()
except Exception as result:
    print ('程序出现了问题:%s'%result)
finally:
    s()










