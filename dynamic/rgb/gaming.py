n,m = map(int,input().split())

dp = [[x for x in map(int,input().split())] for _ in range(n)]
for i in range(1,n):
    for j in range(m):
        A = dp[i-1][:]
        A.pop(j)
        dp[i][j] = min(A) + dp[i][j]
print(min(dp[n-1]))
