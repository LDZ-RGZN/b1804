class Duck(object):
    def walk(self):
        print ('小黄鸭在摇摆着行走．．．')
    def swim(self):
        print ('小黄鸭在湖水中游泳．．．')

class People(object):
    def walk(self):
        print ('老王　在摇摆着行走...')
    def swim(self):
        print ('老王　在湖水中裸泳')

def Func(obj):   #同样一个函数，定义的时候，不知道结果是什么
    obj.walk()   #执行的时候，才会表象出来　它的具体　形态　结果
    obj.swim()

duck = Duck()
p01 = People()
Func(duck)
