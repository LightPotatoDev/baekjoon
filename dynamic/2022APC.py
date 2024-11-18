import sys
input = sys.stdin.readline

MAX_DIFF = 3000
MOD = int(1e9)+7

n,k = map(int,input().split())
diff_range = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*(MAX_DIFF+1) for _ in range(n+1)]
a,b = diff_range[0]
dp[1][a] = 1
for j in range(a+1,MAX_DIFF+1):
    dp[1][j] = dp[1][j-1] + int(j <= b)

for i in range(2,n+1):
    a,b = diff_range[i-1]
    for j in range(1,MAX_DIFF+1):
        dp[i][j] += dp[i][j-1]
        if a <= j <= b:
            dp[i][j] += dp[i-1][min(j+k, MAX_DIFF)]
            dp[i][j] %= MOD
            dp[i][j] -= dp[i-1][max(0, j-k-1)]
            dp[i][j] %= MOD

print(dp[n][MAX_DIFF])