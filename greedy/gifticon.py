import sys
input = sys.stdin.readline
import heapq

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
hq = [(A[i],B[i]) for i in range(n)]
heapq.heapify(hq)
ans = 0
pa,pb = 0,0

while hq:
    a,b = heapq.heappop(hq)
    if a < b:
        ext = (b-a-1)//30 + 1
        heapq.heappush(hq,(a+30*ext,b))
        ans += ext
        pa,pb = a,b
    if a >= b:


print(ans)