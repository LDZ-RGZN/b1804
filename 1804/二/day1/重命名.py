import os
def re(name,name2):
    os.rename(name,name2)
def rv(name3):
    os.remove(name3)


print ('~'*50)
print ('重命名点1')
print ('删除点2')
print ('~'*50)
while True:
    user = int (input ('请选择:'))
    if user == 1:
        a = input ('请输入要重命名的文件:')
        b = input ('请输入新文件名称')
        re (a,b)
        print ('操作完成')
    elif user == 2:
        c = input ('请输入要删除的文件名:')
        rv (c)
    d = input ('是否还要继续:')
    if d == '是':
        continue
    elif d  == '否':
        break
