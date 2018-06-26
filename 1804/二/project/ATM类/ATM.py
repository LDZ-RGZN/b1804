import Adef
import random
import time
#分析ATM的使用场景
#人类 ATM 卡类

#人类_______________________________
class Ren(object):
    __instance = None
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age

    def person(self):
        return '一个名字叫' + self.name +'年龄' + self.age + '岁的' + self.sex + '男'

    def __new__(cls,*K):
        if cls.__instance = None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


#ATM_________________________________
class ATM():
    __instance = None
    information = None
    def __init__(self):
        self.name = None
    def create(self):
        Adef.account()
    def


    def __new__(cls,*k):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

