def jia(x,y):
    return x+y
def jian(x,y):
    return x-y
def cheng(x,y):
    return x*y
def chu(x,y):
    return x/y
while True:
    x = float (input('请你输入数字'))

    while True:
        u = input('请输入符号+-*/:')

        y = float (input('请输入数字：'))
        if x == 000:
            break

        if u == "+":
            q = jia(x,y)
            print("结果是：",q)
        elif u == "-":
            w = jian(x,y)
            print("结果是：",w)
        elif u == "*":
            e = cheng(x,y)
            print("结果是：",e)
        elif u == "/":
            r = chu(x,y)
            print("结果是：",r)


