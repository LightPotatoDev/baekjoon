n,feel = map(int,input().split())
L = list(map(float,input().split()))
dp = [[0,0] for _ in range(n+1)]
dp[0][feel] = 1

for i in range(1,n+1):
    dp[i][0] = dp[i-1][0] * L[0] + dp[i-1][1] * L[2]
    dp[i][1] = dp[i-1][0] * L[1] + dp[i-1][1] * L[3]
for i in dp[n]:
    print(round(i*1000))