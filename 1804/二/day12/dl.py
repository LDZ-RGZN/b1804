#单例模式
class Car(object):
    __instance = None #用于保存实例化对象
    __init_flag = True #表示init一次都没有执行
    def __init__(self,name):
        if Car.__init_flag == True:   #这里表示　第一次执行
            self.name = name
            print ('------__init__方法被调用-----')
            Car.__init_flag = False
    def __new__(cls,*K):
        print ('--__new__方法被调用-----')
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance
c1 = Car('宝马')
print (c1.name)
c2 = Car('奔驰')
print (c2.name)
print (id(c1))
print (id(c2))


#_____________________________________
class Car(object):
    __instance = None
    __init = True

    def __init__(self,name):
        if Car.__init == True:
            self.name = name
            Car.__init = False

    def __new__(cls,*k):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

c1 = Car('兰博基尼')
print (c1.name)
c2 = Car('劳斯莱斯')
print (c2.name)
print (id(c1))
print (id(c2))


#_____________________________________________

class Car(object):
    __instance = None
    __init = True

    def __init__(self,name):
        if Car.__init is True:
            self.name = name
            Car.__init = False

    def __new__(cls,*k):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance


c1 = Car('兰博基尼')
c2 = Car('劳斯莱斯')
print (c1.name)
print (c2.name)
print (id(c1))
print (id(c2))


























































