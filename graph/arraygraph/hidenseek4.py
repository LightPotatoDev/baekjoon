from collections import deque

n,k = map(int,input().split())
pos = deque([n])
visited = [[0,0] for _ in range(100001)] #step, trace
visited[n] = [1,-1]

while pos:
    i = pos.popleft()
    for j in [i+1,i-1,i*2]:
        if 0 <= j <= 100000:
            if visited[j][0] == 0:
                visited[j][0] = visited[i][0] + 1
                visited[j][1] = i
                pos.append(j)

print(visited[k][0]-1)

back = k
L = []
while back != -1:
    L.append(back)
    back = visited[back][1]
print(*L[::-1])