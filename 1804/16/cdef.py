#旗舰版
def home():
    print ('》》》》》LX名片管理系统《《《《《')
    print (' 请在下列列表中选择您要操作的对象 ')
    print ('新建名片请按 1')
    print ('查询名片请按 2')
    print ('显示全部请按 3')
    print ('修改名片请按 4')
    print ('删除名片请按 5')
    print ('退出本次系统请按 888')
    print ('^'*50)
#_____________________________________________________
def newcard(u):
    print('*'*50)
    print('×'*50)
    print('开始创建名片')
    name = input ('请输入您的姓名：')
    com = input ('请输入公司名称：')
    phone = int(input ('请输入手机号：'))
    dic = {'姓名':name,'公司':com,'手机号':phone}
    u.append(dic)
    print (u)
    print ('名片保存成功，姓名是：%s' % dic['姓名'])
    print ('名片保存成功，公司是：%s' % dic['公司'])
    print ('名片保存成功，电话是：%d' % dic['手机号'])
    return u
#_____________________________________________________
def twocard():
    print ('以下是目前创建的所以名片')
    print (list_card)

#_____________________________________________________
def opn(p):
    p -= 1
    if p != 0:
        print ('您还有%d名片没有打印'%p)
    elif p == 0:
        print ('您的名片已经打印完成')

    return p
#_____________________________________________________
def dic(o):
    print ('欢迎您使用名片查询系统')
    print ('退出请按888')
    namesys = input('请输入您要查询的名字：')
    for dic in o :
        if namesys == dic['姓名']:
            print('|'*80)
            print('姓名：%s'%dic['姓名'])
            print('公司：%s'%dic['公司'])
            print('手机号：%s'%dic['手机号'])
            print('*'*50)
    return o
#_____________________________________________________
def qb(n):
    print('以下是您全部的名片')
    v = 1

    for nu in n:
        print('您的第%d张名片:'%v)
        print(nu)
        v += 1
    return n
#______________________________________________________
def rv(b):
    print('*'*50)
    print(b)
    na1=input('请输入您要删除名片的姓名：')
    for dic in b:
        if na1 == dic['姓名']:
            b.remove(dic)
            print('以下就是您要删除的名片：')
            print(b)
            print('您的名片已经删除完成了')
    return b
#_____________________________________________
def xiu_gai(s):
    print('*'*50)
    print(s)
    nam2=input('请输入您要修改名片的名字')
    for dic in s:
        if nam2 == dic['姓名']:
            dic['姓名']=input('请输入姓名')
            dic['公司']=input('请输入公司')
            dic['手机号']=input('请输入电话')
            print('%s的名片修改成功'%dic['姓名'])
            print(s)
            print('您的名片已经修改完成')







































