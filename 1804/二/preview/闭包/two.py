def test(number_out):
    def test_in(number_in):
        '''在函数每部再定义一个函数,并且这个函数用到了外边函数的变量,那么将这个函数以及用到的一些变量称之为闭包'''
        print ('in test_in 函数,number_in is %d'%number_in)
        return number_in + number_out #其实这里返回的就是闭包的结果
    return test_in
print (test(10)(2))


