list_n = [{'a':5},{'a':5}]
b = 0
for i in list_n:
    for x,y in i.items():
        b += y
print (b)
