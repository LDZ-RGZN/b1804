class Car(object):
    def __init__(self,name):
        self.name = name
        print ('-----__init__方法被调用-----')
    def __del__(self):
        print ('-----__del__方法被调用-----')
    def __new__(cls,*k):
        print ('-----__new__方法被调用-----')
        return object.__new__(cls)
c = Car('大众')
print (id(c))
c1 = Car('宝马')
print (id(c1))



