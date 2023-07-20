import sys
input = sys.stdin.readline

import heapq

N = int(input().strip())
heap = []

for _ in range(N):
    x = int(input().strip())

    if x == 0:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)
    #print(heap)