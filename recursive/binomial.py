import math

n,k = map(int,input().split())
p = 1000000007

def perm(a,b):
    num = 1
    for i in range(a,a-b,-1):
        num = (num * i) % p
    return num

print(((perm(n,k) % p) * pow(perm(k,k), p-2, p)) % p)