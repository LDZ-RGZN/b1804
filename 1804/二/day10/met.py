#!/usr/bin/env python
# coding=utf-8
class People(object):
    guoji = 'china'
    def __init__(self):
        self.name = '小明'
    def get_name(self):
        return self.name
    @classmethod
    def get_guoji(cls):
        return cls.guoji

people01 = People()
print (people01.guoji)
people01.guoji = 'usa'
print (People.guoji)
print (people01.guoji)
del people01.guoji
del People.guoji
#print (people01.guoji)








