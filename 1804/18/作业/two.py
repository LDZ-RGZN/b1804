#for循环
tu1 = ((1,2,3),(4,5,6,),(7,8,9))

for ou in tu1:
    print (ou)
    for uo in ou:
        print(uo)
#while循环
p = 0
while p < len(tu1):
    print(tu1[p])
    tu2 = tu1[p]

    q = 0
    while q < len(tu2):
        print (tu2[q])
        q += 1
    p += 1
