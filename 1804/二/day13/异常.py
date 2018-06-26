import time
try:
    f = open ('text.txt','r')
    try:
        while True:
            content = f.readline()
            if len(content) is 0:
                break
            time.sleep(2)
            print (content)
    finally:
        f.close()
        print ('关闭文件')
except:
    print ('没有这个文件')
