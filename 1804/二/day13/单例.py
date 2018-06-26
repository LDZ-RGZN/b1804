class Car(object):
    __instance = None
    __init = True
    def __init(self,name):
        if Car.__init is True:
        self.name = name






    def __new__(cls,*k):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

