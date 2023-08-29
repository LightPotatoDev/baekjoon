import math
T = int(input())

for _ in range(T):
    n,m,k,d = map(int,input().split())
    diff = math.comb(n,2) * m**2
    same = math.comb(m,2) * n * k
    b = int(d/(diff+same))
    if b > 0:
        print((diff+same)*b)
    else:
        print(-1)