import math

a1, a2 = map(int,input().split())
b1, b2 = map(int,input().split())

denom = math.lcm(a2,b2)
a1 = a1 * (denom // a2)
b1 = b1 * (denom // b2)
gcd = math.gcd(a1+b1, denom)
print((a1+b1) // gcd, denom // gcd)
