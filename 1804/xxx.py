
n=[]
def create2():
    account = int (input('请输入您要创建的新账户:'))
    passwd = int (input('请输入密码:'))
    int (input('请确认密码:'))
    dic = {'账户':account,'密码':passwd}
    n.append(dic)
    print ('您的新账号是：',account)
    print ('您的新密码是：',passwd)
def dd():
    user = int(input(""))
    for dic in n:
        a=dic["账户"]

    return a


def mm():
    for dic in n:
        b=dic['密码']
    return b
