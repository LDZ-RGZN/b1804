
def one(a):
    def two():
        nonlocal a
        a += 1
        print (a)
        return a
    return two
one(1)()
