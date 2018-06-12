import time
import random
class cat:
    '''汽车生产的过程'''
    def __init__(self,name,lz,color):
        self.name = name
        self.lun_zi = lz
        self.color = color
#___________________________________
    def introduce(self):
        time.sleep(1)
        print ('正在制作%s汽车，%d个轮子的'%(self.name,self.lun_zi))
        time.sleep(1)
        print ('车子的颜色是%s'%(self.color))

    def base(self):
        time.sleep(1)
        u = random.randint(000000,999999)
        print ('%s汽车已经制作完成,汽车编号是%d'%(self.name,u))

bm = cat('宝马',4,'红色')
bm.introduce()
bm.base()
print ('*'*50)
ad = cat('奥迪',8,'金色')
ad.introduce()
ad.base()

