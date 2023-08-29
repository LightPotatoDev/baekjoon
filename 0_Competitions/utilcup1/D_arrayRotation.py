from collections import deque
from copy import deepcopy

n = int(input())
L = []
for _ in range(n):
    L.append(deque(map(int,input().split())))

q = int(input())
for _ in range(q):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        L[cmd[1]-1].rotate(1)
    else:
        A = [deque([0]*n) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                A[j][n-i-1] = L[i][j]
        L = deepcopy(A)


for row in L:
    print(*row)