#汽车父类
class Father(object):
    def One(self):
        print ('汽车已经生产完成')
    def Two(self):
        print ('汽车已经上路')
    def Three(self):
        print ('汽车已经停车')

#汽车类
class Car(Father):
    __instance = None
    name = None
    def one(self):
        self.name = '伊兰特'
        print (self.name)
        Father().One()
    def two(self):
        Father().Two()
    def three(self):
        Father().Three()
    def __new__(cls,*k):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

#工厂类
class Plant(Car):
    typeName = None
    car = None
    def createCar(self,typeName):
        self.typeName = typeName
        if self.typeName == Car.__init__(self.name):
            print (Plant.__init__(self.typeName))
            self.car = Car()
        return self.car
#汽车的销售类
class Sell(Plant):
    def sx(self):
        self.car = Car()
        self.car.one()
        self.car.two()
        self.car.three()
a = Sell()
a.createCar('伊兰特')
a.sx()






























