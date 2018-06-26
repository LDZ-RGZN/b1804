class single_instance(object):
    __instance = None
    def __init__(self):
        pass
    def __new__(cls,*k):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance
a = single_instance()
b = single_instance()
print (id(a))
print (id(b))

