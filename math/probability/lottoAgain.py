import math

n,m,k = map(int,input().split())
all = math.comb(n,m)
lucky = 0
for i in range(m-k+1):
    lucky += math.comb(m,k+i) * math.comb(n-m,m-k-i)

print(lucky/all)
