class Woman(object):
    __instance = None
    def __init__(self,name):
        self.name = name

    def __new__(cls,*k):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

n1 = Woman('小丽')
print (n1.name)

n2 = Woman('小红')
print (n2.name)


