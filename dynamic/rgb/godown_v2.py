import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
A = deque([])
B = deque([])

for i in range(n):
    L = list(map(int,input().split()))
    A.append(L[:])
    B.append(L[:])
    if i > 0:
        A[1][0] = max(A[0][0], A[0][1]) + A[1][0]
        A[1][1] = max(A[0][0], A[0][1], A[0][2]) + A[1][1]
        A[1][2] = max(A[0][1], A[0][2]) + A[1][2]
        A.popleft()

        B[1][0] = min(B[0][0], B[0][1]) + B[1][0]
        B[1][1] = min(B[0][0], B[0][1], B[0][2]) + B[1][1]
        B[1][2] = min(B[0][1], B[0][2]) + B[1][2]
        B.popleft()
print(*[max(A[0]), min(B[0])])