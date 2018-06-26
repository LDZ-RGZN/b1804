class Car():
    def __init__(self,newwbeelNum,newColor):
        self.wheelNum = newwbeelNum
        self.color = newColor
    def __str__(self):
        msg = '您好,车辆已经制造完毕,车辆的颜色是:' + self.color + ',一共:' + self.wheelNum + '个轮子'
        return msg
    def move(self):
        print ('车子在泡,目标:香港')
#创建对象
msld = Car('6','green')
isCar = isinstance(msld,Car)
print ('*'*28,isCar,'*'*20)
print ('车的颜色为:%s'%msld.color)
print ('车轮胎的数量:%s'%msld.wheelNum)

print ('内存地址:', id(msld))
print (msld)


