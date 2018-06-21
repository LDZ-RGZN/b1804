#类属性就是类对象所拥有的属性
#在类外可以通过类对象和实例对象访问
class People(object):
    address = '山东'  #类属性
    def __init__(self):
        self.name = 'XiaoWang' #实例属性
        self.age = 20 #实例属性
p = People()
p.age = 12 #实例属性
print (p.address)
print (p.name)
print (p.age)

print (People.address) #实例属性
#实例对象名和类名在下面都可调用类属性

#通过实例对象去修改类属性
class People(object):
    country = 'chian'

print (People.country)
p = People()
print (p.country)
p.country = '日本' #这里的修改类似于覆盖,因为
print (p.country)
print (People.country)
del p.country
print (p.country)












