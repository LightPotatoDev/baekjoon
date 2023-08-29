n,k = map(int,input().split())
L = []
for _ in range(n):
    L.append(int(input()))
L.sort()

dp = [[0]*(k+1) for _ in range(2)]
for i in range(1,k+1):
    dp[0][i] = int(i%L[0] == 0)

for i in L[1:]:
    for j in range(1,k+1):
        if j < i:
            dp[1][j] = dp[0][j]
        elif j == i:
            dp[1][j] = dp[0][j] + 1
        else:
            dp[1][j] = dp[0][j] + dp[1][j-i]

    dp[0] = dp[1][:]

print(dp[0][-1])