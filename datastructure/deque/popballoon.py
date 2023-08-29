from collections import deque
n = int(input())
L = deque([i for i in range(1,n+1)])
dq = deque(map(int,input().split()))

ans = []
for _ in range(n):
    p = dq.popleft()
    ans.append(L.popleft())
    dq.rotate(-p+1*int(p>0))
    L.rotate(-p+1*int(p>0))

print(*ans)