def factorize(n):
    if n == 1:
        return 0

    factor = []
    while True:
        isPrime = True
        for i in range(2, int(n**0.5)+1):

            if n % i == 0:
                factor.append(i)
                n = n // i
                isPrime = False
                break

        if isPrime:
            factor.append(n)
            break

    return len(factor)

def sieve(n):
    isPrime = [1] * (n//2+1)

    for i in range(1,n//2+1):
        if isPrime[i]:
            p = 2*i+1
            for j in range((p**2)//2,n//2+1,p):
                isPrime[j] = 0
    isPrime[0] = 0
    return isPrime

a,b = map(int,input().split())
L = [0]*100001
P = sieve(1000)
for i in range(2,100001):
    L[i] = factorize(i)
UP = [0]*100001
for i in range(2,100001):
    if (L[i]%2 == 1 and P[L[i]//2] == 1) or L[i] == 2:
        UP[i] = 1

print(sum(UP[a:b+1]))


