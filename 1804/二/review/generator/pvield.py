from inspect import isgeneratorfunction
def gen():
    print ('not')
print (isgeneratorfunction(gen))
