class SweetPotato:
    """这是地瓜种类"""

    #定义初始化方法
    def __init__(self):
      #python解释器会把这个对象作为第一个参数传递给self，所以开发者只需要传递后面的参数即可
    #0~3还表示是生的，超过３表示半生半熟　超过５表示烤熟
        self.cookedLever = 0
        self.cookedStr = '生的'
        self.condliments = [] #这是一个用来储存地瓜配料的列表

    #烤地瓜的方法
    def cook(self,time):
        self.cookedLever += time #def里添加每次都可以进项时间的相加
        if self.cookedLever >= 8:
            self.cookedStr = '烤成炭了'
        elif self.cookedLever >= 5:
            self.cookedStr = '烤好了'
        elif self.cookedLever >= 3:
            self.cookedStr = '半生半熟'
        else:
            self.cookedStr = '生的'

    def __str__(self):
        msg = self.cookedStr + '地瓜'
        if len(self.condliments) > 0:
            msg = msg + '('

            for temp in self.condliments:
                msg = msg + temp + ','
            msg = msg.strip(',')
            msg = msg + ')'
        return msg
    def addCondiments(self,condliments):
        self.condliments.append(condliments)
#________________________________________________
mySweetPotato = SweetPotato()
print('-----有了一个地瓜，还没有烤地瓜-----')
print(mySweetPotato.cookedLever)
print(mySweetPotato.cookedStr)
print(mySweetPotato.condliments)
print('-----接下来进行烤地瓜了-----')
print('-----地瓜已经烤了4分钟了-----')
mySweetPotato.cook(4)
print(mySweetPotato)
print('-----地瓜又烤了3分钟-----')
mySweetPotato.cook(3)
print(mySweetPotato)
print('-----接下来添加番茄酱-----')
mySweetPotato.addCondiments('番茄酱')
print(mySweetPotato)
print('-----地瓜又经过5分钟火烤-----')
mySweetPotato.cook(5)
print(mySweetPotato)
print('-----地瓜接下来添加芥末了-----')
print(mySweetPotato)




ceback (most recent call last):
      File "potatos.py", line 29, in <module>
          std.time(4)
          TypeError: time() missing 1 required positional argument: 'name'

