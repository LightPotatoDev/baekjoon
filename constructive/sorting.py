import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    inc = n-1
    dq1 = deque(range(1,n+1))
    dq2 = deque([])

    while m-inc >= 0 and inc > 0:
        p = dq1.popleft()
        dq2.appendleft(p)
        m -= inc
        inc -= 1

    p = dq1.popleft()
    dq1.insert(m,p)
    dq1.extend(dq2)
    print(*dq1)