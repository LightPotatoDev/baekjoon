import sys
from decimal import Decimal, ROUND_HALF_UP
n = int(input())

L = []
for _ in range(n):
    L.append(int(sys.stdin.readline()))

L.sort()
nope = Decimal(n*0.15).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
nope = int(nope)

if n != 0:
    L = L[nope:n-nope]
    print(Decimal(sum(L)/len(L)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
else:
    print(0)