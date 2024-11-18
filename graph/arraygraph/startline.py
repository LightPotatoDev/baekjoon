from collections import deque

f,s,g,u,d = map(int,input().split())
pos = deque([s])
visited = [0] * (f+1)
visited[s] = 1

while pos:
    i = pos.popleft()
    for j in [i+u,i-d]:
        if j <= 0 or j > f:
            continue

        if visited[j] == 0:
            visited[j] = visited[i] + 1
            pos.append(j)

if visited[g] == 0:
    print('use the stairs')
else:
    print(visited[g]-1)
