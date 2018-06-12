#汽车类
class Cat(object):
    def __init__(self,name):
        self.name = name
    def Fei(self):
        return '%s汽车正在路面上飞驰'%(self.name)
#大众____
class Dz(Cat):
    def __init__(self,name):
         super().__init__(name)
    def Fei(self):
        return '%s汽车正在路面上飞驰'%(self.name)
#宝马___
class Bm(Cat):
    def __init__(self,name):
         super().__init__(name)
    def Fei(self):
        return '%s汽车正在路面上慢跑'%(self.name)
#奔驰___
class Bc(Cat):
    def __init__(self,name):
         super().__init__(name)
    def Fei(self):
        return '%s汽车正在路面上飞'%(self.name)
#初始化人类_____
class Person(object):
    def __init__(self,name):
        self.name = name
        self.cn = None
    def rc(self,ca):
        print ('%s开着%s'%(self.name,ca.Fei()))

    def nc(self,ca1):
        self.cn = ca1
        print ('这辆车的名字叫%s'%(self.cn))
    def pc(self):
        print ('%s正开着这俩名叫%s车子去泡妞'%(self.name,self.cn))



#______________________________________________

dz = Dz('大众')
print (dz.Fei())

bm = Bm('宝马')
print (bm.Fei())

bc = Bc('奔驰')
print (bc.Fei())

ren = Person('小明')
ren.rc(dz)
ren.nc('大黄蜂')
ren.pc()












































