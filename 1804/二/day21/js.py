def fib():
    for i in range(1,101):
        if i%2 != 0:
            yield (i)
    return 'ok'
f = fib()
for i in f:
    print (i,end = '\t')
