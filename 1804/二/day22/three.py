
def Yz(x):
    def one(user,passwd):
        if user == 123 and passwd == 123:
            x()
        else:
            print ('输入有误')
    return one
def Yz1(x):
    def one1(user1):
        if user1 == 123:
            print ('x()')
        else:
            print ('输入有误')
            print (user1)
    return one1
@Yz
def f1():
        print ('欢迎使用f1')
@Yz
def f2():
        print ('欢迎使用f2')
@Yz
def f3():
        print ('欢迎使用f3')
@Yz
@Yz1
def f4():
        print ('欢迎使用f4')

user = int (input('请输入账户:'))
user1 = int (input('请输入账户:'))
passwd = int (input('请输入密码:'))
f = input('选择您需要的服务:')
if f == 'f1':
    f1(user,passwd)
elif f == 'f2':
    f2(user,passwd)
elif f == 'f3':
    f3(user,passwd)
elif f == 'f4':
    f4(user,passwd)(user1)
