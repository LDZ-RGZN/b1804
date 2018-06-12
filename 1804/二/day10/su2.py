#!/usr/bin/env python
# coding=utf-8
class Father(object):
    def __init__(self,name):
        self.xing = name 
    
    def kaiche(self):
        print ('老司机')
    def age(self):
        print ('能吃')

class Son(Father):
    def __init__(self,name):
        super().__init__(name)

    def kaiche(self):
        super().kaiche()
son = Son('儿子')
print (son.xing)
son.kaiche()

