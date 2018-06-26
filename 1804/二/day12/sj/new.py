#单例模式
class Car(object):
    __instance = None  #用于保存实例化的对象
    def __init__(self,name):
        self.name = name
        print ('-----__init__方法被调用-----')
    def __new__(cls,*k):
        print ('-----__new__方法被调用-----')
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
c1 = Car('宝马')
c2 = Car('奔驰')

print (id(c1))
print (id(c2))




