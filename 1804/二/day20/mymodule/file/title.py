#seek(offest,from) offset:偏移量 from:放向  0开始  1当前 2末尾



f1 = open ('gushi.txt','w+')
f1.write('what do yo do ')
f1.seek(0,0)
content = f1.read()
print (content)
