#!/usr/bin/env python
# coding=utf-8
class People(object):
    country = 'china'

    #类方法，用classmethod在进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country
    @classmethod
    def setCountry(cls,country):  #可以用set对修饰进行修改
        cls.country = country

p = People()
print (p.getCountry())
print (People.getCountry())

p.setCountry('japan')
print (p.getCountry())
print (People.getCountry())


