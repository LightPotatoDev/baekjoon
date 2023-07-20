import sys
input = sys.stdin.readline
from collections import deque
from bisect import bisect_left

T = int(input())

for _ in range(T):
    n = int(input())
    dq = deque()

    for _ in range(n):
        command, num = input().split()
        num = int(num)
        if command == "I":
            index = bisect_left(dq, num)
            dq.insert(index,num)
        if command == "D" and len(dq) >= 1:
            if num == -1:
                dq.popleft()
            else:
                dq.pop()

    if dq:
        print(dq[-1], dq[0])
    else:
        print("EMPTY")
