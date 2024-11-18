def factorize(n):
    if n == 1:
        return []

    factor = []
    while True:
        is_prime = True
        for i in range(2, int(n**0.5)+1):

            if n % i == 0:
                factor.append(i)
                n = n // i
                is_prime = False
                break

        if is_prime:
            factor.append(n)
            break

    return factor

#소인수분해