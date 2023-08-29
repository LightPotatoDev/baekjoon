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

    return (primes,isPrime)

P,isP = sieve(1299709)
T = int(input())

for _ in range(T):
    k = int(input())
    if k == 2 or (k%2 == 1 and isP[k//2] == 1):
        print(0)
        continue

    ind = bisect_left(P,k)
    a = P[ind-1]
    b = P[ind]
    print(b-a)