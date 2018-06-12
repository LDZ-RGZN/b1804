class Father(object):
    def kaiche(self):
        print ('老司机')

class son (Father):
    def kaiche(self,name):
        if name == '好朋友':
            Father.kaiche(self)
        else:
            print ('我是一个赛车手')

s = son()
s.kaiche('好朋友')
