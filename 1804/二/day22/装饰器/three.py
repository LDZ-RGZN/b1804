#定义函数:完成包裹数据
def makeBold(fn):
    def wrapped():
        return 'one     ' + fn()
    return wrapped
#定义函数:完成包裹数据
def makeItalic(fn):
    def wrapped():
        return 'two     ' + fn()
    return wrapped
@makeBold
def test1():
    return 'world -1'

@makeItalic
def test2():
    return 'world -2'


#两个装饰器在没有输入的情况下可以一起显示
@makeBold
@makeItalic
def test3():
    return 'world -3'


print (test1())
print ('*'*50)
print (test2())
print ('*'*50)
print (test3())
