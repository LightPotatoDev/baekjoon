def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

primeNum = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]
N = list(map(int,input().split()))
for n in N:
    p = 1
    for i in range(n):
        p *= primeNum[i]

    q = p+2
    while isPrime(q) == False:
        q += 1

    q2 = p-2
    while isPrime(q2) == False:
        q2 -= 1

    print(f"N = {n} FORTUNATE = {q-p} LESS = {p-q2}")

