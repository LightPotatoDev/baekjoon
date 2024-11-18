import sys
input = sys.stdin.readline

n,m = map(int,input().split())
L = [list(map(int,input().split())) for _ in range(n)]

for i in range(0,n):
    for j in range(1,m):
        L[i][j] += L[i][j-1]

for j in range(0,m):
    for i in range(1,n):
        L[i][j] += L[i-1][j]

k = int(input())

for _ in range(k):
    y1,x1,y2,x2 = map(int,input().split())
    initial = L[y2-1][x2-1]
    minus1 = L[y1-2][x2-1] if y1 != 1 else 0
    minus2 = L[y2-1][x1-2] if x1 != 1 else 0
    dupe = L[y1-2][x1-2] if y1 != 1 and x1 != 1 else 0

    print(initial - minus1 - minus2 + dupe)
