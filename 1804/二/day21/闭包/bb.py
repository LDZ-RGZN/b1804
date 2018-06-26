def out(one):
    def num_in(two):
        print ('in里的数是%d'%two)
        return one + two
    return num_in
print (out(5)(8))
