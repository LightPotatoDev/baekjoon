import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap_pos = []
heap_neg = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if   len(heap_pos) == 0 and len(heap_neg) == 0:
            print(0)
        elif len(heap_pos) == 0 and len(heap_neg) != 0:
            print(heapq.heappop(heap_neg) * -1)
        elif len(heap_pos) != 0 and len(heap_neg) == 0:
            print(heapq.heappop(heap_pos))
        else:
            if heap_pos[0] >= heap_neg[0]:
                print(heapq.heappop(heap_neg) * -1)
            else:
                print(heapq.heappop(heap_pos))
    elif x > 0:
        heapq.heappush(heap_pos, x)
    else:
        heapq.heappush(heap_neg, x*-1)

        #  heapq.heappush(q, (abs(a), a))
        #     print(heapq.heappop(q)[1])
