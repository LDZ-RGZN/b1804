#理解self
#定义一个类
class Animal:
    #方法
    def __init__(self,name):
        self.name = name
    def printName(self):
        print ('名字为：%s'%self.name)
#定义一个函数
def myPrint(animal):
    animal.printName()
sugar_dog = Animal('冰糖')
myPrint(sugar_dog)

ninuiu_dog = Animal('牛牛')
myPrint(ninuiu_dog)

#完成






