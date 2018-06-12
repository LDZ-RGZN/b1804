#!/usr/bin/env python
# coding=utf
class People(object):
    country = 'china'
    
    #类方法　classmetod 来修饰
    @classmethod 
    def getCountry(cls):
        return cls.country
p = People()
print (p.getCountry())
print (People.getCountry()) #通过类对象引用

