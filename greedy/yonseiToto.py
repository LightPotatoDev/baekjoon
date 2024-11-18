n,m = map(int,input().split())
required = [1]*n
for i in range(n):
    p,l = map(int,input().split())
    L = list(map(int,input().split()))
    L.sort(reverse=True)
    if p < l:
        required[i] = 1
    else:
        required[i] = L[l-1]

required.sort()
ans = 0
for i in range(n):
    if required[i] <= m:
        m -= required[i]
        ans += 1
print(ans)
