class Person(object):
    def __init__(self,name,age,taste):
        self.name = name
        self._age = age
        self.__taste = taste
    def showperson(self):
        print (self.name)
        print (self._age)
        print (self.__taste)
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
    #@staticmethod
    def testbug():
        _Bug.showbug()
#模块内可以访问,当from cur_module impor* 时,不导入
class _Bug(object):
    @staticmethod
    def showbug():
        print ('showbug')
