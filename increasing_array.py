
l = [3, 2, 5, 1, 7, 99, 7, 8, 4, 6, 12, 76, 7, 56]



def increasing_array(n, l):
    low =100
    lowi=0
    new = []
    for i in range(n):
        if l[i] < low:
            low = l[i]
            lowi = i
    l.pop(lowi)
    return low, l
    
for i in range(len(l)):
    low, l = increasing_array(len(l), l)
    print(low)

    

