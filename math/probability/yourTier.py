w,l,d = map(float,input().split())
dp = [[0]*43 for _ in range(21)]
dp[0][21] = 1

for i in range(20):
    for j in range(1,42):
        dp[i+1][j+1] += dp[i][j] * w
        dp[i+1][j] += dp[i][j] * d
        dp[i+1][j-1] += dp[i][j] * l

for i in range(5):
    ans = sum(dp[20][i*10+1:i*10+11])
    print("{:.8f}".format(round(ans,8)))