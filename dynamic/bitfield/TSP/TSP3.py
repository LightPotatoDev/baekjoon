import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
pos = [list(map(int,input().split())) for _ in range(n)]
L = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        x1,y1 = pos[i]
        x2,y2 = pos[j]
        d = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
        L[i][j] = d
        L[j][i] = d

dp = [[int(1e9)]*(2**(n-1)) for _ in range(n-1)]
for i in range(n-1):
    dp[i][0] = 0

mask = 2**(n-1)-1

def setKthBit(n,k):
    pos = 1 << k
    return (mask ^ pos) & n


def setDp(visit):
    for i in range(n-1):
        if ((visit >> i) & 1) == 1:
            fromm = setKthBit(visit,i)
            for j in range(n-1):
                if ((visit >> j) & 1) == 0:
                    continue
                if fromm != 0:
                    weight = L[j+1][i+1]
                else:
                    weight = L[0][i+1]
                #print(weight)
                if weight != 0:
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

for i in range(1,n):
    comb = combinations(range(n-1),i)
    for choice in comb:
        visit = 0
        for c in choice:
            visit += 2**c
        #print(bin(visit)[2:].zfill(n-1))
        setDp(visit)
    #printDp()

ans = int(1e9)
for i in range(n-1):
    if L[i+1][0] != 0:
        ans = min(dp[i][-1]+L[i+1][0], ans)
print(ans)