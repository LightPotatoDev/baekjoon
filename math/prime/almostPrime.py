from bisect import bisect_left, bisect_right

def sieve(n):
    isPrime = [1] * (n//2+1)
    primes = [2]

    for i in range(1,n//2+1):
        if isPrime[i]:
            p = 2*i+1
            primes.append(p)
            for j in range((p**2)//2,n//2+1,p):
                isPrime[j] = 0

    return primes

P = sieve(int(1e7))
L = []
for i in P:
    n = i*i
    while n < int(1e14):
        L.append(n)
        n = n*i
L.sort()

a,b = map(int,input().split())
print(bisect_right(L,b) - bisect_left(L,a))
