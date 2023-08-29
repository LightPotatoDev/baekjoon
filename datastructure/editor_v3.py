from collections import deque
import sys
input = sys.stdin.readline

dq = deque(list(input().rstrip()))
m = int(input())
p = len(dq)

for _ in range(m):
    cmd = input().rstrip().split()

    if cmd[0] == "L" and p > 0:
        dq.rotate(1)
        p -= 1
    elif cmd[0] == "D" and p < len(dq):
        dq.rotate(-1)
        p += 1
    elif cmd[0] == "B" and p > 0:
        dq.pop()
        p -= 1
    elif cmd[0] == "P":
        dq.append(cmd[1])
        p += 1

dq.rotate(p)
print(''.join(dq))