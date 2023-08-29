from itertools import product
from bisect import bisect_left, bisect_right

N = list(range(10))
Pelin = []
for rep in range(1,5):
    for p in product(N, repeat=rep):
        if p[0] == 0:
            continue
        p = list(p)
        p1 = p[:]
        p1.extend(p[::-1])
        p2 = p[:]
        p2.extend(p[-2::-1])

        Pelin.append(int(''.join(map(str,p1))))
        Pelin.append(int(''.join(map(str,p2))))

Pelin.sort()

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

a,b = map(int,input().split())
for i in Pelin[bisect_left(Pelin,a):bisect_right(Pelin,b)]:
    if isPrime(i):
        print(i)
print(-1)