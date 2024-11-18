n = int(input())
L = list(map(int,input().split()))
m = int(input())
Marbles = list(map(int,input().split()))
maxW = 15000

for marb in Marbles:
    dp = [[0]*(maxW*2+1) for _ in range(n+1)] #-15000, ... 15000
    dp[0][maxW] = 1

    for i in range(n):
        w = L[i]
        for j in range(maxW*2+1):
            if dp[i][j] == 1:
                dp[i+1][j-w] = 1
                dp[i+1][j]   = 1
                dp[i+1][j+w] = 1

    if marb <= 15000 and dp[n][maxW+marb] == 1:
        print("Y", end=' ')
    else:
        print("N", end=' ')