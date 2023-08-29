n = int(input())
for _ in range(n):
    input()
p = int(1e9)+7

dp = [[1]*n for _ in range(n)]

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])%p

print(2*sum(dp[n-1])%p, n**2)