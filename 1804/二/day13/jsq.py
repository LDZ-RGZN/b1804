#复习 new 单例
class Calc(object):
    __instance = None
    __flag = True
    def __init__(self,name):
        if Calc.__flag is True:
            self.name = name
            Calc.__flag = False
    def add(self,a,b):
        return a + b
    def minus(self,a,b):
        return a - b
    def mul(self,a,b):
        return a * b
    def div(self,a,b):
        return a / b
    def __new__(cls,*k):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
class SimpleCalc(Calc):
    def ji_suan(self,x,y,symbol):
        if symbol == '+':
            return super().add(x,y)
        elif symbol == '-':
            return super().minus(x,y)
        elif symbol == '*':
            return super().mul(x,y)
        elif symbol == '/':
            return super().div(x,y)
        else:
            return '输入的有问题'

c1 = SimpleCalc('简单计算器')
try:
    r = c1.ji_suan(5,5,'*')
    print (r)
except Exception as a:
    print ('计算器出现错误:',a)


