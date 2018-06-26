#父类中属性名为_名字的,子类不基础,子类不能访问
#如果在子类中向_名字赋值,那么会在子类中定义的一个于父类相同名字的属性
#__名的变量,函数,类在使用form xxx import *都不会被导入
class Person(object):
    def __init__(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste
    def showperson(self):
        print (self.name)
        print (self._age)
        print (self.__taste)
    def dowork(self):
        self._work()
        self.__away()
    def _work(self):
        print ('my _work')
    def __away(self):
        print ('my __away')
class Student(Person):
    def construction(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste
    def showstudent(self):
        print (self.name)
        print (self._age)
        print (self.__taste)
    @staticmethod
    def testbug():
        _Bug.showbug()
class _Bug(object):
    @staticmethod
    def showbug():
        print ('showbug')
