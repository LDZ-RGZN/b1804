class A(object):
    def __init__(self):
        print ('这是init方法')

    def __new__(cls):
        print ('这是new方法')
        return object.__new__(cls)

A()
