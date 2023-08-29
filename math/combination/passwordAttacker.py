from math import factorial, comb

def onto(m,n):
    s = 0
    for i in range(n+1):
        s += (-1)**i * comb(n,n-i) * (n-i)**m
    return s

T = int(input())
p = int(1e9)+7
for i in range(T):
    m,n = map(int,input().split())
    print(f"Case #{i+1}: {onto(n,m)%p}")