sqrm = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def number_spiral(sqrm):
    for i in range(1,26):
        #below is logic to populate bands starting and ending with even numbers
        if sqrt(i)%2 == 0:
            sqr = sqrt(i) * sqrt(i)
            if (sqr-i) >= sqrt(i):
                #print('book')
                #print(sqrt(i)-(sqr-(i)+1-sqrt(i)))
                #print(i)
                r = sqrt(i)-(sqr-(i)+1-sqrt(i))
                #print(r)
                sqrm[r-1][sqrt(i)-1] = i
                #print(sqrm)
            elif (sqr-i) < sqrt(i):
                #print('tablet')
                #print(sqr-i)
                #print(i)
                c = sqr-i
                sqrm[sqrt(i)-1][c] = i
                #print(sqrm)
        elif sqrt(i)%2 != 0:
            sqr = sqrt(i) * sqrt(i)
            if (sqr-i)+1 > sqrt(i):
                print('great')
                print(i)
                c = sqrt(i)-(sqr-(i)+1-sqrt(i))-1
                sqrm[sqrt(i)-1][c] = i
            elif (sqr-i)+1 <= sqrt(i):
                print('less')
                print(i)
                sqrm[sqr-i][sqrt(i)-1] = i
    return sqrm

def sqrt(n):
    for j in range(1,6):
        prev = j
        if n == 1:
           return 1
        elif j*j >= n:
            return j


k = 7
sqr1 = sqrt(k) * sqrt(k)  
#maths to get row value of even values greater than sqrt(i)
print(sqrt(k)-(sqr1-(k)+1-sqrt(k)))


print(number_spiral(sqrm))
# min value of spiral ring ((prev*prev)+1) - ((prev+prev)-1)
#range of numbers in spiral list(range(((prev*prev)+1) - ((prev+prev)-1), prev*prev+1))
