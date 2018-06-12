class Human:
    name = '小王'
    sex = '男'
    age = 17

    def inforamtion(self):
        print('姓名:%s\n性别:%s\n年龄:%d'%(self.name,self.sex,self.age))
class Profession(Human):
    def __init__(self,gz,jn):
        self.gz = gz
        self.jn = jn
    def __str__(self):
        return '职业:%s\n技能:%s'%(self.gz,self.jn)



xm = Profession('警察','抓小偷')
xm.inforamtion()
print (xm)
