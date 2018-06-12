import time
class plant:
    def __init__(self,name):
        self.name = name
    def namez(self):
        print ('类名：%s'%(self.name))
    def property(self):
        print ('属性：%s'%(self.py))
    def behavior(self):
        print ('行为：%s'%(self.br))
    def __str__(self):
        s = '植物的名字是' + self.name
        return s
#_________________________________________

class shi:
    def __init__(self,name):
        self.name = name
    def namez(self):
        print ('类名：%s'%(self.name))
    def property(self):
        print ('属性：%s'%(self.py))
    def behavior(self):
        print ('行为：%s'%(self.br))
    def __str__(self):
        s = '僵尸的名字是' + self.name
        return s

#植物类＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
sunflower = plant('向日葵')
sunflower.py = '未知'
sunflower.br = '放阳光'
sunflower.namez()
sunflower.property()
sunflower.behavior()
print (sunflower)
print ('植物的储存位置是:%d'%id(sunflower))
print ('*'*50)
#__________________________________________
pea = plant('豌豆')
pea.py = '颜色,发型，血量'
pea.br = '发炮,摇头'
pea.namez()
pea.property()
pea.behavior()
print (pea)
print ('植物的储存位置是:%d'%id(pea))
print ('*'*50)
#__________________________________________
nut = plant('坚果')
nut.py = '血量'
nut.br = '阻挡'
nut.namez()
nut.property()
nut.behavior()
print (nut)
print ('植物的储存位置是:%d'%id(nut))
print ('*'*50)
#__________________________________________
potato = plant('土豆雷')
potato.py = '一次性'
potato.br = '爆炸'
potato.namez()
potato.property()
potato.behavior()
print (potato)
print ('植物的储存位置是:%d'%id(potato))
print ('*'*50)
#___________________________________________

js= shi ('僵尸')
js.py = '颜色，血量，类型，速度'
js.br = '走，跑跳，吃，死'
js.namez()
js.property()
js.behavior()
print (js)
print ('僵尸的储存位置是:%d'%id(js))
print ('*'*50)



























