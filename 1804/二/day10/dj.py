#!/usr/bin/env python
# coding=utf-8
class Donkey(object):
    '''驴类'''
    def manzou(self):
        print ('走路慢．．．')
    def jiao(self):
        print ('驴在叫．．．')



class Horse(object):
    '''马类'''
    def naili(self):
        print ('日行千里，夜行八百')
    def jiao(self):
        print ('马在叫．．．')

class lv(Donkey,Horse):
    def jiao(self):
        print ('骡子在叫...')
lz = lv()
lz.manzou()
lz.naili()    
lz.jiao()
