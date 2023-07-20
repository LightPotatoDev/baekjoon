import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap) * -1)
        else:
            print(0)
    else:
        heapq.heappush(heap, x * -1)
    print(heap)