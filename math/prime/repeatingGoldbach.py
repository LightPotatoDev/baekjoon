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


P = sieve(1000000)
x = int(input())
cnt = 0
while True:
    i = 2
    while i <= x//2:
        if P[i] == 1 and P[x-i] == 1:
            cnt += 1
            x = x-2*i
            break
        i += 1

    if x < 3:
        break

print(cnt)
