import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
A = []

for _ in range(n):
    A.append(list(map(int,input().split())))

L = deepcopy(A)
for i in range(1,n):
    L[i][0] = max(L[i-1][0], L[i-1][1]) + L[i][0]
    L[i][1] = max(L[i-1][0], L[i-1][1], L[i-1][2]) + L[i][1]
    L[i][2] = max(L[i-1][1], L[i-1][2]) + L[i][2]
print(max(L[n-1]), end=" ")

L = deepcopy(A)
for i in range(1,n):
    L[i][0] = min(L[i-1][0], L[i-1][1]) + L[i][0]
    L[i][1] = min(L[i-1][0], L[i-1][1], L[i-1][2]) + L[i][1]
    L[i][2] = min(L[i-1][1], L[i-1][2]) + L[i][2]
print(min(L[n-1]))
