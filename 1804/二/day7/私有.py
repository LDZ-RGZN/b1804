class People:
    def __init__(self,name,salary):
        self.__name = name   #私有化属性，只能自己访问
        self.salary = salary

    def get_name(self):
        return self.__name
    def set_name(self,n):   #?set 更改
        self.__name = n
        return self.__name
    def get_salary(self):     #获得
        return self.salary
    def __send_msg(self):
        return '验证码发送成功'  #这里的私有化只有自己才可以访问

    def get_msg(self,p):
        '''从这里调用可以查看验证码'''
        if p == 123 :
            print (self.__send_msg())
        else :
            print ('验证码错误')

xh = People('小花',8000)
print (xh.get_name())
xh.set_name('小王')
print (xh.get_name())
print (xh.get_salary())
print (xh.get_msg(111))
