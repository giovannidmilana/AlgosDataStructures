sqr = []

def number_spiral(n, t):
    
    
    
    
    
    
def square_root(n):
    i = 0
    t = False
    while t != True:
        prev = i
        if n == 1:
            return 1
        elif i*i >= n:
            t = True
            if i%2 == 0:
                print(list(range(((prev*prev)+1) - ((prev+prev)-1), prev*prev+1)))
                
            return prev, list(range(((prev*prev)+1) - ((prev+prev)-1), prev*prev+1))
            
                
            
        i += 1

print(square_root(3))
# min value of spiral ring ((prev*prev)+1) - ((prev+prev)-1)
