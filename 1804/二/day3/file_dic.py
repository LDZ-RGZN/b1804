import os
def de(name):
    os.remove(name)
def cr(x,j):
    os.rename(x,j)
    print ('新文件名是%s'%j)
def de2(name2):
    import shutil
    shutil.rmtree(name2)


#_____________________________________
print ('删除请按1   重命名请按2')
user = int (input('请选择:'))
if user == 1:
    print ('文件1     文件夹2')
    user2 = int(input('请选择'))

    if user2 == 1:
        name = input ('请输入要删除的文件名:')
        de(name)
    elif user2 == 2:
        name2 = input ('请输入要删除的文件夹名:')
        de2(name2)




elif user == 2:
    x = input ('请输入旧文件名:')
    j = input ('请输入新文件名:')
    cr(x,j)




