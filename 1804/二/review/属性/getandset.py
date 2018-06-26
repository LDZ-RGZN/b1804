class Money(object):
    def __init__(self):
        self.__money = 0
    def getMoney(self):
        print (self.__money)
    def setMoney(self,value):
        if isinstance(value,int):
            self.__money = value
        else:
            print ('不是整型数字')
money = Money()
money.getMoney()
print ('*'*20)
money.setMoney(520)
money.getMoney()
