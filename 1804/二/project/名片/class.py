from cdef import *
#在名片管理系统中只有一个类
class Card(object):
    __instance = None
    def __init__(self):
        self.list_card = []
    def Home(self):
        home()
    def Js(self):
        while True:
            home()
            action = int(input('请填写您需要服务的序列号'))
            if action == 1:
                p = int(input('请问您想新建多少张名片：'))
                while p > 0:
                    print ('欢迎您登录新建名片系统')
                    if action == 1:
                        self.list_card = newcard(self.list_card)
                    opn(p)
                    p -= 1
            #退出
            elif action == 888:
                print ('您已经成功退出')
                break
            #查询
            elif action == 2:
                self.list_card = dic(self.list_card)
            #显示全部
            elif action == 3:
                self.list_card = qb(self.list_card)
            #删除
            elif action == 5:
                self.list_card = rv(self.list_card)
            #修改
            elif action == 4:
                self.list_card = xiu_gai(self.list_card)
    def File(self):

        f = open ('1.txt','a+')
        s = self.list_card
        f.write(str(s))
        f.close()
    def __new__(cls,*k):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
user = Card()
user.Js()
user.File()

