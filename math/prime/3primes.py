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

P = sieve(1000)
T = int(input())
for _ in range(T):
    k = int(input()) - 3

    i = 2
    while True:
        if P[i] == 1 and P[k-i] == 1:
            L = [i,k-i,3]
            L.sort()
            print(*L)
            break
        i += 1
