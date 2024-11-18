
K = [0]*10

lo,hi = map(int,input().split())
L = [0]*(hi+1)

for i in range(lo,hi+1):
    iter = 0
    num = i
    while i > 1:
        i = i.bit_count()
        iter += 1
    L[num] = iter
    K[iter] += 1
print(K)