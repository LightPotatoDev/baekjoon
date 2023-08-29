import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]

dp = [[int(1e9)]*(2**(n-1)) for _ in range(n-1)]
for i in range(n-1):
    dp[i][0] = L[0][i+1]

def setDp(visited):
    for i in range(n-1): #from
        if ((visited >> i) & 1) == 0:
            visit = visited + 2**i
            for j in range(n-1): #to
                print(L[i+1][j+1])
                if L[i+1][j+1] != 0:
                    dp[j][visit] = min(dp[j][visit], dp[i][visited]+L[i+1][j+1])

def printDp():
    for row in dp:
        for c in row:
            if c == int(1e9):
                print(-1, end=' ')
            else:
                print(c, end=' ')
        print('')
    print('')

for i in range(n-1):
    comb = combinations(range(n-1),i)
    for choice in comb:
        visited = 0
        for c in choice:
            visited += 2**c
        print(bin(visited)[2:])
        setDp(visited)
    printDp()
