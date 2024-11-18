n,l,r = map(int,input().split())
MOD = int(1e9) + 7

def perm(n,k):
    res = 1
    for i in range(n,n-k,-1):
        res = (res * i) % MOD
    return res

def facto(n):
    return perm(n,n)

def comb(n,k):
    return ((perm(n,k) % MOD) * pow(perm(k,k), MOD-2, MOD)) % MOD

factorial = [facto(i) for i in range(n+1)]
combination = [[comb(i,j) for j in range(n+1)] for i in range(n+1)]

build = [[0]*(n+1) for _ in range(n+1)]
build[0][0] = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(i):
            build[i][j] += build[k][j-1] * factorial[i-k-1] * combination[i-1][k]
            build[i][j] %= MOD

ans = 0
for i in range(n):
    ans += build[i][l-1] * build[n-i-1][r-1] * combination[n-1][i]
    ans %= MOD
print(ans)