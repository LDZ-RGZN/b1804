#创建单例-保证只有1个对象
class JiuMei(object):
    __instance = None

    def __new__(cls,age,name):
        #如果类数字能够__instance 没有或者没有赋值
        #那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时
        #能够知道之前已经创建过对象了　这样保证了只有一个对象
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

a = JiuMei(18,'九妹')
b = JiuMei(8,'九妹')

print (id(a))
print (id(b))

a.age = 19 #给a指向的对象添加一个属性
print (b.age)




















