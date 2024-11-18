n,k = map(int,input().split())
L = [0]+list(map(int,input().split()))
for i in range(n):
    L[i+1] += L[i]

ans = -100000
for i in range(k,n+1):
    ans = max(ans,L[i]-L[i-k])

print(ans)