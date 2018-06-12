#!/usr/bin/env python
# coding=utf-8
class Father(object):
    def __init__(self,name):
        self.xing = name 
    def kaiche(self):
        print ('是个老司机...')
    def eat(self):
        print ('能吃...')
class Son(Father):
    def __init__(self,name):
        #self.ming = name 
        #Father.__init__(self,name)
        #super(Son,self).__init__(name)  2.子类调用父类的方法
        super().__init__(name)
    def kaiche(self):
        # print('是个赛车手...')
        super().kaiche()
            
son = Son('大头儿子')
#print(son.ming)
print(son.xing)
son.kaiche()





