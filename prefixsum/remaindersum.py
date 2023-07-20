import sys
input = sys.stdin.readline
import math

n,m = map(int,input().split())

def intremain(x):
    return int(x) % m

L = list(map(intremain,input().split()))
D = dict()

for i in range(m):
    D[i] = 0

D[L[0]] += 1
for i in range(n-1):
    L[i+1] = (L[i] + L[i+1]) % m
    D[L[i+1]] += 1

cnt = D[0]
for i in D:
    cnt += math.comb(D[i],2)
print(cnt)