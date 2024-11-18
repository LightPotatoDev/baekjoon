import math

m,k = map(int,input().split())
pretty = [False]*5001

def digit_sum(n):
    s = 0
    while n > 0:
        s += n%10
        n //= 10
    return s

for i in range(1,5001):
    d = digit_sum(i)
    if math.gcd(d,i) == d:
        pretty[i] = True

SIZE = 5001
dp = [[0]*SIZE for _ in range(SIZE)]
for i in range(SIZE):
    dp[0][i] = 1

for i in range(1,SIZE):
    for j in range(1,SIZE):
        dp[i][j] = dp[i][j-1]
        if i-j >= 0 and pretty[j] == True:
            dp[i][j] += dp[i-j][j]
            dp[i][j] %= k

print(dp[m][m])