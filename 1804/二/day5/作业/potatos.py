class Potatos:
    '''土豆丝的加工过成'''
    def __init__(self):
        self.name = '生的'
        self.lever = 0
        self.seasoning = []
#________________________________________________________________
    def time(self,t):
        self.lever += t
        if self.lever >= 8:
            self.name = '炒糊了的'
        elif self.lever >= 6:
            self.name = '炒的有点焦的'
        elif self.lever >= 5:
            self.name = '新鲜美味的'
        else :
            self.name = '还没有做熟的'
    def __str__(self):
        msg = self.name + '土豆丝'
        if len(self.seasoning) > 0:
            msg = msg + '('

            for temp in self.seasoning:
                msg = msg + temp + ','
            msg = msg.strip(',')
            msg = msg + ')'
        return msg
    def addseasoning(self,seasoning):
        self.seasoning.append(seasoning)
#_________________________________________________
tds = Potatos()
print ('-----有了一个土豆-----')
print ('---让我们先把土豆切丝---')
print ('土豆丝的状态')
print (tds.name)
print (tds.lever)
print (tds.seasoning)
print ('---接下来把土豆丝放进锅里---')
print ('－－－土豆丝抄了３分钟－－－')
tds.time(3)
print (tds)
print ('---土豆丝又炒了2分钟---')
tds.time(2)
print (tds)
print ('-----接接添加点醋-----')
tds.addseasoning('醋')
print(tds)
print ('---土豆丝又炒了5分钟---')
tds.time(5)
print(tds)
print ('---再来加点辣椒---')
tds.addseasoning('辣椒')
print(tds)




















