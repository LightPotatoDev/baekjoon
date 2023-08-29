c,n = map(int,input().split())
cost = [0]
ppl  = [0]
for _ in range(n):
    co,p = map(int,input().split())
    cost.append(co)
    ppl.append(p)

dp = [[int(1e9)]*(c+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,c+1):
        if j < cost[i]:
            dp[i][j] = dp[i-1][j]
        else:
            minCost = dp[i][j-cost[i]]+ppl[i]
            isInf = int(minCost>=int(1e9))
            dp[i][j] = min(dp[i-1][j], minCost - int(1e9) * isInf)

print(min(dp[n][c:]))
for row in dp:
    print(row)