def fib(x):
    n = 0
    a,b = 0,1
    while n < x:
        yield (b)
        a,b = b,a+b
        n += 1
    return 'ok'
f = fib(10)
for i in f:
    print (i,end = '')
def fib(x):
    n = 0
    a,b = 0,1
    while n < x:
        print (b)
        a,b = b,a+b
        n += 1
    return 'ok'
f = fib(5)
for i in f:
    print (i,end='')
