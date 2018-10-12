import re
'''
#*________________________________________________
ret = re.match('[A-Za-z][a-z]*','A').group()
print(ret)
print('*'*50)

ret = re.match('[A-Za-z][a-z]*','AbbA').group()
print(ret)
print('*'*50)

ret = re.match('[A-Za-z][a-z]*','aadfa').group()
print(ret)
print('*'*50)
'''

#+的使用___________________________________________

names = ["name1","_name2","2_name","__name__"]

for name in names:
    ret = re.match('[a-zA-Z_]+[\w]*',name)
    if ret:
        print('变量名%s符合要求'%ret.group())
    else:
        print('变量名%s非法'%name)
    print('*'*50)















