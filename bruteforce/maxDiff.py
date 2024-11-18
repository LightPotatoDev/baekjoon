from itertools import permutations

n = int(input())
L = list(map(int,input().split()))
perms = permutations(L,n)

ans = 0
for p in perms:
    s = 0
    for i in range(n-1):
        s += abs(p[i]-p[i+1])
    ans = max(ans,s)

print(ans)