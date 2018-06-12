#python对于文件夹的操作
import os

#创建文件夹
#os.mkdir()  #当前路径下创建文件夹

#os.mkdir('../xl')  #相对或绝对路径下,创建文件夹

#pwd 获取当前路径
p = os.getcwd()
print (p)


# 修改默认路径 change
'''
os.chdir('./LH')
print (os.getcwd())
f = open ('1.txt','w')
os.mkdir ('xhh')
'''
'''
# 删除文件夹
os.chdir('./LH')
os.rmdir('xhh')
'''
#当文件夹空的时候,可以用 os.rmdir 删除
#当文件夹不空的时候,用以下方法删除
#import shutil
#shutil.rmtree('LH')



os.mkdir('备份系统')
