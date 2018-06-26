#打开一个已经存在的文件
f = open ('test.txt','r')
content = f.read(3)
print ('读取的内容是:',content)

#查找当前位置
position = f.tell()
print ('当前读取的位置是:',position)

content = f.read(3)
print ('读取的数据是:',content)

#查找当前位置
position = f.tell()
print ('当前读取的位置是:',position)

f.close()
