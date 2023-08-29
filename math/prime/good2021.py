from bisect import bisect_right

def sieve(n):
    p = 2
    isPrime = [1 for i in range(n+1)]
    while p**2 <= n:
        i = p
        while i <= n-p:
            i += p
            isPrime[i] = 0
        p += 1
    isPrime[1] = 0

    primes = []
    for i in range(2,n+1):
        if isPrime[i] == 1:
            primes.append(i)

    return primes

P = sieve(400)
specials = []

for i in range(27):
    specials.append(P[i] * P[i+1])
n = int(input())
print(specials[bisect_right(specials,n)])
