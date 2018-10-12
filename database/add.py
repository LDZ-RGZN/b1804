from pymysql import *
def main():

    #创建Connection链接
    conn = connect(host='localhost',port=3306,database='jing_dong',user='root',password='150136',charset='utf8')
    #获得Cursor对象
    cs1 = conn.cursor()
    # 执行insert语句，并返回受影响的行数：添加一条数据
    # 增加
    count = cs1.execute('DELETE FROM goods_cates WHERE name = "张伟"')
    print(count)
    #count = cs1.execute('insert into roods_cates(name) values("光盘")')
    #print(count)
    conn.commit()
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()









