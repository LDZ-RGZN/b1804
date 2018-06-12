class People(object):
    country = 'china'

print (People.country)
p = People()
print (p.country)
p.country = '日本'  #此时的类属性已经变成了实例属性
print (p.country)   #实例属性会屏蔽掉同名的类属性
print ('此时在来看一下类属性')
print (People.country)
del p.country #删除实例属性
print (p.country)

#实例属性不会更改类属性
#如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。

