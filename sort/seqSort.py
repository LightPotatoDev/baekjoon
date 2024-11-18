n = int(input())
L = list(map(int,input().split()))

cur = 0
target = 1
ans = [-1]*n

while cur < n:
    for i in range(n):
        if L[i] == target:
            ans[i] = cur
            cur += 1
    target += 1

print(*ans)