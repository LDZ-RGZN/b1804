import re
'''
#[]的使用 大小写h都可以的情况
ret = re.match("[hH]","Hello Python").group()
print(ret)
print('*'*50)

#匹配0到9的二种写法
ret = re.match("[0-9]Hello Python","7Hello Python").group()
print(ret)
print("*"*50)

#下面这个正则不能够匹配到数字4,因此ret为None
ret = re.match("[0-35-9]Hello Python","4Hello Python")
print(ret)
print("*"*50)

#使用\d进行匹配
ret = re.match('嫦娥\d号发射成功','嫦娥1号发射成功')
print(ret.group())
'''
#使用\s与\S进行空格和非空格匹配
#\s空白字符  \S非空白字符
ret = re.match('\D娥\d\s\D*',"嫦娥1 号发射成功").group()
print(ret)
print('*'*50)

ret = re.match('\S娥\d\s\S*','嫦娥1 号发射成功').group()
print(ret)
print('*'*50)











































































































