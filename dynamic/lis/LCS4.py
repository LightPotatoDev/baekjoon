import sys
from bisect import bisect_left
input = sys.stdin.readline

def lis(L):
    dp = [L[0]]

    for a in L[1:]:
        if a > dp[-1]:
            dp.append(a)
        else:
            index = bisect_left(dp,a)
            dp[index] = a

    return len(dp)

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

D = dict()
for i,x in enumerate(A):
    D[x] = i+1
L = []
for i in B:
    L.append(D[i])
print(lis(L))