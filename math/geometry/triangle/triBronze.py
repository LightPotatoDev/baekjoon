from itertools import combinations

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]
comb = combinations(L,3)
area = 0

for points in comb:
    pick = combinations(points,2)
    y = 0
    x = 0
    for p1,p2 in pick:
        if p1[0] == p2[0]:
            y = abs(p1[1]-p2[1])
        elif p1[1] == p2[1]:
            x = abs(p1[0]-p2[0])
    area = max(y*x,area)

print(area)