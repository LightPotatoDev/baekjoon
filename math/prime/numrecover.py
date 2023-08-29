from collections import defaultdict

def factorize(n):
    if n == 1:
        return 0

    factor = defaultdict(int)
    while True:
        isPrime = True
        for i in range(2, int(n**0.5)+1):

            if n % i == 0:
                factor[i] += 1
                n = n // i
                isPrime = False
                break

        if isPrime:
            factor[n] += 1
            break

    return factor

T = int(input())
for _ in range(T):
    x = int(input())
    D = factorize(x)
    Factor = []
    for i in D:
        Factor.append((i,D[i]))
    Factor.sort()

    for i in Factor:
        print(*i)

