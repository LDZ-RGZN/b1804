import random, time
def a(b):
    num = random.randint(1,12)
    snow = random.randint(1,5)
    print(b*num,end='')#两个函数组合起来有问题
    print('*'*snow)
    time.sleep(0.2)
    a(b)
a('\t\t\t')
