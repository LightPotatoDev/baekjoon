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

def euler_phi(n):
    factors = factorize(n)
    factor_dict = dict()
    for f in factors:
        if f not in factor_dict:
            factor_dict[f] = 0
        factor_dict[f] += 1

    ans = 1
    for k,v in factor_dict.items():
        ans *= (k**v - k**(v-1))

    return ans

n = int(input())
print(euler_phi(n))