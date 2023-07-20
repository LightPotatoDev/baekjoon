n = int(input())

L = [0]
for _ in range(n):
    L.append(int(input()))

dp = [0] * (n+1)

dp[1] = L[1]
if n >= 2:
    dp[2] = L[1]+L[2]
if n >= 3:
    dp[3] = max(L[1],L[2])+L[3]
for i in range(4,n+1):
    dp[i] = max(dp[i-3]+L[i-1],dp[i-2])+L[i]

print(max(dp[n],dp[n-1]))
