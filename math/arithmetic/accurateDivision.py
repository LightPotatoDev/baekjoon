from decimal import Decimal, getcontext
getcontext().prec = 1100
a,b = map(int,input().split())
print(Decimal(a)/Decimal(b))