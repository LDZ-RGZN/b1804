#定义一个基本的4s店类
class CarStore(object):
    #仅仅是定义了有这个方法,并没有实现,具体功能,这个需要在子类中实现
    def createCar(self,typeName):
        pass
    def order(self,typeName):
        #让工厂根据类型,生产一辆汽车
        self.car = self.createCar(typeName)  #不明白create前面为什么要加self/这个creat是下面那个
        self.car.move()
        self.car.stop()
#定义一个北京现代4s店类      这里实际上是创建工厂对象的过程
class XiandaiCarStore(CarStore):
    def createCar(self,typeName):  #one
        self.carFactory = CarFactory()     #这是创建对象的过程
        return self.carFactory.createCar(typeName)   #最终suo变成createCar
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
        print ('---停车---')
#定义一个生产汽车的工厂,让其根据具体的订单生产车
class CarFactory(object):
    def createCar(self,typeName):   #two   问这个create不会把上面那个重写吗
        self.typeName = typeName
        if self.typeName == '伊兰特':
            self.car = YilanteCar()
        elif self.typeName == '索纳塔':
            self.car = SuonataCar()
        return self.car     #这个return返回的应该是这个del在个类也就变成了SuonataCar到15行
suonata = XiandaiCarStore()
suonata.order('索纳塔')




















