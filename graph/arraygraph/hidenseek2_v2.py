from collections import deque

n,k = map(int,input().split())
dq = deque()
upnext = deque([n])
visited = [[0,0] for _ in range(100001)] #step,ways
visited[n] = [1,1]

while upnext and visited[k][1] == 0:
    dq = upnext.copy()
    upnext = deque()
    while dq:
        v = dq.popleft()
        for i in [v+1,v-1,v*2]:
            if 0 <= i <= 100000:
                if visited[i][0] == 0:
                    visited[i][0] = visited[v][0] + 1
                    upnext.append(i)
                if visited[i][0] == visited[v][0] + 1:
                    visited[i][1] += visited[v][1]

print(visited[k][0]-1)
print(visited[k][1])
