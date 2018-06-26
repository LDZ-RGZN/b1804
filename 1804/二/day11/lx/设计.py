class MusicPlayer(object):

    def __new__(cls,*args,**kwargs):
        #如果不返回任何结果
        return super().__new__(cls)

    def __init__(self):
        print ('初始化音乐播放器')

player = MusicPlayer()
print (player)
