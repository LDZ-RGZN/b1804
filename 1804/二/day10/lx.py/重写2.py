#!/usr/bin/env python
# coding=utf-8
#子类调用父类的方法　和　重写

class Father(object):
    def kaiche(self):
        print('是个老司机．．．')
class Son(Father):
    def kaiche(self):
        super(Son,self).kaiche()
        print ('是个赛车手')
            
s = Son()
s.kaiche()




















