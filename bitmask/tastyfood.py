from itertools import combinations

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]

ans = int(1e12)
for i in range(1,n+1):
    comb = combinations(L,i)
    for Choice in comb:
        sour = 1
        for j in Choice:
            sour *= j[0]
        bitter = sum([j[1] for j in Choice])

        ans = min(ans, abs(sour-bitter))

print(ans)