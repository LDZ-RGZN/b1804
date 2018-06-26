class Car(object):
    def one(self):
        print ('one')
    def two(self):
        print ('two')
class CarStore(object):
    def One(self):
        self.car = Car()
        self.car.one()
        self.car.two()
o = CarStore()
o.One()
