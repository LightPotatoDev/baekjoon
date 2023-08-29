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

    return factor[-1]

#소인수분해