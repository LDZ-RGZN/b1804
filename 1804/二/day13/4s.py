#设计一个卖车的4s店,该怎么做呢?
#定义类
class Car(object):

#定义车的方法
    def move(self):
        print ('-----车在移动------')
    def stop(self):
        print ('----停车----')

#定义一个销售锄车的店类
class CarStore(object):
    def order(self):
        self.car = Car() #找一辆车 相当于用car创建了Car的实例对象
        self.car.move()
        self.car.stop()

d = CarStore()
d.order()
