def missing(n, l):
    m = ['nin'] * n
    for i in l:
        m[i] = i
    for i in range(0, len(m)):
        if m[i] == 'nin' and i != 0:
            print(i)

l = list(range(1,5))
print(l[2])
l.pop(2)
missing(5, l)
