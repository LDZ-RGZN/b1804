#使用类来实现
#定义伊兰特车类
class Yilante(object):
    def one(self):
        print ('----车辆在奔驰------')
    def two(self):
        print ('---停车---')

#定义索塔纳车类
class Suotana (object):
    def one(self):
        print ('----车辆在奔驰------')
    def two(self):
        print ('---停车---')
#定义一个生产汽车的工厂，让其根据具体的订单生产车
class SuonataCar(object):
    def cearte(self,typeName):
        if typeName is '伊兰特':
            car = Yilante()
        elif typeName is '索拉塔':
            car = Suotana()
        return car

#定义一个销售北京现代车的店类
class CarStore(object):
    def __init__(self):
        #设置4s店的指定生产汽车的工厂
        self.carFactory = CarFactory()

    def order(self,typeName):
        #让工厂根据类型,生产一辆汽车
        car = self.carFactory.createCar(typeName)
        return car





