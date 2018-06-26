class Student(object):
    __instance = None
    def __init__(self,name,age,scores):
        self.name = name
        self.age = age
        self.scores = scores
    def get_name(self):
        print (self.name)
    def get_age(self):
        print (self.age)
    def get_course(self):
        print (max(self.scores))
    def __new__(cls,*k):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
lhx = Student('LHDXZL',17,[80,90,70])
lhx.get_name()
lhx.get_age()
lhx.get_course()

