def gen():
    i = 0
    while i<3:
        temp = yield i
        print (temp)
        i + 1
f = gen()
print ('next(f) = %s'%next(f))
print ('f.__next()__%s'%f.__next__())
print ('f.send(ha)%s'%f.send('haha'))    #不理解
print ('f.send(aa)%s'%f.send('aa'))

