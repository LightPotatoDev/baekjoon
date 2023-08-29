n,m = map(int,input().split())
A = [0]+list(map(int,input().split()))
C = [0]+list(map(int,input().split()))
dp = [[0]*10001 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(10001):
        if C[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-C[i]] + A[i])

for i,x in enumerate(dp[n]):
    if x >= m:
        print(i)
        break

for row in dp:
    print(row[:16])
