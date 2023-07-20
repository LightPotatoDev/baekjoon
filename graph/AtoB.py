from collections import deque

a,b = map(int,input().split())
upnext = deque([a])
steps = 1

while upnext:
    steps += 1
    dq = upnext.copy()
    upnext = deque()
    while dq:
        p = dq.popleft()
        for i in [p*10+1, p*2]:
            if i == b:
                print(steps)
                exit(0)
            elif i < b:
                upnext.append(i)

print(-1)