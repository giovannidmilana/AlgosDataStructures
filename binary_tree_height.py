# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task

def solution(T):
    count = 0
    n = []
    dl = checkT(T, None)
    n.append(dl)
    #tl = dl['lt']
    count +=1
    #while True:
    for i in n:
        #print(len(n))
        if i['lt'] != None:
            n.append(checkT(i['lt'], i['x']))
            count += 1
        if i['rt'] != None:
            n.append(checkT(i['rt'], i['x']))
            count += 1
    j = countP(n[-1], dl, n)
    print(j)

    


def checkT(T, P):
    d = {}
    #print(T.x)
    d['X'] = T.x
    if T.l != None:
        d['lv'] = True
        d['lt'] = T.l
        d['x'] = T
        d['p'] = P
    else:
        d['lv'] = False
        d['lt'] = None
        d['x'] = T
        d['p'] = P
    if T.r != None:
        d['lv'] = True
        d['rt'] = T.r  
        d['x'] = T
        d['p'] = P
    else:
        d['lv'] = False
        d['rt'] = None
        d['x'] = T
        d['p'] = P
    #print(d)
    return d

def countP(P, T, n):
    count = 0
    while P['p'] != None:
        for i in n:
            print(P)
            if i['x'] == P['p']:
                print('gggg')
                P = i
                count +=1
        
    return count

