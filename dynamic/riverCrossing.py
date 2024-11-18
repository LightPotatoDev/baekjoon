n,m = map(int,input().split())
L = [int(input()) for _ in range(n)]
for i in range(1,n):
    L[i] += L[i-1]
dp = [[0]*n for _ in range(n)]
for j in range(n):
    dp[0][j] = L[j] + m

for i in range(1,n):
    for j in range(n):
        dp[i][j] = min(dp[i-1][j], )

for row in dp:
    print(row)