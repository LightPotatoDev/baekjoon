import math

n,k = map(int,input().split())
print(math.comb(n,2)*(1/k))