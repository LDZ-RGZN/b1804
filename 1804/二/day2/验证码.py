import random
tmp = ''
for  i in range(4):
    n = random.randint(0,2)
    if n == 0:
        num = random.randint(62,91)
        tmp += chr(num)
    else:
        k = random.randint(0,10)
        tmp += str(k)
print (tmp)
