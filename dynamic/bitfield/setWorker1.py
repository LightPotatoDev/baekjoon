import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]

dp = [[int(1e9)]*(2**n) for _ in range(n)]
for i in range(n):
    dp[i][0] = 0

mask = 2**n-1

def setKthBit(n,k):
    pos = 1 << k
    return (mask ^ pos) & n

def setDp(visit):
    for i in range(n):
        if ((visit >> i) & 1) == 1:
            fromm = setKthBit(visit,i)
            for j in range(n):
                if ((visit >> j) & 1) == 0:
                    continue
                if fromm != 0:
                    weight = L[j][i]
                else:
                    weight = L[0][i]
                #print(weight)
                dp[i][visit] = min(dp[i][visit], dp[j][fromm]+weight)

def printDp():
    for row in dp:
        for c in row:
            if c == int(1e9):
                print(-1, end=' ')
            else:
                print(c, end=' ')
        print('')
    print('')

for i in range(1,n+1):
    comb = combinations(range(n),i)
    for choice in comb:
        visit = 0
        for c in choice:
            visit += 2**c
        #print(bin(visit)[2:].zfill(n-1))
        setDp(visit)
    printDp()
