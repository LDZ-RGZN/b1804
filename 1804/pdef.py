def jie_shao():
    print ('~'*50)
    print ('========== 欢迎使用易支付网络银行 ==========')
    print ('感谢您选择易支付交易平台，我们将为您提供最优质的服务')
    print ('~'*50)
    print ('登录（1）                              注册（2）')
#______________________________________________________________

list_n = []
def dd():
    account = ""
    if len(list_n) > 0 :
        for dic in list_n:
            account = dic['账户']
    return account
def mm():
    b = ""
    if len(list_n) > 0:
        for dic in list_n:
            b = dic['密码']
    return b
#_______________________________________________________________
#账户登录
def login():
    s = dd()
    h = mm()
    account = int(input('请输入您的账户:'))
    for i in range(1,4):
        while account != s:
            print ('您输入的账户有误')
            account = int(input('请输入您的账户:'))
            break
        if account == s:
            print ('账户正确')
            passwd = int(input('请您输入密码:'))
            if passwd == h:
                print('登录成功')
                break
            else:
                print('密码错误')

#______________________________________________________________


def create2():
    account = int (input('请输入您要创建的新账户:'))
    passwd = int (input('请输入密码:'))
    int (input('请确认密码:'))
    dic = {'账户':account,'密码':passwd}
    list_n.append(dic)
    print ('您的新账号是：',account)
    print ('您的新密码是：',passwd)
#_______________________________________________________________
#主菜单介绍
def home():
    print ('*'*50)
    print ('存取款转账业务请按1')
    print ('理财产品业务请按2')
    print ('吃喝玩乐请按3')
    print ('交通出行请按4')
    print ('想要退出本平台请按5')
#_______________________________________________________________
#存取款业务
def one():
    print ('*'*50)
    print ('您好，欢迎您使用存取转账业务')
    money = input ('请问您想要存款还是转账:')
    if money == '存款':
        mon = float (input ('请输入您要存款的金额：'))
        print ('您的%2f人民币以存入您的账户中，感谢您的使用'%mon)
    elif money == '转账':
        accounts = float (input('请输入您要转账的金额：'))
        account = input ('请输入您要转入的账户：')
        print ('您以成功的向%s账户转入%2f人民币'%(account,accounts))
#________________________________________________________________
#理财产品
def two():
    while True:
        print ('*'*50)
        print ('您好，欢迎您使用理财产品业务')
        print ('请选择您要购买的理财产品')
        print ('1.易付一号，每份300元')
        print ('2.北京医药，每份400元')
        print ('3.财富神州，每份1000元')
        print ('4.易欣科技，每份5000元')
        print ('5.退出')
        print ('~'*50)
        manage = int(input('请输入您想要购买产品的序列号'))
        if manage == 1:
            yifu = int(input('欢迎您购买易付一号理财产品，本产品每份300元，请输入您要购买的份数：'))
            mon1 = yifu*300
            print ('恭喜您购买成功，本次消费金额是%2f人民币'%mon1)
        elif manage == 2:
            beijin = int(input('欢迎您购买北京医药理财产品，本产品每份400元，请输入您要购买的份数：'))
            mon2 = beijin*400
            print ('恭喜您购买成功，本次消费金额是%2f人民币'%mon2)
        elif manage == 3:
            sz = int(input('欢迎您购买财富神州理财产品，本产品每份1000元，请输入您要购买的份数：'))
            mon3 = sz*1000
            print ('恭喜您购买成功，本次消费金额是%2f人民币'%mon3)
        elif manage == 4:
            yx = int(input('欢迎您购买易欣科技理财产品，本产品每份5000元，请输入您要购买的份数：'))
            mon4 = yx*5000
            print ('恭喜您购买成功，本次消费金额是%2f人民币'%mon4)
        elif manage == 5:
            print ('您以经回到主界面')
            break
        else:
            print ('您输入的有误，没有此产品')

