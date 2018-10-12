from pymysql import *
from redis import *

conn = connect(host='localhost',port=3306,database='jing_dong',user='root',password='150136',charset='utf8')
cs1 = conn.cursor()

count = cs1.execute('select * from goods')
print(cs1.fetchone())

conn.commit()
cs1.close()
conn.close()

#sr = StrictRedis(host='localhost',port=6379,db=0)
sr = StrictRedis(decode_responses=True)
result = sr.set('name','100cxy')
#print(result)





