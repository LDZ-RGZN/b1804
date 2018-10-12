from pymongo import *
def insert():
    try:
        client = MongoClient(host='localhost',port=27017)
        db = client.demo
        db.stu.insert_one({'name':'zs','age':10})
        db.stu.insert_many([{'name':1},{'name':2}])
    except Exception as e:
        print(e)
insert()



