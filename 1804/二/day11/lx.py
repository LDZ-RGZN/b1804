class Duck(object):
    def walk(self):
        print ("小黄鸭在摇摆着行走...")
    def swim(self):
        print("小黄鸭在湖水中游泳...")

class Ren(object):
    def walk(self):
        print ("老王　在摇摆着行走...")
    def swim(self):
        print ('老王　在湖水中裸泳...')

def Func(obj):
    obj.walk()
    obj.swim()

duck = Duck()
p01 = Ren()
Func(p01)
























