class Money(object):
    def __init__(self):
        self.__money = 0
    @property
    def moneyo(self):
        return self.__money
    @moneyo.setter
    def moneyo(self,value):
        self.__money = value
m = Money()
m.money = 100
print (m.money)
