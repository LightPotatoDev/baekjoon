def sieve(n):
    is_prime = [0,1] * (n//2+1)

    for i in range(3,n+1,2):
        if is_prime[i]:
            for j in range(i*3,n+1,i*2):
                is_prime[j] = 0

    is_prime[1] = 0
    is_prime[2] = 1
    return is_prime

#아래 함수에서 is_prime을 더 사용하기 직관적이게 변경

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

#최적화 v3 - 짝수인 소수는 2밖에 없음을 활용 - 지금까진 이게 제일 빠름

def sieve(n):
    p = 2
    isPrime = [1 for i in range(n+1)]
    while p**2 <= n:
        if isPrime[p] == 0:
            continue
        i = p**2
        while i <= n-p:
            isPrime[i] = 0
            i += p
        p += 1
    isPrime[1] = 0

    primes = []
    for i in range(2,n+1):
        if isPrime[i] == 1:
            primes.append(i)

    return primes

#소수 여러 개를 찾아야 할 시 사용

def sieve(n):
    p = 2
    isPrime = [1] * (n+1)
    primes = []
    for i in range(2,int(n**0.5)+1):
        if isPrime[i]:
            primes.append(i)
            for j in range(i**2, n+1, i):
                isPrime[j] = 0

    for i in range(int(n**0.5)+1, n+1):
        if isPrime[i]:
            primes.append(i)
    return primes

#최적화시킨 버전

def sieve(n):
    p = 2
    isPrime = [1] * (n+1)
    primes = []
    while p**2 <= n:
        if isPrime[p] == 0:
            p += 1
            continue
        primes.append(p)
        i = p**2
        while i <= n-p:
            isPrime[i] = 0
            i += p
        p += 1
    isPrime[1] = 0

    for i in range(int(n**0.5)+1, n+1):
        if isPrime[i] == 1:
            primes.append(i)

    return primes

#최적화 v2

def sieve(MAXP):
    primes = [2]
    sieve = [0] * ((MAXP)//2)
    for i in range(1, MAXP//2):
        if not sieve[i]:
            p = 2*i+1
            primes.append(p)
            cur = p
            ind = i
            tp = p*2
            while cur < MAXP:
                sieve[ind] = 1
                ind += p
                cur += tp
    return primes

# by thahn106