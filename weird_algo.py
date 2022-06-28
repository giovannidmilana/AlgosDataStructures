def weird(n):
    print(n)
    if n != 1:
        if n%2 == 0:
            nn = n/2
            weird(nn)
        else:
            nn = (n * 3) + 1
            weird(nn)
    else:
        return n
        
print(weird(103))
