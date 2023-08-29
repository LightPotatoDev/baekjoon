from itertools import combinations

n,s = map(int,input().split())
L = list(map(int,input().split()))

cnt = 0
for i in range(1,n+1):
    comb = combinations(L,i)
    for c in comb:
        if sum(c) == s:
            cnt += 1

print(cnt)