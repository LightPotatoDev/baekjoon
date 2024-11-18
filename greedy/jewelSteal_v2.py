import sys
input = sys.stdin.readline
import heapq

n,k = map(int,input().split())
jewels = [tuple(map(int,input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jewels.sort(key = lambda x:(-x[0],-x[1]))
bags.sort(reverse=True)
capacity = 0

stealed = []
for weight,value in jewels:
    if capacity < k and weight <= bags[capacity]:
        capacity += 1
    heapq.heappush(stealed,value)
    if len(stealed) > capacity:
        heapq.heappop(stealed)

print(sum(stealed))