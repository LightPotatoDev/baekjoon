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

P = sieve(1000000)
P_square = list(map(lambda x:x**2, P))
a,b = map(int,input().split())
L = [1]*(b-a+1)

for i in P_square:
    r = (a-1) % i
    d = i - r
    start = a-1 + d
    #find the smallest multiple of i, bigger than or same with a
    for j in range(start, b+1, i):
        L[j-a] = 0

print(sum(L))