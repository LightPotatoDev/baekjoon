import sys
input = sys.stdin.readline

T = 0
while True:
    T += 1
    n = int(input())
    if n == 0:
        break

    cost = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0]*3 for _ in range(n)]
    dp[0][1] = cost[0][1]
    dp[0][2] = cost[0][1] + cost[0][2]
    dp[1][0] = cost[0][1] + cost[1][0]
    dp[1][1] = min(dp[0][1], dp[0][2], dp[1][0]) + cost[1][1]
    dp[1][2] = min(dp[0][1], dp[0][2], dp[1][1]) + cost[1][2]

    for i in range(2,n):
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0]) + cost[i][1]
        dp[i][2] = min(dp[i-1][1], dp[i-1][2], dp[i][1]) + cost[i][2]

    print(f"{T}. {dp[n-1][1]}")