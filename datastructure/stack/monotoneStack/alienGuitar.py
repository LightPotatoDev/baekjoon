import sys
input = sys.stdin.readline

n,p = map(int,input().split())
L = [[] for _ in range(7)]
ans = 0

for _ in range(n):
    a,b = map(int,input().split())
    while L[a] and L[a][-1] > b:
        L[a].pop()
        ans += 1
    if not L[a] or L[a][-1] != b:
        L[a].append(b)
        ans += 1
print(ans)