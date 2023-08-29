from collections import defaultdict

n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))
p = int(1e9)

D1 = defaultdict(int)
D2 = defaultdict(int)

def factorize(n):
    if n == 1:
        return [1]

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

    return factor

for i in A:
    for j in factorize(i):
        D1[j] += 1

for i in B:
    for j in factorize(i):
        D2[j] += 1

S = set(D1) & set(D2)

ans = 1
bigNum = False
for i in S:
    if bigNum == False:
        ans *= i ** min(D1[i], D2[i])
        if ans >= p:
            bigNum = True
            ans %= p
    else:
        ans = (ans * (i ** min(D1[i],D2[i]))) % p

if bigNum:
    print("{:09d}".format(ans))
else:
    print(ans)

