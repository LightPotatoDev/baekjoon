from collections import deque

n,k = map(int,input().split())
dq = deque()
upnext = deque([n])
visited = [0] * 100001
visited[n] = 1
ways = 0

while upnext and ways == 0:
    dq = upnext.copy()
    upnext = deque()
    while dq:
        v = dq.popleft()
        for i in [v+1,v-1,v*2]:
            if 0 <= i <= 100000 and visited[i] == 0:
                visited[i] = visited[v] + 1
                print(visited[i])
                upnext.append(i)
            if i == k:
                ways += 1
                print(v,i)

print(visited[k]-1)
print(ways)
