class Sum(object):
    def sum(self):
        pass

class Plus(Sum):
    def sum(self):
        return self.a + self.b

class minus(Sum):
    def sum(self):
        return self.a - self.b

class mul(Sum):
    def sum(self):
        return self.a * self.b

class div(Sum):
    def sum(self):
        try:
            return self.a / self.b
        except:
            print ('输入错误')
class undef(Sum):
    def sum(self):
        print ('此运算符暂未开放')
class Factory(object):
    operation = {}
    operation['+'] = Plus()
    operation['-'] = minus()
    operation['*'] = mul()
    operation['/'] = div()
    def create(self,ch):
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = undef()
        return op
if __name__ == '__main__':
    op = input('请输入运算符:')
    a = int (input('a:'))
    b = int (input('b:'))
    factory = Factory()
    cal = factory.create(op)
    cal.a = a
    cal.b = b
    print (cal.sum())





