from collections import deque

n = int(input())
dq = list(map(int,input().split()))
dq.sort()
dq = deque(dq)
ans = 0

while dq:
    p = dq.popleft()
    if p < len(dq):
        s = 0
        for _ in range(p+1):
            s += dq.pop()
        ans += p
        dq.append(s+p)
    else:
        ans += len(dq)
        break

print(ans)