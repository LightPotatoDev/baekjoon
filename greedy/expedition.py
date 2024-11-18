import sys
input = sys.stdin.readline
import heapq

n = int(input())
L = [tuple(map(int,input().split())) for _ in range(n)]
l,p = map(int,input().split())
coords = [0]*(l+1)
for pos,fuel in L:
    coords[pos] = fuel
stops = []
dist = 0
ans = 0
finished = False

while dist < l:
    if p > 0:
        dist += 1
        p -= 1
    if dist == l:
        finished = True
        break
    if coords[dist] != 0:
        heapq.heappush(stops,-coords[dist])
    if p == 0:
        if stops:
            fuel = -heapq.heappop(stops)
            p += fuel
            ans += 1
        else:
            break

if finished:
    print(ans)
else:
    print(-1)