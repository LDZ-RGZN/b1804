class Dictclass(object):
    def __init__(self,dict):
        self.dict = dict
        self.key = None
    def get_dict(self,key):
        print (self.dict)
        self.key = key
        a = self.dict.keys()
        for i in a:                    #如何才能让在没有的情况下只显示一遍
            if self.key == i:
                return self.dict[self.key]
                break
            #return 'not found'

    def del_dict(self,key):
        self.key = key
        a = self.dict.keys()
        for i in a:
            if self.key == i:
                self.dict.pop(self.key)
                break
            #else:
            #    return 'no that key'
    def get_key(self):
        return self.dict.keys()
    def update_dict(self,dict2):
        self.dict = dict(self.dict,**dict2)
        return self.dict.values()
a = Dictclass({'a':1,'b':2})
print (a.get_dict('b'))
print (a.del_dict('a'))
print (a.get_key())
print (a.update_dict({'c':3,'d':4}))
