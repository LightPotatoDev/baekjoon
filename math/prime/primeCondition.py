from bisect import bisect_left, bisect_right

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

a,b,d = map(int,input().split())
P = sieve(4000000)
L = P[bisect_left(P,a):bisect_right(P,b)]

cnt = 0
for i in L:
    i = str(i)
    cnt += str(d) in i
print(cnt)