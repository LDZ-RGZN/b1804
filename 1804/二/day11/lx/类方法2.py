class People(object):
    country = 'china'

    #类方法，用classmethod来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country

    @classmethod
    def setCountry(cls,country):
        cls.country = country

p = People()
print (p.getCountry())  #可用用实例对象引用
print (People.getCountry())  #可用通过类对象引用

p.setCountry('japen')

print (p.getCountry())
print (People.getCountry())

