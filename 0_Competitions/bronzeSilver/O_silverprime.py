def sieve(n):
    p = 2
    isPrime = [1] * (n+1)
    primes = []
    for i in range(2,int(n**0.5)+1):
        if isPrime[i]:
            primes.append(i)
            for j in range(i**2, n+1, i):
                isPrime[j] = 0

    isPrime[1] = 0
    return isPrime

P = sieve(5000000)
dp = [[1,0],[0,2],[0,3]]
n = int(input())
for i in range(4,n+1):
    if P[i] == 1:
        dp.append([dp[-1][0]-1, dp[-1][1]+2])
    else:
        dp.append([dp[-1][0]+1,dp[-1][1]])

print(*dp[n-1])