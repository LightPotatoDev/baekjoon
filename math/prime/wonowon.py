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
    return isPrime

def wono(n):
    if n == 2 or n == 5:
        return 0

    digits = 3
    num = 101

    while num%n != 0:
        num = num*100 + 1
        #num = (num*100 + 1) % n   by rootcucu
        digits += 2

    if n-digits == 2:
        return 1
    else:
        return 0

Primes = sieve(10000)
print(Primes)

n = int(input())
ans = 0
for i in range(2,n+1):
    if Primes[i] == 1:
        ans += wono(i)

print(ans)