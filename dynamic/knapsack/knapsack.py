n,k = map(int,input().split())

L = [0]+[list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if j >= L[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i][0]]+L[i][1])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

for row in dp:
    print(row)
print(dp[n][k])