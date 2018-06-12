class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def ne(self):
        print ('姓名:%s'%(self.name))
    def ae(self):
        print ('年龄:%d'%(self.age))
        print (self.grade)
    def ge(self):
        print (self.grade.sort())
        s = self.grade[2]
        print ('最高成绩%d'%(s))
xm = Student('小王',20,[60,80,100])
xm.ne()
xm.ae()
xm.ge()
