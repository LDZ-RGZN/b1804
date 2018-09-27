from pymysql import *
import time,random
#基本信息____________________________________________
def home():
    print('='*50)
    print('             欢迎使用茯苓餐厅管理系统')
    print('='*50)

def letter():
    print('='*50)
    print('查询菜单请按:1')
    print('添加新菜品请按:2')
    print('删除菜品请按:3')
    print('修改菜品名称即价格请按:4')
    print('点餐餐请按:5')
    print('打印订单结算额请按:6')
    print('查询会员用户请按:7')
    print('账户设置请按:8')
<<<<<<< HEAD
    print('外卖订单请按:9')
    print('退出本次操作请按:10')
=======
    print('退出本次操作请按:9')
>>>>>>> 9ad448752fe66d0d2b8c6422ca860a397008780c
    print('='*50)

def one():
    print('='*50)
    print('查询全部请按:1')
    print('查询全部菜品请按:2')
    print('查询指定菜品以及单价请按:3')
    print('='*50)

def set():
    print('登录账户请按:1')
    print('注册账户请按:2')
    print('='*50)

def set_s():
    print('切换账户请按:1')
    print('注册账户请按:2')
    print('='*50)

#获取数据库___________________________________________
def link():
    conn = connect(host='localhost',port=3306,database='dining',user='root',password='150136',charset='utf8')
    cs1 = conn.cursor()

    return [cs1,conn]
#关闭结束数据库
def close(sc1,conn):
    conn.commit()
    sc1.close()
    conn.close()
#功能函数_____________________________________________
def menu():
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('select * from menu')
    result = cs1.fetchall()
    for i in range(count):
        print(result[i])
    '''
    for i in range(count):
        result = cs1.fetchone()
        print(result)

    '''
    close(cs1,conn)
def menu1():
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('select class,GROUP_CONCAT(name) from menu group by class')
    for i in range(count):
        result = cs1.fetchone()
        print(result,end='\t')
        print('*'*50)
    close(cs1,conn)

def menu2(CP):
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('select * from menu WHERE mid=%d'%CP)
    print(cs1.fetchone())
    close(cs1,conn)

def insert(cls,name,price):
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('insert into menu(class,name,price) values("%s","%s",%d)'%(cls,name,price))
    close(cs1,conn)

def delete(SC):
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('delete from menu where mid = %d'%SC)
    close(cs1,conn)

def update_name(mid,name):
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('update menu set name="%s" where mid=%d'%(name,mid))
    close(cs1,conn)

def update_price(mid,price):
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('update menu set price=%d where mid=%d'%(price,mid))
    close(cs1,conn)

def order_select(oid):
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('select price * (select discount FROM DingDan where oid = %d) from menu me join DingDan di ON di.greens_number = me.mid where di.oid = %d'%(oid,oid))
    result = cs1.fetchone()
    print(result[0])
    close(cs1,conn)

def order(table,greens,uid,discount):
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('insert into DingDan(table_number,greens_number,uid,discount) values(%d,%d,%d,%d)'%(table,greens,uid,discount))
    close(cs1,conn)

def user():
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('select mem.account,user.name,user.gender,user.age,user.address,user.phone  FROM member mem JOIN user  ON mem.uid = user.uid')
    for i in range(count):
        result = cs1.fetchone()
        print(result)
    close(cs1,conn)

def user_one(account):
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('select mem.account,user.name,user.gender,user.age,user.address,user.phone  FROM member mem JOIN user  ON mem.uid = user.uid where mem.account = %d'%account)
    result = cs1.fetchone()
    print(result)
    close(cs1,conn)

<<<<<<< HEAD
def take():
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('SELECT ta.tid,me.name,ta.address,ta.phone FROM take_out ta JOIN menu me ON ta.mid = me.mid')
    result = cs1.fetchall()
    for i in range(count):
        print(result[i])
    close(cs1,conn)

def take_inst(name,address,phone):
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('insert into take_out values(0,%d,"%s",%d)'%(name,address,phone))
    result = cs1.fetchone()
    close(cs1,conn)

def take_one(tid):
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('SELECT ta.tid,me.name,ta.address,ta.phone FROM take_out ta JOIN menu me ON ta.mid = me.mid where tid = %d'%tid)
    result = cs1.fetchone()
    print(result)

=======
>>>>>>> 9ad448752fe66d0d2b8c6422ca860a397008780c

#注册函数______________________________________________
def register(account,password):
    cs1,conn = link()
    cs1 = conn.cursor()
    count = cs1.execute('insert into user_password values(%d,"%s")'%(account,password))
    close(cs1,conn)

