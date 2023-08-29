from collections import defaultdict

Hand = defaultdict(int)

for i in input().split():
    Hand[i] += 1

def headReplace(L,i):
    a = L.index(i)
    L[a] = 0
    b = L.index(i)
    L[b] = 0
    return (a,b)

def getComb(L,head,body):

    for i in L:
        if i != 0 and L.count(i) >= 2:
            i1,i2 = headReplace(L,i)
            getComb(L,head+1,body)
            L[i1] = i
            L[i2] = i
        if i != 0 and
        print(L,head,body)
