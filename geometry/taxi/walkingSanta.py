import sys
input = sys.stdin.readline

input()
n = int(input())

L = [[],[]]
for _ in range(n):
    x,y = map(int,input().split())
    L[0].append(x)
    L[1].append(y)

def getFurthest(least,most,medL,medR):
    d1 = most - medL
    d2 = medR - least
    if d1 >= d2:
        return medL
    else:
        return medR

Point = []
for i in L:
    A = i[:]
    A.sort()
    l = len(A)
    if n%2 == 1:
        Point.append(A[(l-1) // 2])
    else:
        Point.append(getFurthest(A[0],A[-1],A[(l-1)//2],A[l//2]))

maxDist = 0
cnt = 0
for i in range(n):
    x,y = Point
    dist = abs(x-L[0][i]) + abs(y-L[1][i])
    maxDist = max(dist, maxDist)
    cnt += dist*2

cnt -= maxDist
print(cnt)
print(*Point)