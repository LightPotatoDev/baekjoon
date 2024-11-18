n = int(input())
numbers = list(map(int,input().split()))
dp = [[0]*21 for _ in range(n-1)]

dp[0][numbers[0]] = 1
for i in range(1,n-1):
    for j in range(0,21):
        a,b = j+numbers[i], j-numbers[i]
        if dp[i-1][j] != 0 and 0 <= a < 21:
            dp[i][a] += dp[i-1][j]
        if dp[i-1][j] != 0 and 0 <= b < 21:
            dp[i][b] += dp[i-1][j]

print(dp[-1][numbers[-1]])
