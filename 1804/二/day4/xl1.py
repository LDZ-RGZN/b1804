f = open ('1.txt','r')
content = f.read()
f1 = open ('2.txt','w')
f1.write(content)
f.close()
f1.close()

