def text1():
    print ('___text1-1___')
    print (num)
    print ('___text1-2___')
def text2():
    print ('___text2-1___')
    text1()
    print ('___text2-2___')
def text3():
    try:
        print ('___text3-1___')
        text1()
        print ('___text3-2___')
    except Exception as result:
        print ('捕获到了异常,信息是:%s'%result)

    print ('___text3-2___')

text3()
print ('_________华丽的分割线__________')
