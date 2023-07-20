from collections import deque

n,k = map(int,input().split())
pos = deque([n])
visited = [0] * 100001
visited[n] = 1

while visited[k] == 0:
    i = pos.popleft()
    for j,x in enumerate([i*2,i-1,i+1]):
        if 0 <= x <= 100000:
            if visited[x] == 0:
                if j == 0:
                    visited[x] = visited[i]
                    pos.appendleft(x)
                else:
                    visited[x] = visited[i] + 1
                    pos.append(x)

print(visited[k]-1)