from inspect import isgenerator

def fib(a,b):
    while a < b :
        yield (a)
        a += 1
f = fib(1,10)
for i in f:
    print (i)
