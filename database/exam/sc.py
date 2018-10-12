from redis import *
#sr = StrictRedis(host='localhost',port=6379,db=0)
sr = StrictRedis()
result = sr.set('name','100cxy')
print(result)
