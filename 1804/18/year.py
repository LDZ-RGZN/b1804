def rn(year):
    if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
        print ('闰年')
    else:
        print ('平年')
while True:
    year = int(input('请输入年份：'))
    rn(year)
