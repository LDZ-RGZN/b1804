f = open ('exe1.txt','w')
f.write('中国')
f.close()

f1 = open ('exe1.txt','r')
a = f1.read()
print (a)
f1.close()

f2 = open ('exe1.txt','a')
f2.write('你好')
f2.close()
