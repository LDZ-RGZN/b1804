class Animal:
    def __init__ (self,name,what):
        self.name = name
        self.f = open ('name.txt',what)

    def get_name(self):
        self.name = self.f.read()
        self.f.close()
        return self.name

    def __del__(self):
        self.f.write(self.name)
        self.f.close()

        print ('当前对象被销毁了')

dog = Animal('大黄','r')
print (dog.get_name())
del dog
print ('=======================')

