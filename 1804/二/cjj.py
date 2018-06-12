#!/usr/bin/env python
# coding=utf-8
#苍井井，女，１８，初始化战斗力１０００，东尼木木，男，２０，初始化战斗力１８００，波多多，女，１９，初始化战斗力２５００
#草丛战斗，消耗２００战斗力，自我修炼，增长１００战斗力，多人游戏，消耗５００战斗力
class Ren:
    user = [] 
    def __init__(self,name,sex,age):
        self.name = name 
        self.sex = sex
        self.age = age 
    def Tj(self):
        u = {'姓名':self.name,'性别':self.sex,'年龄':str(self.age)}
        Ren.user.append(u) 
    def __get_yx(self):
        print ('请选择英雄') 
        a = 1 
        for i in self.user:
            u1 = '姓名:%s    性别:%s    年龄:%s'%(i['姓名'],i['性别'],str(i['年龄']))
            print ('%d : %s'%(a,u1))
            a += 1    
    def __str__(self):
        return str(self.__get_yx()) 
#场景类
class Cj:
    cl = [] 
    def __init__(self,cj,jg,xh):
        self.cj = cj
        self.jg = jg 
        self.xh = xh 
    def get_ccj(self):
        b = 1
        for i in Cj.cl:
            c1 = '场景：%s '%i['场景']
            
    def ccj(self):
        c = {'场景':self.cj,'结果':self.jg,'数值':self.xh}
        Cj.cl.append(c)
        print (Cj.cl)    
#







#先创建３个对象　
cjj = Ren('苍井井','女',18)
cjj.Tj()
dnmm = Ren('东尼木木','男',20)
dnmm.Tj()
bdd = Ren('波多多','女',19)
bdd.Tj()
print (bdd)
#场景_____________________________
cc = Cj('草丛战斗','消耗',200)
cc.ccj()
zw = Cj('自我修炼','收获',100)
zw.ccj()
br = Cj('多人游戏','消耗',500)
br.ccj()
#________________________________









































