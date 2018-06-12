#1.获取用户要复制的文件名
user = input ('请输入要复制的文件名:')

#2.打开要复制的文件
old_file = open (user,'r')

#3.新建一个文件
new_file = open ('新文件.txt','w')

#4.从旧文件中读取数据,并写入新的文件中
content = old_file.read()
new_file.write(content)

#5.关闭2个文件
old_file.close()
new_file.close()
