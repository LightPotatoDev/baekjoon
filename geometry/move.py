import sys
input = sys.stdin.readline

n = int(input())
points = [list(map(int,input().split())) for _ in range(n)]
xa,xb = 0,0
ans = int(1e9)
for x1,y1 in points:
    furthest = 0
    for x2,y2 in points:
        furthest = max(furthest, ((x1-x2)**2 + (y1-y2)**2) ** 0.5)
    if furthest < ans:
        xa,xb = x1,y1
        ans = furthest

print(xa,xb)
