#理解self
#定义一个类
class Animal:
    #方法
    def __init__(self,name):
        Animal.name = name  #此时的self = Animal,虽然不知道为什么，但是在这一步self可以进行变化
    def printName(self):
        print ('名字为：%s'%Animal.name)
        #同时在这里一直用的self同理要更改成Animal

#定义一个函数
def myPrint(animal): #这里的animal与上的没有关系，这里的只是一个形参
    animal.printName()

sugar_dog = Animal('冰糖')
myPrint(sugar_dog)

niuniu_dog = Animal('牛牛')
myPrint(niuniu_dog)





