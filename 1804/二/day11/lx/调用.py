class Cat(object):
    '''dnametring for Cat'''
    def __init__(self,name):
        self.name = name
        self.color = 'yellow'

class Bosi(Cat):
    def __init__(self,name):
        super().__init__(name)

    def getName(self):
        return self.name

bosi = Bosi('花花')
print (bosi.name)
print (bosi.color)
