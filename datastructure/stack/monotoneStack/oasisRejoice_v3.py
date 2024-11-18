import sys
input = sys.stdin.readline

n = int(input())
L = [int(input()) for _ in range(n)]
watchLeft = [0]*n
watchRight = [n-1]*n

stack = []
for i,x in enumerate(L):
    while stack and stack[-1][1] < x:
        watchRight[stack[-1][0]] = i
        stack.pop()
    stack.append((i,x))

stack = []
for i,x in enumerate(L[::-1]):
    while stack and stack[-1][1] < x:
        watchLeft[stack[-1][0]] = n-i-1
        stack.pop()
    stack.append((n-i-1,x))

ans = 0
check = set()
for i in range(n):
    rmv = []
    for ind,watchR in check:
        if watchR >= i and watchLeft[i] <= ind:
            ans += 1
            if watchR == i:
                rmv.append((ind,watchR))
    for r in rmv:
        check.remove(r)

    check.add((i,watchRight[i]))

print(ans)