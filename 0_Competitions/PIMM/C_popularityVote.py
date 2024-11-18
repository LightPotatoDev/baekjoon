from math import gcd,lcm

n,p = map(int,input().split())
Before = list(map(int,input().split()))
After  = list(map(int,input().split()))

val = 10**(p+2)
befppl = val // gcd(*Before)
Befres = [befppl*i//val for i in Before]

aftppl = val // gcd(*After)
Aftres = [aftppl*i//val for i in After]

def voting(mul):
    for i in range(n):
        if Befres[i] > Aftres[i]*mul:
            return False
    return True

def binsearch():
    lo = 0
    hi = int(1e9)

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if voting(mid):
            hi = mid
        else:
            lo = mid
    return hi

aftppl *= binsearch()
print(befppl, aftppl)