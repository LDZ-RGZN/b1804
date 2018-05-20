#旗舰版
list_card=[]
import cdef
#名片增加
while True:
    cdef.home()
    action = int(input('请填写您需要服务的序列号'))
    if action == 1:
        p = int(input('请问您想新建多少张名片：'))
        while p > 0:
            print ('欢迎您登录新建名片系统')
            if action == 1:
                list_card = cdef.newcard(list_card)
            cdef.opn(p)
            p -= 1
            continue
    #退出
    elif action == 888:
        print ('您已经成功退出')
        break
    #查询
    elif action == 2:
        list_card = cdef.dic(list_card)
    #显示全部
    elif action == 3:
        list_card = cdef.qb(list_card)
    #删除
    elif action == 5:
        list_card = cdef.rv(list_card)
    #修改
    elif action == 4:
        list_card = cdef.xiu_gai(list_card)



















