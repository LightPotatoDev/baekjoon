import sys
input = sys.stdin.readline
from itertools import combinations
from math import factorial, gcd

n = int(input())
L = [int(input()) for _ in range(n)]
k = int(input())

dp = [[0]*(1<<n) for _ in range(k)]
mask = (1<<n)-1
Digits = [len(str(i)) for i in L]
DComb = [0]*(mask+1)
allDigit = sum(Digits)
dp[0][0] = 1

for i in range(mask):
    DComb[i] = allDigit
    for j in range(n):
        if (i >> j) & 1 == 1:
            DComb[i] -= Digits[j]

L = list(map(lambda x:x%k, L))

def PSW(visited):
    for j in range(n):
        ref = visited | (1 << j)
        if ref == visited:
            continue
        R = (L[j]*pow(10,DComb[ref],k))%k
        for r in range(k):
            newR = (r+R)%k
            dp[newR][ref] += dp[r][visited]

for i in range(n):
    comb = combinations(range(n),i)
    for choice in comb:
        visit = 0
        for c in choice:
            visit += 1<<c
        PSW(visit)

p = dp[0][mask]
q = factorial(n)
div = gcd(p,q)
print(f"{p//div}/{q//div}")

#1357529/127702575