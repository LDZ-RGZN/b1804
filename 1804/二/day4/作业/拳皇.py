import qdef
import time
class People:
    def __init__(self,name,heigh,weight):
        self.name = name
        self.heigh = heigh
        self.weight = weight
    def jump(self):
        print ('%s的%s跳起来了....'%(self.weight,self.name))
    def run(self):
        print ('%s又跑起来了'%(self.name))
    def zhiquan(self):
        print ('%s身高的%s打了一套组合拳'%(self.heigh,self.name))
        print ('上勾拳，下勾拳,OK!')
    def ok(self):
        print ('%s把对手打趴下了'%(self.name))
    def __str__(self):
        s = '本次参赛选手是' + self.name
        return s

#________________________________________
cgh = People('陈国汉','2.5米','200公斤')
qdef.bs(cgh)
qdef.tm()
#____________________________________
dm = People('德玛','1.8米','180公斤')
qdef.bs(dm)
qdef.tm()
#____________________________________
ys = People('亚索','1.5米','100公斤')
qdef.bs(ys)
qdef.tm()
#____________________________________
strn= People('石头人','3.8米','500公斤')
qdef.bs(strn)
qdef.tm()
#____________________________________
hb = People('寒冰','1.7米','90斤')
qdef.bs(hb)
