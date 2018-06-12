class Dog(object):
    def game(self):
        return "普通狗只是简单的玩耍"

class XiaoTianDog(Dog):
    def game(self):
        return "哮天犬需要在天上玩耍"
class Person(object):
    def hgw(self,dog):
        print ('人在和'+dog.game())


dg= Dog()
xt = XiaoTianDog()
ren = Person()

ren.hgw(dg)
