import jdaf
class plant:
    '''植物类'''
    def __int__(self,name1,name,ph,color,py):
        self.type = name1 #种类
        self.name = name #姓名
        self.ph = ph #血量
        self.color = color #颜色
        self.py = py #属性
    def













#僵尸类_____________________________________________________
class zombie:
    ''' 僵尸类 '''
    def __init__(self,name,ph,color):
        self.name = name
        self.ph = ph
        self.color = color
    def __str__(self):
        s = self.name + '僵尸出现了，很闪闪' + self.color + '的光芒 充满' + self.ph + '的血量,向你飞奔过来'
        return s
    def eat (self):
        ''' 这是一个吃的方法'''
        print ('%s僵尸正在努力的啃咬着目标'%(self.name))
    def run (self):
        print ('%s僵尸跑起来了'%(self.name))
#____________________________________________________________
pu_tong = zombie ('普通','100','灰色')
jdaf.bs(pu_tong)

zhong_ji = zombie ('中级','80','绿色')
jdaf.bs(zhong_ji)

gao_ji= zombie ('高级','100','金色')
jdaf.bs(gao_ji)

jsw = zombie ('僵尸王','9999','彩色')
jdaf.bs(jsw)


















