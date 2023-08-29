import math

x,y = map(int,input().split())
d = y-x
if d == 0:
    print(0)
    exit()
n = math.ceil((-1 + (1+4*d) ** 0.5) / 2)
print(n*2 - int(d-(n-1)*n <= n))