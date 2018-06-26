def dg(a):
    if a >= 1:
        b = a*dg(a-1)
    else :
        b = 1
    return b
c = dg(9)
print(c)
