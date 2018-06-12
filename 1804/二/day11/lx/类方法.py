class People(object):
    country = 'china'

    #类方法classmethod来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country

p = People()
print(p.getCountry())       #可用通过实例引用
print(People.getCountry())  #可用用过类对象引用
