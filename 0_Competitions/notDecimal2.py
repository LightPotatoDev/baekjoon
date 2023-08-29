from decimal import Decimal, getcontext
getcontext().prec = 10
n = Decimal(input())
l = n.as_tuple().exponent * -1
print("YES")
print(int(n*(10**l)),10**l)