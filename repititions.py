
def func(dna):
    best = 1
    l = 1
    for i in range(1,len(dna)):
        if dna[i] == dna[i-1]:
            l += 1
        else:
            l = 1
        if l > best:
            best = l
    return best   

   

'''
def func(dna, i, l, best):
    if l > best[-1]:
            best.append(l)
    if i != len(dna):
        if dna[i] == dna[i-1]:
            l += 1
        else:
            l = 1
        func(dna, i+1, l, best)
   
    if True:
        #print(best)
        return best[-1]
'''


