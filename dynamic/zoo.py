n = int(input())
mod = 9901

dp = [[1,2]]
for i in range(n-1):
    dp.append([(dp[i][0]+dp[i][1])%mod, (dp[i][0]*2+dp[i][1])%mod])
print(sum(dp[n-1])%mod)
