from math import gcd

n = int(input())
L = list(map(int,input().split()))

for i in range(1,n):
    g = gcd(L[0],L[i])
    print(f"{L[0]//g}/{L[i]//g}")