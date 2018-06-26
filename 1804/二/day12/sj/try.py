try:
    print ('name')

    try:
        for i in range(1,o,10):
            print (i)
    except NameError:
        print ('for 循环 出问题了')

except IOError as a :
    print (a)
