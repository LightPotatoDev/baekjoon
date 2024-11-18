from collections import deque
import sys

n = int(input())
dq = deque([i for i in range(1,n+1)])

while len(dq) > 1:
    print(dq.popleft(), end=' ')
    a = dq.popleft()
    dq.append(a)

print(dq[0])