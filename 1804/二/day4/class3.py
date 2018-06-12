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
    def ok(self):
        print ('%s把对手打趴下了'%(self.name))



cgh = People('陈国汉','2.5米','200公斤')
cgh.jump()
time.sleep(1)
cgh.run()
time.sleep(1)
cgh.zhiquan()
time.sleep(1)
cgh.ok()

print ('请稍等,第二常即将开始')
time.sleep(0.5)
print ('one')
time.sleep(0.3)
print ('two')
time.sleep(0.3)
print ('three')
time.sleep(0.3)
print ('begin')
time.sleep(0.3)

cgh = People('德玛','1.8米','180公斤')
cgh.jump()
time.sleep(1)
cgh.run()
time.sleep(1)
cgh.zhiquan()
time.sleep(1)
cgh.ok()
