class MyError(Exception):
    def __init__(self,str_error):
        self.name = str_error

# raise 抛出异常
def get_pwd():
    pwd = input('请输入密码:')
    if len(pwd) < 6:
        raise MyError('密码小于6位不符合要求!!!')

try:
    get_pwd()
except Exception as re:
    print ('遇到了异常:%s'%re)
