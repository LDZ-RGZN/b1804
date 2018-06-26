class Test(object):
    def __init__(self):
        self.switch = 'open'
    def tr(self,a,b):
        try:
            print (a/b)
        except Exception as rt:
            if self.switch is 'open':

