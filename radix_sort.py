mylist = [46, 35, 52, 103, 201, 68, 74, 201]


def sig(mylist):
    cur = 0
    for i in range(0, len(mylist)):
        if mylist[i] > cur:
            cur = mylist[i]
    return len(str(cur))
    
    
    
def sort(mylist, s):
    #print(swaps)
    i = 0
    swaps = 0
    while i < len(mylist)-1:
        try:
            a = get_sig(mylist[i])[s]
        except Exception as e:
            a = 0
        try:
            b = get_sig(mylist[i+1])[s]
        except Exception as e:
            b = 0
        
        
        print(mylist[i])
        print(a)
        print(mylist[i+1])
        print(b)
        if a > b:
            print('swap')
            mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
            swaps += 1
        if swaps == 0 and i == len(mylist)-2:
            return mylist
        i += 1
    return sort(mylist, s)
    
    
    
def get_sig(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10
    return pos_nums

def M(mylist):
    for i in range(0, sig(mylist)):
        mylist = sort(mylist, i)
        print(mylist)
    return mylist


print(get_sig(104))
    
M(mylist)


