import pdef

#介绍
pdef.jie_shao()
nam3 = int(input('请输入：'))
if nam3 == 1:
    pdef.login()
elif nam3 == 2:
    pdef.create2()
    pdef.login()
    while True:
        pdef.home()
        number=int(input('请输入您需要办理业务的编号：'))
        if number == 1:
            pdef.one()
        elif number == 2:
            pdef.two()
        elif number == 3:
            pdef.play()
        elif number == 4:
            pdef.bus()
        elif number == 5:
            break

