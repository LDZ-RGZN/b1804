#!/usr/bin/env python
# coding=utf-8
#老王开抢　
#四大类　人类　抢类　弹夹类　子弹类

class Ren:
    def __init__(self,name):
        self.namd = name
        self.xue = 100
        self.qiang = None
    def __str__(self):
        return self.name + '剩余血量为：' + str(self.xue)

    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)

    def andanjia(self,qiang,danjia):
        qiang.lianjiedanjia(danjia)

    def naqiang(self,qiang):
        self.qiang = qiang

    def kaiqing(self,diren):
        self.qiang.she(diren)

    def diaoxue(self,shashangli):
        self.xue -= shashangli

#弹夹类　
class Danjia:
    def __init__(self,rongliang):
        self.rongliang = rongliang
        self.ronglist = []

    def __str__(self):
        return "子弹数量为" + str(len(self.ronglist)) + "/" + str(self.rongliang)

    def baocounzidan(self,zidan):
        if len(self.ronglist) < self.rongliang:
            self.ronglist.append(zidan)
    
    def chuzidan(self):
        if len(self.ronglist) > 0:
            zidan = self.ronglist[-1]
            self.ronglist.pop()
            return zidan
        else:
            return None
#子弹类
class Zidan:
    def __init__(self,shashangli):
        self.shashangli = shashangli

    def shanghai(self,diren):
        diren.diaoxue(self.shashangli)

#枪
class Qiang:
    def __init__(self):
        self.danjian = None

    def __str__(self):
        if self.danjian:
            return "枪当前有弹夹"
        else:
            return "枪当前没有弹夹"

    def lianjiedanjia(self,danjia):
        if not self.danjian:
            self.danjian = danjia

    def she(self,diren):
        zidan = self.danjian.chuzidan()
        if zidan:
            zidan.shanghai(diren)
        else:
            print ("没有子弹了，放了空枪．．")
#创建一个对象
laowang = Ren("老王")

#创建一个弹夹
danjia = Danjia(20)
print (danjia)

i = 0
while i < 5:
    zidan = Zidan(5)
    laowang.anzidan(danjia,zidan)
    i += 1

print (danjia)

qiang = Qiang()
print (qiang)

laowanga.andanjia(qiang,danjia)
print(qiang)

diren = Ren("敌人")
print (diren)

laowang.kaiqiang(diren)
print(diren)
print(danjia)

laowang.kaiqiang(diren)
print (diren)
print (danjia)








































