list_n = [{'北京':{'面积':'100平米','人口':'200w'},'上海':{'面积':'60平米','人口':'150w'},'成都':{'面积':'160平米','人口':'50w'}}]
for i in list_n:
    for a,b in i.items():
        for x,y in b.items():
            print(a,x,y)
