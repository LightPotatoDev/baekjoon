import sys
input = sys.stdin.readline
from itertools import combinations

class vector:
    def __init__(self,p1,p2):
        self.x = p2[0]-p1[0]
        self.y = p2[1]-p1[1]

    def __repr__(self):
        return (self.x,self.y)

def dotProd(v1,v2):
    return v1.x*v2.x + v1.y*v2.y

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]
comb = combinations(L,3)

cnt = 0
for p1,p2,p3 in comb:
    v1 = vector(p1,p2)
    v2 = vector(p2,p3)
    v3 = vector(p3,p1)
    if dotProd(v1,v2) == 0 or dotProd(v2,v3) == 0 or dotProd(v3,v1) == 0:
        cnt += 1
print(cnt)