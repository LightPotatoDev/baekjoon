n = int(input())

if n <= 9:
    print(0)
    exit()

dp = [[0]*10 for _ in range(n-9)]
dp[0][0] = 1