'''private property add getter and setter method'''
class Money(object):
    def __init(self):
        self.__money = 0
    def getMoney(self):
        return self.__money
    def setMoney(self,value):
        if isinstance(value,int):
            self.__money = value
        else:
            print ('not 整形')
    money = property(getMoney,setMoney)

m = Money()
m.money = 10
print (m.getMoney())
