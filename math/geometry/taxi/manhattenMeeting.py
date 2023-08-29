import sys
input = sys.stdin.readline

n,m = map(int,input().split())

L = [[] for _ in range(n)]
for _ in range(m):
    T = list(map(int,input().split()))
    for i in range(n):
        L[i].append(T[i])

Point = []
for i in L:
    i.sort()
    Point.append(i[len(i) // 2])

dist = 0
for i in range(n):
    dist += sum([abs(L[i][j]-Point[i]) for j in range(m)])
print(dist)
print(*Point)