def body():
    home()
    while True:
        letter()
        button = int(input('请选择您需要的服务:'))
        if button == 1:
            one()
            button1 = int(input('请选择您需要的服务:'))
            if button1 == 1:
                print('请稍后...')
                time.sleep(1)
                menu()
                print('查询完成')
                time.sleep(0.5)
            elif button1 == 2:
                print('请稍后...')
                time.sleep(1)
                menu1()
                print('查询完成')
                time.sleep(0.5)
            elif button1 == 3:
                CP = int(input('请输入菜品的编号:'))
                print('请稍后...')
                time.sleep(1)
                menu2(CP)
                print('查询完成')
                print('='*50)
                time.sleep(0.5)
        elif button == 2:
            button2 = input('请输入菜品类型:')
            button2_2 = input('请输入菜品名称:')
            button2_3 = int(input('请输入菜品单价:'))
            print('请稍后...')
            time.sleep(1)
            insert(button2,button2_2,button2_3)
            print('添加成功')
        elif button == 3:
            SC = int(input('请输入要删除菜品的编号:'))
            delete(SC)
            print('请稍后...')
            time.sleep(1)
            print('删除成功')
        elif button == 4:
            mid = int(input('请输入要修改的菜品编号:'))
            print('修改名称请按1         修价格称请按2')
            button4 = int(input('请先选择服务'))
            if button4 == 1:
                name = input('请输入菜品的新名称:')
                update_name(mid,name)
                print('请稍后...')
                time.sleep(1)
                print('菜名跟新成功')
            elif button4 == 2:
                price = int(input('请输入新价格:'))
                update_price(mid,price)
                print('请稍后...')
                time.sleep(1)
                print('价格跟新成功')
        elif button == 5:
            table = int(input('请输入桌号:'))
            greens = int(input('请输入菜品编号:'))
            uid = int(input('请输入用户编号:'))
            discount = int(input('请输入折扣/1为不打折:'))
            print('请稍后...')
            time.sleep(1)
            order(table,greens,uid,discount)
            print('订单打印成功')
        elif button == 6:
            table = int(input('请输入需要计算金额的桌号:'))
            print('请稍后...')
            time.sleep(1)
            order_select(table)
            print('金额打印成功')
        elif button == 7:
            print('查询全部用户信息:1')
            print('查询指定用户信息:2')
            button7 = int(input('请选择您需要的服务:'))
            if button7 == 1:
                print('请稍后...')
                time.sleep(1)
                user()
                print('查询成功')
            elif button7 == 2:
                print('请稍后...')
                time.sleep(1)
                account = int(input('请输入会员号:'))
                user_one(account)
                print('查询成功')
        elif button == 8:
            set_s()
            button8 = int(input('请输入您需要的服务'))
            if button8 == 1:
                swi()
            elif button8 == 2:
                print('正在随机账户,请稍后...')
                account = random.randint(0000000000,9999999999)
                time.sleep(1)
                print('账户随机完成,正在打印...')
                print('您的账户是%d,请妥善保管'%account)
                a = 4
                while a > 0:
                    password = input('请输新入密码')
                    password2 = input('请再次输入输入密码')
                    if password == password2:
                        print('正在保存,请稍等...')
                        time.sleep(1)
                        register(account,password)
                        print('保存成功,即将跳回主菜单')
                        time.sleep(0.5)
                        break
                    elif password != password2:
                        print('两次输入的密码不正确,请重新输入')
                        a -= 1
                        if a > 0:
                            print('含有%d次机会'%a)
                        else:
                            print('您已经没有机会了,请重新获取账户')
        elif button == 9:
<<<<<<< HEAD
            print('添加订单请按:1')
            print('查看所有订单请按:2')
            print('查看指定订单请按:3')
            button9 = int(input('选择服务号:'))
            if button9 == 1:
                name = int(input('请输入菜品号:'))
                address = input('请输入外卖地址:')
                phone = int(input('请输入联系电话:'))
                print('正在保存,请稍等...')
                time.sleep(1)
                take_inst(name,address,phone)
            elif button9 == 2:
                print('正在查询,请稍等...')
                time.sleep(1)
                take()
            elif button9 == 3:
                tid = int(input('请输入订单号:'))
                print('正在查询,请稍等...')
                time.sleep(1)
                take_one(tid)
        elif button == 10:
            break
        else:
            print('输入有误')
=======
>>>>>>> 9ad448752fe66d0d2b8c6422ca860a397008780c
            break

