import math

n = int(input())
L = list(map(int,input().split()))
primes = 0

def isprime(num):
    if num == 1: return 0

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return 0

    return 1

for i in L:
    primes += isprime(i)

print(primes)