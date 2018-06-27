L = [11,22,33,44,11]
#set(L)

L1 = []
for i in L:
    if i not in L1:
        L1.append(i)
print (L1)
