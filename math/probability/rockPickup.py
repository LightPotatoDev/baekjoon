import math

m = int(input())
L = list(map(int,input().split()))
k = int(input())

allCase = math.comb(sum(L),k)
goodCase = 0
for i in L:
    goodCase += math.comb(i,k)
print(goodCase/allCase)