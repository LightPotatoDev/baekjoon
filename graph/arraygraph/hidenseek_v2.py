from collections import deque

n,k = map(int,input().split())
pos = deque([n])
visited = [0] * 100001
visited[n] = 1
ways = 0

while pos:
    i = pos.popleft()
    for j in [i+1,i-1,i*2]:
        if 0 <= j <= 100000:
            if visited[j] == 0:
                visited[j] = visited[i] + 1
                if j == k:
                    ways += 1
                if ways == 0:
                    pos.append(j)

print(visited[k]-1)
print(ways)
