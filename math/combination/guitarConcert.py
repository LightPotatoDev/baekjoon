from itertools import combinations

n,m = map(int,input().split())
possible = []
for _ in range(n):
    possible.append(input().split()[1])

def getSongs(c):
    cnt = 0
    for i in range(m):
        if any([inst[i]=="Y" for inst in c]):
            cnt += 1
    return cnt

maxPlay = 0
ans = -1
for i in range(n,0,-1):
    comb = combinations(possible,i)
    for c in comb:
        songs = getSongs(c)
        if songs > maxPlay:
            maxPlay = songs
            ans = i
        elif songs == maxPlay and songs != 0:
            ans = min(ans, i)

print(ans)