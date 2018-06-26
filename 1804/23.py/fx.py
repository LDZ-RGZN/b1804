print ('练习1')
sum = lambda arg1, arg2: arg1 + arg2
print ("Value of total': ",sum(10,20))
print ("Value of total': ",sum(20,20))

print ('练习2')
f = lambda x,y,z : x+y+z
print (f(1,2,3))#把lambda表达式当做函数的使用

g = lambda x,y=2,z=3 : x+y+z
print (g(1))#含有默认值的参数

print (g(2,z=4,y=5))#调用时使用关键参数

L = [(lambda x:x**2),(lambda x:x**3),(lambda x:x**4)]#配合列表使用
print (L[0](2),L[1](2),L[2](2))

D = {'f1':(lambda:2+3),'f2':(lambda:2*3),'f3':(lambda:2**3)}#配合字典使用
print (D['f1'](),D['f2'](),D['f3']())
