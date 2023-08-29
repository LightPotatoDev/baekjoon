from collections import Counter

def factorize(n):
    if n == 1:
        return Counter({1:1})

    factor = Counter({1:1})
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

for i in range(100001,200101):
    factorize(i)