#___________________________________________________________________
#吃喝玩乐
def play():
    while True:
        print ('-'*50)
        print ('易玩欢迎您的使用')
        print ('以下是我们为您提供的吃喝玩乐服务：')
        print ('1.美食')
        print ('2.休闲娱乐')
        print ('3.酒店')
        print ('4.美容，美发')
        print ('退出请按888')
        py = int (input('请输入您需要服务的序列好：'))
        if py == 888:
            print ('您已经回到了主界面')
            break
        elif py == 1:
            print ('*'*50)
            print ('您好，欢迎光临易餐厅')
            print ('以下是本餐厅的美食，希望您可以喜欢')
            print ('鱼香肉丝(10元/份)')
            print ('糖醋排骨(10元/份)')
            print ('红烧肉(15元/份)')
            print ('水煮鱼(15元/份)')
            print ('土豆泥(15元/份)')
            print ('='*50)
            print ('到店就餐请点1   外卖请点2')
            py11 = int (input('请选择您需要的服务：'))
            if py11 == 1:
                py12 = input('请问您要吃什么:')
                if (py12 == '鱼香肉丝') or (py12 == '糖醋排骨') :
                    print ('您预定的是%s,应付金额是10元'%py12)
                    p1 = input ('请确认付款：')
                    if p1 == '确认':
                        print ('请您在下单后1小时内准时到餐厅就餐，如因您延迟造成的损失本店概不负责')
                    elif p1 == '否':
                        print ('看来您还是不饿')
                elif (py12 == '红烧肉') or (py12 == '水煮鱼') or (py12 == '土豆泥'):
                    print ('您预订的是%s,应付金额是15元'%py12)
                    p2 = input ('请确认付款：')
                    if p2 == '确认':
                        print ('请您在下单后1小时内准时到餐厅就餐，如因您延迟造成的损失本店概不负责')
                    elif p2 == '否':
                        print ('看来您还是不饿')
            elif py11 == 2:
                py13 = input('请输入您的所在的地址：')
                py14 = input('请问您想吃点什么：')
                if (py14 == '鱼香肉丝') or (py14 == '糖醋排骨') :
                    py3 = input ('您的外卖是10元，请确认付款：')
                    if py3 == '确认':
                        print ('您的外卖%s，正在向您(%s)的地方飞奔过去，请您耐心等待'%(py14,py13))
                        print ('温馨提示：请您务必在您填写的地址等待，如因您的单方面为题造成的损失请您自己负责')
                    elif py3 == '否':
                        print ('看来您还是不饿呀！')
                elif (py14 == '红烧肉') or (py14 == '水煮鱼') or (py14 == '土豆泥'):
                    py4 = input ('您的外卖是15元，请确认付款：')
                    if py4 == '确认':
                        print ('您的外卖%s，正在向您(%s)的地方飞奔过去，请您耐心等待'%(py14,py13))
                        print ('温馨提示：请您务必在您填写的地址等待，如因您的单方面为题造成的损失请您自己负责')
                    elif py4 == '否':
                        print ('看来您还是不饿呀！')
        elif py == 2:
            print ('*'*50)
            print ('您好，以下是我们为您提供的服务')
            print ('1.逛公园')
            print ('2.KTV')
            print ('3.酒吧')
            print ('4.运动健身')
            py21 = input ('请输入您需要的服务：')
            py22 = input ('请输入您现在所在的位置：')
            if py21 == '逛公园' or 'KTV' or '酒吧' or '运动健康':
               py23 = input ('请问要去那个%s：'%py21)
               print ('您现在%s位置，请稍等，我们将派出租车去接您。'%py22)
               print ('到达的指定位置的%s%s'%(py23,py21))
        elif py == 3:
            print ('*'*50)
            y1 = '标准单人间'
            y2 = '标准双人间'
            y3 = '情侣双人间'
            y4 = '豪华总统间'
            print ('我们易付联合酒店您提供易下套房供您选择')
            print ('1.%s,300元每间'%y1)
            print ('2.%s,500元每间'%y2)
            print ('3.%s,800元每间'%y3)
            print ('4.%s,1000元每间'%y4)
            py31 = int(input('请输入您需要居住的房间编号:'))
            if py31 == 1 :
                print('欢迎您选择联合酒店,您订购是%s'%y1)
                py331 = input('请确认付款300元')
                if py331 == '确认':
                    print ('欢迎您入住联合酒店,祝您旅行愉快')
                else :
                    print ('很遗憾,您抛弃了我')
            elif py31 == 2 :
                print('欢迎您选择联合酒店,您订购是%s'%y2)
                py332 = input('请确认付款500元')
                if py332 == '确认':
                    print ('欢迎您入住联合酒店,祝您旅行愉快')
                else :
                    print ('很遗憾,您抛弃了我')
            elif py31 == 3 :
                print('欢迎您选择联合酒店,您订购是%s'%y3)
                py333 = input('请确认付款800元')
                if py333 == '确认':
                    print ('欢迎您入住联合酒店,祝您旅行愉快')
                else :
                    print ('很遗憾,您抛弃了我')
            elif py31 == 4:
                print('欢迎您选择联合酒店,您订购是%s'%y4)
                py334 = input('请确认付款1000元')
                if py334 == '确认':
                    print ('欢迎您入住联合酒店,祝您旅行愉快')
                else :
                    print ('很遗憾,您抛弃了我')
#_______________________________________________________________
#交通出行
def bus():
    import random
    while True:
        print ('*'*50)
        print ('你好')
        print ('我们为您提供了以下几种交通选择')
        print ('公共汽车(1)----------出租车(2)')
        print ('退出本次操作请按888')
        b1 = int (input('请输入您需要的出行工具编号'))
        if b1 == 1:
            print ('*'*50)
            print ('欢迎选择公共出行,低碳环保从我做起')
            b11 = input ('请问您要去那?')
            b12 = random.randint(0,20)
            print ('我们已经查询了您的要去的地址%s'%b11)
            print ('请您去做%d公共汽车到达目的地'%b12)
        elif b1 == 2:
            print ('*'*50)
            b21 = input('请输入您现在的位置:')
            b22 = input('请问您要到哪:')
            b23 = random.randint(0000,9999)
            print ('订单:%s到%s'%(b21,b22))
            print ('请您稍等,正在为您安排司机')
            print ('司机正在向您飞奔过去,车牌号是京%d'%b23)
        elif b1 == 888:
            print('欢迎下次使用')
            break
#______________________________________________________________
