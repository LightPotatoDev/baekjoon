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

P = [0]+sieve(4000000)
for i in range(len(P)-1):
    P[i+1] += P[i]

n = int(input())
pi = 0
pj = 0
cnt = 0
while pj < len(P)-1:
    val = P[pi] - P[pj]
    if val < n and pi < len(P)-1:
        pi += 1
    else:
        if val == n:
            cnt += 1
        pj += 1

print(cnt)