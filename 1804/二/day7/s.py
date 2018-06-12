import sys
class Student:
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
        self.cj = {}
    def Cj(self):
        for i in range(1,3):
            k = input('科目:')
            v = int (input('成绩:'))
            self.cj[k] = v
    def __str__(self):
        return '姓名:%s,性别:%s,年龄:%d'%(self.name,self.sex,self.age)
    def Cjx(self):
        for x,y in self.cj.items():
            print ('%s的成绩是：%s 得分 %d'%(self.name,x,y))



xw = Student('小明','男',20)
xw.Cj()
print ('*'*30)
print (xw)
xw.Cjx()
print (sys.getrefcount(xw))
print (isinstance(xw,Student))
print ('你好')






