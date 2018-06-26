class ShowError(Exception):
    '''自定义的异常类'''
    def __init__(self,length,atleast):
        #super.()__init__()
        self.length = length
        self.atleast = atleast

def main():
    try:
        s = input('请输入')
        if len(s) < 3:
            raise ShowError(len(3),3)
    except ShowError as reault: #这个变量被绑定到了错误的实例
        print ('ShowError:输入的长度是%d,长度至少应该是%d'%(result.length,result.atleast))
    else:
        print('没有异常发生')
main()
