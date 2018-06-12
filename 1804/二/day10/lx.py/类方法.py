#!/usr/bin/env python
# coding=utf-8
#实例　属性　方法
#类　属性　方法
class People(object):
    guoji = 'china'
    def __init__(self):
        self.name = '小明'  #实例属性
    def get_name(s):   #实例方法
        return s.name
    @classmethod
    def get_guojji(cls):
        return cls.guoji
    @classmethod
    def say_chinese(c):
        print('巴拉巴拉．．．中国话')

people01 = People()
print (people01.guoji)
people01.guoji = 'usa'
print (People.guoji)
print (people01.guoji)
del people01.guoji
print (people01.guoji)

















