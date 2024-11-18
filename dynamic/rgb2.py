import sys
input = sys.stdin.readline
from copy import deepcopy

n = int(input())
L = [list(map(int,input().split())) for _ in range(n)]

def rgb(start):
    A = deepcopy(L)
    for i in range(3):
        A[1][i] += A[0][start]
    A[1][start] = int(1e8)
    for i in range(2,n):
        A[i][0] += min(A[i-1][1], A[i-1][2])
        A[i][1] += min(A[i-1][0], A[i-1][2])
        A[i][2] += min(A[i-1][0], A[i-1][1])
    A[-1][start] = int(1e8)

    return min(A[-1])

ans = int(1e8)
for i in range(3):
    ans = min(ans,rgb(i))
print(ans)