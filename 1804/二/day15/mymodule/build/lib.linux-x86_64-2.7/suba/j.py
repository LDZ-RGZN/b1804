def plus(a,b):
    return a + b
def minus(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
class Jsq(object):
    __instance = None
    __init = True
    def __init__(self,first):
        if Jsq.__init is True:
            self.first = first
            Jsq.__init = False
    def ff(self):
        while True:
            fh = input('请输入符号:')
            if fh is '=':
                break
            elif fh is 'q':
                break
            two = int(input('请输入数字:'))
            if fh is '+':
                self.first = plus(self.first,two)
                print ('答案提示:',self.first)
            elif fh is '-':
                self.first = minus(self.first,two)
                print ('答案提示:',self.first)
            elif fh is '*':
                self.first = multiply(self.first,two)
                print ('答案提示:',self.first)
            elif fh is '/':
                self.first = divide(self.first,two)
                print ('答案提示:',self.first)
    def __new__(cls,*k):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
def counter():
    try:
        print ('='*30)
        print ('    欢迎使用python计算器')
        print ('='*30)
        print ('在符号内输入q退出')
        first = int (input('请输入数字:'))
        jsq = Jsq(first)
        jsq.ff()
        print ('*'*50)
        print ('最终计算结果是:',jsq.first)
        print ('*'*50)
    except Exception as result:
        print ('程序出现了问题:%s'%result)
