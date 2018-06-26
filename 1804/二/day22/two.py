def one(a,b):
    def two(x):
        nonlocal b
        print ('y = %d*%d+%d'%(a,x,b))
        y = a*x+b
        x += 1
        print (x)
        return y
    return two
u = one(3,5)
print (u(5))   #不明白为什么这里加print不报错
#___________________________
def One(a,b,x):
    def Two():
        print ('y = %d*%d+%d'%(a,x,b))
        y = a*x+b
        return y
    return Two
u = One(3,3,3)
print (u())





