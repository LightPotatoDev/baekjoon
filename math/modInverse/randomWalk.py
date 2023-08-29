import sys
input = sys.stdin.readline

T = int(input())
p = int(1e9)+7

def perm(a,b):
    num = 1
    for i in range(a,a-b,-1):
        num = (num * i) % p
    return num

for _ in range(T):
    n = int(input())
    a = ((perm(2*n,n) % p) * pow(perm(n,n), p-2, p)) % p
    b = pow(n+1,-1,p)
    print((a%p * b%p)%p)