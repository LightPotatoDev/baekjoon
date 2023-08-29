n,m,k = map(int,input().split())

def gridCases(n,m):
    dp = [[1]*m for _ in range(n)]
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]

if k == 0:
    print(gridCases(n,m))
else:
    midN = (k-1)//m +1
    midM = (k-1)%m +1
    print(gridCases(midN,midM) * gridCases(n-midN+1, m-midM+1))