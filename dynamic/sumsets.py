n = int(input())
mod = int(1e9)
dp = [[0]*(21) for _ in range(n+1)]
dp[1][0] = 1

def power_of_2(n):
    if (n & (n-1)) != 0:
        return -1
    x = 0
    while n > 1:
        n = n // 2
        x += 1
    return x

for i in range(2,n+1):
    exp = power_of_2(i)
    if exp != -1:
        dp[i][exp] = 1
    for j in range(21):
        j2 = 2 ** j
        if i-j2 <= 0:
            break
        dp[i][j] = sum(dp[i-j2][j:]) % mod

for i in range(1,n+1):
    print(sum(dp[i]) % mod)