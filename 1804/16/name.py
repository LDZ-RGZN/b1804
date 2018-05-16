list_n=[]
for i in range(0,11):
    n = input ('请输入姓名：')
    list_n.append(n)
print(list_n)
print ('第三位成员的名字是%s'% list_n[3])
print ('第五位成员的名字是%s'% list_n[5])
print ('第八位成员的名字是%s'% list_n[3])
print ('第十位成员的名字是%s'% list_n[10])
list_n.sort()
print ('顺序',list_n)
list_n.sort(reverse=True)
print ('倒序',list_n)
print ('已经弹出最后哪位同学',list_n.pop())
del list_n[8]
print ('已经删除的8个人',list_n)
list_n2=['小明']
list_n.extend(list_n2)
print (list_n)
print('小明同学所在的位置是第',list_n.index('小明'))

