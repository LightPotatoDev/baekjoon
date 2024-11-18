import sys
import heapq
input = sys.stdin.readline

n = int(input())
L = [tuple(map(int,input().split())) for _ in range(n)]
L.sort()
scores = []

for day,score in L:
    heapq.heappush(scores,score)
    if day < len(scores):
        heapq.heappop(scores)

print(sum(scores))