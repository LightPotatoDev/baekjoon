import heapq

n,m = map(int,input().split())
hq = list(map(int,input().split()))
heapq.heapify(hq)

for _ in range(m):
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    heapq.heappush(hq,a+b)
    heapq.heappush(hq,a+b)

print(sum(hq))