
l = [4, 2, 5, 3, 1]
new= []

def premute(n):
    if len(n) == 0:
        return []
 
    if len(n) == 1:
        return [n]
 
    new = [] # empty list
    for i in range(len(n)):
        m = n[i]
        rem = n[:i] + n[i+1:]
        for j in premute(rem):    
            new.append([m] + j)
    return new
    
print(premute(l))

