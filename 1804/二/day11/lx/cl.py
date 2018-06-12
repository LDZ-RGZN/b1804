class one(object):
    def one1(self):
        print('1')
class two(one):
    def one2(self):
        print('2')
class san(two):
    def one3(self):
        print('3')

s = san()
s.one1()
s.one2()
s.one3()