#切换函数______________________________________________
def swi():
    cs1,conn = link()
    cs1 = conn.cursor()
    a = 4
    while a > 0:
        account = int(input('请输入您的账户:'))
        print('正在验证...')
        time.sleep(0.5)
        count_u = cs1.execute('select account from user_password where account={}'.format(account))

        if count_u == 1:
            print('ok')
            b = 4
            while b > 0:
                a = cs1.fetchone()
                password = input('请输入您的密码:')
                print('正在验证...')
                time.sleep(0.5)
                count_p = cs1.execute('select password from user_password where password="{}"'.format(password))
                c = cs1.fetchone()
                print(count_p)
                if count_p >= 1:
                    if password == c[0]:
                        print('成功登录')
                        break
                else:
                    print('登录失败')
                    b -= 1
                    if b > 0:
                        print('含有%d次机会'%b)
                    else:
                        print('您已经没有机会了')

            break
        else:
            print('账户有误')
            a -= 1
            if a > 0:
                print('含有%d次机会'%a)
            else:
                print('您已经没有机会了')

    close(cs1,conn)

#主体______________________________________________
def main():
    cs1,conn = link()
    cs1 = conn.cursor()
    a = 4
    while a > 0:
        account = int(input('请输入您的账户:'))
        print('正在验证...')
        time.sleep(0.5)
        count_u = cs1.execute('select account from user_password where account={}'.format(account))

        if count_u == 1:
            print('ok')
            b = 4
            while b > 0:
                a = cs1.fetchone()
                password = input('请输入您的密码:')
                print('正在验证...')
                time.sleep(0.5)
                count_p = cs1.execute('select password from user_password where password="{}"'.format(password))
                c = cs1.fetchone()
                print(count_p)
                if count_p >= 1:
                    if password == c[0]:
                        print('成功登录')
                        body()
                        break
                else:
                    print('登录失败')
                    b -= 1
                    if b > 0:
                        print('含有%d次机会'%b)
                    else:
                        print('您已经没有机会了')

<<<<<<< HEAD
            break
        else:
            print('账户有误')
            a -= 1
            if a > 0:
                print('含有%d次机会'%a)
            else:
                print('您已经没有机会了')

=======
#切换函数______________________________________________
def swi():
    cs1,conn = link()
    cs1 = conn.cursor()
    a = 4
    while a > 0:
        account = int(input('请输入您的账户:'))
        print('正在验证...')
        time.sleep(0.5)
        count_u = cs1.execute('select account from user_password where account={}'.format(account))

        if count_u == 1:
            print('ok')
            b = 4
            while b > 0:
                a = cs1.fetchone()
                password = input('请输入您的密码:')
                print('正在验证...')
                time.sleep(0.5)
                count_p = cs1.execute('select password from user_password where password="{}"'.format(password))
                c = cs1.fetchone()
                print(count_p)
                if count_p >= 1:
                    if password == c[0]:
                        print('成功登录')
                        break
                else:
                    print('登录失败')
                    b -= 1
                    if b > 0:
                        print('含有%d次机会'%b)
                    else:
                        print('您已经没有机会了')

            break
        else:
            print('账户有误')
            a -= 1
            if a > 0:
                print('含有%d次机会'%a)
            else:
                print('您已经没有机会了')

    close(cs1,conn)

#主体______________________________________________
def main():
    cs1,conn = link()
    cs1 = conn.cursor()
    a = 4
    while a > 0:
        account = int(input('请输入您的账户:'))
        print('正在验证...')
        time.sleep(0.5)
        count_u = cs1.execute('select account from user_password where account={}'.format(account))

        if count_u == 1:
            print('ok')
            b = 4
            while b > 0:
                a = cs1.fetchone()
                password = input('请输入您的密码:')
                print('正在验证...')
                time.sleep(0.5)
                count_p = cs1.execute('select password from user_password where password="{}"'.format(password))
                c = cs1.fetchone()
                print(count_p)
                if count_p >= 1:
                    if password == c[0]:
                        print('成功登录')
                        body()
                        break
                else:
                    print('登录失败')
                    b -= 1
                    if b > 0:
                        print('含有%d次机会'%b)
                    else:
                        print('您已经没有机会了')

            break
        else:
            print('账户有误')
            a -= 1
            if a > 0:
                print('含有%d次机会'%a)
            else:
                print('您已经没有机会了')

>>>>>>> 9ad448752fe66d0d2b8c6422ca860a397008780c
    close(cs1,conn)


if __name__ == '__main__':
    main()




























































































