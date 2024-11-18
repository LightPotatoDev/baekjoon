import sys
import heapq
input = sys.stdin.readline

n = int(input())
lines = [list(map(int,input().split())) for _ in range(n)]
l = int(input())

not_included = []
included = []
points = []
for a,b in lines:
    if a > b:
        a,b = b,a
    if b-a > l:
        continue
    s = b-l
    e = a
    heapq.heappush(not_included,(s,e))
    points.append(s)
    points.append(e)

ans = 0
points.sort()
for x in points:
    while not_included:
        s = not_included[0][0]
        if s <= x:
            a,b = heapq.heappop(not_included)
            heapq.heappush(included, (b,a))
        else:
            break

    while included:
        e = included[0][0]
        if e < x:
            heapq.heappop(included)
        else:
            break

    ans = max(ans, len(included))

print(ans)