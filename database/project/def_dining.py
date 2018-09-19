from pymysql import *
import time
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
    print('打印订单结算额:6')
    print('退出本次操作请按:7')
    print('='*50)

def one():
    print('='*50)
    print('查询全部请按:1')
    print('查询全部菜品请按:2')
    print('查询指定菜品以及单价请按:3')
    print('='*50)

#获取数据库
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

def main():
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
            break























if __name__ == '__main__':
    main()






























































































