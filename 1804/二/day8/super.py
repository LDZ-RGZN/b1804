#!/usr/bin/env python
# coding=utf-8
#父级
class Cat(object):
    '''调用父类的方法'''
    def __init__(self,name,age):
        self.name = name
        self.color = 'yellow'
        self.age = age 
#子类
class Bosi(Cat):
    def __init__(self,name,age):
        super().__init__(name,age)  #调用父类的公式

    def __str__(self):
        return '姓名%s颜色%s%s'%(self.name,self.color,self.age)

bosi = Bosi('花花','10')

print (bosi)


