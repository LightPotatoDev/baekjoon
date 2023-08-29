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

while True:
    L = list(map(int,input().split()))
    if L == [0]:
        break

    x = 1
    for i in range(0,len(L),2):
        x *= L[i]**L[i+1]
    x -= 1

    D = factorize(x)
    Factor = []
    for i in D:
        Factor.append((i,D[i]))
    Factor.sort(reverse=True)

    for i in Factor:
        print(*i, end=" ")
    print('')
