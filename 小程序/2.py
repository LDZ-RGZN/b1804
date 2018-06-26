class People(object):
    def __init__(self,mone):
        self.__money = mone
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self,money):
        self.__money = money
class zhangsan(People):
    def __init__(self,money):
        People.__init__(self,money)
m = zhangsan(100)
m.money = 999
print (m.money)
