from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

dq = deque()
for i in range(n):
    if A[i] == 0:
        dq.append(B[i])

m = int(input())
L = list(map(int,input().split()))

for x in L:
    dq.appendleft(x)
    print(dq.pop(), end=' ')