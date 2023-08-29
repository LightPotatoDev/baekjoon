from bisect import bisect_left

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

def pelin(n):
    a = str(n)
    b = a[::-1]
    return a==b

n = int(input())
P = sieve(1003001)
ind = bisect_left(P,n)
while pelin(P[ind]) == False:
    ind += 1
print(P[ind])