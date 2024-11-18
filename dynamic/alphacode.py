L = [0]+list(map(int,input()))
n = len(L)-1
mod = 1000000

for i in range(1,n+1):
    if i == 1 and L[i] == 0:
        print(0)
        exit()
    elif L[i] == 0 and (not 1 <= L[i-1] <= 2):
        print(0)
        exit()

dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1
for i in range(2,n+1):
    num = 10 * L[i-1] + L[i]

    if L[i] == 0:
        dp[i] = dp[i-2]
    elif 10 <= num <= 26:
        dp[i] = (dp[i-1] + dp[i-2]) % mod
    else:
        dp[i] = dp[i-1]

print(dp[n])
