n = int(input())
L = list(map(float,input().split()))
ans = sum(L)
for i in range(n-1):
    ans += L[i] * (1-L[i+1]) + (1-L[i]) * L[i+1]
print(ans)