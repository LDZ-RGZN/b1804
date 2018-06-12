class People(object):
    country = 'china'

    @staticmethod
    #静态方法
    def getCountry():
        return People.country

print(People.getCountry())
