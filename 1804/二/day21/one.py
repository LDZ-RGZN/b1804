one_list = []
two_list = []
for i in range(100):
    one_list.append(i)
one_list = iter(one_list)
n = 0
a,b = 0,1
while n<100:
    two_list.append(b)
    a,b = b,a+b
    n += 1
for i in one_list:
    if i in two_list:
        print (i)

