class Animal(object):
    '''docstring for Animal'''
    def __init__(self,name):
        self.name = name
    def run(self):
        print ('Animal is running...')
class Dog(Animal):
    '''docstring for Dog'''
    def __init__(self,name):
        Animal.__init__(self,name)
    def printName(self):
        print ('Name: %s'%self.name)
kk = Dog('Kity')
kk.printName()
kk.run()
