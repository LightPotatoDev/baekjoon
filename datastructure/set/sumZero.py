import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
L = [[] for _ in range(4)]
for _ in range(n):
    A = map(int,input().split())
    for i,x in enumerate(A):
        L[i].append(x)

D1 = defaultdict(int)
D2 = defaultdict(int)

for i in L[0]:
    for j in L[1]:
        D1[i+j] += 1

for i in L[2]:
    for j in L[3]:
        D2[i+j] += 1

ans = 0
for i in D1:
    if -i in D2:
        ans += min(D1[i],D2[-i])
print(ans)