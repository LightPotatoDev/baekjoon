##def fibo(n):
##    if n == 0:
##        return 0
##    if n == 1:
##        return 1
##    else:
##        return fibo(n-1) + fibo(n-2)
##
##n = int(input())
##print(fibo(n))
##

n = int(input()) % 1500000
L = [0] * (n+1)
if len(L) != 1:
    L[1] = 1
for i in range(2,n+1):
    L[i] = (L[i-1] + L[i-2])%1000000

print(L[n])
"""
pisano period
F mod 2: 3
F mod 3: 8
F mod 4: 6
F mod 5: 20
F mod 6: 24
"""