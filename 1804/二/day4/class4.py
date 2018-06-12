import time


class cat:
    def __init__(self,lun_zi,color):
        self.lunzi = lun_zi
        self.color = color
    def pao(self):
        print ('一辆%d个轮子的%s色%s汽车正在公里上飞驰'%(self.lunzi,self.color,self.name))
    def jiao(self):
        print ('这辆%s汽车正在冲着前面的那辆%s汽车鸣笛'%(self.name,self.name2))

    def zw(self):
        print ('后面的%s汽车成功的追尾了前面的%s汽车,鼓掌'%(self.name,self.name2))
    def __str__(self):
        s = '车的品牌是:'+self.name+'      车的颜色是:'+self.color
        return s


bm = cat(4,'红')
bm.name = '宝马'
bm.name2 = '奥迪'
bm.pao()
bm.jiao()
print ('请稍等.即将追尾')
time.sleep(1)
bm.zw()
print (bm)
print ('内存位置是%d'%(id(bm)))
print ('下一波操作即将进行')
time.sleep(1)
bm1 = cat(8,'蓝')
bm1.name = '奥迪'
bm1.name2 = '宝马'
bm1.pao()
bm1.jiao()
print ('请稍等.即将追尾')
time.sleep(1)
bm1.zw()
print (bm1)
print ('内存位置是%d'%(id(bm1)))
