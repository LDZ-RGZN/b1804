import xxx

xxx.create2()

def login():
    s=xxx.dd()
    h=xxx.mm()
    for i in range(1,4):
        user =int(input("账户"))
        while user != s:
            print("账户错误")
            break
        if user == s:
            print("正确")
            user1 = int(input("密码"))
            if user1==h:
                print("你牛逼")
                break
            else:
                print("sb")


login()
