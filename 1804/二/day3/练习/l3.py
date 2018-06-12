f = open ('锄地.txt','w')
f.write('锄禾日当午\n')
f.write('汗滴禾下土\n')
f.write('谁知盘中餐\n')
f.write('粒粒皆辛苦\n')

f = open ('锄地.txt','r')
content = f.readlines()
for i in content:
    con = i[:len(i)-1]
    print(con + '*')
f.close
f.close
