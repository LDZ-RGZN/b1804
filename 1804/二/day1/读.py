#练习1
f = open ('龟虽寿.txt','w')
f.write('老骥伏枥\n')
f.write('志在千里\n')
f.write('烈士暮年\n')
f.write('壮心不已\n')

f = open ('龟虽寿.txt','r')
a = 0
while a < 4:
    line = f.readline()
    s = line[:len(line)-1]
    print (s + '*_*')
    a += 1

f = open ('龟虽寿.txt','r')
line2 = f.readlines()

f2 = open ('龟虽寿.txt','a')
f2.write('|\n')
for i in line2:
    s = i[:len(i)-1]
    f2.write(s + '*_*\n')

f.close()
f.close()
f2.close()
