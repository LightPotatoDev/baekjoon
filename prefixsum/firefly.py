import sys
input = sys.stdin.readline

n,h = map(int,input().split())
floor = [0]
ceiling = [0]
obstacle = [0]*h

for i in range(n):
    if i%2 == 0:
        floor.append(int(input()))
    else:
        ceiling.append(int(input()))

floor.sort()
ceiling.sort()

idx = 0
for i in range(n//2):
    for j in range(floor[i+1]-floor[i]):
        obstacle[idx] += n//2-i
        idx += 1

idx = h-1
for i in range(n//2):
    for j in range(ceiling[i+1]-ceiling[i]):
        obstacle[idx] += n//2-i
        idx -= 1

ans = min(obstacle)
print(ans, obstacle.count(ans))
