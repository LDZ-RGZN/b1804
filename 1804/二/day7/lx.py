class Game:
    def __init__(self,name,passwd):
        self.__name = name
        self.__passwd = passwd
    def __set_msg(self):
        return self.__name,self.__passwd
    def get_msg(self,information):
        if information == '是':
            print ('您的个人信息是' + str(self.__set_msg()))

xx = Game('ldz',123)
xx.get_msg('是')


