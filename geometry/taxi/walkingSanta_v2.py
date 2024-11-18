import sys
input = sys.stdin.readline

input()
n = int(input())

L = [[],[]]
for _ in range(n):
    x,y = map(int,input().split())
    L[0].append(x)
    L[1].append(y)

def getDist(points):
    cnt = 0
    maxDist = 0
    x,y = points
    for i in range(n):
        dist = abs(x-L[0][i]) + abs(y-L[1][i])
        maxDist = max(dist, maxDist)
        cnt += dist*2
    return cnt-maxDist

Point = []
A = []
for i in L:
    A.append(sorted(i))

if n%2 == 1:
    Point.append([A[0][(n-1)//2], A[1][(n-1)//2]])
else:
    Point.append([A[0][(n-1)//2], A[1][(n-1)//2]])
    Point.append([A[0][(n-1)//2], A[1][n//2]]    )
    Point.append([A[0][n//2]    , A[1][(n-1)//2]])
    Point.append([A[0][n//2]    , A[1][n//2]]    )

ans = int(1e15)
px,py = 0,0
for i in Point:
    d = getDist(i)
    if d < ans:
        ans = d
        px,py = i

print(ans)
print(px,py)
