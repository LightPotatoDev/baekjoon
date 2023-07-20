L = [0] + [1]*9 #끝이 0인 수, 끝이 1인 수, ...
n = int(input())

for _ in range(n-1):
    A = [0]*10
    for i in range(10):
        if i == 0:
            A[i+1] += L[i]
        elif i == 9:
            A[i-1] += L[i]
        else:
            A[i+1] += L[i]
            A[i-1] += L[i]

    L = A[:]


print(sum(L)%1000000000)

""" by line1029
n = int(input())
dp = [[0]*10 for _ in range(n)]
dp[0] = [1]*10
for i in range(1, n):
    dp[i][0] += dp[i - 1][1]
    dp[i][9] += dp[i - 1][8]
    for j in range(1, 9):
        dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[-1][1:])%1_000_000_000)
"""