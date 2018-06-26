def Year(y,k):
    if y < 2:
        pass
    else:
        for i in range(2,int(y/2)):
            if y%i == 0:
                print ('非素数年')
                k = 1
                break
            else:
                continue
    if k == 0 or y == 2:
        print ('yes')

year = int (input('请输入年份:'))
k = 0
Year(year,k)
print (int(15/2))
