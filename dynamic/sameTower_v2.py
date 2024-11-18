n = int(input())
towers = list(map(int,input().split()))
DP_SIZE = 250001
dp = [[-1]*DP_SIZE for _ in range(n)] #[towers used][height diff]
dp[0][0] = 0
if towers[0] < DP_SIZE:
    dp[0][towers[0]] = towers[0]

for i in range(n-1):
    for j in range(DP_SIZE):
        if dp[i][j] != -1:
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
            h = towers[i+1]
            if j+h < DP_SIZE:
                dp[i+1][j+h] = max(dp[i+1][j+h], dp[i][j]+h)
            if abs(j-h) < DP_SIZE:
                dp[i+1][abs(j-h)] = max(dp[i+1][abs(j-h)], max(dp[i][j], dp[i][j]-j+h))

print(dp[n-1][0] if dp[n-1][0] != 0 else -1)