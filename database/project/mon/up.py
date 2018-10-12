from pymongo import *

def update():
    try:
        client = MongoClient(host='localhost',port=27017)
        db = client.demo
        #db.stu.update_one({'age':10},{'$set':{'age':88}})
        db.stu.update_many({'age':{'$in':[10,88]}},{'$set':{'age':188}})
    except Exception as e:
        print(e)
update()
