import math
import sys
input = sys.stdin.readline

n,b = map(int,input().split())

Points = []
for _ in range(n):
    x,y = map(int,input().split())
    Points.append([x,y])

a = 0
c = 0
for x,y in Points:
    a += x
    c += (b-y)

if a == 0:
    print("EZPZ")
else:
    gcd = math.gcd(c,a)
    c = c // gcd
    a = a // gcd
    if abs(a) == 1:
        print(c//a*-1)
    else:
        print(f"{c*-1*(2*(a>0)-1)}/{abs(a)}")
