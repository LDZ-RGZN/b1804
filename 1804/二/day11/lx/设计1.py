class MusicPlayer(object):
    #定义类属性记录单例对象
    instance = None

    def __new__(cls,*args,**kwargs):

        #1 判断类属性是否已经
