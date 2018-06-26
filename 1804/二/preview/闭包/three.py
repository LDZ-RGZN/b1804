def counter(start = 0):
    count = [start]
    def incr():
        count[0] += 1
        return count[0]
    return incr
c1 = counter(1)
#闭包会叠加
print ('c1 = %d'%c1())
print ('c1 = %d'%c1())
print ('c1 = %d'%c1())
c2 = counter(5)
print ('c2 = %d'%c2())
