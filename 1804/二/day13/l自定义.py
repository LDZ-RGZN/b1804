class UserError(Exception):    #用户名异常
    def __init__(self,user):
        self.user = user
class PasswdError(Exception):   #密码异常
    def __init__(self,passwd):
        self.passwd = passwd


def yh():
    user = int(input('请输入用户名:'))
    passwd = int(input('请输入密码:'))
    if user != 123456:
        raise UserError('没有此用户')
    elif user == 123456:
        if passwd == 123456:
            print ('登录成功')
        elif passwd != 123456:
            raise PasswdError('用户密码不正确')
try:
    yh()
except Exception as result:
    print (result)
