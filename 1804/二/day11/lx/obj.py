class People(object):
    address = '山东'  #类属性
    def __init__(self):
        self.name = 'XiaoWang'   #实例属性
        self.age = 20 #实例属性

p = People()
p.age = 12  #实例属性
print (p.address) #正确
print (p.name) #正确
print (p.age) #正确
print (People.address) #正确

#print (People.name) 错误
#print (People.age) 错误
