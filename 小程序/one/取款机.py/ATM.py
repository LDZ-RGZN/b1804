
import Adef
Adef.introduce()
n = 3
while n > 0:
    s = Adef.ac()
    Adef.home()
    user1 = int (input('请选择您需要的服务:'))
    if user1 == 1:
        Adef.account()
    elif user1 == 2:
        user2 = int (input('请插入您的账账号:'))
        passwd = int (input('请输入您的密码:'))
        Adef.ac()
        if user2 == s['账户'] and passwd == s['密码']:
            Adef.whole()
        else:
            print('没有此账户')
            print('请重新登录')
            print('您还有%d次机会'%n)
            n -= 1
            continue
    elif user1 == 6:
        break
    else:
        print ('您还没有登录')
        print ('请登录')
        continue

