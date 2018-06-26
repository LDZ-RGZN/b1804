#多态我们不关心这个对象的类型本身或是这个类继承,而是这个类是如何被使用的.
class duck:
    def walk(self):
        print ('I walk like a duck')
    def swim(self):
        print ('I swim like a duck')
class person:
    def walk(self):
        print ('one I walk like a duck')
    def swim(self):
        print ('two i swim like a duck')
def you(a):
    a.walk()

w=duck()
c=person()
you(c)

