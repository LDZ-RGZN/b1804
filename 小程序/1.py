class People(object):
    def __init__(self,mone):
        self.__money = mone
    def get1(self):
        return self.__money
    def set1(self,money):
        self.__money = money
    money = property(get1,set1)
class zhangsan(People):
    def __init__(self,money):
        People.__init__(self,money)
m = zhangsan(100)
m.money = 999
print (m.money)
