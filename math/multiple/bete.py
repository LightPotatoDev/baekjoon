def sieve(n):
    p = 2
    prime = [1 for i in range(n+1)]
    for i in range(2,int(n**0.5)+1):
        if prime[i] == 0:
            continue
        for j in range(2,n//i+1):
            prime[j*i] = 0
    prime[0:2] = [0,0]
    return prime

while True:
    n = int(input())
    if n == 0:
        break
    isprime = sieve(n*2)
    print(sum(isprime[n+1:2*n+1]))