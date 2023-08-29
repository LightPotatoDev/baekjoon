from itertools import combinations

h,w = map(int,input().split())
n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]

def putSticker(r1,c1,r2,c2):
    sameL = (r1+r2) <= h and max(c1,c2) <= w
    sameU = (c1+c2) <= w and max(r1,r2) <= h
    if sameL or sameU:
        return (r1*c1) + (r2*c2)
    else:
        return 0

area = 0
comb = combinations(L,2)
for s1,s2 in comb:
    r1,c1 = s1
    r2,c2 = s2
    area = max(putSticker(r1,c1,r2,c2),area)
    area = max(putSticker(c1,r1,r2,c2),area)
    area = max(putSticker(r1,c1,c2,r2),area)
    area = max(putSticker(c1,r1,c2,r2),area)

print(area)