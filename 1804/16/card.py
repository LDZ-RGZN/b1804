#初级版

def home():
    print ('》》》》》LX名片管理系统《《《《《')
    print (' 请在下列列表中选择您要操作的对象 ')
    print ('新建名片请按 1')
    print ('显示全部请按 2')
    print ('查询名片请按 3')
    print ('退出本次系统请按 888')

#_____________________________________________________
def newcard():

    print('×'*50)
    print('开始创建名片')
    name = input ('请输入您的姓名：')
    com = input ('请输入公司名称：')
    phone = int(input ('请输入手机号：'))
    dic = {'姓名':name,'公司':com,'手机号':phone}
    list_card.append(dic)
    print (list_card)
    print ('名片保存成功，姓名是：%s' % dic['姓名'])
    print ('名片保存成功，公司是：%s' % dic['公司'])
    print ('名片保存成功，电话是：%d' % dic['手机号'])

#_____________________________________________________
def twocard():
    print ('以下是目前创建的所以名片')
    print (list_card)

#_____________________________________________________
def opn():
    zhang -= 1
    if zhang != 0:
        print ('您还有%d名片没有打印'%zhang)
    elif zhang == 0:
        print ('您的名片已经打印完成')

#_____________________________________________________
home()
action = int(input('请填写您需要服务的序列号'))
list_card=[]
zhang = int ( input('请问您要新建几张名片:'))
while zhang > 0:
    print ('欢迎您登录新建名片系统')
    if action == 1:
        newcard()
    elif action == 2:
        twocard()
    elif action == 888:
        print ('您已经成功退出')
        break
    else:
        print()
    opn()




























