l = [(lambda x,y:x+y),(lambda x,y=2:x+y),(lambda x:x**3)]
print (l[0](2,5),l[1](5),l[2](3))
d = {'a':(lambda:2**2),'a1':(lambda:2**3),'a2':(lambda:2**4)}
print (d['a'](),d['a1'](),d['a2']())
