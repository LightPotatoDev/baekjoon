import sys
input = sys.stdin.readline

def sieve(n):
    p = 2
    isPrime = [1] * (n+1)
    for i in range(2,int(n**0.5)+1):
        if isPrime[i]:
            for j in range(i**2, n+1, i):
                isPrime[j] = 0

    isPrime[0],isPrime[1] = 0,0
    return isPrime

P = sieve(100000)

while True:
    s = input().rstrip()
    if s == "0":
        break

    prime = 0
    for i in range(4,-1,-1):
        for j in range(len(s)-i):
            sub = s[j:j+i+1]
            if P[int(sub)] == 1:
                prime = max(prime,int(sub))

    print(prime)

