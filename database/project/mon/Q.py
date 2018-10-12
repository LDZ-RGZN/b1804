from pymongo import *
def select():
    try:
        #创建链接对象
        client = MongoClient(host='localhost',port=27017)
        #获取数据库
        db = client.王者荣耀
        res = db.wzry.find_one({'age':{'$gte':3}})
        print(res)
        res = db.wzry.find({'age':{'$gte':3}})
        for i in res:
            print(i)

    except Exception as e:
        print(e)

select()
