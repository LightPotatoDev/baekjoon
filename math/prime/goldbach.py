import sys
input = sys.stdin.readline

def sieve(n):
    p = 2
    isPrime = [1] * (n+1)
    for i in range(2,int(n**0.5)+1):
        if isPrime[i]:
            for j in range(i**2, n+1, i):
                isPrime[j] = 0

    isPrime[1] = 0
    return isPrime


P = sieve(32768)
while True:
    x = int(input())
    if x == 0:
        break
    i = 2
    cnt = 0
    while i <= x//2:
        if P[i] == 1 and P[x-i] == 1:
            cnt += 1
        i += 1

    print(cnt)
