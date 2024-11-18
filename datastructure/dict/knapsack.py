from bisect import bisect_left

n,c = map(int,input().split())
L = list(map(int,input().split()))
l = len(L)//2
D = dict()

def getSum(size,pos):
    s = 0
    for j in range(size):
        if ((i >> j) & 1) == 1:
            s += L[j+pos]
    return s

for i in range(1 << l):
    s = getSum(l,0)

    if s not in D:
        D[s] = 1
    else:
        D[s] += 1

D = dict(sorted(D.items()))
A = list(D.keys())
B = list(D.values())
for i in range(l):
    B[i+1] += B[i]

for i in range(1 << (len(L)-l)):
    s = getSum(len(L)-l,l)
    weight = c-s
    ind = bisect_left(A,weight)

print(A)
print(B)
