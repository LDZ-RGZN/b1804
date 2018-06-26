#某个年份能被4整除但不能被100整除，则是闰年。
#若某个年份能被400整除，则也是闰年


year = int (input('请输入年份:'))
if (year%4 == 0) and (year%100 != 0) or (year%400 == 0):
    print ('%d年是闰年'%year)
else:
    print ('%d不是闰年'%year)

