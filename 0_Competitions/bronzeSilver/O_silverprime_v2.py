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
n = int(input())
pNum = sum(P[1:n+1])
if n == 1:
    print(1,0)
elif n == 2:
    print(0,2)
else:
    print(n - (pNum*2-1), pNum*2-1)