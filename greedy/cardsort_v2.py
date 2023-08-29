import sys
input = sys.stdin.readline
import heapq

T = int(input())

for _ in range(T):
    n = int(input())
    hq = list(map(int,input().split()))
    heapq.heapify(hq)

    ans = 0
    for _ in range(n-1):
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        ans += (a+b)
        heapq.heappush(hq,a+b)

    print(ans)