#1.获取用户要复制的文件
old_file_name = input('请输入要复制的文件名:')

#2.打开要复制的文件
old_file = open(old_file_name,'r')

#源文件--->新文件[复制].py
#rfind返回的是下标
position = old_file_name.rfind('.')
new_file_name = old_file_name[:position] + '[复制]' + old_file_name[:position:]

#new_file_name = '[复制]'+old_file_name
#new_file = open('gebi_laowang.txt','w')

new_file




























