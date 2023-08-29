c,n = map(int,input().split())
cost = [0]
ppl  = [0]
for _ in range(n):
    co,p = map(int,input().split())
    cost.append(co)
    ppl.append(p)

dp = [[int(1e9)]*(c+100) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,c+100):
        if j < ppl[i]:
            dp[i][j] = dp[i-1][j]
        else:
            minCost = dp[i][j-ppl[i]]+cost[i]
            dp[i][j] = min(dp[i-1][j], minCost - int(1e9) * int(minCost>=int(1e9)))

print(min(dp[n][c:]))
for row in dp:
    print(row)