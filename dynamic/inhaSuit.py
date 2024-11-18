n = int(input())
k = int(input())
hole = [[0]*21 for _ in range(n+1)]

for i in range(n):
    L = list(map(int,input().split()))[1:]
    for h in L:
        hole[i+1][h] = 1

dp = [[999]*21 for _ in range(n+1)]
dp[0][1] = 0

for i in range(n):
    for j in range(1,21):
        if dp[i][j] != 999:
            if hole[i+1][j] == 1:
                dp[i+1][j] = min(dp[i][j], dp[i+1][j])
            if hole[i+1][min(20,j+1)] == 1:
                dp[i+1][min(20,j+1)] = min(dp[i][j],dp[i+1][min(20,j+1)])
            if hole[i+1][max(1,j-1)] == 1:
                dp[i+1][max(1,j-1)] = min(dp[i][j],dp[i+1][max(1,j-1)])
            if hole[i+1][min(20,j*2)] == 1:
                dp[i+1][min(20,j*2)] = min(dp[i][j],dp[i+1][min(20,j*2)])
        if hole[i+1][j] == 1:
            dp[i+1][j] = min(min(dp[i])+1,dp[i+1][j])

ans = min(dp[n])
if ans <= k:
    print(ans)
else:
    print(-1)