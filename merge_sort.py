def mergeSort(myList):
    #if len(myList) > 1:
    '''
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)
        
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
    '''
    i = 0
    j = 0
        
    # Iterator for the main list
    k = 0
        
    n1 = 1
    n2 = 1
    left = []
    right = []
        
    while True:
        
        n1 = get(n1, 100)
        left.append(n1) 
        n2 = get(n2, 100)
        right.append(n2)
        
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              print(left[i])
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                print(left[i])
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            print(left[i])
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            print(left[i])
            myList[k]=right[j]
            j += 1
            k += 1



def get(n1, s):
    if n1 <= s:
        n1 = n1 +1
        #print(n1)
        return n1
    else:
        return 0

myList = [0]*100    
#myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)
