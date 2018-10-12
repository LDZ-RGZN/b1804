from pymongo import *
def delete():
    try:
        client = MongoClient(host='localhost',port=27017)
        db = client.demo

        #db.stu.delete_many({'age':188})

        db.stu.delete_many({})
    except Exception as e:
        print(e)

delete()


