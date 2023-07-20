def sieve(n):
    p = 2
    prime = [1 for i in range(n)]
    while p**2 <= n:
        i = p
        while i <= n-p:
            i += p
            prime[i-1] = 0
        p += 1

    prime[0] = 0
    return prime

m, n = map(int,input().split())
isprime = sieve(n)

for i in range(m, n+1):
    if isprime[i-1] == 1:
        print(i)