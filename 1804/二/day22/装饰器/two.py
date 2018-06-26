def wl(func):  #闭包
    def inner(user,passwd):
        if user == 123 and passwd == 123:
            print ('登录成功')
            func()
        else:
            print ('输入错误')
    return inner

@wl
def f1():
    print ('欢迎使用f1...')

@wl
def f2():
    print ('欢迎使用f2...')

@wl
def f3():
    print ('欢迎使用f3...')

@wl
def f4():
    print ('欢迎使用f4...')

user = int(input('请输入账户:'))
passwd = int(input('请输入密码:'))
f1 (user,passwd)
