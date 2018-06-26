def f():
    a,b = 0,1
    for i in range(1,10):
        yield (b)
        a,b = b,a+b
    return b
F = f()
for i in F:
    print (i)
