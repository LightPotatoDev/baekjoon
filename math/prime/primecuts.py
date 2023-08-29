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

    primes = [1]
    for i in range(2,n+1):
        if isPrime[i] == 1:
            primes.append(i)

    return primes

Primes = sieve(1000)

while True:
    n,c = 0,0
    try:
        n,c = map(int,input().split())
    except:
        break
    lim = bisect_right(Primes,n)
    L = Primes[:lim]
    print(f"{n} {c}: ",end='')

    if len(L) % 2 == 0:
        if c*2 <= len(L):
            print(*L[len(L)//2-c:len(L)//2+c])
        else:
            print(*L)
    else:
        if c*2-1 <= len(L):
            print(*L[len(L)//2-c+1:len(L)//2+c])
        else:
            print(*L)
    print('')