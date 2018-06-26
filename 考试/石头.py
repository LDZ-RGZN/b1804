#1.石头  2.剪刀 3.布
import random
pc = random.randint(1,3)
user = int (input('请输入1.石头,2.剪刀,3.布'))
if (user == 1 and pc == 2) or (user == 2 and pc == 3) or (user == 3 and pc ==1):
    print ('恭喜你赢了')
elif user == pc:
    print ('真巧呀,平局了')
else :
    print ('电脑赢了')

