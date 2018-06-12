#这个项目中一共有４个大类，第一步先把４个大类创建出来
import time
import random

#人类________________________________________________
class Human:
    def __init__(self,name,):
        self.name = name    #姓名
        self.ph = 100       #血量
        self.gun = None     #储存枪的
    def __str__(self):
        return self.name + '剩余血量为:' + str(self.ph)  #人类最终的效果展示
    def An_Zi_Dan(self,Dan_Jia,Zi_Dan):
        Dan_Jia.czd(Zi_Dan)  #把子弹装进弹夹的过程
    def An_Dan_Jia(self,gun,Dan_Jia):
        gun.lianjiedanjia(Dan_Jia)  #老王的枪
    def nagun(self,gun):
        self.gun = gun
    def Kai_Qiang(self,diren):    #敌人
        self.gun.she(diren)     #?
    def Dph(self,lethality):
        self.ph -= lethality
#弹夹类_______________________________________________
class clip:
    def __init__(self,capacity):
        self.capacity = capacity
        self.capacityList = []
    def __str__(self):
         return '弹夹当前的子弹数量为:' + str(len(self.capacityList)) + '/' + str(self.capacity)
    def czd(self,Zi_Dan):
        if len(self.capacityList) < self.capacity:
            self.capacityList.append(Zi_Dan)
    def launch(self):
         #判断当前弹夹中是否有子弹          #难以理解
        if len(self.capacityList) > 0:
            #获取最后压入到弹夹中的子弹
            Zi_Dan = self.capacityList[-1]
            self.capacityList.pop()
            return Zi_Dan
        else:
            return None
#子弹类________________________________________________
class Zi_Danc:
    def __init__(self,lethality):
        self.lethality = lethality

    def lenthality(self,diren):
        diren.Dph(self.lenthality)

#抢类__________________________________________________
class Qiang:
    def __init__(self):
        self.Dan_Jia = None

    def __str__(self):
        if self.Dan_Jia:    #是如何判断弹夹是否为空的
            return '枪当前有弹夹'
        else:
            return '枪没有弹夹'

    def lianjiedanjia(self,Dan_Jia): #不明白
        if not self.Dan_Jia:
            self.Dan_jia = Dan_Jia

    def she(self,diren):
        Zi_Dan = self.Dan_Jia.launch()
        if Zi_Dan:
            Zi_Dan.lenthaity(diren)
        else:
            print ('没有子弹了．．．')
#开始开枪＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
#创建一个人对象
laowang = Human('老王')
print(laowang)

#创建一个弹夹
Dan_Jia = clip(20)
print (Dan_Jia)

#循环的方式创建一颗子弹，然后让老王把这颗子弹压入到弹夹中
i = 0
while i < 5:
    Zi_Dan = Zi_Danc(5)
    laowang.An_Zi_Dan(Dan_Jia,Zi_Dan)
    i += 1
print (Dan_Jia)

#创建一个枪的对象
ot = Qiang()
print(ot)

#让老王把枪拿起来
laowang.An_Dan_Jia(ot,Dan_Jia)
print(ot)



#创建一个敌人
diren = Human('敌人')
print (diren)

#让老王拿起枪
laowang.nagun(ot)

#老王开始想敌人开枪
laowang.Kai_Qiang(diren)
print(diren)
print(Dan_Jia)

laowang.Kai_Qiang(diren)
print(diren)
print(Dan_Jia)















































































































