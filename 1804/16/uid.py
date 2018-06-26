list_n = [{'北京':{'面积':'1000平','人口':'200w'},'上海':     {'面积':'600平','人口':'150w'}}]
for i in list_n:
    for k,v in i.items():
        for j,l in v.items():
            print(k,j,l)
