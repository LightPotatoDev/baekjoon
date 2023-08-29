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

P = sieve(118)

n = int(input())
for _ in range(n):
    a = int(input())
    result = "No"
    for i in range(1,a//2+1):
        if P[i] and P[a-i]:
            result = "Yes"
            break
    print(result)
