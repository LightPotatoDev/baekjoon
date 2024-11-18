import sys
input = sys.stdin.readline

m = int(input())
L = [[0]*(m+1) for _ in range(19)]
L[0] = [0]+list(map(int,input().split()))

for i in range(1,19):
    for j in range(1,m+1):
        L[i][j] = L[i-1][L[i-1][j]]

q = int(input())
for _ in range(q):
    n,x = map(int,input().split())
    for i in range(19):
        if ((n >> i) & 1) == 1:
            x = L[i][x]
    print(x)