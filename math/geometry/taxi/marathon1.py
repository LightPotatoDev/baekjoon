import sys
input = sys.stdin.readline

n = int(input())
check = [list(map(int,input().split())) for _ in range(n)]
dist = [] #[1->2],[2->3],...,[n-1->n]
skip = [] #[1->3],[2->4],...,[n-2->n]

for i in range(n-1):
    x1,y1 = check[i]
    x2,y2 = check[i+1]
    dist.append(abs(x1-x2)+abs(y1-y2))

for i in range(n-2):
    x1,y1 = check[i]
    x2,y2 = check[i+2]
    skip.append(abs(x1-x2)+abs(y1-y2))

total = sum(dist)
minD = total
for i in range(n-2):
    minD = min(minD, total-dist[i]-dist[i+1]+skip[i])
print(minD)