import math

n,k = map(int,input().split())
L = list(map(lambda x:int(x)%k,input().split()))
p = int(1e9)+7

Mod = [0] * k
for i in L:
    Mod[i] += 1

print(Mod)