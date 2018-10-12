import hashlib
from redis import *
from pymysql import *

def mysql_login(account,upwd):
    try:
        conn = connect(host='localhost',port=3306,user='root',password='150136',database='D6',charset='utf8')
        cs1 = conn.cursor()
        r = cs1.execute('select password from user where account="{}"'.format(account))
        a = cs1.fetchone()
        a = a[0]
        print(a)
        if r == None:
            print('请去注册')
        else:
            print('mysql')
            if upwd == a:
                sr = StrictRedis(decode_responses=True)
                sr.set(account,upwd)
                print('登录成功')
                user = input('请选择:')
                if user == '1':
                    record()
                elif user == '2':
                    for i in range(1,7):
                        record_d()
                else:
                    print('密码错误')
            else:
                print('密码错误')
    except Exception as e:
        print(e)

def redis_login():
    account = input('请输入用户名:')
    password = input('请输入密码:')
    s1 = hashlib.sha1()
    s1.update(password.encode('utf8'))
    upwd = s1.hexdigest()
    try:
        sr = StrictRedis(decode_responses=True)
        r = sr.get(account)
        if r == None:
            mysql_login(account,upwd)
        else:
            if upwd == r:
                print('登录成功')
                print('用户[1]      店家[2]')
                user = input('请选择:')
                if user == '1':
                    record()
                elif user == '2':
                    for i in range(1,7):
                        record_d()
                else:
                    print('密码错误')
    except Exception as e:
        print(e)

def register():
    name = input('请输入姓名')
    address = input('请输入地址:')
    age = int(input('请输入年龄:'))
    gender = input('请输入性别:')
    account = input('请输入账户:')
    password = input('请输入密码:')
    s1 = hashlib.sha1()
    s1.update(password.encode('utf8'))
    upwd = s1.hexdigest()
    print(account,upwd)
    try:
        conn = connect(host='localhost',port=3306,user='root',password='150136',database='KS',charset='utf8')
        cs1 = conn.cursor()


        cs1.execute('insert into user(name,address,age,gender,account,password) values("{}","{}",{},"{}","{}","{}")'.format(name,address,age,gender,account,password))
        conn.commit()
        sr = StrictRedis(decode_responses=True)
        sr.set(account,upwd)
    except Exception as e:
        print(e)

def record():
        conn = connect(host='localhost',port=3306,user='root',password='150136',database='KS',charset='utf8')
        cs1 = conn.cursor()
        print('查询自己的订单')
        name = input('请输入姓名:')
        count = cs1.execute('select * from record where uid = (select id from user where name = "%s")'%name)
        for i in range(count):
            a = cs1.fetchone()
            print(a)
        conn.commit()

def record_d():
        conn = connect(host='localhost',port=3306,user='root',password='150136',database='KS',charset='utf8')
        cs1 = conn.cursor()
        print('查看总消费金额:1')
        print('查看平均消费金额:2')
        print('查看最高消费金额:3')
        print('查看最低消费金额:4')
        print('查看指定用户信息:5')
        print('查看指定项目金额:6')
        b = int(input('请选择'))
        if b == 1:
            count = cs1.execute('select sum(money) from record')
            a = cs1.fetchone()
            print(a)
        elif b == 2:
            count = cs1.execute('select avg(money) from record')
            a = cs1.fetchone()
            print(a)
        elif b == 3:
            count = cs1.execute('select max(money) from record')
            a = cs1.fetchone()
            print(a)
        elif b == 4:
            count = cs1.execute('select min(money) from record')
            a = cs1.fetchone()
            print(a)
        elif b == 5:
            name = input('请输入用户姓名:')
            count = cs1.execute('select * from record where uid = (select id from user where name = "%s")'%name)
            for i in range(count):
                a = cs1.fetchone()
                print(a)
        elif b == 6:
            name = input('请输入项目:')
            count = cs1.execute('select sum(money) from record where project = "%s"'%name)
            a = cs1.fetchone()
            print(a)
        conn.commit()



def main():
    print('注册:1')
    print('登录:2')
    a = input('请输入您需要的服务:')
    if a == '1':
        register()
    elif a == '2':
        redis_login()
    else:
        print('输入有误')


if __name__ == '__main__':
    main()



