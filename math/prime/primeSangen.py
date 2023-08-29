from bisect import bisect_right
import math

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

def sangen(n):
    while True:
        if n == 1:
            return True
        elif n == 4:
            return False

        digits = [n // 10**i % 10 for i in range(int(math.log10(n))+1)]
        n = 0
        for i in digits:
            n += i**2

P = sieve(1000000)
n = int(input())
ind = bisect_right(P,n)
for i in range(ind):
    if sangen(P[i]):
        print(P[i])