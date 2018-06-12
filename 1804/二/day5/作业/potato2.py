import pdef
class Potato:
    def __init__(self,name):
        self.name = name
        self.lever = 0
        self.seasoning = []

    def Name_dic(self,name):
        dic = {'名称':self.name}
        self.seasoning.append(dic)
        print (self.seasoning)
#实物程度的类＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
    def time(self,t):  #这里的ｔ只是一个形参
        self.lever += t   #这里的变量必须跟上面想要保存的变量一样
        if self.lever >= 8:
            n1 = '烤糊的黑' + name
            self.name = n1
            print (self.name)
        elif self.lever >= 6:
            n2 = '烤的有点糊的黄' + name
            self.name = n2
            print (self.name)
        elif self.lever >= 5:
            n3 = '新鲜出炉的上好烤' + name
            self.name = n3
            print (self.name)
        else:
            n4 = '生' + name
            self.name = n4
            print (self.name)
   # def __str__(sef)


name = input('请输入您要烧烤的物品：')
tm = int (input('请输入您要烧烤物品的时间：'))
barbecue = Potato(name)
barbecue.Name_dic(name)
barbecue.time(tm)







































