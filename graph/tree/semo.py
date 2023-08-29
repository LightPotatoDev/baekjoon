from math import comb
n = int(input())

print(n-1 + 2*comb(n-1,2))
for i in range(n-1):
    print(1,i+2)