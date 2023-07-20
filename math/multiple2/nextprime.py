T = int(input())

def isprime(num):
    if 0 <= num <= 1: return 0

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return 0
    return 1


for _ in range(T):
    n = int(input())

    while isprime(n) == 0:
        n += 1
    print(n)