#!/usr/bin/env python
# coding=utf-8
class Father(object):
    def __init__(self,name):
        self.xing = name 
    def ff(self):
        print('父类')

class Son(Father):
    def __init__(self,name):
        super().__init__(name)

    def ff(self):
        super().ff()

son = Son('儿子')
print(son.xing)
son.ff()
