#one__________________________________
class People(object):
    def __init__(self):
        self.__money = 1
    def get_money(self):
        print (self.__money)
    def set_money(self,name):
        self.__money = name
    money = property(get_money,set_money)

p = People()
p.get_money()
p.money = 999
p.get_money()
#two____________________________-
class People1(object):
    def __init__(self):
        self.__money = 999
    @property
    def money(self):
        print (self.__money)
    @money.setter
    def money(self,name):
        self.__money = name

p = People1()
p.money     #到这里money不像个方法更像是个属性
p.money = 888
p.money
p.money
