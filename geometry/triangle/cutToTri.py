from itertools import combinations

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]
comb = combinations(L,3)

def crossProd(v1,v2):
    return v1[0]*v2[1] - v1[1]*v2[0]

def triArea(p1,p2,p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3

    v1 = [x2-x1,y2-y1]
    v2 = [x3-x2,y3-y2]
    return abs(crossProd(v1,v2)) / 2

area = 0
for p1,p2,p3 in comb:
    area = max(area,triArea(p1,p2,p3))
print(area)