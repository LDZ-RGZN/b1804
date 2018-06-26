def fib(times):
    n = 0
    a,b = 0,1
    while n<times:
        yield (b)   #这个生成器最终返回个fib
        a,b = b,a+b
        n += 1
    return '错误'   #不理解return 的意义
f = fib(10) #得到一个 生成器 yield
while True:
    try:
        x = next(f)
        print (x,end='')
    except StopIteration as a:    #不明把为什么错误会返回这
        print ('生成器返回的结果是:',a)
        break

