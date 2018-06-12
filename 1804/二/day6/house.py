#两个类  房子　家具
class House:
    def __init__(self,area,addr):
        self.area = area
        self.addr = addr
        self.item = []
    def get


    def __str__(self):
        return '房子的地址是%s,大小是%d平米,包含的家具有%s'%(self.addr,self.area,str(self.item))

    def add_items(self,item): #添加家具
        if self.area > item.area:
            self.area -= item.area
            self.item.append(item.name)
        else :
            print ('家太小了，容不下了')
class Bed:  #家具类
    def __init__(self,area,name):
        self.area = area
        self.name = name
    def __str__(self):
        return '%s已经购买完成，它的尺寸是%d平米'%(self.name,self.area)




house1 = House(100,'北京二环')
print (house1)
by = Bed(20,'成人床')
print (by)
house1.add_items(by)
print (house1)
by1 = Bed(50,'双人床')
house1.add_items(by1)
print (house1)





