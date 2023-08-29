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

n = int(input())
k = int(input())
cnt = 0
for i in range(1,n+1):
    if factorize(i) <= k:
        cnt += 1
print(cnt)