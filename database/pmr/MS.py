from pymysql import *
from pymongo import *
from redis import *

def main():
    '''
    conn = connect(host='localhost',port=3306,database='EKD',user='root',password='150136',charset='utf8')
    cs1 = conn.cursor()

    count = cs1.execute('insert into zhaozhao_comic(name,zone) values("我爱罗","风之国"),("奇拉比","雷之国")')
    print('共有%d行受影响!'%count)
    count = cs1.execute('insert into zhaozhao_comic values(0,"奥特曼","M78星云")')
    print('共有%d行受影响!'%count)
    conn.commit()

    count = cs1.execute('update zhaozhao_comic set name="赛罗奥特曼" where name = "奥特曼"')
    print('共有%d行受影响!'%count)
    conn.commit()

    count = cs1.execute('select * from zhaozhao_comic where id > 0')
    print('共查询%d行数据'%count)
    for i in range(count):
        result = cs1.fetchone()
        print ("第%d次查到的数据为%s:"%(i+1, result))
    cs1.close()
    conn.close()
    client = MongoClient(host = 'localhost',port = 27017)

    db = client.python
    db.stu.insert_one({'name':'佐助','gender':'男'})
    db.stu.insert_one({'name':'春野樱','gender':'女'})
    db.stu.insert_one({'name':'蒙奇 D 路飞','gender':'男'})
    db.stu.insert_one({'name':'索隆','gender':'男'})
    db.stu.insert_one({'name':'娜美','gender':'女'})
    result = db.stu.find_one({'name':'索隆'})
    #print(result)
    result = db.stu.find({'gender':'男'})
    #for item in result:
       # print ('%s--%s'%(item['name'],item['gender']))
    #db.stu.update_one({'name':'佐助'},{'$set':{'name':'宁智波佐助'}})
    #db.stu.update_many({'gender':'男'},{'$set':{'gender':'boy'}})
    #db.stu.delete_one({'gender':'男'})
    db.stu.delete_many({'gender':'女'})
    '''
    sr = StrictRedis()

    result = sr.set('name','zhaozhao')
    #print('添加结果:',result)
    #result = sr.get('name')

    #result = sr.set('name','zhaozhaolee')
    result = sr.delete('n2')
    print(result)

if __name__ == '__main__':
    main()





