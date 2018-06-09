#!/usr/bin/env python
# coding=utf-8
import time
class BanJi:
    student = []
    br = '习大大' 
    bh = 1804 
    ''' 
    def __init__(self,br,bh):
        self.br = br 
        self.bh = bh 
    ''' 
    def __get_Bc(self): 
        print ('班级详情信息') 
        print (self.bh)
        print ('班主任：%s'%(self.br))
        for i in self.student:
            b1 = '姓名：%s    性别：%s    年龄：%d'%(i['姓名:'],i['性别:'],i['年龄:']) 
            print (b1)
    
    def __str__(self):
        return str(self.__get_Bc())
#_____________________________________
class Student(BanJi):
    grade = []
    def __init__(self,name,sex,age):
         
        self.name = name
        self.sex = sex
        self.age = age
        self.dic1 = {} 
    def add_Grade(self):
        print (self.grade)
    def Cx(self,n):      #学生成绩查询
        self.name = n
        for i in self.grade:
            if self.name == i['姓名']:
                print ('成绩详情信息')
                print (i['英语'])                
                print ('姓名：%s\n成绩＊＊＊\n语文:%d\n数学:%d\n英语:%d'%(i['姓名'],i['语文'],i['数学'],i['英语']))
    def C_stu(self):     #把学生信息追加到Student
        self.dic1 = {'姓名:':self.name,'性别:':self.sex,'年龄:':self.age} 
        self.student.append(self.dic1)
 #_____________________________________
class Grade(Student):
    def __init__(self,name,yw,sx,yy):
        self.yw= yw
        self.sx= sx
        self.yy= yy
        self.cname = None 
        self.name = name 
        self.dic = {} 
    def __get_Cx(self):
        for i in self.grade:
            a = i[self.cname]
            b = i['姓名'] 
            print ( '姓名:%s   %s : %d'%(b,self.cname,a))   #此时的显示的是成绩单
            
    def Jgrade(self):
        self.dic = {'姓名':self.name,'语文':self.yw,'数学':self.sx,'英语':self.yy}            
        self.grade.append(self.dic)
        
    def set_Cx(self,n):    #此时输入的ｎ是要查询什么程序的科目
        self.cname = n 
        self.__get_Cx() 
    def Cq (self):       #查询全部成绩的方法
        print ('           ------学生成绩单------')
        for i in self.grade:
            print ('姓名：%s　　语文:%d　　数学:%d　　英语:%d'%(i['姓名'],i['语文'],i['数学'],i['英语']))
    
    def __str__(self):
        return str(self.Cq())
#对象_______________________________________
小王= Student('小王','男',18)
小王.C_stu()
小王= Grade('小王',50,10,80)
小王.Jgrade()

小j= Student('小金','男',17)
小j.C_stu()
小j= Grade('小金',53,72,98)
小j.Jgrade()

小i= Student('小爱','男',21)
小i.C_stu()
小i= Grade('小爱',80,40,60)
小i.Jgrade()

小h= Student('小红','女',15)
小h.C_stu()
小h= Grade('小红',91,87,86)
小h.Jgrade()

小l= Student('小丽','女',17)
小l.C_stu()
小l= Grade('小丽',58,82,60)
小l.Jgrade()
#_______________________________________
print ('='*40)    
print ('           欢迎使用班级管理系统')
print ('='*40)    
while True:    
    print ('1.录入学生信息')
    print ('2.录入成绩信息')
    print ('3.查看全部信息')
    print ('4.查看个人信息')
    print ('5.查看单科成绩')
    print ('6.查看全部成绩')    
    print ('7.退出') 
    user = int(input ('请选择您要的操作：')) 
    print ('请稍后，正在处理．．．') 
    time.sleep(1) 
    if user == 1 :
        print ('*'*40) 
        name = input ('请输入姓名：')    
        sex = input ('请输入性别：')
        age = int (input ('请输入年龄:'))
        name = Student(name,sex,age)     
        name.C_stu() 
        print ('请稍后，正在处理．．．') 
        time.sleep(1) 
        print ('*'*40) 
    elif user == 2:
        name1 = input ('请输入学生的姓名：')
        yw= int (input('请输入语文成绩')) 
        sx= int (input('请输入数学成绩')) 
        yy= int (input('请输入英语成绩')) 
        print ('请稍后，正在处理．．．') 
        time.sleep(1) 
        name1 = Grade(name1,yw,sx,yy)
        name1.Jgrade() 
        print ('*'*40) 
    elif user == 3:
        print (name)
        print ('*'*40) 
    elif user == 4:
        name3 = input ('请输入您要查看人员的姓名：')
        print ('请稍后，正在处理．．．') 
        time.sleep(1) 
        name.Cx(name3)
        print ('*'*40) 
    elif user == 5:
        cj = input ('请输入您要查看的科目：')
        print ('请稍后，正在处理．．．') 
        time.sleep(1) 
        name1.set_Cx(cj)
        print ('*'*40) 
    elif user == 6:
        print (name1)
        print ('*'*40) 
    elif user == 7:
        break 


















