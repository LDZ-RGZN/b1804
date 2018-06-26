'''
L = (i*2 for i in range(1,5))
print ('*'*20)
a = 0
for i in L:
    print (int(i))
    a += i
print ('和是',a)
'''
L = [i for i in range(1,100) if i%2 != 0]
print (L)
