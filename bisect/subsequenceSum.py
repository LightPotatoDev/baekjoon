from itertools import combinations
from collections import defaultdict

n,s = map(int,input().split())
L = list(map(int,input().split()))
maxi = int(2e6)

def subseq(L):
    D = defaultdict(int)
    for i in range(1,len(L)+1):
        comb = combinations(L,i)
        for c in comb:
            D[sum(c)] += 1
    return D

D1 = subseq(L[:n//2])
D2 = subseq(L[n//2:])

ans = 0
for i in range(-maxi, maxi+1):
    if (i in D1) and (-i+s in D2):
        ans += D1[i]*D2[-i+s]
ans += D1[s]+D2[s]
print(ans)