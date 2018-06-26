#设计一个卖北京现代车的4s店

#定义伊兰特车类
class YilanteCar(object):

    #定义车的方法
    def move(self):
        print ('车在移动')
    def stop(self):
        print ('----停车----')

#定义索纳塔车类
class SuonataCar(object):

    #定义车的方法
    def move(self):
        print ('车在移动')
    def stop(self):
        print ('停车')

#定义一个销售北京现代车的店类
class CarStore(object):
    def __init__(self,name):
        self.name = name
    def order(self,typeName):
        #根据客户的不同 生成不同的类型的车
        if typeName == self.name or typeName == '伊兰特':
            car = YilanteCar()
            car.move()
            car.stop()
        elif typeName == '索塔纳':
            car = SuonataCar()
            car.move()
            car.stop()

        return car
q = CarStore('宝马')   #从这里新建汽车
q.order('宝马')
