class Cat:
    def eat(self):
        print ('%s在吃鱼------'%(self.name))
    def drink(self):
        print ('%s在喝啤酒------'%(self.name))
    def introduce(self):
        print ('我的名字是%s,我是一只%s色的猫,我今年%d岁了.'%(self.name,self.color,self.age))

tom = Cat()
tom.age = 7
tom.color = '蓝'
tom.name = 'tom'
tom.eat()
tom.drink()
tom.introduce()

