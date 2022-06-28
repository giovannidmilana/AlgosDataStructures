mylist = [10,3,1,0,2,11,5,4,6,7,8,9]

i = 0
swaps = 0


def sort(mylist):
    #print(swaps)
    i = 0
    swaps = 0
    while i < len(mylist)-1:
        #a = mylist[i]
        #b = mylist[i+1]
        #print(i)
        #print(mylist[i+1])
        #i += 1
        if mylist[i] > mylist[i+1]:
            print("1")
            mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
            #mylist[i] = b
            #mylist[i+1] = a
            swaps += 1
        if swaps == 0:
            print("2")
            return mylist
            #print("3")
        i += 1
    return sort(mylist)
    
    

print(sort(mylist))


