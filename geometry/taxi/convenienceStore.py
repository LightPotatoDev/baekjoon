import sys
input = sys.stdin.readline

n = int(input())

L = [[] for _ in range(2)]
for _ in range(n):
    x,y = map(int,input().split())
    L[0].append(x)
    L[1].append(y)

Point = []
for i in L:
    i.sort()
    Point.append(i[len(i) // 2])

dist = 0
for i in range(2):
    dist += sum([abs(L[i][j]-Point[i]) for j in range(n)])
print(dist)