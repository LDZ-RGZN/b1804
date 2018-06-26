#题目:判断1~101之间有多少个素数,并输出所有素数
for i in range(2,101):
    fg = 0
    for j in range(2,i):
        if i%j == 0:
            fg = 1
            break
    if fg == 0:
        print (i)
