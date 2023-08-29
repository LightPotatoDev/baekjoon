import math

T = int(input())
for _ in range(T):
    x,y = map(int,input().split())
    d = y-x
    n = math.ceil((-1 + (1+4*d) ** 0.5) / 2)
    print(n*2 - int(d-(n-1)*n <= n))