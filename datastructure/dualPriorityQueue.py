import sys
input = sys.stdin.readline
import heapq

T = int(input())

for _ in range(T):
    n = int(input())
    heapmin = []
    heapmax = []

    #parent: (i+1)//2 - 1
    for _ in range(n):
        command, num = input().split()
        num = int(num)
        if command == "I":
            if len(heapmin) == 0:
                heapq.heappush(heapmin, num)

            elif len(heapmin) == len(heapmax): #even number of elements
                parent_i = (len(heapmin)+1)//2 - 1
                if -heapmax[parent_i] > num:
                    heapq.heappush(heapmin, num)
                else:
                    heapq.heappush(heapmax, -num)

            else:                               # odd number of elements
                if len(heapmin) > len(heapmax):
                    p = heapmin.pop(-1)
                else:
                    p = heapmax.pop(-1) * (-1)

                a,b = p,num
                if a > b:
                    a,b = b,a
                heapq.heappush(heapmin,a)
                heapq.heappush(heapmax,-b)

        print(heapmin)
        print(heapmax)

        if command == "D" and len(heap) >= 1:
            if num == -1:
                heapq.heappop(heap)
            else:
                heap = list(map(lambda x:x*-1, heap))
                heapq.heapify(heap)
                heapq.heappop(heap)
                heap = list(map(lambda x:x*-1, heap))
                heapq.heapify(heap)

    if heap:
        print(heap[-1], heap[0])
    else:
        print("EMPTY")
