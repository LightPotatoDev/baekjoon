n = int(input())
cost = [0]+list(map(int,input().split()))
m = int(input())
value = [0]+[10000+i for i in range(n)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if j >= cost[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i]]+value[i])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

for i in dp:
    print(i)