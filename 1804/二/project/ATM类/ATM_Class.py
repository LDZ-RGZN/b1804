import Adef
#分析ATM的使用场景
#人类 ATM 卡类
#ATM_________________________________
class ATM():
    __instance = None
    information = None
    def __init__(self):
        self.name = None
    def js(self):
        Adef.introduce()
        Adef.home()
    def Login(self):
        Adef.login()
    def __new__(cls,*k):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
#用户__________________________________
class User():
    __instance = None
    __init = True
    def __init__(self):
        user = None
    def Account(self):
        Adef.account()
    def Kh(self):
        return Adef.ac()
#人类_______________________________
class Ren(User,ATM):
    __instance = None
    __init = True
    def __init__(self,name,sex,age):
        if Ren.__init is True:
            self.name = name
            self.sex = sex
            self.age = age
            self.kh1 = None
    def person(self):
        return '一个名字叫' + self.name +',年龄' + str(self.age) + '岁的' + self.sex + '性,拿着张卡号为' + str(self.kh1) + '的银行卡去取钱...'
    #def nacard(self,card):
        #card.create.()     #银行卡
    def cacard(self):
        a = User().Kh()
        self.kh1 = a
    def __new__(cls,*K):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

try:
    atm = Ren('吕东泽','男',17)
    print ('以下为办卡的场景')
    print ('='*50)
    atm.Account()
    atm.cacard()
    print ('='*50)
    print (atm.person())
    atm.js()
    atm.Login()
except Exception as a:
    print ('程序错误:',a)























