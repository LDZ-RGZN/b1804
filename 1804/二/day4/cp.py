
def file(user):
    #1.打开源文件:
    old_file = open (user,'r')
    #3.打开一个新的备份文件:
    p = user.rfind('.') #找到文件中.的下标位置
    u1 = user[:p] #截取文件名称
    u2 = user[p:] #截取文件扩展名

    new_file = open (u1+'[复本]'+u2,'w')
    print ('复制成功')
    #4.将内容写入新文件里:
    #2.读取源文件内容:
    while True:
        c = old_file.read(1024)
        new_file.write(c)
        if len(c) == 0:
            break
    #5.关闭打开的文件夹:
    old_file.close()
    new_file.close()

u = input('请输入文件名:')
file(u)



