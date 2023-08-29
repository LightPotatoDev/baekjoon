def sieve(n):
    p = 2
    isPrime = [1] * (n+1)
    for i in range(2,int(n**0.5)+1):
        if isPrime[i]:
            for j in range(i**2, n+1, i):
                isPrime[j] = 0

    isPrime[0],isPrime[1] = 0,0
    return isPrime

P = sieve(1000000)

n = int(input())
L = set(map(int,input().split()))
ans = 1
for i in L:
    if P[i] == 1:
        ans *= i

if ans == 1:
    print(-1)
else:
    print(ans)