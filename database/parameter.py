from pymysql import *

def main():
    find_name = input('请输入物品名称:')

    #创建Connection
    conn = connect(host = 'localhost',
            port = 3306,
            user = 'root',
            database = 'jing_dong',
            password = '150136',
            charset = 'utf8')
    #获得Cursor对象
    cs1 = conn.cursor()
    params = [find_name]

    count = cs1.execute('select * from goods where name=%s',params)
    print(count)
    for i in range(count):
        result = cs1.fetchone()
        print(result)

    cs1.close()
    conn.close()
if __name__ == '__main__':
    main()


















