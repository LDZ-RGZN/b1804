#除第一个和第二个数外,任意一个数都可以有前两个数相加的到
def fib(itmes):
    n = 0
    a,b = 0,1
    while n<itmes:
        print (b)
        a,b = b,a+b
        n += 1
    #return 'done'
f = fib(10)
print (f)

