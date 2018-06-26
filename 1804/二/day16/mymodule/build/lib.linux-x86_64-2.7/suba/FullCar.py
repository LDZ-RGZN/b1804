#定义伊兰特车类
class YilanteCar(object):
    #定义车的方法
    def move(self):
        print ('---车在移动---')
    def stop(self):
        print ('---停车---')
#定义索纳塔车类
class SuonataCar(object):
    #定义车的方法
    def move(self):
        print ('---车在移动---')
    def stop(self):
        print ('--停车--')
#用来生成具体的对象
def createCar(typeName):
    if typeName == '伊兰特':
        car = YilanteCar()
    elif typeName == '索纳塔':
        car = SuonataCar()
    return car   #让createCar变成s or y
#定义一个销售北京现代车的店类
class CarStore(object):
    #def __init__(self):
        #设置4s店的指定生产汽车的的工厂
    def order(self,typeName):
        #让工厂根据类型,生产一辆汽车
        car = createCar(typeName)
        car.move()
        car.stop()
        return car     #着个return 好像没什么意义
'''
class b(CarStore):
    def ren(self,name):

        self.name = name
        car = CarStore.order(self.name)
        car.move()
        car.stop()
a = b()
a.ren('伊兰特')
'''


a = CarStore()
a.order('伊兰特')

