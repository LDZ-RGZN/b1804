from pymysql import *

def main():
    conn = connect(host='localhost',port=3306,user = 'root',password = '150136',charset = 'utf8',database='jing_dong')
    cs1 = conn.cursor()

    count = cs1.execute('select id,name from goods where id>=4')
    #打印受影响的行数
    print('查询到%d条数据'%count)
    '''
    for i in range(count):
        result = cs1.fetchone()
        print(result)
    '''
    result = cs1.fetchall()
    print(result)
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
