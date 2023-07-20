import sys

k, n = map(int,input().split())
L = [int(sys.stdin.readline()) for _ in range(k)]

start = 0
end = sum(L) // n

while start <= end:

    mid = (start + end + 1) // 2
    s = sum([i//mid for i in L])
    if s >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)