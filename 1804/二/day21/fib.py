one_list = []
two_list = []
for i in range(1,101):
    one_list.append(i)
a,b = 0,1
for i in range(1,101):
    two_list.append(b)
    a,b = b,a+b
for i in one_list:
    if i in two_list:
        print (i)
