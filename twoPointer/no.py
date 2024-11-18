n,m = map(int,input().split())
L = [0] + list(map(int,input().split()))

for i in range(n):
    L[i+1] += L[i]

a = 0
b = 0
cnt = 0
ans = 0

while a <= n:
    cnt = L[b] - L[a]
    if (cnt <= m):
        ans = max(ans,cnt)

    if (cnt <= m) and (b < n):
        b += 1
    else:
        a += 1

print(ans)