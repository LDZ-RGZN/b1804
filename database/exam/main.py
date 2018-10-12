#mysql_____________________________
from pymysql import *
conn = connect(host='localhost',port=3306,database='jing_dong',user='root',password='150136',charset='utf8')
cs1 = conn.cursor()

#count = cs1.execute('操作的内容')
count = cs1.execute('select * from goods')
#print(cs1.fetchone())

conn.commit()
cs1.close()
conn.close()



#redis_____________________________
from redis import *
#sr = StrictRedis(host='localhost',port=6379,db=0)
sr = StrictRedis()
result = sr.set('name','100cxy')
#print(result)


#mongodb__________________________
from pymongo import *
client = MongoClient(host='localhost',port=27017)
db = client.demo #demo数据库
'''
db.集合.功能('')

insert_one：加入一条文档对象   insert_many：加入多条文档对象

find_one：查找一条文档对象   find：查找多条文档对象

update_one：更新一条文档对象   update_many：更新多条文档对象

delete_one：删除一条文档对象   delete_many：删除多条文档对对象

'''

#mysql备份__________________________
'''
备份:mysqldump –uroot –p 数据库名 > python.sql

恢复:mysql -uroot –p 新数据库名 < python.sql

'''


#加密_______________________________
import hashlib
user = input('请输入:')

s1 = hashlib.sha1()
s1.update(user.encode('utf8'))
result = s1.hexdigest() #获得加密
print(result)
#解密______________________________








