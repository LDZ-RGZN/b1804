def su_shu(n):
    a = 0
    for i in range(2,n):
        if n%i == 0:
            a = 1
            print ('非素数')
            break
    if a == 0:
        print ('素数')
n = int (input('请输入数字:'))
su_shu(n)
