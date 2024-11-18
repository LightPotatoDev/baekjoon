import sys
input = sys.stdin.readline

n,k,m = map(int,input().split())
m = m-1
S = list(map(int,input().split()))
L = [[0]*(k+1) for _ in range(30)]
L[0] = [0]+list(map(int,input().split()))

for i in range(1,30):
    for j in range(1,k+1):
        L[i][j] = L[i-1][L[i-1][j]]

for x in S:
    for i in range(30):
        if ((m >> i) & 1) == 1:
            x = L[i][x]
    print(x, end=' ')