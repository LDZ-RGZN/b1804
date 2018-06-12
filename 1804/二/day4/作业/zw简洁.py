class zw:
    def __init__(self,name,py,br):
        self.name = name
        self.py = py
        self.br = br
    def namez(self):
        print ('类名：%s\n属性：%s\n行为：%s'%(self.name,self.py,self.br))
    def __str__(self):
        s = '类型是' + self.name
        return s
xrk = zw('向日葵','未知','放阳光')
xrk.namez()
print ('*'*30)
wd = zw('豌豆','颜色，发型，血量','发炮，摇头')
wd.namez()
print ('*'*30)
jg = zw('坚果','血量，类型','阻挡')
jg.namez()
print ('*'*30)
td= zw('土豆雷','一次性','爆炸')
td.namez()
print ('*'*30)
js = zw('僵尸','颜色，血量，类型，速度','走，炮跳，吃，死')
js.namez()
print ('*'*30)
