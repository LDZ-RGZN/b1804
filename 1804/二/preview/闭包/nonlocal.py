def counter(start = 0):
    def incr():
        nonlocal start #python3 访问外部函数的局部变量(nonlocal)
        start += 1
        return start
    return incr

c1 = counter(1)
print ('c1 = %d'%c1())
print ('c1 = %d'%c1())
c2 = counter(5)
print ('c2 = %d'%c2())




