n = int(input())
m = 10
div = int(1e9)
mask = (1<<m)-1
dp = [[[0]*m for _ in range(mask+1)] for _ in range(n)] #[n][has number][ends with]
for i in range(1,m):
    dp[0][1<<i][i] = 1

def setKthBit(n,k):
    pos = 1<<k
    return (mask ^ pos) & n

for i in range(1,n):
    for j in range(mask+1):
        for k in range(m):
            if k != 0:
                if setKthBit(j,k) != j:
                    dp[i][j][k] += dp[i-1][setKthBit(j,k)][k-1] % div
                if ((j >> k)&1) == 1:
                    dp[i][j][k] += dp[i-1][j][k-1] % div
            if k != m-1:
                if setKthBit(j,k) != j:
                    dp[i][j][k] += dp[i-1][setKthBit(j,k)][k+1] % div
                if ((j >> k)&1) == 1:
                    dp[i][j][k] += dp[i-1][j][k+1] % div

print(sum(dp[n-1][mask]) % div)

##for i in dp:
##    for j in i:
##        print(j)
##    print('')
##
