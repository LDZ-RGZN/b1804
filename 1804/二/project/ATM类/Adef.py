#coding=utf-8
import time
def introduce():
    print ('='*50)
    print ('        欢迎使用东丽ATM存取款一体机')
    print ('='*50)
#______________________________________________
def home():
    print ('在您开始操作之前请确保您的周围没有小偷')
    print ('*'*50)
    print ('请选择服务')
    print ('1.插卡')
    print ('2.存款')
    print ('3.取款')
    print ('4.查询余额')
    print ('5.退卡')
    print ('*'*50)
#______________________________________________
def home2():
    print ('在您开始操作之前请确保您的周围没有小偷')
    print ('*'*50)
    print ('请选择服务')
    print ('1.存款')
    print ('2.取款')
    print ('3.查询余额')
    print ('4.退卡')
    print ('*'*50)
#________________________________________________
def login():
    for i in list_user:
        b = i['密码']
    while True:
        user = int(input('请输入选项:'))
        if user is 1:
            c = 3
            while c > 0:
                passwd = int(input('请输入密码'))
                if passwd is b:
                    print ('登录完成')
                    whole()
                    break
                elif passwd != b:
                    print ('密码错误,还有%d次机会'%c)
                    c -= 1
            break
        elif user != 1:
            print ('请先登录')

#创建新的账户______________________________________________
def account():
    import random
    import time
    name = input('请输入您的姓名')
    card = int (input('请输入您的身份证号:'))
    account = random.randint(000000000000,999999999999)
    print ('正在为您办理银行卡')
    print ('请稍等...')
    time.sleep(2)
    print ('您的卡号是%d,请妥善保管'%account)
    print ('接下来请设置您的账户密码')
    print ('只能输入6为数字密码')
    passwd = int (input('请输入您的新密码:'))
    int (input('请确认密码:'))
    dic_ur = {'姓名':name,'身份证号':card, '账户':account,'密码':passwd,'账户余额':0}
    list_user.append(dic_ur)
    print (list_user)
    print ('正在保存用户信息,请稍等...')
    time.sleep(2)
    print ('银行卡已创建成功')

#存款____________________________________________________
list_user = []
def fund():
    count = 4
    while count >= 0:
        print ('温馨提示,此机器只能存100纸币')
        ne = input ('请输入您插入卡片的姓名:')
        ck = int (input('请输入您要存款的金额'))
        for i in list_user :
            if ne == i['姓名']:
                print ('系统正在处理,请稍后...')
                time.sleep(0.2)
                a = i['账户余额']
                b = a+ck
                i['账户余额'] = b
                print ('交易成功')
                break
            elif ne != i['姓名']:
                count -= 1
                print ('查无此人')
                print ('您还有%d次机会'%count)
                continue
        us2 = input ('请问是否打印账单:')

        if us2 == '是':
            print ('*'*50)
            for l in list_user:
                if ne == l['姓名']:
                    print ('交易账户:%d'%l['账户'])
                    print ('交易金额是:%d元'%ck)
                    print ('原账户金额是%d元'%a)
                    print ('账户余额是:%d元'%l['账户余额'])
                    print ('*'*50)
        else:
            continue
        us3 = input ('请问还要继续存款吗:')
        print ('*'*50)
        if us3 == '是':
            print ('正在跳转,请稍后...')
            time.sleep(2)
            continue
        elif us3 == '否':
            print ('正在返回主菜单,请稍后...')
            time.sleep(2)
            break

#取款_________________________________________________
def fetch():
    dic_variate = {'q1':300,'q2':500,'q3':800,'q4':1000,'q5':2000,'q6':5000}

    #账户总金额的变量_____________
    ne2 = input ('请输入您要取款的用户名')
    for x in list_user:
        if ne2 == x['姓名']:
            get3 = x['账户余额']
    #_____________________________
    print('*'*50)
    print('(q1)300元                (q2)500元')
    print('(q3)800元                (q4)1000元')
    print('(q5)2000元               (q6)5000元')
    print('请选择要取款的金额')
    get1 = input('请输入需要取款的金额编号:')
    get2 = input ('请确认取款:')
    if get2 == '确认':
        if get3 >= dic_variate[get1]:
            get4 = get3 - dic_variate[get1]
            x['账户余额'] = get4
            print ('系统正在执行,请稍后...')
            time.sleep(2)
            print ('交易成功,交易金额%s人民币'%dic_variate[get1])
            print ('账户余额:')
            print ('%d人民币'%get4)
            print ('系统正在返回主菜单,请稍后...')
            time.sleep(2)
        elif get3 < dic_variate[get1]:
            print ('您的余额不足,无法取款')
#查看_________________________________________________
def inquire():
    u1 = input('请输入用户名:')
    print ('*'*50)
    for i in list_user:
        if u1 == i['姓名']:
            for x,y in i.items():
                print (x,y)
    print ('*'*50)

#要执行的全局________________________________________
def whole():
    while True:
        home2()
        user = int (input('请输入你要办理的业务:'))
        if user == 1:
            fund()
        elif user == 2:
            fetch()
        elif user == 3:
            inquire()
        elif user == 4:
            break
#___________________________
def ac():
    a = ''
    for i in list_user:
        a = i['账户']
    return a
#__________________________e_












